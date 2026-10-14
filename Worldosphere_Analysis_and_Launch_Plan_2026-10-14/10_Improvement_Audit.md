# 10 — Improvement audit and prioritised action list

**Scope:**
- Only the two supplied reference videos were inspected, visuals and audio: REF01 *The Last Farm, Part 2* (87.12 s) and REF02 *Part 1* (61.04 s).
- The online catalog, publication data, metrics and comments were **not accessible** (02). So nothing here claims what the reference's audience did, and repetition across the catalog **cannot** be assessed.
- Timestamps are from the breakdowns (03) and the findings ledger (04).

**Labels:**
- **Evidence confidence** is about the observation (MEASURED or OBSERVED is high).
- **Likely viewer effect** is always INFERRED: no viewer data exists.
- **"Better"** means a defined, observable improvement to a viewer: comprehension, trust, satisfaction or readability. More detail, motion or rendering cost is not counted as better.

**Rule followed:** no flaws were invented. Several categories from the brief's checklist were examined and found **not** to be weaknesses; they are listed as such in §2.

---

## 1. Audit table

| # | Reference and timestamp | Existing strength | Specific weakness | Likely viewer effect (INFERRED) | Evidence confidence | Proposed improvement (Worldosphere) | Production cost | Validation method |
|---|---|---|---|---|---|---|---|---|
| A1 | REF02 0.0–4.27 (conditional "If the zombie apocalypse starts while you're on a farm…" + phone alert) | A clear premise and stakes in 4 s; a diegetic alert as the inciting device (F01, F14) | None significant. The second-person promise switches to a third-person story at 12.3 s, which is a small shift of frame | Strong viewing choice is plausible | High (OBSERVED) | **PRESERVE** the principle (frame 0 = protagonist + anomaly + reason to watch). Execution is original: a city alert card in WS-001, a waterline clock in WS-002 | None (design rule) | T-01; QA S-01/S-02 |
| A2 | REF02 7.85–9.13, 16.67–19.37, 23.95–26.73, 31.97–33.90; REF01 43.70–47.80, 51.20–53.37 (blueprint, maps, well diagram, noise rings) | Invisible mechanisms made visible: noise, water, threat routes (F02) | Mechanism graphics vary in style shot to shot; no consistent visual grammar for "force" | Comprehension is good; brand recall from the graphics is weaker | Medium (OBSERVED; the effect is inferred) | **IMPROVE**: one consistent grammar, **the Sphere** (colour-typed domes, ledger-checked distances) + L1 labels | Medium (HUD template ≈6 h once; then minutes per use) | T-06 confusion rate; QA V-06 |
| A3 | REF02 49.4–53.8 ("WATER 73 GAL ✓", "on paper… weeks" for 12 cattle, a horse, 30 hens, a dog) | Concrete numbers feel practical | **The water claim is false**: extension-service figures give ≈110–183 gal/day for these animals, so 73 gal lasts under a day, not weeks (C-020) | Corrections from knowledgeable viewers; loss of trust in "practical" framing | High (MEASURED claim check) | **REPLACE** with the claim-ledger discipline: every real-world number SUPPORTED or QUALIFIED with a source, or cut | Low (≈0.5–1.5 h research per episode) | QA F-01–F05; correction rate (21 §1) |
| A4 | REF01 8.3–10.2 ("She crossed three miles of fields" following the generator) | Strong cause-and-effect story link ("so did they") | Audibility at ≈4.8 km is doubtful: spherical spreading takes a 57–73 dB(A)@7 m generator to about 0–16 dB(A) (C-012/013/021) | Viewers who know sound may object; most won't notice | High on physics; the effect is low-medium | **IMPROVE**: keep sound-driven plots, but scale Sphere distances to real acoustics (WR-03); no distance number unless verified | Low | QA F-06/F-09; T-06 |
| A5 | REF01 57.47–59.73 (Mara's line plays over Eli's open-mouth reaction) | — | Speaker attribution is ambiguous | A brief "who said that?" moment | High (OBSERVED) | **IMPROVE**: off-screen lines play over a *closed-mouth* listener; D1 speaker bar + S1 chip (09 §7) | None | QA W-08, V-01 |
| A6 | REF01 8.37, 76.33 (caption text differs from the spoken words); REF01 33.47, 41.67 (awkward line breaks) | Dense, fast captions (51/68 groups, ≈3 words) aid muted viewing (F05) | Mismatches and splits that break a phrase | Small reading friction; trust in captions | High (MEASURED with ASR alignment) | **IMPROVE**: re-time to the final VO; the segmentation rules (weak-word, orphan and pronoun penalties) in `tools/package_engine.py`; a word-for-word check | Low (≈20 min per episode) | QA W-01–W-03 |
| A7 | REF02 52–57 (day to near-night with no cue); REF01 1.9–3.1 (a dusk exterior between night shots) | — | Time-of-day continuity jumps | Momentary disorientation | Medium (OBSERVED; possibly intended compression) | **IMPROVE**: the continuity column in every shot list; light changes only with a visible cause (08 §6.3) | None | QA F-08 |
| A8 | REF02 overall (194 wpm while speaking; speech 96% of the time; 2 pauses > 0.4 s; mean shot 1.39 s) | High information density and momentum (F06) | Little breathing room; reveals compete with continuous narration | Unknown: it could raise or lower mid-video retention | High (MEASURED); the effect is UNKNOWN | **TEST**: Worldosphere default ≈171 wpm with one planned "drop" per episode; T-04 tests a lighter density | None | T-04 (50% retention, confusion guardrail) |
| A9 | REF01 39.5–41.7 and 50.6–51.3 (music drops to −47/−53 dBFS around "So did they." and "Silence.") | Silence used as punctuation (F07) | None | Emphasis on key lines | High (MEASURED) | **PRESERVE** the principle: one planned drop per episode, paired with a visual hold (08 §8) | None | T-07 (retention through the drop) |
| A10 | REF02 54.1–61.0; REF01 70.9–87.1 (cliffhanger endings + story-tied follow CTA; end cards 1.7 s / 3.2 s) | Story-tied CTAs; a strong forward pull for series viewers (F08) | **The episode question is unresolved** for a viewer who sees one video, and resolution depends on following | Possible frustration for cold Shorts viewers; can't be measured from here | Medium (OBSERVED; the effect is inferred) | **REPLACE** with **the Verdict** (every episode resolves) + an optional ≤1.5 s forward line after it. Saga only as a test (R-F) | Low (Verdict template) | T-09, T-12; "unfinished?" comment coding |
| A11 | REF02 57.6–59.3 = REF01 0.0–1.87 (continuity bridge between parts) | A smooth series join (F09) | Part 2 needs Part 1 context for full meaning (re-explained, so cold viewers can follow) | Fine for series viewers; partial for cold viewers | Medium | **TEST** once: the WS-015/016 saga, with Part 1 resolved | Medium (the saga kit is reused) | T-12 |
| A12 | REF02 18.67, 35.53; REF01 18.8–21.4 (rule cards; one stays across three cuts) | Quotable takeaways (F04) | Cards mix rules of fiction and claimed real practice without distinguishing them | Viewers may take fiction rules as real advice | Medium | **IMPROVE**: the Verdict separates the story outcome from a **REAL RULE** line (ledger-verified, "Sources in description"); fiction rules stay inside the story (WR sheet) | Low | QA F-07; correction rate |
| A13 | Whole videos (caption band at 62–65% height; caption style) | Phone-readable, consistent | The caption look is the reference's own identity, so copying it would make Worldosphere look derivative | Brand confusion | High (OBSERVED) | **REPLACE**: the original type system (Atkinson Hyperlegible Next + Big Shoulders Display + JetBrains Mono; Ink tags; lanes clear of the Shorts UI) | Done (09) | Identity review; QA W-04 |
| A14 | Whole videos (flat-vector look, round heads, thin limbs, soft gradients) | High phone readability (F11) | Again the reference's identity | Derivative look | High | **REPLACE** the look with the **inked diorama** style (08 §6: bean heads with brows, 6 px ink line, no background outlines, 4 depth planes); **PRESERVE** the readability principles | Medium (rig build ≈24 h once) | Style frames SF1–SF3 (11); QA V-04 |
| A15 | REF01 5.5–8.3, 63.6–66.0; REF02 39.9–43.3 (the dog as warning and comic relief) | Character economy and warmth (F10) | None as a flaw; a pet sidekick would be too close to the reference | — | — | **PRESERVE** a small recurring cast; **REPLACE** the specific device (no dog sidekick; the sibling dynamic Kai/Mia, the skills of Tess/Owen) | Done (08 §4) | T-03 |
| A16 | REF01 overall loudness −14.1 LUFS, −0.9 dBTP; REF02 −14.1 / −1.0 | A competent, consistent mix | None | — | High (MEASURED) | **PRESERVE**: −14 LUFS ±1, ≤ −1 dBTP (as a convention, not a platform rule) | None | QA A-02 |
| A17 | REF02 1.73–4.27 (an "EMERGENCY ALERT / SHELTER IN PLACE" phone screen) | An effective inciting device | Mimicking real emergency-alert formats can confuse or alarm; real alert tones are restricted in many contexts | Viewers may mistake fiction for a real alert | Medium (the risk is inferred) | **IMPROVE**: original alert designs and original chimes, never the real WEA/EAS layout or tones (C-104; QA A-08) | None | QA A-08, F-07 |

