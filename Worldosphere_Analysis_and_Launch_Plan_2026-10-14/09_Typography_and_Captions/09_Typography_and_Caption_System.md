# 09 — Worldosphere typography and caption system (v1.0)

Working canvas: **1080 × 1920 (9:16), 24 fps**. All sizes are pixels at that canvas.
Rendering rule: all text is rendered by a text engine (ASS/libass via ffmpeg, DaVinci Resolve Text+/subtitles, or After Effects text layers). **Never bake lettering into generated images.**

## 1. Typefaces (all SIL Open Font License 1.1, which allows commercial use and burning into video)

| Role family | Primary (licence verified 2026-10-14 from package metadata) | Licensed alternatives (OFL) | Why |
|---|---|---|---|
| **Display** (hooks, warnings, Fork labels, Verdict status) | **Big Shoulders Display** (weights 800–900) | Barlow Condensed ExtraBold; Oswald Bold | Condensed, industrial signage voice, so it reads as "field instructions". Distinct from the reference's caption face |
| **Text** (narration and dialogue captions, Verdict factor, CTAs) | **Atkinson Hyperlegible Next** (700–800) | Inter Bold/ExtraBold; Barlow SemiBold | Designed by the Braille Institute for legibility (letter shapes differentiated: I/l/1, 0/O). Sentence case reads naturally for 3–7 word phrases |
| **Mono** (timers, counters, distances, labels, scenario tag) | **JetBrains Mono** (700–800) | IBM Plex Mono Bold; Space Mono Bold | Tabular digits don't jitter while counting. A "technical" voice for data |

Font files: `@fontsource/big-shoulders-display`, `@fontsource/atkinson-hyperlegible-next`, `@fontsource/jetbrains-mono` (npm, v5.3.0, license field `OFL-1.1`). They are also on Google Fonts. Keep a copy of each licence (OFL.txt) in the project's `/fonts` folder (see 22).

## 2. Platform safe areas (verify on device; layouts change)

The only official numeric guidance found is **Google's Shorts ads guidance**: keep text, logos and CTAs out of the **top 10%, bottom 25% and right 10%** (1080×1920 → **192 px top, 480 px bottom, 108 px right**). It was retrieved via search excerpt, so treat it as provisional (22 / research appendix B §10). Third-party templates disagree by up to 2.8×. Worldosphere therefore uses a **conservative zone**:

| Zone | Pixels | Use |
|---|---|---|
| Top UI band | y 0–219 | No text, no faces |
| **Hook lane** | y 220–620 | Hook cards, timers (top-left), scenario tag, Fork labels |
| Story area | y 620–1100 | Faces, threats, key action (keep captions out unless lane B) |
| **Caption lane A (default)** | y 1100–1300 | Narration and dialogue captions |
| Low safe band | y 1300–1400 | Verdict lower edge, CTA chip (last 1.5 s only) |
| Bottom UI band | y 1400–1920 | No text, no key action (title, channel, music, description overlays) |
| Right UI column | x 936–1080 (from y 700 down) | No text; no critical action |
| Left margin | x 0–72 | No text |

**Text boxes are centred on x = 540 with a maximum width of 792 px (x 144–936).** This leaves a symmetrical layout that clears the right action column.

A visual overlay is provided: `safe_zone_overlay_1080x1920.png`. Put it on the top track in your editor while laying out every shot.
**Device check (required once a month and after any YouTube app update):** export one test frame with the overlay burned in, upload it as a **private** video (not public), view it on an iPhone and an Android phone in the Shorts player, and adjust the zones if the UI has moved. Record the result in the change log (21).

## 3. Role presets

