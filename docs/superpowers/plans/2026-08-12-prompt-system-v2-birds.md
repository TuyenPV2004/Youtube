# Prompt System v2 and Birds Visual Plan Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace mandatory per-row Gemini prompts with routed execution specifications, add a reusable project skill and static validator, then rebuild the English and Vietnamese Birds visual plans without changing either locked script.

**Architecture:** `Pormpt.md` remains a six-column timeline, but the last column becomes a typed `Execution Spec`. A project skill defines Scene Contracts, Asset Router rules, generation-mode compilers, failure modes, and QA; dependency-free Python scripts validate the mechanical parts. The Birds plans become the first complete production example and the Lightning failures become regression fixtures rather than another migration target.

**Tech Stack:** Markdown, Python 3 standard library (`argparse`, `dataclasses`, `pathlib`, `re`, `unittest`), PowerShell validation commands.

## Global Constraints

- Do not modify either Birds `Kich_Ban.md`.
- Preserve exactly six timeline columns: `Timeline`, `Scene / Sequence`, `Asset`, `Nội dung chi tiết`/`Detailed Content`, `Nguồn tham khảo`/`Reference Sources`, `Execution Spec`.
- Every row has exactly one supported execution mode; only generative-video modes contain a copy-ready Gemini Omni/Veo prompt.
- `EDITOR_MG` must never compile to a generative-video prompt.
- AI and hybrid rows must define Scene Contract fields required by their representation and mechanism.
- Technical labels, topology, measurements, potential gradients, and equations remain editor-controlled.
- AI clip duration is 4–10 seconds and every `TIMED ACTION` covers `0.0 s` through the declared duration without gaps or overlaps.
- ENG and VIE must match Asset ID, timeline, mode, duration, state transition, and failure exclusions; operational prompt prose is English in ENG and natural Vietnamese in VIE.
- Use no new third-party dependency when Python standard library is sufficient.
- Do not modify unrelated files, generated files, lockfiles, Git history, branches, or remotes.
- Do not commit: repository rules require explicit user authorization, and none has been given.
- Do not regenerate Lightning S01–S36 in this implementation; use selected Lightning scenes only as regression evidence.

---

### Task 1: Freeze Baselines and Create Failing Validator Tests

**Files:**
- Create: `.agents/skills/video-prompt-engineering/tests/test_lint_pormpt.py`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/good/minimal_execution_spec.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/graphic_with_generative_prompt.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/abstract_without_semantics.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/timed_action_gap.md`
- Inspect only: `Video/Why Birds Don’t Get Electrocuted on Power Lines — Until They Do/eng/Kich_Ban.md`
- Inspect only: `Video/Why Birds Don’t Get Electrocuted on Power Lines — Until They Do/vie/Kich_Ban.md`

**Interfaces:**
- Consumes: approved design at `docs/superpowers/specs/2026-08-12-prompt-system-v2-birds-design.md`.
- Produces: fixture format and test expectations for `lint_pormpt.py`; SHA-256 baseline values recorded in command output before edits.

- [ ] **Step 1: Read skill-authoring instructions before creating the project skill**

Read completely:

```powershell
Get-Content -Raw -Encoding utf8 'C:\Users\Tuyen\.codex\skills\.system\skill-creator\SKILL.md'
Get-Content -Raw -Encoding utf8 'C:\Users\Tuyen\.codex\plugins\cache\openai-curated-remote\superpowers\6.2.0\skills\writing-skills\SKILL.md'
Get-Content -Raw -Encoding utf8 'C:\Users\Tuyen\.codex\plugins\cache\openai-curated-remote\superpowers\6.2.0\skills\test-driven-development\SKILL.md'
```

Expected: all three instruction files are readable; stop and report the exact missing path if one cannot be read.

- [ ] **Step 2: Record locked-script hashes and current worktree state**

Run:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Kich_Ban.md','Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Kich_Ban.md'
git status --short
```

Expected: two SHA-256 hashes are captured; existing unrelated changes are identified and preserved.

- [ ] **Step 3: Write minimal good and bad fixtures**

