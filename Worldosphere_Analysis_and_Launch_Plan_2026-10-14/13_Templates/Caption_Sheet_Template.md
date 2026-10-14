# Caption sheet template and procedure

Styles: `09_Typography_and_Captions/worldosphere_caption_styles.ass` (load it as the style header of every episode's ASS file). Rules: 09 §3–§9. Worked examples: `19_Production_Packages_Days_1-3/*/WS-00N_captions_PROVISIONAL.ass/.srt`.

## Procedure
1. Start from the provisional caption file from the timed read (engine output) or from the script's " | " breaks.
2. Import the **final** VO into Subtitle Edit / Aegisub; re-time every group to the waveform (in-point ≈83 ms before the first syllable).
3. Check each group against the table below; fix by re-splitting, never by shrinking type.
4. Export **ASS** (burn-in, brand styles) and **SRT** (upload subtitle track; plain text, no styling).

## Group table (fill or export from the ASS file)
| # | In | Out | Dur | Words | Lines (≤2 × ≤24 chars) | Style (N1/N2/D1+S1) | Lane (A/B) | Emphasis word + tint | Min display max(0.5, 0.3+0.22×words) met? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | N1 | A | | |

## Checks (QA W-01…W-09)
- [ ] Word-for-word match with the final VO
- [ ] ≤7 words, ≤2 lines, ≤24 characters per line; no weak word ending a line ("a", "the", "to", "of"); no orphan last word
- [ ] ≤1 emphasised word per group; ≤1 emphasised group per 3 s; tints only Amber #FFC247 / Threat #FF8A7A / Cold #7FE0F0 / Safe #9BE58A
- [ ] Lane A by default; lane B only when a face or the decisive action sits in y 1050–1350; never lane B during the Fork
- [ ] No captions during the drop, the final image hold, or the first 0.5 s of the Verdict
- [ ] Speaker chips on each speaker's first line per scene
- [ ] SRT exported for upload
