# All-Timeline Gemini Video Prompts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace every edit-direction cell in both `Pormpt.md` files with a detailed English Gemini Omni video prompt while preserving the approved timeline and asset mix.

**Architecture:** Keep the existing six-column timeline and the first five columns unchanged except for necessary prompt IDs. Replace the sixth column with one or more self-contained 4–10 second prompts per row, then mirror the exact prompt payload from ENG to VIE. Update reusable rules so future episodes use the same contract.

**Tech Stack:** Markdown, PowerShell validation, SHA-256 integrity checks.

## Global Constraints

- Timeline remains continuous from `00:00` to `06:22` with 36 Scene/Sequence rows.
- Column six is named `Prompt Gemini Omni` in both files.
- Every prompt is written fully in English.
- Every clip duration is 4–10 seconds; 10 seconds is a maximum, not a default.
- Every `TIMED ACTION` starts at `0.0 s`, ends at the declared duration and has no gaps.
- Asset mix and reference-source columns remain available; a prompt does not reclassify every row as AI.
- No edit directions, status fields, production gates or release gates in `Pormpt.md`.
- Do not modify either `Kich_Ban.md`.
- Do not commit, branch or push without explicit user authorization.

---

### Task 1: Rewrite the English prompt map

**Files:**
- Modify: `Video/Why Lightning Strikes the Same Place Again and Again/eng/Pormpt.md`

**Interfaces:**
- Consumes: approved 36-row timeline, asset types, detailed content and sources.
- Produces: canonical English prompt payload for every Scene/Sequence.

- [ ] Rename column six to `Prompt Gemini Omni` and remove the editing-direction framing from the introduction.
- [ ] For S01–S36, replace editor instructions with complete English video prompts.
- [ ] Give every generated clip a unique prompt ID and declared duration of 4–10 seconds.
- [ ] Split rows longer than one useful AI clip into prompt A/B only when the narrative action requires it.
- [ ] Ensure graphic rows request clean plates/visual mechanisms without generated text, labels or unsupported data.

### Task 2: Mirror prompts into the Vietnamese map

**Files:**
- Modify: `Video/Why Lightning Strikes the Same Place Again and Again/vie/Pormpt.md`

**Interfaces:**
- Consumes: canonical prompt payloads from Task 1.
- Produces: Vietnamese timeline descriptions with identical English prompts.

- [ ] Rename column six to `Prompt Gemini Omni`.
- [ ] Remove all Vietnamese editing instructions from column six.
- [ ] Copy the complete English prompt payload for each matching Scene/Sequence from ENG.
- [ ] Preserve Vietnamese detailed-content descriptions and reference sources.

### Task 3: Persist the new project rules

**Files:**
- Modify: `.agent/AGENT.md`
- Modify: `docs/VISUAL STORYTELLING PLAYBOOK.md`
- Modify: `docs/Bố_Cục_prompt.md`

**Interfaces:**
- Consumes: approved design spec.
- Produces: reusable rule contract for future `Pormpt.md` files.

- [ ] Replace the mixed `Hướng dẫn edit / Prompt` rule with a prompt-only sixth column.
- [ ] Require English video prompts on every timeline row in ENG and VIE.
- [ ] Record how REAL/graphic rows use prompts without changing the primary asset classification.
- [ ] Record multi-prompt behavior for timeline rows longer than a single 10-second clip.

### Task 4: Validate the complete change

**Files:**
- Verify: both `Pormpt.md` files and three rule documents.
- Verify unchanged: both `Kich_Ban.md` files.

**Interfaces:**
- Consumes: Tasks 1–3 outputs.
- Produces: fresh pass/fail evidence.

- [ ] Parse both Markdown tables and assert 36 rows, six columns and continuous `00:00–06:22` coverage.
- [ ] Assert every sixth-column cell contains English prompt structure and no edit-direction phrases.
- [ ] Assert every duration is 4–10 seconds and every timed action covers its declared duration.
- [ ] Assert ENG/VIE prompts match by Scene ID.
- [ ] Assert removed gates/status sections remain absent.
- [ ] Compare both `Kich_Ban.md` SHA-256 hashes with the recorded pre-change hashes.