The good fixture contains one row with `MODE: GMO_TEXT_TO_VIDEO`, all required contract headings, `DURATION: 4 seconds`, and contiguous intervals `0.0–2.0 s` and `2.0–4.0 s`.

The bad fixtures encode these exact failures:

```text
E_MODE_PROMPT: MODE: EDITOR_MG contains PROMPT:
E_VISUAL_SEMANTICS: abstract term "electric field" appears without VISUAL_SEMANTICS
E_TIMING_GAP: duration 6 seconds contains 0.0–2.0 s then 3.0–6.0 s
```

- [ ] **Step 4: Write failing unit tests against the intended public API**

```python
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lint_pormpt import lint_document


class LintPormptTests(unittest.TestCase):
    def fixture(self, group: str, name: str) -> Path:
        return Path(__file__).parent / "fixtures" / group / name

    def codes(self, group: str, name: str) -> set[str]:
        return {issue.code for issue in lint_document(self.fixture(group, name))}

    def test_minimal_execution_spec_passes(self):
        self.assertEqual([], lint_document(self.fixture("good", "minimal_execution_spec.md")))

    def test_editor_graphic_rejects_generative_prompt(self):
        self.assertIn("E_MODE_PROMPT", self.codes("bad", "graphic_with_generative_prompt.md"))

    def test_abstract_mechanism_requires_visual_semantics(self):
        self.assertIn("E_VISUAL_SEMANTICS", self.codes("bad", "abstract_without_semantics.md"))

    def test_timed_action_rejects_gap(self):
        self.assertIn("E_TIMING_GAP", self.codes("bad", "timed_action_gap.md"))
```

- [ ] **Step 5: Run tests and confirm the RED state**

Run:

```powershell
python -m unittest discover -s '.agents\skills\video-prompt-engineering\tests' -p 'test_*.py' -v
```

Expected: FAIL because `lint_pormpt` does not exist yet; a passing result means the test does not exercise the intended missing implementation.

---

### Task 2: Implement the Dependency-Free Preflight Validator

**Files:**
- Create: `.agents/skills/video-prompt-engineering/scripts/lint_pormpt.py`
- Create: `.agents/skills/video-prompt-engineering/scripts/validate_timeline.py`
- Modify: `.agents/skills/video-prompt-engineering/tests/test_lint_pormpt.py`
- Create: `.agents/skills/video-prompt-engineering/tests/test_validate_timeline.py`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/non_contiguous_timeline.md`

**Interfaces:**
- Consumes: Markdown fixture convention from Task 1.
- Produces:
  - `Issue(code: str, message: str, line: int | None)` dataclass.
  - `lint_document(path: Path) -> list[Issue]`.
  - `lint_pair(eng_path: Path, vie_path: Path) -> list[Issue]`.
  - `validate_timeline_ranges(ranges: list[str]) -> list[Issue]`.
  - CLI exit code `0` for pass and `1` for lint failures.

- [ ] **Step 1: Add a failing timeline continuity test**

```python
from validate_timeline import validate_timeline_ranges


def test_timeline_gap_is_rejected():
    issues = validate_timeline_ranges(["00:00–00:04", "00:05–00:08"])
    assert {issue.code for issue in issues} == {"E_TIMELINE_GAP"}
```

Use `unittest.TestCase` syntax in the actual repository test file to avoid adding pytest.

- [ ] **Step 2: Run the focused tests and confirm failure**

Run:

```powershell
python -m unittest discover -s '.agents\skills\video-prompt-engineering\tests' -p 'test_*.py' -v
```

Expected: existing Task 1 failures remain, plus import failure for `validate_timeline`.

- [ ] **Step 3: Implement `lint_pormpt.py` with explicit rule codes**

Implement:

```python
@dataclass(frozen=True)
class Issue:
    code: str
    message: str
    line: int | None = None


VALID_MODES = {
    "REAL_SOURCE",
    "EDITOR_MG",
    "GMO_TEXT_TO_VIDEO",
    "GMO_REFERENCE_VIDEO",
    "VEO_FIRST_FRAME",
    "VEO_FIRST_LAST",
    "HYBRID",
}

