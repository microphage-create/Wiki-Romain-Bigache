---
id: project-video-transcriber
title: Video Transcriber + voice chat (CLI and live)
type: project
domain: project
tags: [transcription, whisper, ffmpeg, python, cli, audio, video, speech-to-text, openai-whisper, srt, voice-chat, mediarecorder, nextjs, tooling]
status: live
created: 2026-05-06
updated: 2026-05-06
period: 2026-02 / present
client: Personal / Microphage internal
industries: [Internal Tooling, AI/ML, Productivity, Media]
team: 1 (Romain Bigache, solo)
url: https://romainbigache.com
demo: https://romainbigache.com (voice input in the AI chat, live)
technologies: [Python, ffmpeg, openai-whisper, OpenAI Whisper API, Next.js 16, MediaRecorder Web API, SpeechRecognition Web API, TypeScript]
links:
  - projects/romainbigache-com.md
  - projects/mycelium.md
  - stack.md
---

# Video Transcriber + voice chat

| Key | Value |
|-----|-------|
| **Type** | Audio/video transcription pipeline. CLI tool + live voice chat for AI agents |
| **Status** | In production. CLI in daily use. Voice chat live on romainbigache.com |
| **Year** | 2026 - ongoing |
| **Team** | Romain Bigache (solo) |
| **Visibility** | CLI: internal Microphage tool. Voice chat: live on romainbigache.com |

## Short title

Two-surface speech-to-text pipeline: a Python CLI for batch transcription, and a live voice input layer plugged into AI agents.

## Short description

Two complementary surfaces, same goal: turn audio/video into text usable by an AI agent or a human reviewer.

**Surface 1, CLI**: `video-transcriber.py`, Python tool to extract audio from MP4 (or any ffmpeg-supported format) and transcribe it to `.txt` or `.srt` subtitles. Two modes: local on CPU via `openai-whisper`, or remote via the OpenAI Whisper API with auto-chunking for files above 24 MB. Batch mode on a folder, model size selectable, language overridable.

**Surface 2, live voice chat**: Whisper-powered voice input embedded in the AI chat on romainbigache.com (and morphow-portal). WhatsApp-style UX: record button, scrolling waveform with noise gate, auto-stop on 2.5s of silence, transcript dropped into the input for human review before sending. MediaRecorder + SpeechRecognition fallback in browser, OpenAI Whisper-1 server-side with auth and rate limiting.

Both surfaces are wired to feed an agent: the CLI for prepared material (interviews, meetings, podcasts), the live chat for real-time interaction with an AI persona.

## Long description

### Surface 1, CLI: video-transcriber.py

#### Problem

Need to transcribe long audio/video files (interviews, recorded meetings, podcasts) without paying SaaS subscription fees, and without uploading sensitive material to a third-party SaaS UI. Also need batch processing on a folder.

#### Solution

A 600-line Python CLI. Single command, both modes:

```bash
python video-transcriber.py video.mp4                # local CPU, FR, small model
python video-transcriber.py video.mp4 --api          # OpenAI Whisper API, ~1-2 min/h
python video-transcriber.py folder/                  # batch all MP4 in folder
python video-transcriber.py video.mp4 --srt          # subtitles output
python video-transcriber.py video.mp4 --lang en      # force English
```

#### Architecture

- ffmpeg extracts the audio: WAV 16 kHz mono for local mode, MP3 mono 48 kbps for API mode (compact upload).
- ffprobe pulls duration up front, used to estimate cost (API) or processing time (local).
- Local mode: `openai-whisper` Python package, model selectable from `tiny` to `large`, model cached across batch.
- API mode: OpenAI Whisper-1 endpoint. Auto-detects when audio is over 24 MB and splits into 20-minute chunks via ffmpeg, transcribes each, reassembles segments with corrected time offsets.
- Output formats: plain text or SRT subtitles with proper `HH:MM:SS,mmm` timestamps.
- Console UI: header with mode, language, format, file count, cost estimate; per-file progress with steps (extract, transcribe, export); summary table with per-file segment count and timing.

#### Why both modes

- **Local**: free, offline, no upload. Slower on CPU (a 1h video on `small` model takes 20-40 min). Used for sensitive material or when the API quota is irrelevant.
- **API**: 1-2 min for a 1h video at \$0.006/min. Used when speed matters (live workflows, rapid turnaround on client deliverables).

