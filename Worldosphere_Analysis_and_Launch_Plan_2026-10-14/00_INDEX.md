# 00 — INDEX · Worldosphere analysis and launch plan (2026-10-14)

**Start here:** `01_Executive_Overview.md` (one page), then `24_Make_the_Next_Worldosphere_Video_Checklist.md` (how to make any episode).

**Status:** planning package complete. **Nothing has been published, scheduled or purchased, and no existing file was overwritten** (the repository was empty when work began). Evidence labels used throughout: **OBSERVED · MEASURED · INFERRED · RECOMMENDED · UNKNOWN**.

---

## 1. Deliverables map (the brief's 24 items)

| # | Deliverable | File(s) |
|---|---|---|
| 1 | Executive overview and recommended direction | `01_Executive_Overview.md` |
| 2 | Source inventory and coverage report | `02_Source_Inventory_and_Coverage.md`; `../References_Supplied/README.md` (checksums; the videos are kept out of the public repo) |
| 3 | Timestamped analysis of every inspected unique video | `03_Video_Breakdowns/REF01_The_Last_Farm_Part2_breakdown.md`, `REF02_The_Last_Farm_Part1_breakdown.md`; measured data in `data/REF0x_*.csv`, `data/reference_measured_stats.json` |
| 4 | Cross-video findings and evidence ledger | `04_Cross_Video_Findings_and_Evidence_Ledger.md` (F01–F15, E01–E18) |
| 5 | Niche, audience and content pillars | `05_Niche_Audience_and_Pillars.md` |
| 6 | Performance hypotheses and limitations | `06_Performance_Hypotheses_and_Limitations.md` (H1–H10) |
| 7 | Survival-logic and factual-verification framework | `07_Survival_Logic_and_Facts/07_Survival_Logic_and_Fact_Framework.md` (world rules WR-01–WR-12); `claim_ledger.csv` / `.md` (71 claims); `Verification_Worksheet.md` + `verification_results.csv` (how to close every open claim and platform fact) |
| 8 | Brand and animation bible | `08_Brand_and_Animation_Bible.md` |
| 9 | Typography and caption specifications | `09_Typography_and_Captions/` (system doc, ASS styles, presets JSON, type specimen, Verdict specimen, safe-zone overlay) |
| 10 | Improvement audit and prioritised actions | `10_Improvement_Audit.md` |
| 11 | Style frames and motion proof | `11_Style_Frames_and_Motion_Proof/` (SF1–SF3 PNG, MP1 MP4, contact sheet, inspection notes) |
| 12 | Complete production manual | `12_Production_Manual.md` (incl. the YouTube Shorts translation §8 and the reconstructed workflow §6) |
| 13 | Reusable templates | `13_Templates/`: script, storyboard, shot list (CSV), character sheet, sound cue sheet (CSV), caption sheet, **QA checklist**, upload package, performance review, daily brief, production recipes |
| 14 | Hook, retention and conversion playbook | `14_Hook_Retention_Conversion_Playbook.md` (HP01–HP14) |
| 15 | Research pool (≥60 ideas) | `15_Topic_Research_Pool.md` (94 premises, scoring rubric); `data/topic_pool.csv` |
| 16 | Selected 30 + 10 reserves | `16_Selected_30_and_10_Reserves.md` |
| 17 | Dated 30-day calendar | `17_30_Day_Posting_Calendar.md`; `data/calendar_30_days.csv`; fallback `data/calendar_fallback_launch_2026-11-09.csv` |
| 18 | Briefs for all 30 videos | `18_Daily_Briefs/WS-001 … WS-030` (29 fields each) |
| 19 | Full production packages for Days 1–3 | `19_Production_Packages_Days_1-3/WS-001_…`, `WS-002_…`, `WS-003_…` (package doc + provisional SRT/ASS + shot list CSV + sound cues CSV) |
| 20 | Deadlines, dependencies, buffer plan | `20_Production_Schedule_and_Buffer.md` |
| 21 | Measurement and iteration plan | `21_Measurement_and_Iteration_Plan.md` (T-01–T-12, checkpoints, diagnosis, change log) |
| 22 | Asset-rights and factual-source records | `22_Asset_Rights_and_Sources.md`; `22_Asset_Rights_and_Sources/asset_register.csv`; `research_appendices/A–F` |
| 23 | Limitations and next actions | `23_Limitations_and_Next_Actions.md`; `tools/desktop_intake.py` (read-only check of the Desktop folder, run locally) |
| 24 | "Make the Next Worldosphere Video" checklist | `24_Make_the_Next_Worldosphere_Video_Checklist.md` |
| + | Editable workbook | `Worldosphere_Launch_Workbook.xlsx` (Calendar, Fallback calendar, Briefs, Reserves, Topic pool, Claims, Schedule, Pilot hours, Tracking, QA log, Change log, Asset register) |
| + | Tools | `tools/README.md` (generators, timing engine, renderer, analysis scripts) |