GENERATIVE_MODES = {
    "GMO_TEXT_TO_VIDEO",
    "GMO_REFERENCE_VIDEO",
    "VEO_FIRST_FRAME",
    "VEO_FIRST_LAST",
    "HYBRID",
}
```

The parser must locate the six-column table without a third-party Markdown parser, preserve `<br>`-separated field headings inside cells, and report these stable codes:

```text
E_TABLE_SCHEMA
E_MODE_MISSING
E_MODE_INVALID
E_MODE_PROMPT
E_PROMPT_MISSING
E_CONTRACT_FIELD
E_VISUAL_SEMANTICS
E_INVARIANTS
E_GUARDRAIL
E_NOT_YET_TRUE
E_DURATION_RANGE
E_TIMING_START
E_TIMING_END
E_TIMING_GAP
E_TIMING_OVERLAP
E_PAIR_MISMATCH
```

Abstract-term detection is intentionally conservative: `electric field`, `potential`, `charge redistribution`, `energy flow`, and `probability field` trigger `VISUAL_SEMANTICS` only in generative modes.

- [ ] **Step 4: Implement timeline validation and CLI**

`validate_timeline.py` converts `MM:SS–MM:SS` or `MM:SS-MM:SS` to integer seconds and reports:

```text
E_TIMELINE_FORMAT
E_TIMELINE_REVERSED
E_TIMELINE_GAP
E_TIMELINE_OVERLAP
```

Both scripts accept one or two paths via `argparse`, print `CODE: path:line: message`, and return exit code `1` when any issue exists.

- [ ] **Step 5: Run all validator tests and confirm GREEN**

Run:

```powershell
python -m unittest discover -s '.agents\skills\video-prompt-engineering\tests' -p 'test_*.py' -v
```

Expected: all tests PASS.

- [ ] **Step 6: Run syntax compilation**

Run:

```powershell
python -m py_compile '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' '.agents\skills\video-prompt-engineering\scripts\validate_timeline.py'
```

Expected: exit code 0 and no output.

---

### Task 3: Author the Reusable Video Prompt Engineering Skill

**Files:**
- Create: `.agents/skills/video-prompt-engineering/SKILL.md`
- Create: `.agents/skills/video-prompt-engineering/references/asset-routing.md`
- Create: `.agents/skills/video-prompt-engineering/references/scene-contract.md`
- Create: `.agents/skills/video-prompt-engineering/references/generation-modes.md`
- Create: `.agents/skills/video-prompt-engineering/references/scientific-visual-semantics.md`
- Create: `.agents/skills/video-prompt-engineering/references/failure-modes.md`
- Create: `.agents/skills/video-prompt-engineering/references/examples.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/f001_multiple_attachment.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/f002_field_to_network.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/f003_geometry_morph.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/f004_abstract_substitution.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/f005_temporal_collapse.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/f006_premature_discharge.md`
- Create: `.agents/skills/video-prompt-engineering/tests/fixtures/bad/f007_scientific_ambiguity.md`

**Interfaces:**
- Consumes: validator rule names from Task 2 and approved design vocabulary.
- Produces: skill instructions loaded by agents before any future `Pormpt.md` creation/modification; failure-code definitions shared by prompt review and post-generation QA.

- [ ] **Step 1: Verify the project skill location and manifest rules from the loaded skill-authoring instructions**

Expected decision: use `.agents/skills/video-prompt-engineering/` if supported by the current Codex skill convention; if official/local instructions require another project-relative location, update all plan paths consistently before creating files.

- [ ] **Step 2: Write `SKILL.md` as a router, not a monolith**

Required frontmatter and trigger description:

```yaml
---
name: video-prompt-engineering
description: Create, modify, review, lint, or QA Pormpt.md visual execution specifications for documentary videos, including asset routing, Scene Contracts, Gemini Omni/Veo prompt compilation, technical graphics, and generated-video failure analysis.
---
```

The body must require this order:

```text
Read project rules → verify locked narration/evidence → fingerprint scene
→ write Scene Contract → run Asset Router → select mode
→ compile only if generative → lint → generate externally
→ compare output with contract → keep/trim/regenerate
```

It must route readers to only the reference file needed for the current stage and show the exact lint commands.

- [ ] **Step 3: Write focused references**

Each file has one responsibility:

- `asset-routing.md`: decision tree and mode definitions.
- `scene-contract.md`: required fields, conditional fields, invariants, not-yet-true, and one-dominant-change rule.
- `generation-modes.md`: compiler templates for text, reference, first frame, first/last, hybrid, and the `EDITOR_MG` no-compile rule.
- `scientific-visual-semantics.md`: pixel definitions for invisible mechanisms and allowed/excluded representation pattern.
- `failure-modes.md`: F001–F007 with symptom, likely cause, prompt rule, lint signal, QA question, and repair strategy.
- `examples.md`: one good AI contract/prompt, one good real-source brief, one good editor-MG build spec, and bad-to-good S10-style conversion.

- [ ] **Step 4: Encode F001–F007 fixtures and expected failure assertions**

Add tests that map every bad fixture to at least one stable lint code. Static lint may use a structural proxy; document when `F007` still requires human QA rather than pretending it is fully machine-detectable.

- [ ] **Step 5: Run the skill validator supplied by `skill-creator`**

Run the exact validation script/command named by the loaded `skill-creator` instructions. If no validator is available, manually check frontmatter, skill name, referenced-file existence, and absence of stale placeholders.

- [ ] **Step 6: Re-run unit tests**

Run:

```powershell
python -m unittest discover -s '.agents\skills\video-prompt-engineering\tests' -p 'test_*.py' -v
```

Expected: all tests PASS, including F001–F007 structural regression checks.

---

### Task 4: Align Repository Rules and Production Documentation

**Files:**
- Modify: `.agent/AGENT.md`
- Modify: `docs/Bố_Cục_prompt.md`
- Modify: `docs/VISUAL STORYTELLING PLAYBOOK.md`
- Modify: `docs/Quy_trình.md`
- Modify: `docs/Check_List.md`

**Interfaces:**
- Consumes: skill vocabulary and validator commands from Tasks 2–3.
- Produces: one non-contradictory repository-wide workflow that future agents must follow.

- [ ] **Step 1: Write a documentation regression scan before edits**

Run and save the occurrences that must be removed or rewritten:

```powershell
rg -n "mỗi hàng.*prompt|Mỗi hàng.*prompt|Prompt Gemini Omni|mọi hàng|kể cả khi asset" '.agent\AGENT.md' 'docs\Bố_Cục_prompt.md' 'docs\VISUAL STORYTELLING PLAYBOOK.md' 'docs\Quy_trình.md' 'docs\Check_List.md'
```

Expected: the current mandatory-prompt contradiction is visible in `.agent/AGENT.md`, `Bố_Cục_prompt.md`, and the Playbook.

- [ ] **Step 2: Update `.agent/AGENT.md`**

Replace the mandatory-prompt rule with:

```text
Every timeline row MUST contain an Execution Spec.
Only rows routed to generative video contain a copy-ready Gemini Omni/Veo prompt.
REAL_SOURCE rows contain sourcing briefs.
EDITOR_MG rows contain controlled build specifications and MUST NOT contain a generative-video prompt.
HYBRID rows split the base plate from editor-controlled overlays.
Before creating or modifying Pormpt.md, load and follow the project video-prompt-engineering skill.
```

Update the exact six-column schema and ENG/VIE language rule. Preserve unrelated research, safety, folder, and Git rules.

- [ ] **Step 3: Upgrade `Bố_Cục_prompt.md` to Prompt System v2**

Update frontmatter version/date and replace the old universal template section with:

- Scene Contract schema;
- Asset Router gate;
- execution-mode compiler templates;
- allowed representation then exclusions;
- preflight command;
- post-generation QA schema;
- mode-specific ENG/VIE language rules.

Retain valid image-generation, reference, disclosure, and realism guidance that does not contradict v2.

- [ ] **Step 4: Align the Playbook, process, and checklist**

Make these focused edits:

- Playbook: change the table header and forbid automatic generative routing for technical graphics.
- Process: change Flow step to Contract → Route → Compile → Preflight → Generate → QA → Refine.
- Checklist: add Prompt Preflight and Generated Video QA checks; remove universal Gemini prompt expectations.

Do not rewrite unrelated policy, voice, or evidence sections.

- [ ] **Step 5: Run contradiction and placeholder scans**

Run:

```powershell
rg -n "mỗi hàng.*prompt video|Mỗi hàng.*prompt video|kể cả khi asset chính|cả .* hàng.*prompt" '.agent\AGENT.md' docs
rg -n "TBD|TODO|PLACEHOLDER" '.agent\AGENT.md' 'docs\Bố_Cục_prompt.md' 'docs\VISUAL STORYTELLING PLAYBOOK.md' 'docs\Quy_trình.md' 'docs\Check_List.md'
```

Expected: no active rule still mandates generative prompts for every asset; no new placeholder appears.

---

### Task 5: Rebuild the English Birds `Pormpt.md`

**Files:**
- Modify: `Video/Why Birds Don’t Get Electrocuted on Power Lines — Until They Do/eng/Pormpt.md`

**Interfaces:**
- Consumes: locked English timeline/claims, execution modes, Scene Contract schema, and compiler templates.
- Produces: canonical execution map used as the semantic source for the Vietnamese version.

- [ ] **Step 1: Create an asset-routing worksheet from the locked English script**

Use these final routes unless official Flow capability verification requires the noted equivalent:

```text
REAL-01 REAL_SOURCE
AI-01 HYBRID
REAL-02 REAL_SOURCE
AI-02 GMO_REFERENCE_VIDEO or VEO_FIRST_FRAME
EDIT-01 EDITOR_MG
MG-01 EDITOR_MG
AI-03 GMO_TEXT_TO_VIDEO
MG-02 EDITOR_MG
TEXT-01 EDITOR_MG
AI-04 VEO_FIRST_LAST or HYBRID
MG-03 EDITOR_MG
REAL-03 REAL_SOURCE
MG-04 EDITOR_MG
TEXT-02 EDITOR_MG
```

Choose one mode for every `or` after checking the current official Google feature guidance. Record reference requirements instead of assuming the user already has frames.

- [ ] **Step 2: Rewrite the six-column timeline**

Cover `00:00–01:01` continuously. Every row includes:

- visual fingerprint in Detailed Content;
- entry/exit relationship;
- direct candidates/search terms where applicable;
- one typed Execution Spec.

`REAL_SOURCE` cells contain no `PROMPT:` marker. `EDITOR_MG` cells contain build instructions but no fake AI alternative.

- [ ] **Step 3: Compile the AI prompts from their contracts**

For `AI-01`, `AI-02`, `AI-03`, and `AI-04`:

- define all contract fields required by the selected mode;
- state exact reference ownership;
- give one dominant change;
- define allowed visual representation before exclusions;
- keep timed action contiguous and within 4–10 seconds;
- remove model-generated text, equations, labels, topology, potential gradients, and visible electricity;
- describe `NOT_YET_TRUE` as mechanism state, not one vague negative sentence.

- [ ] **Step 4: Run the validator against ENG**

Run:

```powershell
python '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Pormpt.md'
python '.agents\skills\video-prompt-engineering\scripts\validate_timeline.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Pormpt.md'
```

Expected: both commands exit 0.

- [ ] **Step 5: Manually audit content quality**

Confirm:

```text
No repeated bird-on-wire zoom pattern.
No AI-generated electrical diagram or potential label.
No real clip described as evidence that its photographed wire is energized.
No fake electrocution reenactment.
AI illustration remains labeled as illustration, not evidence.
```

---

### Task 6: Rebuild the Vietnamese Birds `Pormpt.md` and Validate the Pair

**Files:**
- Modify: `Video/Why Birds Don’t Get Electrocuted on Power Lines — Until They Do/vie/Pormpt.md`
- Modify: `.agents/skills/video-prompt-engineering/tests/test_lint_pormpt.py`

**Interfaces:**
- Consumes: canonical English asset map from Task 5.
- Produces: natural Vietnamese execution map with mechanical parity and pair-validation coverage.

- [ ] **Step 1: Add a failing pair-mismatch test**

Test `lint_pair()` with two fixtures that differ in Asset ID, execution mode, or declared duration and assert `E_PAIR_MISMATCH`.

- [ ] **Step 2: Run the focused pair test and confirm RED if pair parsing is incomplete**

Run:

```powershell
python -m unittest discover -s '.agents\skills\video-prompt-engineering\tests' -p 'test_*.py' -v
```

Expected: the new pair test fails until parity extraction handles the full production-table format.

- [ ] **Step 3: Complete `lint_pair()` and make the test GREEN**

Compare normalized row tuples:

```python
(timeline, asset_id, mode, declared_duration)
```

Do not compare translated prose byte-for-byte.

- [ ] **Step 4: Rewrite the Vietnamese timeline from the English canonical map**

Translate naturally while preserving:

- Asset IDs and timecodes;
- mode and duration;
- subject/action/state logic;
- invariants and forbidden inference;
- allowed representation and exclusions.

All copy-ready operational prompts in VIE are written fully in Vietnamese. Do not retain English prompts or say “xem bản ENG”.

- [ ] **Step 5: Run single-file and pair validation**

Run:

```powershell
python '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Pormpt.md'
python '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' --pair 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Pormpt.md' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Pormpt.md'
python '.agents\skills\video-prompt-engineering\scripts\validate_timeline.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Pormpt.md'
```

Expected: all commands exit 0.

---

### Task 7: Full Verification and Scope Audit

**Files:**
- Verify all files listed in Tasks 1–6.
- Inspect only: both Birds `Kich_Ban.md` files.

**Interfaces:**
- Consumes: completed implementation.
- Produces: evidence-backed completion report with changed files, commands, residual risks, and no unsupported success claim.

- [ ] **Step 1: Load the verification-before-completion skill**

Read completely:

```powershell
Get-Content -Raw -Encoding utf8 'C:\Users\Tuyen\.codex\plugins\cache\openai-curated-remote\superpowers\6.2.0\skills\verification-before-completion\SKILL.md'
```

- [ ] **Step 2: Run the complete automated verification suite**

Run:

```powershell
python -m unittest discover -s '.agents\skills\video-prompt-engineering\tests' -p 'test_*.py' -v
python -m py_compile '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' '.agents\skills\video-prompt-engineering\scripts\validate_timeline.py'
python '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Pormpt.md'
python '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Pormpt.md'
python '.agents\skills\video-prompt-engineering\scripts\lint_pormpt.py' --pair 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Pormpt.md' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Pormpt.md'
python '.agents\skills\video-prompt-engineering\scripts\validate_timeline.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Pormpt.md'
python '.agents\skills\video-prompt-engineering\scripts\validate_timeline.py' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Pormpt.md'
```

Expected: every command exits 0.

- [ ] **Step 3: Verify locked scripts are unchanged**

Re-run SHA-256 and compare to Task 1:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Kich_Ban.md','Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Kich_Ban.md'
```

