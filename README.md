# Worldosphere — analysis and launch plan

Planning package for the **Worldosphere** YouTube Shorts channel: reference analysis, an original creative system, a 30-day calendar with a brief for every day, full production packages for Days 1–3, and the production, QA, scheduling and measurement manuals.

**Planning only.** Nothing has been published, scheduled or purchased.

## Where to start
1. `Worldosphere_Analysis_and_Launch_Plan_2026-10-14/00_INDEX.md`: navigation, completion ledger and acceptance audit.
2. `…/01_Executive_Overview.md`: the whole plan on one page.
3. `…/24_Make_the_Next_Worldosphere_Video_Checklist.md`: how to make any episode.

## Layout
```
README.md                                   this file
References_Supplied/README.md               names and checksums of the two supplied reference videos (the videos themselves are not stored here)
Worldosphere_Analysis_and_Launch_Plan_2026-10-14/
  00_INDEX.md … 24_….md                     the 24 deliverables (see the index)
  03_Video_Breakdowns/                      timestamped analysis of each reference video
  07_Survival_Logic_and_Facts/              world rules + claim ledger (CSV and readable copy)
  09_Typography_and_Captions/               type system, ASS caption styles, specimens, safe-zone overlay
  11_Style_Frames_and_Motion_Proof/         prototype frames and the Fork/breath motion proof (MP4)
  13_Templates/                             script, storyboard, shot list, character, sound, caption, QA, upload, review templates
  18_Daily_Briefs/                          WS-001 … WS-030
  19_Production_Packages_Days_1-3/          full packages for WS-001, WS-002, WS-003
  22_Asset_Rights_and_Sources/              asset register + research appendices A–F
  data/                                     machine-readable calendar, topic pool and reference measurements
  tools/                                    generators, caption/timing engine, renderer, analysis scripts (tools/README.md)
  Worldosphere_Launch_Workbook.xlsx         editable workbook (calendar, briefs, claims, schedule, tracking, QA log, change log)
```

## Downloading to your computer
- **ZIP:** on GitHub, switch to the branch `claude/worldosphere-production-launch-4v6lci`, then **Code → Download ZIP**.
- **Git:** `git clone -b claude/worldosphere-production-launch-4v6lci https://github.com/betostylesbarber/Worldosphere.git`

Then copy the folder `Worldosphere_Analysis_and_Launch_Plan_2026-10-14` **into** your Desktop "Worldosphere" folder. It is a separate dated subfolder, so it doesn't overwrite anything already there. The Desktop folder couldn't be checked from the cloud environment, so compare its contents with the plan (23 L1).

## Notes
- **This repository is public.** Consider making it private, and never commit licensed music, raw voice recordings, contracts or the reference videos (23 L5).
- The reference videos are analysed for study only; their rights belong to their creator. To regenerate the measurements, put local copies in `References_Supplied/` (git-ignored) and follow `tools/analysis/README.md`.
- Fonts bundled in `tools/render/fonts/` are licensed under the SIL Open Font License 1.1 (licence files included).