| Preset | Font / weight / size | Case | Line height · tracking | Colour | Box / outline | Position | Max | Timing |
|---|---|---|---|---|---|---|---|---|
| **N1 Narration** | Atkinson Hyperlegible Next 800 · **62 px** | Sentence case | 1.15 · 0 | White #FFFFFF | Ink tag **#161A22 @ 88%**, radius 18, padding 16 × 26, no outline | Lane A, centre y = 1200 | 2 lines · ≤24 characters per line · ≤7 words | In 2 frames (fade + 96→100% scale); out on the next caption; 3-frame gap only at sentence ends |
| **N2 Narration emphasis** | as N1 | — | — | Amber tint **#FFC247** (resource/clue) · Threat tint **#FF8A7A** · Cold tint **#7FE0F0** · Safe tint **#9BE58A** | — | — | **One emphasised word per group; at most one emphasised group per ~3 s** | Colour present from entry (no karaoke) |
| **D1 Dialogue** | as N1 | Sentence case, with quotation marks omitted | as N1 | White | Ink tag + **8 px left bar in the speaker colour** (Kai #F2C230, Mia #B48EE0, Tess #F28C28, Owen #7FA650, guest #9FB3B6) | Lane A; tag aligned toward the speaker's side (left-aligned at x = 144 or right-aligned at x = 936) | as N1 | First line of a speaker per shot gets a **speaker chip** (S1) |
| **S1 Speaker chip** | JetBrains Mono 800 · 28 px | CAPS | 1.0 · +4% | Ink text | Fill = speaker colour, radius 8, padding 6 × 12 | 10 px above the D1 tag, same alignment | 1 word | Same in/out as its D1 |
| **H1 Hook card** | Big Shoulders Display 900 · **120 px** | CAPS | 0.95 · +1% | White, with **one** Amber #F5A524 keyword | Ink drop shadow 0/6 px @ 50%, no box | Hook lane, centre y = 400 | 2 lines · ≤14 characters per line · ≤6 words | **Fully visible on frame 0**; 6-frame settle (2% scale); hold 2.0–2.8 s; 4-frame fade |
| **W1 Warning / alert** | Big Shoulders Display 900 · 84 px | CAPS | 0.95 · +2% | Paper #F2EBDD | Signal Red #E5483B bar, full safe width (x 144–936), height 128 | Hook lane | 1 line ≤18 characters | 3-frame wipe-in from the left; hold ≥1.2 s |
| **L1 Label / callout** | JetBrains Mono 700 · 32 px | CAPS | 1.0 · +3% | Ink | Paper tag #F2EBDD, 3 px ink border, radius 6; 3 px ink leader line with a dot | Next to the object, never over a face | ≤20 characters | 3-frame pop with 8% overshoot; hold while relevant |
| **T1 Timer / counter** | JetBrains Mono 800 · 56 px digits + 26 px unit | — | — | White digits, Amber icon | Ink pill @ 88%, radius 999 | Top-left of the hook lane (x 72, y 240) | — | Ticks on change only; time jumps use a 2-frame roll |
| **R1 Sphere distance tick** | JetBrains Mono 700 · 30 px | — | — | Paper | none (ink 4 px outline) | On the dome rim, outside faces | e.g. "≈100 M" | With the dome |
| **F1 Fork label** | Big Shoulders Display 900 · 76 px | CAPS | — | Paper (unchosen) / Ink (chosen) | Ink chip (unchosen) / Amber chip (chosen), radius 10 | Centre of each panel, upper third | ≤3 words | 4-frame slide from the panel edge |
| **V1 Verdict card** | Status: Big Shoulders Display 900 · 132 px · CAPS · Ink; underline bar 12 px in the status colour (Survived/Escaped/Safe = Safe Green #6BBF59, Trapped = Amber, Lost = Signal Red, Unknown = Fog) | — | — | Ink on Paper card | Paper card #F2EBDD, radius 24, width 840, slight 1.5° tilt | Lower story area (y 900–1380) | Factor ≤8 words | Card slides up 8 frames (ease-out); hold ≥2.0 s |
| **V2 Verdict factor** | Atkinson Hyperlegible Next 700 · 50 px | Sentence case | 1.15 | Ink | on the V1 card | — | ≤2 lines | with V1 |
| **V3 Real Rule** | Label: JetBrains Mono 800 · 26 px Ink on Amber chip "REAL RULE"; text: Atkinson 700 · 42 px Ink | Sentence case | 1.15 | Ink | on V1 | — | ≤14 words + "Sources in description" (Atkinson 400 · 28 px) | with V1 |
| **C1 CTA chip (optional)** | Atkinson Hyperlegible Next 700 · 40 px | Sentence case | — | White | Ink tag @ 88% | y 1320 | ≤6 words | Last 1.5 s only; never over the Verdict factor |
| **G1 Scenario tag** | JetBrains Mono 700 · 28 px | CAPS | +6% | Paper @ 60% | none | x 72, y 232 | "SCENARIO 001" | Frames 0–48 (2.0 s), then a 6-frame fade |

**Measured reference vs Worldosphere (why the numbers differ):** the reference shows about 3 words per caption for ~1.0 s at 62–65% of frame height (MEASURED, 04 E06/E07). Worldosphere keeps the *speed and position logic* (short groups in sync with speech, lane A at about 62%). It changes the *typographic voice*: sentence case, a boxed tag instead of a drop shadow, speaker identification, and a mono data layer.

## 4. Segmentation and reading-time rules
1. Break at natural phrase boundaries (subject | verb phrase | object). Never split a name, a number or its unit ("73 | gal" ✗).
2. 2–5 words per group is typical; 7 is the maximum. A one-word group is allowed for punctuation beats ("Nothing.").
3. **Minimum on-screen time = max(0.5 s, 0.3 s + 0.22 s × words)**. A target reading load of ≤3.5 words per second over any 3-second window.
4. Captions enter **2 frames before** the first spoken word of the group and leave when the next group enters (or 6 frames after the last word at a pause).
5. Two-line groups: the top line is shorter than or equal to the bottom line (pyramid). No orphans ("…the only / one" ✗).
6. Captions must match the final audio **word for word**. Deliberate paraphrases are not allowed in N1. Paraphrased ideas belong in L1 labels.
7. Numbers: digits for ≥10 and for all measurements ("6 inches", "73 gal", "≈100 m"). Spell out one to nine in prose.

## 5. When the screen should contain **no** caption
- During a held reveal (0.5–1.0 s after the reveal frame). The image must land first.
- During the planned audio drop (the silence is the message).
- When an on-screen label, counter or Fork chip already carries the same words.
- During wordless action longer than 0.6 s when the narrator is silent.
- During the Verdict card's first 0.5 s (the card is the text).

## 6. Keeping text off faces, hands and threats
- Each storyboard panel marks the **caption lane**: A (low) or B (high: y 470–610, same style). Lane B is used when a face, hands, or the threat occupies y 1050–1350.
- Each shot draws a "subject box" around faces, hands and the threat. Captions must not intersect it (QA item T-04).
- During the Fork, captions stay in lane A on their ink tag, which sits above the crack layer. F1 chips sit in the hook lane (y≈520). Never place text over the chips or the Sphere's source point.

## 7. Speaker identification
- Narrator: no chip, centred tag.
- Characters: a coloured left bar + a speaker chip on the first line per shot, aligned toward the speaker's side of the frame.
- Off-screen speakers: the chip carries "(off)" (for example "TESS (OFF)"). The visible listener keeps a closed mouth (08 §4.3).

## 8. Restraint rules
- ≤1 emphasised word per caption group; ≤1 emphasised group per ~3 s; red tint only for threats.
- At most 3 text elements visible at once (e.g. hook + timer + caption). The Verdict is the exception.
- No all-caps narration. Caps are reserved for display, labels and chips.

## 9. Accessibility and phone readability
- Contrast (WCAG 2.x formula; tag at 88% over a white background, which is the worst case): white text **12.3:1**, amber tint #FFC247 **7.6:1**, threat tint #FF8A7A **5.4:1**, cold tint #7FE0F0 **8.1:1**, safe tint #9BE58A **8.2:1**; Ink on Paper card **14.7:1**. All exceed 4.5:1.
- Smallest text on screen is 26 px (the Verdict source line). Body captions are 62 px, about 3.2% of frame height.
- Also upload a **closed-caption file (SRT)** to YouTube for each video, generated from the same script (it helps viewers who rely on captions and translation). Burned-in captions remain the primary layer for muted viewing.
- Muted test: a person who has not seen the script must be able to state the decision and the outcome from a muted viewing (QA S-02).

## 10. Reusable files in this folder
| File | Purpose |
|---|---|
| `worldosphere_caption_styles.ass` | Subtitle (ASS) style sheet with every preset + example events. Burn in with `ffmpeg -i in.mp4 -vf "ass=worldosphere_caption_styles.ass:fontsdir=fonts" out.mp4` |
| `typography_presets.json` | Machine-readable presets for templates and scripts |
| `safe_zone_overlay_1080x1920.png` | Layout guide overlay (transparent PNG) |
| `type_specimen_1080x1920.png` | Rendered specimen of every preset (inspected; see §11) |

## 11. Examples (rendered in the specimen)
- H1: "WHO'S IN **COSTUME**?"
- N1: "The alert said: avoid anyone acting strangely."
- N2: "On a cold night, you can see **breath**."
- D1 + S1: [TESS] "Kill the engines. All of them."
- L1: "DOCK 6 · ROLL-UP DOOR"
- T1: "00:58"
- W1: "SHELTER INDOORS NOW"
- F1: "DOOR" | "WINDOW"
- V1–V3: "ESCAPED / He used the window, not the door. / REAL RULE: Car in water — get out through a side window in the first minute."

## 12. Typography QA (included in the master QA checklist, `13_Templates/QA_Checklist.md` section W and V-04/V-05)
- TY-01 Every on-screen word matches the final audio.
- TY-02 No text in the UI bands; no text box wider than 792 px.
- TY-03 Reading-time rule satisfied for every group (export the caption CSV and check `duration ≥ 0.3 + 0.22×words`).
- TY-04 No caption intersects a subject box.
- TY-05 Emphasis budget respected.
- TY-06 Spelling, names, numbers and units checked against the script and the claim ledger.
- TY-07 Phone check at 100% brightness and at 30% brightness.