The same tool covers both situations without reconfiguration.

### Surface 2, live voice chat (romainbigache.com, morphow-portal)

#### Problem

A typed chat UI is fast for desktop users with technical fluency. For exploratory conversations, demo with a non-technical participant, or simply a more natural interview-like interaction with an AI agent, voice is the right input. The transcription must appear in the input field for human review before the message is actually sent: the user wants to read what was heard before pressing send.

#### Solution

A persistent voice input layer plugged into the existing AI chat:

- **UX**: WhatsApp-style. Three buttons height/width matched (h-10 w-10): trash (cancel), pause, validate (check). Same container as the typed input, only the inner content morphs (no cheap component swap).
- **Waveform**: 2px-wide bars, scrolling right to left. Noise gate at amplitude < 12 flattens the bars (silence is visibly silence, not background fuzz).
- **Auto-stop on silence**: 2.5s of silence after the first detected speech triggers an auto-validate, with a pulse on the check button. The silence countdown only starts after the first speech is detected: no false triggers from initial environment noise.
- **Flow**: user speaks, silence is detected, Whisper transcribes server-side, the text drops into the input field, focus moves there automatically, the user reviews and presses send manually. No auto-send.

#### Server-side

- Endpoint `/api/chat/whisper`: cookie-based auth, rate limiting, OpenAI Whisper-1 transcription.
- Browser-side primary: MediaRecorder Web API records progressive 1-second chunks.
- Browser-side fallback: SpeechRecognition Web API, used when no API key is configured (offline / dev fallback).
- i18n FR and EN out of the box (`transcribing`, `listening` keys).

#### Why the no-auto-send rule

Voice input on a chat with an AI agent must let the human read the transcript before the message goes. Auto-send would surface every misheard word straight into the conversation. Asymmetric error cost: a missed word in a casual chat is friction, the same missed word on a regulated topic is a problem. Read-before-send is the default.

## Use cases covered

- Transcribe a long-form interview into a `.txt` ready to feed a RAG agent.
- Generate `.srt` subtitles for a client video deliverable.
- Capture a vocal note on the phone, drop the MP4 in the folder, batch-transcribe overnight.
- In a live design fiction or research interview: have a participant talk to an AI persona via voice, see the transcript appear, validate before send.
- Couple the CLI (offline interviews) and the live chat (in-room interaction with an AI persona) to cover the full pipeline of a workshop: live capture + post-workshop transcription for synthesis.

## Technologies used

### CLI

- Python 3
- `ffmpeg` and `ffprobe` (audio extraction, duration probing, chunking)
- `openai-whisper` (local CPU mode, models `tiny` to `large`)
- `openai` Python SDK (API mode, Whisper-1)
- `argparse`, `glob`, `pathlib`, `tempfile`, `subprocess`

### Live voice chat

- Next.js 16, strict TypeScript
- MediaRecorder Web API (primary recording path)
- SpeechRecognition Web API (browser fallback)
- OpenAI Whisper-1 (server-side transcription)
- Server endpoint with auth + rate limiting
- shadcn/ui + Tailwind for the input UI
- i18n FR and EN

## Impact

- CLI in daily use on Microphage workflows: post-meeting notes, interview transcripts, vocal-to-text capture, subtitle generation for client video deliverables.
- Voice chat live in production on **romainbigache.com**: a recruiter or visitor can have a vocal interaction with the AI assistant on the site instead of typing. Tested by external visitors since rollout.
- Same pattern reusable on a design fiction or research workshop: voice interaction with an AI persona in the room, transcripts captured for synthesis.

## Why it matters in context

For any project that needs voice as an input channel to an AI agent (interviews, design fiction, accessibility, multilingual interaction), this pipeline is already wired and tested. The two surfaces cover the two tempos: the CLI for prepared material and post-session synthesis, the live chat for in-room real-time interaction. End-to-end ownership: extraction, chunking, transcription, UX, server-side auth, fallback, i18n, no-auto-send rule.

## Related

- [projects/romainbigache-com.md](./romainbigache-com.md)
- [projects/mycelium.md](./mycelium.md)
- [stack.md](../stack.md)