## 2. Checklist categories examined and **not** found to be weaknesses
| Category (from the brief) | Finding |
|---|---|
| Unclear openings | Both openings are clear (A1; REF01's mystery voice is resolved by 5.6 s) |
| Weak character motivation | Clear survival motives; no issue |
| Confusing geography | REF01 keeps consistent left/right staging in the barn; maps clarify threat locations. **Strength** |
| Flat compositions / poor hierarchy | Centred subjects and uncluttered backgrounds. **Strength** (F11) |
| Inconsistent characters | Costumes are consistent across shots |
| Mechanical movement, tangled silhouettes, broken contact | Not observed as defects at the supplied 720p re-encode. Economical performance suits the format |
| Generic narration / ineffective sound | Calm, authoritative narration; effective drops. **Strength** |
| Excessive effects | Not observed |
| CTAs interrupting the story | The CTAs come after the story. The issue is resolution, not interruption (A10) |
| Repeated premises; weak channel identity | **Cannot be assessed**: the catalog was not accessible (02) |

## 3. Decisions summary
- **PRESERVE:**
  - a frame-0 anomaly + stakes (A1)
  - silence as punctuation (A9)
  - a small recurring cast (A15)
  - the loudness convention (A16)
  - phone-readable composition (A14, the principle).
- **IMPROVE:**
  - mechanism graphics into the Sphere grammar (A2)
  - acoustics realism (A4)
  - speaker attribution (A5)
  - caption accuracy and segmentation (A6)
  - time-of-day continuity (A7)
  - separating fiction rules from real rules (A12)
  - original alert designs (A17).
- **REPLACE:**
  - unverified numbers with the claim ledger (A3)
  - cliffhanger dependency with the Verdict (A10)
  - the caption look with the original type system (A13)
  - the visual style with the inked diorama (A14)
  - the dog-sidekick device (A15).
- **TEST:**
  - narration density (A8, T-04)
  - a two-part saga (A11, T-12).

## 4. Prioritised action list
| Priority | Action | Where it lives | Owner stage (12 §5) | When |
|---|---|---|---|---|
| 1 | Verify every BLOCKING claim before its script lock; never ship UNVERIFIED-BLOCKING (A3, A4, A12) | Ledger, 20 §6 | 5.2 Research | Pre-launch sprint Oct 15–17; then T-10 |
| 2 | Every episode ends on a truthful Verdict; forward lines only after it (A10) | 08 §8.3; recipes | 5.5 Script | All episodes |
| 3 | Re-time captions to the final VO; run the W checks (A6) | QA W-01–W-08 | 5.13 Captions | All episodes |
| 4 | Build the Sphere, Fork and Verdict as templates once (A2) | HUD kit (12 §4) | 5.8 Assets | By Thu 22 Oct |
| 5 | Continuity column + floor plan per location (A7) | Storyboard template | 5.7 Storyboard | All episodes |
| 6 | Closed-mouth listener rule + speaker chips (A5) | 08 §4.3; 09 §7 | 5.9 Animation | All episodes |
| 7 | Original alert UI and chimes only (A17) | Asset register (22) | 5.8 Assets / 5.12 Mix | WS-001 onward |
| 8 | Run T-04 (density) and T-12 (saga) as planned; don't change other variables at the same time (A8, A11) | 21 §3 | 5.17 Review | Weeks 2–3 |
| 9 | Keep identity separation: no reference caption styling, character designs or devices (A13–A15) | 08, 09; QA V-08 | 5.14 QA | All episodes |
| 10 | Keep the −14 LUFS / −1 dBTP mix and verify on the exported file (A16) | QA A-02 | 5.15 Export | All episodes |
