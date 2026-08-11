from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline


TIMELINE_ROW = re.compile(r"^\|\s*(\d{2}:\d{2}[–-]\d{2}:\d{2})\s*\|")


def extract_voiceover(script_path: Path) -> list[dict[str, str]]:
    chunks: list[dict[str, str]] = []
    for line in script_path.read_text(encoding="utf-8").splitlines():
        match = TIMELINE_ROW.match(line)
        if not match:
            continue
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) != 7:
            raise ValueError(f"Unexpected timeline row structure: {line}")
        voiceover = cells[4]
        if voiceover.startswith("“") and voiceover.endswith("”"):
            voiceover = voiceover[1:-1]
        if not voiceover:
            raise ValueError(f"Empty voiceover at {match.group(1)}")
        chunks.append({"timeline": match.group(1), "text": voiceover})

    if not chunks:
        raise ValueError("No timeline voiceover chunks found")
    return chunks


def render(
    chunks: list[dict[str, str]],
    output_path: Path,
    voice: str,
    speed: float,
    section_pause_seconds: float,
) -> dict[str, object]:
    sample_rate = 24_000
    pipeline = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
    silence = np.zeros(round(sample_rate * section_pause_seconds), dtype=np.float32)
    rendered: list[np.ndarray] = []
    chunk_manifest: list[dict[str, object]] = []
    cursor_samples = 0

    for chunk_index, chunk in enumerate(chunks, start=1):
        parts: list[np.ndarray] = []
        for _, _, audio in pipeline(chunk["text"], voice=voice, speed=speed):
            parts.append(np.asarray(audio, dtype=np.float32))
        if not parts:
            raise RuntimeError(f"Kokoro returned no audio for {chunk['timeline']}")

        chunk_audio = np.concatenate(parts)
        start_seconds = cursor_samples / sample_rate
        rendered.append(chunk_audio)
        cursor_samples += len(chunk_audio)
        end_seconds = cursor_samples / sample_rate
        chunk_manifest.append(
            {
                "index": chunk_index,
                "script_timeline": chunk["timeline"],
                "actual_start_seconds": round(start_seconds, 3),
                "actual_end_seconds": round(end_seconds, 3),
                "duration_seconds": round(end_seconds - start_seconds, 3),
                "word_count": len(re.findall(r"\b[\w’'-]+\b", chunk["text"])),
                "text_sha256": hashlib.sha256(chunk["text"].encode("utf-8")).hexdigest(),
            }
        )
        if chunk_index < len(chunks):
            rendered.append(silence)
            cursor_samples += len(silence)

    audio = np.concatenate(rendered)
    peak = float(np.max(np.abs(audio)))
    if peak > 0.98:
        audio = audio * (0.98 / peak)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(output_path, audio, sample_rate, subtype="PCM_24")

    word_count = sum(int(chunk["word_count"]) for chunk in chunk_manifest)
    duration_seconds = len(audio) / sample_rate
    return {
        "file": output_path.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_script": str(output_path.parent.parent / "eng" / "Kich_Ban.md"),
        "source_script_sha256_at_generation": hashlib.sha256(
            (output_path.parent.parent / "eng" / "Kich_Ban.md").read_bytes()
        ).hexdigest(),
        "source_voiceover_sha256": hashlib.sha256(
            "\n\n".join(chunk["text"] for chunk in chunks).encode("utf-8")
        ).hexdigest(),
        "model": "hexgrad/Kokoro-82M v1.0",
        "kokoro_package": "0.9.4",
        "voice": voice,
        "lang_code": "a",
        "speed": speed,
        "sample_rate_hz": sample_rate,
        "channels": 1,
        "subtype": "PCM_24",
        "section_pause_seconds": section_pause_seconds,
        "word_count": word_count,
        "duration_seconds": round(duration_seconds, 3),
        "effective_wpm": round(word_count / (duration_seconds / 60), 2),
        "chunks": chunk_manifest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--voice", default="af_heart")
    parser.add_argument("--speed", type=float, default=0.86)
    parser.add_argument("--section-pause", type=float, default=0.65)
    args = parser.parse_args()

    chunks = extract_voiceover(args.script)
    manifest = render(
        chunks,
        args.output,
        voice=args.voice,
        speed=args.speed,
        section_pause_seconds=args.section_pause,
    )
    manifest_path = args.output.with_suffix(".json")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
