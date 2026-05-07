#!/usr/bin/env python3
"""Wiki Romain Bigache CLI — Karpathy LLM Wiki tooling.

Subcommands:
  new {case|project|experience|writing|expertise} "Title"
  update {cv|profile|stack|availability|methodology|expertise|keywords}
  validate                                       Check frontmatter + wikilinks + naming
  rebuild-llms-txt                               Regenerate llms.txt from filesystem
  stats                                          Count files per folder + last updated
  search "query"                                 Full-text search titles + tags + content
  missing-translation                            List en/ files without fr/ counterparts
  sync                                           git add + commit conventional + push origin

Requires: PyYAML (pip install pyyaml)
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)


WIKI_ROOT = Path(__file__).parent.parent
TEMPLATES = Path(__file__).parent / "templates"

# Required frontmatter fields (per _schema.md)
REQUIRED_FIELDS = ["id", "title", "type", "domain", "tags", "status", "created", "updated"]

# Type taxonomy (per _schema.md)
VALID_TYPES = {
    "meta", "profile", "cv", "stack", "availability", "expertise",
    "keywords", "education", "methodology", "process", "writing",
    "experience", "project", "personal",
}

# Top-level files that have fr/ counterparts
BILINGUAL_TOP_LEVEL = [
    "README.md", "profile.md", "cv.md", "stack.md", "availability.md",
    "expertise.md", "keywords.md", "education.md", "methodology.md",
    "process.md", "personal.md", "writing.md",
]

DATE = datetime.now().strftime("%Y-%m-%d")


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s_]+", "-", s).strip("-")


def parse_frontmatter(path: Path) -> tuple[dict | None, str | None]:
    """Returns (frontmatter_dict | None, error_message | None)."""
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None, "no frontmatter delimiter (---)"
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "frontmatter not closed"
    try:
        return yaml.safe_load(parts[1]), None
    except yaml.YAMLError as e:
        return None, f"YAML invalid: {str(e).splitlines()[0]}"


def cmd_new(args):
    """Scaffold a new wiki entry."""
    kind = args.kind
    title = args.title
    if not title:
        print(f"ERROR: title required. Usage: new {kind} \"Title\"")
        sys.exit(1)

    template_map = {
        "case": ("case-study.md", lambda s: WIKI_ROOT / "projects" / s / "case-study.md"),
        "project": ("project.md", lambda s: WIKI_ROOT / "projects" / s / f"{s}.md"),
        "experience": ("experience.md", lambda s: WIKI_ROOT / "experience" / f"{s}.md"),
        "writing": ("writing.md", lambda s: WIKI_ROOT / "writing" / f"{s}.md"),
        "expertise": ("expertise.md", lambda s: WIKI_ROOT / "expertise" / f"{s}.md"),
    }
    if kind not in template_map:
        print(f"ERROR: unknown kind '{kind}'. Available: {', '.join(template_map.keys())}")
        sys.exit(1)

    template_name, path_builder = template_map[kind]
    slug = slugify(title)
    target = path_builder(slug)

    if target.exists():
        print(f"ERROR: already exists: {target.relative_to(WIKI_ROOT)}")
        sys.exit(1)

    template = (TEMPLATES / template_name).read_text(encoding="utf-8")
    body = template.replace("{{ID}}", slug).replace("{{TITLE}}", title).replace("{{DATE}}", DATE)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8")
    print(f"Created: {target.relative_to(WIKI_ROOT)}")

    if kind == "case":
        assets = target.parent / "assets" / ".gitkeep"
        assets.parent.mkdir(parents=True, exist_ok=True)
        assets.touch()
        print(f"Created: {assets.relative_to(WIKI_ROOT)}")


def cmd_update(args):
    """Bump 'updated' field in a top-level file's frontmatter."""
    valid = ["cv", "profile", "stack", "availability", "methodology", "expertise", "keywords", "education", "process", "personal"]
    target = args.target
    if target not in valid:
        print(f"ERROR: unknown target '{target}'. Available: {', '.join(valid)}")
        sys.exit(1)

    path = WIKI_ROOT / f"{target}.md"
    if not path.exists():
        print(f"ERROR: file not found: {path.relative_to(WIKI_ROOT)}")
        sys.exit(1)

    content = path.read_text(encoding="utf-8")
    new_content = re.sub(
        r"(?m)^updated:\s*\S+\s*$",
        f"updated: {DATE}",
        content,
        count=1,
    )
    if new_content == content:
        print(f"WARN: no 'updated' field replaced. Check frontmatter manually.")
    else:
        path.write_text(new_content, encoding="utf-8")
        print(f"Bumped 'updated: {DATE}' in {path.relative_to(WIKI_ROOT)}")
    print(f"Now edit: {path}")