## 2. Producer quick-finder (for episode WS-0NN)

| I need… | Go to |
|---|---|
| The story, hook, beats, payoff, assets, measures | `18_Daily_Briefs/WS-0NN_*.md` |
| The recipe and word budget | Brief field 6 → `13_Templates/Production_Recipes.md` |
| A worked full package to copy | `19_Production_Packages_Days_1-3/` |
| Real-world facts and approved wording | `07_Survival_Logic_and_Facts/claim_ledger.csv` (IDs from brief field 8) |
| Outbreak rules | `07_…Framework.md` §3 (WR-01–WR-12) |
| Character designs and colours | `08_Brand_and_Animation_Bible.md` §4–§5 |
| Fork / Sphere / Verdict rules | `08` §8 |
| Caption and text styles, safe zones | `09_Typography_and_Captions/09_Typography_and_Caption_System.md` |
| Kits and asset deadlines | `12_Production_Manual.md` §4; `20` §7 |
| Stage-by-stage how-to, tools, render settings | `12` §1–§5 |
| Quality checks | `13_Templates/QA_Checklist.md` + brief/package §18 |
| Deadlines for this episode | `20` §3 (or the workbook *Schedule* sheet) |
| What to measure afterwards | `21` §1, §3, §5 + `13_Templates/Performance_Review_Template.md` |
| Reserve if something blocks | Brief field 29; `16` |

## 3. ID conventions
- `WS-0NN`: episode (calendar order).
- `R01–R10`: reserves.
- `C-…`: claim (ledger).
- `WR-01–12`: world rules.
- `HP01–14`: hook patterns.
- `T-01–12`: measurement tests.
- `CL-0NN`: change log.
- `K1–K10`: environment kits.
- `AR-0NN`: asset register.
- QA item prefixes: `S` story, `F` facts, `V` visuals, `W` words, `A` audio, `P` playback, `U` upload, `CAL` calendar; typography sub-checks `TY-`.
- `REF01/REF02`: the supplied reference videos.
- `F01–F15` / `E01–E18`: findings and evidence (04).
- `H1–H10`: performance hypotheses (06).

## 4. Completion ledger

| Section of the brief | Status | Notes |
|---|---|---|
| 1 Locate materials | Done, with gaps stated | No Desktop in the cloud environment; repo empty; the two uploaded videos used (02 §1). The Desktop folder can be checked locally with `tools/desktop_intake.py` (23 L1) |
| 2 Inventory and coverage | Done | 2 local / 0 online; reconciled (02 §4) |
| 3 Evidence standards | Done | Labels used across all documents |
| 4 Niche, promise, pillars | Done | 05 |
| 5 Timestamped breakdowns | Done | 80 shots, every second covered, A–J components (03) |
| 6 Survival logic, world rules, claim ledger | Done | 07; 71 claims (46 SUPPORTED, 20 QUALIFIED, 1 FALSE, 2 FICTION, 1 DESIGN, 1 UNVERIFIED in-story detail with no real-world claim); **no BLOCKING claims** after the 2026-10-14 verification (`verification_results.csv`, CL-013) |
| 7 Production workflow reconstruction | Done | 12 §6 (labelled as reconstruction) |
| 8 Improvement audit | Done | 10 |
| 9 Creative directions + chosen system | Done | 08 §1, §8 |
| 10 Typography and captions | Done | 09 (+ rendered specimens) |
| 11 Visual standard, style frames, motion proof | Done (prototype level) | 08 §12; 11 (inspected; silent motion proof, so no sound review claimed) |
| 12 YouTube Shorts translation | Done | 12 §8; platform facts checked on YouTube Help 2026-10-14 (23 §2; the Content ID rule for Shorts over 60 s is contradictory across Help pages, so the conservative rule stays) |
| 13 Performance hypotheses | Done; no metrics accessible | 06 |
| 14 Topic pool and selection | Done | 94 premises; 29 premises → 30 days (one saga premise covers 2 days) + 10 reserves + 55 rejected/deferred with reasons (15, 16) |
| 15 30-day calendar | Done | 17; posting time stated as an assumption |
| 16 Briefs for every day | Done | 30 briefs × 29 fields; cross-checked against the calendar by script |
| 17 Day 1–3 packages | Done | 19; caption timings provisional until VO is recorded |
| 18 Production manual | Done | 12 |
| 19 Daily feasibility | Done | 20 (capacity conflict stated; scenarios A/B/C; gate) |
| 20 Playbook | Done | 14 (14 patterns) |
| 21 Measurement plan | Done | 21 |
| 22 Final QA checklist | Done | `13_Templates/QA_Checklist.md` |
| 23 Organised deliverables | Done | This index |
| 24 Final acceptance audit | Done | §5 below |

