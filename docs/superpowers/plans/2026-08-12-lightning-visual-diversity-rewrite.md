# Lightning Visual Diversity Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the 36-scene lightning asset-prompt map so each timeline advances the story with a distinct visual idea instead of restaging the same storm, tower and strike.

**Architecture:** Preserve the approved narration timeline and six-column document contract. Assign every row a visual fingerprint—subject, action, scale, representation and new information—then rewrite Asset, Detailed content and Gemini prompt where necessary. ENG remains English; VIE remains Vietnamese with equivalent visual intent.

**Tech Stack:** Markdown and PowerShell validation.

## Global Constraints

- Do not modify either `Kich_Ban.md`.
- Preserve 36 continuous timeline rows from `00:00` to `06:22`.
- Preserve the six columns and existing source links unless a source no longer fits the redesigned visual.
- Adjacent scenes must not repeat the same core subject, setting and action merely with different lens, lighting or wording.
- Every scene must introduce a new visual function or information layer.
- ENG prompts use English; VIE prompts use Vietnamese.
- Every Gemini clip remains 4–10 seconds with complete timed action.
- Intentional repetition is allowed only for a clearly marked return/payoff, such as S34 returning to the opening composition.
- Do not perform Git operations.

### Task 1: Design the 36-scene visual progression

- [ ] Assign each scene a distinct narrative function and visual fingerprint.
- [ ] Audit every adjacent pair for repeated subject, action, scale and representation.
- [ ] Replace superficial variants with a different visual mode: observation, evidence, measurement, macro, cutaway, diagram, comparison, consequence, infrastructure or safety behavior.

### Task 2: Rewrite ENG Pormpt.md

- [ ] Update Asset and Detailed content where the visual concept changes.
- [ ] Replace all 36 Gemini prompts with prompts matching the redesigned visual fingerprints.
- [ ] Keep source references aligned with the primary asset.

### Task 3: Rewrite VIE Pormpt.md

- [ ] Mirror the redesigned Asset and visual meaning.
- [ ] Write all 36 prompts naturally in Vietnamese, preserving IDs, durations and timed actions.

### Task 4: Persist the lesson

- [ ] Add the visual-fingerprint rule to `.agent/AGENT.md`.
- [ ] Add continuity-without-repetition and adjacent-scene diversity rules to `docs/VISUAL STORYTELLING PLAYBOOK.md`.
- [ ] Add prompt-sequence auditing guidance to `docs/Bố_Cục_prompt.md`.

### Task 5: Validate

- [ ] Verify table shape, continuous timeline and prompt durations.
- [ ] Verify ENG/VIE language and semantic Scene-ID alignment.
- [ ] Verify adjacent scenes do not share the same declared visual fingerprint.
- [ ] Verify both `Kich_Ban.md` hashes remain unchanged.