def collect_atoms() -> list[dict]:
    """Walk all .md files in the wiki, parse frontmatter."""
    atoms = []
    for md in WIKI_ROOT.rglob("*.md"):
        if "scripts" in md.parts or "node_modules" in md.parts or ".git" in md.parts:
            continue
        fm, err = parse_frontmatter(md)
        atoms.append({"path": md, "fm": fm, "error": err})
    return atoms


def cmd_validate(args):
    """Check frontmatter + wikilinks + IDs unique + bilingual + naming."""
    atoms = collect_atoms()
    errors = []
    warnings = []

    # Frontmatter check
    # IDs are tracked per language: same ID in en + fr/ is OK (bilingual mirror)
    ids_en = {}
    ids_fr = {}
    for a in atoms:
        rel = a["path"].relative_to(WIKI_ROOT)
        if a["error"]:
            errors.append(f"FRONTMATTER ISSUE ({a['error']}): {rel}")
            continue
        fm = a["fm"]
        for field in REQUIRED_FIELDS:
            if field not in fm:
                errors.append(f"MISSING FIELD '{field}': {rel}")
        if fm.get("type") and fm["type"] not in VALID_TYPES:
            errors.append(f"INVALID TYPE '{fm['type']}': {rel}")
        if fm.get("id"):
            is_fr = "fr" in rel.parts
            bucket = ids_fr if is_fr else ids_en
            if fm["id"] in bucket:
                errors.append(f"DUPLICATE ID '{fm['id']}': {bucket[fm['id']]} and {rel}")
            else:
                bucket[fm["id"]] = rel
    # Combined IDs set for wikilink check (en + fr counts)
    ids = {**ids_en, **ids_fr}

    # Naming convention (kebab-case)
    for a in atoms:
        name = a["path"].stem
        if name == "_schema" or name == "README":
            continue
        if not re.match(r"^[a-z0-9][a-z0-9-]*$", name):
            warnings.append(f"NAMING NOT KEBAB-CASE: {a['path'].relative_to(WIKI_ROOT)}")

    # Wikilinks check (basic [[ID]] syntax)
    wikilink_pattern = re.compile(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]")
    for a in atoms:
        if a["error"]:
            continue
        body = a["path"].read_text(encoding="utf-8")
        for match in wikilink_pattern.finditer(body):
            target = match.group(1).strip()
            # Strip trailing extension or path
            target_stripped = target.replace(".md", "").split("/")[-1]
            if target_stripped not in ids and not (WIKI_ROOT / target).exists() and not (WIKI_ROOT / f"{target}.md").exists():
                warnings.append(f"BROKEN WIKILINK [[{target}]] in {a['path'].relative_to(WIKI_ROOT)}")

    # Bilingual symmetry check
    fr_dir = WIKI_ROOT / "fr"
    if fr_dir.exists():
        for top in BILINGUAL_TOP_LEVEL:
            top_path = WIKI_ROOT / top
            fr_path = fr_dir / top
            if top_path.exists() and not fr_path.exists():
                warnings.append(f"MISSING FR TRANSLATION: {top} (no fr/{top})")

    # Confidential check
    confidential = [a for a in atoms if a["fm"] and a["fm"].get("confidential")]
    if confidential:
        for a in confidential:
            warnings.append(f"CONFIDENTIAL flagged: {a['path'].relative_to(WIKI_ROOT)} (review before push public)")

    if errors:
        print(f"\n{len(errors)} ERRORS:\n")
        for e in errors:
            print(f"  {e}")
    if warnings:
        print(f"\n{len(warnings)} WARNINGS:\n")
        for w in warnings:
            print(f"  {w}")

    if errors:
        sys.exit(1)
    if not warnings:
        print(f"OK: {len(atoms)} atoms valid, {len(ids)} unique IDs.")


def cmd_rebuild_llms_txt(args):
    """Regenerate llms.txt from current filesystem."""
    atoms = collect_atoms()
    lines = ["# Wiki Romain Bigache — LLM Index", "", "Auto-generated. Do not edit manually.", ""]

    by_type = {}
    for a in atoms:
        if a["error"] or not a["fm"]:
            continue
        if a["fm"].get("confidential"):
            continue
        t = a["fm"].get("type", "unknown")
        by_type.setdefault(t, []).append(a)

    for t in sorted(by_type.keys()):
        lines.append(f"## {t}")
        lines.append("")
        for a in sorted(by_type[t], key=lambda x: str(x["path"])):
            rel = a["path"].relative_to(WIKI_ROOT).as_posix()
            title = a["fm"].get("title", a["fm"].get("id", rel))
            tags = ", ".join(a["fm"].get("tags", []))
            lines.append(f"- [{title}](./{rel}) — `tags: {tags}`")
        lines.append("")

    target = WIKI_ROOT / "llms.txt"
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"Rebuilt: {target.relative_to(WIKI_ROOT)} ({sum(len(v) for v in by_type.values())} entries, {len(by_type)} types)")


