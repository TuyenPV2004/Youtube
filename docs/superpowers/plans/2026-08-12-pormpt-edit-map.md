# Pormpt Edit Map Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Do not use subagents unless the user explicitly requests delegation.

**Goal:** Replace both episode `Pormpt.md` files with detailed timeline-driven edit maps that combine real footage, AI video and 2D/3D graphics, with multiple source references and second-by-second Gemini Omni prompts.

**Architecture:** The English file is the canonical edit map. The Vietnamese file mirrors every timeline row, asset decision, source and full English Gemini prompt while explaining edit direction in Vietnamese. Project rules are updated so future episodes use the same six-column structure.

**Tech Stack:** Markdown, PowerShell validation, web research using primary/official pages and direct stock item pages.

## Global Constraints

- Keep the filename `Pormpt.md` exactly as established by the repository.
- Do not modify `Kich_Ban.md` or any Voiceover wording.
- Timeline starts at `00:00`, ends at `06:22` and covers the radio edit continuously.
- Main table columns are exactly: `Timeline`, `Scene / Sequence`, `Asset`, `Nội dung chi tiết`, `Nguồn tham khảo`, `Hướng dẫn edit / Prompt Gemini Omni` (translated headings are allowed in ENG).
- There is no `Status` / `Trạng thái` column.
- AI clips use flexible durations from 4 to 10 seconds; 10 seconds is a maximum, not a default.
- Every AI prompt covers every second of its clip and is directly copyable into Gemini Omni.
- The VIE file contains full English Gemini prompts and must not redirect the user to the ENG file.
- Remove the requested motion-graphic recipe, rights/release, final-gate, production and public-release sections.
- Do not commit, stage, push or modify Git history; the user requested file edits, not Git actions.

---

### Task 1: Research candidate sources for real footage

**Files:**
- Read: `Video/Why Lightning Strikes the Same Place Again and Again/eng/Kich_Ban.md`
- Read: `Video/Why Lightning Strikes the Same Place Again and Again/eng/Pormpt.md`

**Produces:** A verified working set of direct candidate links for repeated lightning, thundercloud development, lightning flicker/multiple strokes, and protected tall infrastructure.

- [ ] Search at least three relevant candidates per real-footage group where suitable results exist.
- [ ] Prefer a mix of official/scientific media and direct stock item pages.
- [ ] Open the candidate page before including its URL.
- [ ] Record what each candidate can contribute and add alternate search terms.

### Task 2: Build the canonical English edit map

**Files:**
- Modify: `Video/Why Lightning Strikes the Same Place Again and Again/eng/Pormpt.md`

**Produces:** A self-contained English edit map covering `00:00–06:22`.

- [ ] Replace the existing media map with the approved six-column structure.
- [ ] Split the 11 narration beats into smaller Scene/Sequence rows where the visual idea changes.
- [ ] Assign the best-fitting real footage, A-roll/B-roll, AI video, 2D, 3D or composite asset to every row.
- [ ] Expand every content cell with voice cue, visual role, action, subject/environment, camera/composition and transition.
- [ ] Put multiple source candidates and alternate search terms in every real-footage row.
- [ ] Write a dedicated Gemini Omni prompt for every AI asset, using a 4–10 second duration and complete timed actions.
- [ ] Put 2D/3D build instructions directly in the relevant timeline row.
- [ ] Remove all disallowed sections and all status language.

### Task 3: Build the self-contained Vietnamese edit map

**Files:**
- Modify: `Video/Why Lightning Strikes the Same Place Again and Again/vie/Pormpt.md`

**Consumes:** The final timeline, assets, sources and prompts from the English edit map.

**Produces:** A Vietnamese edit map with identical production decisions and full English AI prompts.

- [ ] Mirror every timeline boundary and Scene/Sequence ID.
- [ ] Translate content and edit guidance into natural Vietnamese.
- [ ] Preserve all direct source links.
- [ ] Include every Gemini Omni prompt in full English for direct copy/paste.
- [ ] Remove references that instruct the user to look at the ENG file for missing details.

### Task 4: Persist the new Pormpt rules

**Files:**
- Modify: `.agent/AGENT.md`
- Modify: `docs/VISUAL STORYTELLING PLAYBOOK.md`
- Modify: `docs/Bố_Cục_prompt.md`

**Produces:** Future project instructions that match the approved Pormpt format.

- [ ] Replace mandatory Status/rights-gate structure with the six-column edit-map definition.
- [ ] Record Scene/Sequence and asset-selection rules.
- [ ] Require detailed content cells and multiple source references.
- [ ] Require Gemini Omni prompts with 4–10 second durations and full timed action.
- [ ] State that the VIE file contains full English copy-ready prompts.

### Task 5: Validate the implementation

**Files:**
- Test: both episode `Pormpt.md` files and the three updated rule files.

- [ ] Confirm both edit maps start at `00:00`, end at `06:22` and have matching row boundaries.
- [ ] Confirm the main tables have six columns and no Status/Trạng thái column.
- [ ] Confirm every real-footage group has multiple source links or documented alternate searches.
- [ ] Confirm every AI asset has a 4–10 second duration and timed actions with no uncovered interval.
- [ ] Confirm the VIE file contains full English prompts.
- [ ] Confirm removed headings/lines are absent.
- [ ] Confirm hashes of both `Kich_Ban.md` files did not change during implementation.
- [ ] Report any candidate source that could not be fully verified.