## 5. Final acceptance audit (brief §24)

| Check | Result | Evidence |
|---|---|---|
| Every supplied unique video accounted for | **Yes**: 2 of 2 | 02 §2–§4 (MD5s in `References_Supplied/README.md`) |
| Every claim of full inspection includes visuals and audio | **Yes**: visuals were inspected frame by frame; audio was analysed by measurement (ASR with two models, loudness, pitch, gaps, spectral features). This is stated as machine analysis of the audio, not human listening | 02 §4; 03 §1 |
| Online coverage and access gaps stated accurately | **Yes**: 0 online videos; every blocked method logged | 02; appendix A §1 |
| Recommendations supported or labelled as hypotheses | **Yes** | Labels throughout; 06 H1–H10; 21 tests |
| The guide explains how to make the videos, not just how they look | **Yes** | 12 §5 (17 stages), 13 templates, 19 packages, 24 checklist |
| A distinct identity and original typography | **Yes** | 08, 09, 11 (rendered and inspected) |
| Visual improvements preserve clarity and feasibility | **Yes** | 10 (cost and validation per item); 12 §6 simplifications; 20 §9 |
| Facts and fictional assumptions distinguished | **Yes**; every real-world claim checked against official or primary sources on 2026-10-14, with no BLOCKING rows left | 07 §1 (five statement classes); ledger classes and `verification_results.csv`; WR sheet; "Fiction scenario" labelling |
| 30 complete daily entries in a reasoned order | **Yes** | 17 (dates and weekdays verified by script: Sat 31 Oct – Sun 29 Nov 2026, consecutive) |
| Topic choices have genuine research behind them | **Partly**: labelled honestly. Retrieved evidence [R-S#] where it exists; [BK]/[J] where it doesn't; demand data was largely inaccessible | 15, 16, appendix C |
| Every daily brief contains a real story and payoff | **Yes** | 18 field 15 (beginning, middle, ending) and field 18 (payoff + Verdict) in all 30 |
| The first three packages are complete and consistent | **Yes**: titles, Verdicts and durations match the calendar (WS-003's target was revised to its timed length; CL-011) | 19; 17 |
| The daily schedule is workable | **Yes, under the recommended scope.** Brief §19 requires that a conflict with the quality standard be explained and a workable scope or launch date recommended. 20 §2 does this: two people launch on 31 Oct, or one person launches on 9 Nov with the lean scope. Each scenario has hour budgets, a bank, a gate and a pilot measurement. One person at full scope daily is shown **not** to work, and that is stated plainly | 20 §2–§5 |
| Testing and adaptation rules are clear | **Yes** | 21 §3–§7 |
| No guaranteed views or invented analytics | **Yes**: no view figures for Worldosphere appear; third-party figures are cited only as research context with sources | 06; 21 |
| Nothing published, scheduled, purchased or overwritten | **Yes** | No upload or scheduling actions were taken; no purchases; work saved in this dated subfolder of a previously empty repository |

**Open items that keep the plan honest, not incomplete:**
- reopen each cited source page before script lock to confirm the live wording (QA F-03; every claim was verified from search excerpts on 2026-10-14)
- a quick safe-zone look on your phone (23 §2 P6)
- capacity to measure (20 §5)
- the Desktop folder and the reference catalog to check manually (23 L1–L2)
- the public-repository decision (23 L5).
