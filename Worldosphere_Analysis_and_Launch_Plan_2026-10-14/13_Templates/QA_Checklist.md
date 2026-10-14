# Worldosphere master QA checklist (run on every episode)

Use this together with the episode-specific checklist in the brief or package (e.g. §18 of each Day 1–3 package). Copy it into the episode folder as `WS-0NN_QA_vNN.md` and tick it there. Every item has an ID so a failure can be logged in the change log (`21_Measurement_and_Iteration_Plan.md` §8) and in the workbook's *QA log* sheet.

**Pass rule.** An episode may be exported for upload only when **all items are ticked or marked N/A with a reason**. Items marked ★ are **hard stops**: if one fails, the episode does not ship, and the reserve in brief field 29 is used instead.

**Honesty rule.** Tick the playback items (section P) only after watching the actual exported file. A script, storyboard or animatic review never counts as a playback pass. Write who checked it, on what device, and the file name and version.

---

## S — Story
| ID | Check | How to verify |
|---|---|---|
| S-01 ★ | The premise is understandable from frame 0 to 3 s, with the sound **off** | Muted watch by someone who hasn't read the script; they say in one sentence what is happening |
| S-02 | The first 3 seconds give a specific reason to keep watching (a question, a contradiction, a clock or a threat), not a generic intro | Compare against the hook pattern named in brief field 10 (`14_Hook_Retention_Conversion_Playbook.md`) |
| S-03 | Every sentence and shot does at least one of four things: reveals information, changes the situation, raises or resolves stakes, or deepens a character | Go line by line through the script table. If a line does none of them, cut it |
| S-04 | Each character action has a visible cause and a visible consequence. Nobody survives by luck alone | Trace the Fork choice to the payoff; the Verdict factor must name the cause |
| S-05 ★ | The payoff fulfils the hook's promise. The title, H1 and the first line make no promise the video doesn't keep | Read the title, H1 and the opening line; then watch the ending |
| S-06 | The ending has time to land: the final image holds at least 1.5 s before the Verdict, and the Verdict holds at least 2.5 s | Read from the timeline |
| S-07 | The Fork appears once, holds 1.0–1.6 s, and the chosen option is the one that leads to the outcome | Frame count on the timeline |
| S-08 | Signature elements are present: Fork, Sphere where the threat is sensed, Verdict card. Two Spheres never overlap | Shot list |
| S-09 | Any saga Part 1 resolves its own question; any forward line comes after the Verdict and is not a condition for understanding the episode | Watch Part 1 alone |

## F — Facts, world rules and continuity
| ID | Check | How to verify |
|---|---|---|
| F-01 ★ | Every real-world claim spoken, written or shown is in `07_Survival_Logic_and_Facts/claim_ledger.csv` with status SUPPORTED or QUALIFIED, and the script uses the ledger's "Script wording" | Search the script for each number, rule and safety step; match each to a Claim ID |
| F-02 ★ | **No claim with status UNVERIFIED-BLOCKING is in the episode.** Either it was verified (ledger updated, with source and date), or the episode uses its reserve or a rewrite without the claim | Ledger status column on the day of export |
| F-03 | Each SUPPORTED claim has at least one citable source (publisher, title, URL, access date). Real-rule episodes list the sources in the description | Ledger "Source" column; description draft |
| F-04 | Qualified claims keep their qualifier on screen and in voice ("about", "in tests", "can"). No stronger wording in the title or H1 | Compare the title and H1 with the ledger "Qualification" |
| F-05 ★ | Safety advice never contradicts official guidance and does not ask viewers to do anything dangerous to "test" it | Read the REAL RULE line against the source |
| F-06 | Fictional rules follow the world-rules sheet WR-01…WR-12 (`07_Survival_Logic_and_Facts/07_Survival_Logic_and_Fact_Framework.md` §3): e.g. the Turned don't breathe, can push but not pull, climb, swim or work handles | Check every Turned action in the shot list |
| F-07 | Fiction is not presented as fact. Zombie mechanics are never phrased as real science, and the description says "Fiction scenario" for P1 | Read the description and narration |
| F-08 | Continuity: threat positions, open or closed doors, lights, weather, time of day, clothing, injuries, props in hand, screen direction | Continuity column in the shot list; scrub at every cut |
| F-09 | Visuals never contradict the narration (count, side, order, distance, timing) | Watch with the script table open |
| F-10 | Numbers on screen (timers, distances, counts) are internally consistent with screen time. A countdown runs in real time or is labelled as compressed | Use a stopwatch against any T1 timer |