def cmd_stats(args):
    """Count atoms per type + folder + last updated."""
    atoms = collect_atoms()
    by_type = {}
    by_folder = {}
    last_updated = None

    for a in atoms:
        if a["error"]:
            continue
        fm = a["fm"]
        t = fm.get("type", "unknown")
        by_type[t] = by_type.get(t, 0) + 1

        rel = a["path"].relative_to(WIKI_ROOT)
        folder = rel.parts[0] if len(rel.parts) > 1 else "(top-level)"
        by_folder[folder] = by_folder.get(folder, 0) + 1

        upd = fm.get("updated")
        if upd and (last_updated is None or str(upd) > str(last_updated)):
            last_updated = upd

    total = len(atoms)
    print(f"\nWiki Romain Bigache stats: {total} atoms\n")
    print("By type:")
    for t in sorted(by_type.keys(), key=lambda x: -by_type[x]):
        print(f"  {t:20s} {by_type[t]}")
    print("\nBy folder:")
    for f in sorted(by_folder.keys(), key=lambda x: -by_folder[x]):
        print(f"  {f:20s} {by_folder[f]}")
    print(f"\nLast updated: {last_updated}")


def cmd_search(args):
    """Full-text search."""
    query = args.query.lower()
    atoms = collect_atoms()
    matches = []
    for a in atoms:
        if a["error"]:
            continue
        body = a["path"].read_text(encoding="utf-8").lower()
        if query in body:
            title = a["fm"].get("title", a["fm"].get("id", ""))
            matches.append((a["path"], title))
    if matches:
        print(f"\n{len(matches)} matches for '{args.query}':\n")
        for p, t in matches:
            print(f"  {p.relative_to(WIKI_ROOT)}  {t}")
    else:
        print(f"No matches for '{args.query}'.")


def cmd_missing_translation(args):
    """List en/ files without fr/ counterparts."""
    fr_dir = WIKI_ROOT / "fr"
    if not fr_dir.exists():
        print("No fr/ directory found.")
        return
    missing = []
    for top in BILINGUAL_TOP_LEVEL:
        top_path = WIKI_ROOT / top
        fr_path = fr_dir / top
        if top_path.exists() and not fr_path.exists():
            missing.append(top)

    if missing:
        print(f"\n{len(missing)} files missing fr/ translation:\n")
        for f in missing:
            print(f"  {f}  →  fr/{f}")
    else:
        print("All top-level files have fr/ counterparts.")


def cmd_sync(args):
    """git add + commit + push origin."""
    msg = args.message or f"chore(wiki): update {DATE}"
    try:
        subprocess.run(["git", "-C", str(WIKI_ROOT), "add", "-A"], check=True)
        result = subprocess.run(
            ["git", "-C", str(WIKI_ROOT), "diff", "--cached", "--name-only"],
            capture_output=True, text=True, check=True,
        )
        if not result.stdout.strip():
            print("Nothing to commit.")
            return
        subprocess.run(["git", "-C", str(WIKI_ROOT), "commit", "-m", msg], check=True)
        subprocess.run(["git", "-C", str(WIKI_ROOT), "push", "origin", "main"], check=True)
        print(f"Pushed: {msg}")
    except subprocess.CalledProcessError as e:
        print(f"ERROR: git command failed: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Wiki Romain Bigache CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_new = sub.add_parser("new", help="Scaffold a new entry")
    p_new.add_argument("kind", choices=["case", "project", "experience", "writing", "expertise"])
    p_new.add_argument("title", nargs="?", default="")
    p_new.set_defaults(func=cmd_new)

    p_upd = sub.add_parser("update", help="Bump 'updated' field on a top-level file")
    p_upd.add_argument("target", help="cv | profile | stack | availability | methodology | expertise | keywords | education | process | personal")
    p_upd.set_defaults(func=cmd_update)

    p_val = sub.add_parser("validate", help="Check frontmatter + wikilinks + naming + bilingual")
    p_val.set_defaults(func=cmd_validate)

    p_llms = sub.add_parser("rebuild-llms-txt", help="Regenerate llms.txt from filesystem")
    p_llms.set_defaults(func=cmd_rebuild_llms_txt)

    p_stats = sub.add_parser("stats", help="Count atoms per type / folder / last updated")
    p_stats.set_defaults(func=cmd_stats)

    p_search = sub.add_parser("search", help="Full-text search")
    p_search.add_argument("query")
    p_search.set_defaults(func=cmd_search)

    p_miss = sub.add_parser("missing-translation", help="List en/ files without fr/")
    p_miss.set_defaults(func=cmd_missing_translation)

    p_sync = sub.add_parser("sync", help="git add + commit + push origin")
    p_sync.add_argument("-m", "--message", default=None, help="Commit message override")
    p_sync.set_defaults(func=cmd_sync)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