Expected: both hashes are identical to the recorded baselines.

- [ ] **Step 4: Run repository contradiction, placeholder, and diff checks**

Run:

```powershell
rg -n "mỗi hàng.*prompt video|Mỗi hàng.*prompt video|kể cả khi asset chính|xem bản ENG|TBD|TODO|PLACEHOLDER" '.agent\AGENT.md' '.agents\skills\video-prompt-engineering' 'docs\Bố_Cục_prompt.md' 'docs\VISUAL STORYTELLING PLAYBOOK.md' 'docs\Quy_trình.md' 'docs\Check_List.md' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\eng\Pormpt.md' 'Video\Why Birds Don’t Get Electrocuted on Power Lines — Until They Do\vie\Pormpt.md'
git diff --check
git status --short
```

Expected: no active contradiction or placeholder in changed artifacts; `git diff --check` exits 0; only planned files plus pre-existing user changes appear.

- [ ] **Step 5: Re-read both production plans and report residual risks honestly**

Residual risks that must remain explicit:

- no generated Flow video has been visually inspected in this task;
- candidate footage and license proof remain user-side production gates;
- current Flow/Veo feature availability can vary by account/region;
- static lint catches structural errors, not every scientific ambiguity.

- [ ] **Step 6: Suggest user review the final diff**

Provide clickable absolute paths, summarize which files changed and why, list validation commands and results, state that no commit/push occurred, and ask the user to review the diff before any Git action.