## V — Visuals and identity
| ID | Check | How to verify |
|---|---|---|
| V-01 | Characters match their model sheets: proportions, line weight, signature colour (Kai #F2C230, Mia #B48EE0, Tess #F28C28, Owen #7FA650), props | Side by side with `08_Brand_and_Animation_Bible.md` §4 |
| V-02 | Clean motion: no foot sliding while planted, no hand-to-object gaps, no broken arc pops, correct depth order (props behind or in front of the right hand) | Scrub contact frames at 50% speed |
| V-03 | Silhouettes don't tangle: limbs don't cross faces, and figures are separated by at least 40 px where the read matters | Freeze key poses; view as a solid black fill if unsure |
| V-04 ★ | Phone-size readability: the decisive visual information (breath puff, waterline, Sphere, chip labels) reads at 360 px wide and at 30% screen brightness | Export a 360×640 preview; view on a phone |
| V-05 | Every text element and decisive detail sits inside the safe zones: text box x 144–936; nothing important at y > 1400 or in the right column x ≥ 936 below y 700 | Lay `09_Typography_and_Captions/safe_zone_overlay_1080x1920.png` over the export |
| V-06 | Effects support the story: one Sphere colour per meaning (Amber sound, Cyan water/cold, Red threat, Violet gas), and no decorative shake, glow or particles that hide action | Shot-by-shot review |
| V-07 | No gore focus: violence is implied or off-screen, with no lingering on wounds (age-restriction risk) | Review all threat-contact moments |
| V-08 | The palette and grade match the bible (Ink, Night Teal, Dusk Slate, Fog, Paper, plus the signal colours); the frame is never darkened beyond the Verdict's 20% | Colour picker on 5 random frames |
| V-09 | No unintended watermark, placeholder, missing media (red/offline frames), font fallback or AI artefact | Scrub the full export at 2× speed, then key frames at 1× |

## W — Words: captions and on-screen text
| ID | Check | How to verify |
|---|---|---|
| W-01 ★ | Captions match the **final recorded** speech word for word (the package timings are provisional and must be re-timed to the VO) | Play with the SRT; read along |
| W-02 | Caption groups have ≤7 words and ≤2 lines of ≤24 characters. Each stays on screen for at least max(0.5, 0.3 + 0.22 × words) s | Run the caption linter (`tools/package_engine.py` rules) or check by hand |
| W-03 | Emphasis: at most 1 emphasised word per group, and at most 1 emphasised group per 3 s. Tint colours only from the approved set | ASS file |
| W-04 | Captions sit in lane A (y 1100–1300) on their Ink tag. During the Fork, captions stay in lane A with the tag drawn above the crack. Hook text stays in the hook lane (y 220–620) | Safe-zone overlay |
| W-05 | Captions never cover a face or the decisive action. If they would, move the action (subject-box rule), not the caption | Scrub each caption event |
| W-06 | Spelling, names, numbers and units are correct and consistent with the ledger and the cast sheet | Spell-check the SRT and description |
| W-07 | No-text moments in the brief (drop, final image, the first 0.5 s of the Verdict) are respected | Timeline |
| W-08 | Speaker chips (S1) appear on the first line of each non-narrator speaker in each scene | ASS file |
| W-09 | The SRT file is exported for upload as a subtitle track, as well as burned-in captions (accessibility, translations) | File present in `06_Export/` |

## A — Audio
| ID | Check | How to verify |
|---|---|---|
| A-01 ★ | Dialogue is intelligible on a phone speaker at medium volume, and music and effects never mask a word | Phone-speaker playback |
| A-02 | Integrated loudness −14 LUFS ±1. True peak ≤ −1.0 dBTP. No clipping | `ffmpeg -i file.mp4 -af ebur128=peak=true -f null -` (see the manual, `12_Production_Manual.md` §5.14) |
| A-03 | The narrator is never filtered or ducked under effects. Character dialogue sits within 2 LU of narration | Meter the stems |
| A-04 | The drop (music silence) lands exactly at the brief's moment and lasts the planned length | Timeline |
| A-05 | Sound sources match their pictures (a door slam on the slam frame; the Sphere's sound starts when it is drawn) | Scrub sync points |
| A-06 | Brand cues are present: the Fork whoosh, the motif under the Verdict, and the boom only on the Verdict | Listen through |
| A-07 ★ | Every music and SFX file is original or licensed for **monetized YouTube use** and logged in the asset-rights register (`22_Asset_Rights_and_Sources.md` §3), with licence and proof saved | Register row for each file |
| A-08 | No real emergency-alert tones (EAS/WEA attention signal) or real sirens recorded from broadcasts; use original designs | Listen for alert-like tones |

## P — Playback review of the exported file (never ticked from a script or storyboard)
| ID | Check | How to verify |
|---|---|---|
| P-01 ★ | **Complete viewing with sound** of the final export file, start to end, in one sitting | Write: viewer, date, file name |
| P-02 ★ | **Complete muted viewing**: story, rule and outcome are understandable from images and captions alone | Write it down |
| P-03 ★ | **Phone-size inspection** on a real phone (or a 360 px-wide preview if no phone is available), checking the UI overlay areas | Device name |
| P-04 | **Critical transitions** inspected frame by frame: the Fork crack, split and wipe; the cut into and out of the drop; the Verdict entry | Frame numbers |
| P-05 | **Continuity points** inspected at every cut listed in the shot list's continuity column | List any fixes |
| P-06 | The first frame is a usable cover (it is what many viewers see first) | Pause at 0:00 on a phone |

## U — Upload package and publication
| ID | Check | How to verify |
|---|---|---|
| U-01 ★ | Export: 1080×1920, 24 fps (the project rate, unconverted), H.264 High, yuv420p, AAC-LC 48 kHz stereo, MP4 with faststart; duration ≤ 3:00 (all plans are 48–72 s) | `ffprobe` output pasted in the QA log |
| U-02 | The title is ≤100 characters, with the key words in the first ~60, and represents the actual video (no false stakes, no "99%") | Read it next to the Verdict |
| U-03 | The description: a one-line summary; "Fiction scenario" (P1) or sources (P2 and P3, from the ledger); a CC BY attribution if any CC BY asset is used; ≤3 hashtags | Template `13_Templates/Upload_Package_Template.md` |
| U-04 | Cover or thumbnail: a frame from the video that represents the actual content. A custom thumbnail only if the channel has access (YPP, per research appendix B §4) | Compare it with the video |
| U-05 ★ | Audience setting: **"No, it's not made for kids"** (violence and horror themes; appendix B §8). The creator is responsible for this setting | Studio upload screen |
| U-06 | Altered or synthetic content toggle: **No** for stylized 2D animation (YouTube exempts "clearly unrealistic, animated" content). Re-evaluate if any photorealistic synthetic footage or a cloned real voice is ever used | Studio upload screen |
| U-07 | The pinned comment is drafted (brief field 25), and the subtitle file is attached | Upload package |
| U-08 ★ | Nothing is published or scheduled without the owner's explicit go-ahead. This plan never publishes | Owner sign-off |
| U-09 | The project files, stems, captions, licences and export are saved in the episode folder and backed up (manual §3) | Folder listing |

## CAL — Calendar-level checks (run weekly and before launch)
| ID | Check |
|---|---|
| CAL-01 | All 30 days have a brief, a date, a weekday and a reserve; dates and weekdays are correct |
| CAL-02 | No two consecutive days share a lead character *and* a primary location. Days 29–30 share a palette on purpose (see 17) |
| CAL-03 | BLOCKING claims due in the next 10 days are verified, or their reserve is in production |
| CAL-04 | The episode in production is at least 3 days ahead of publication (the buffer rule, `20_Production_Schedule_and_Buffer.md` §4) |
| CAL-05 | The Day 1–3 packages still match their calendar entries (title, Verdict, duration) after any change |
| CAL-06 | The change log records every swap, with the reason and the evidence |

---
**Sign-off line (copy into the QA log):** `WS-0NN | export file | viewer | device | date | S F V W A P U all pass (or N/A + reason) | hard stops: none | signed`
