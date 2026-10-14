# 22 — Asset rights and factual-source records

**Files in this section:**
- this page
- `22_Asset_Rights_and_Sources/asset_register.csv` (the live register; one row per asset)
- `22_Asset_Rights_and_Sources/research_appendices/` (A–F, the full research records with access dates).

**How licence facts were checked:**
- Font licences were read from the licence files shipped in the font packages (bundled in `tools/render/fonts/`).
- All other licence terms come from **search excerpts on 2026-10-14** (appendix F). No page could be opened, so confirm each on the provider's page before relying on it.
- **Nothing was purchased or subscribed to.**

---

## 1. Originality and ownership
- All Worldosphere characters, worlds, rules, scripts, typography decisions, HUD designs, style frames and the motion proof were created in this project. None of them is traced from, generated from or copied from the reference.
- The reference videos (REF01, REF02) belong to their creator.
  - They are kept **outside** the repository (`.gitignore`). Only their file names and MD5 checksums are recorded (`References_Supplied/README.md`).
  - Frame grabs, audio and ASR text of the reference are **not committed**. The analysis tools can regenerate every measurement from a local copy (`tools/analysis/README.md`).
  - The breakdowns quote short transcript fragments for analysis only.
- **The GitHub repository holding this package is public.** Keep licensed audio, raw VO, contracts and any reference media out of it (23 §1).

## 2. Fonts (verified from the licence files)
| Font | Licence | Proof | Notes |
|---|---|---|---|
| Big Shoulders Display 800/900 | SIL Open Font License 1.1 | `tools/render/fonts/LICENSE_big-shoulders-display.txt` | Google Fonts may list it as the "Big Shoulders" family with an optical-size axis (F §6) |
| Atkinson Hyperlegible Next 400/700/800 | SIL OFL 1.1 | `tools/render/fonts/LICENSE_atkinson-hyperlegible-next.txt` | Braille Institute legibility design |
| JetBrains Mono 700/800 | SIL OFL 1.1 | `tools/render/fonts/LICENSE_jetbrains-mono.txt` | — |

**What the OFL allows (per the OFL FAQ as summarised in F §6; re-read it at openfontlicense.org):**
- Text rendered into a video is output and is not covered by the OFL, so burning it into monetized videos is allowed, with no attribution or fee.
- Do not sell the font files themselves, and do not distribute modified fonts under a reserved name.
- If project files that bundle the fonts are ever shared, include the licence files.

## 3. Music and sound effects
**Rules for Worldosphere:**
1. **Prefer original audio**: the motif, pulse beds and Foley. Original audio carries no claims and stays consistent with the brand.
2. **Shorts over 60 s:** a third-party source says that a Short over 1 minute with an active Content ID claim is blocked. This is **unverified** (B §9). Until it is checked on YouTube Help, use **no claimable third-party music** in any episode (all are 48–72 s).
3. Every non-original audio file gets an asset-register row with its source, licence, proof file and download date (QA A-07).
4. Content ID can't read licences, so a licence doesn't prevent claims; it wins disputes. Keep the proof.

| Source | Terms as seen (2026-10-14; verify) | Use in Worldosphere |
|---|---|---|
| **YouTube Audio Library** | Free. Per YouTube Help (search excerpt): its tracks "are not claimed by a rights holder through Content ID", and YPP members can monetize videos that use them. Some tracks are CC BY 4.0 (paste the attribution into the description). The standard licence is reportedly scoped to YouTube use | **Allowed** for YouTube. Check each track's licence type and any limit on Shorts length |
| **Sonniss GDC Game Audio Bundle** | Free, royalty-free, commercial use, no attribution. No redistribution as standalone SFX. AI/ML training reportedly prohibited | **Allowed** for SFX. Keep the licence PDF from the download |
| **Freesound** | Per file: CC0 (no credit), CC BY (credit), CC BY-NC (non-commercial only) | **CC0 and CC BY only**; credit CC BY in the description |
| **Pixabay audio** | Pixabay Content License: commercial use, no attribution. Third parties report retroactive Content ID claims | SFX only, with care; keep the download record. Avoid it for music |
| **Epidemic Sound / Artlist** | Subscriptions; Artlist "Social" clears monetization for one channel per platform; Epidemic safelists channels. Prices conflict across sources | Optional later. Confirm the plan covers monetized YouTube Shorts and safelist the channel first |
| **BBC Sound Effects (RemArc)** | Free licence excludes commercial use | **Not allowed** (a monetized channel is commercial) |
| **YouTube Creator Music** | YouTube Help notes paid licences phasing out from Aug 2026 (search excerpt) | Not planned |
| **Real emergency-alert tones (EAS/WEA), broadcast sirens** | Not licensable for this use, and they risk alarming viewers | **Not allowed**: original alert chimes only (QA A-08; C-104) |

## 4. Voice
| Option | Requirement before use |
|---|---|
| Owner's own voice | None beyond keeping the raw recordings |
| Contracted actor (e.g. a marketplace or agency booking) | A written licence covering: organic YouTube/Shorts, monetization, worldwide, term (perpetual preferred), cut-downs, and **no synthetic cloning of the actor's voice without separate written consent**. Paid-ad boosting needs broadcast or paid-media rights (F §4) |
| Licensed synthetic narrator | A paid plan that includes a commercial licence (e.g. the ElevenLabs Free tier has **no** commercial licence and requires attribution; paid plans include one, excluding Beta features, per F §4). **No cloning of any real person's voice.** Save the plan terms on the day of each generation |
| Never | Imitating an identifiable creator's or celebrity's voice (08 §10). Voice-and-likeness laws vary; e.g. Tennessee's ELVIS Act is in force, and the federal NO FAKES Act was **not** law as of the research date (F §4) |

**Monetization note:** whether AI narration affects YouTube monetization was **not verified** (B §6). The inauthentic-content policy targets mass-produced, repetitive videos. Worldosphere's protection is original scripts, staging and edits for every episode.

## 5. Generative tools (optional helpers)
Allowed only as described in 12 §7 (ideation, background drafts redrawn as vector). Before using any tool:
- save its terms
- confirm commercial use is allowed for the plan in use
- confirm it doesn't claim ownership of outputs
- note any training-use restrictions on uploaded inputs.

Disclosure: not required for clearly animated content (B §7; C-P01).

## 6. Third-party software used to build this package (analysis and prototypes only; not distributed in videos)
Licence details below are from prior knowledge **[PK]** and were not re-verified this session.

| Software / model | Used for | Licence [PK] |
|---|---|---|
| FFmpeg / ffprobe | Measuring loudness, cuts and audio; encoding prototypes | LGPL/GPL (build-dependent) |
| Playwright + Chromium (headless) | Rendering style frames and specimens | Apache-2.0 (Playwright); BSD-style (Chromium) |
| sherpa-onnx | Speech recognition runtime for the transcript timing | Apache-2.0 |
| NVIDIA Parakeet-TDT 0.6B v2 (int8) | ASR with word timestamps | CC-BY-4.0 |
| OpenAI Whisper small.en | ASR cross-check | MIT |
| Silero VAD | Voice activity detection | MIT |
| NumPy, fontTools | Analysis; font conversion | BSD / MIT |
| @fontsource packages 5.3.0 | Font files | Fonts: OFL 1.1 (verified, §2) |

## 7. Factual-source records
| Record | What it holds |
|---|---|
| `07_Survival_Logic_and_Facts/claim_ledger.csv` (+ `.md`) | **71 claims:** ID, class, source, assumptions, qualification, approved script wording, visual implication, status, episodes. Regenerate with `python3 -I tools/gen_ledger.py <root>` after editing `tools/ledger_data.py` |
| `22_Asset_Rights_and_Sources/research_appendices/D1_facts_natural.md` | Natural-hazard facts with exact quotes, URLs and access dates (earthquakes, water, weather, ice, rip currents, etc.) |
| `22_Asset_Rights_and_Sources/research_appendices/D2_facts_home_outdoor.md` | Home and outdoor facts (generators/CO, fire, water storage, elevators, etc.) |
| `22_Asset_Rights_and_Sources/research_appendices/B_youtube_platform.md` | YouTube requirements with quotes, URLs, and official / non-official flags |
| `22_Asset_Rights_and_Sources/research_appendices/C_topic_demand.md` | Topic-demand evidence, comparable creators [R-S#] and seasonal signals |
| `22_Asset_Rights_and_Sources/research_appendices/A_reference_account.md` | The access log for the reference account (nothing retrievable) |
| `22_Asset_Rights_and_Sources/research_appendices/F_tools_licensing.md` | Tools, prices as seen, and licences |

**Source standard for publication (QA F-01–F-05):**
- every real-world claim on screen or in voice has a ledger row marked SUPPORTED or QUALIFIED, with publisher, title, URL, access date and the exact supporting words
- the description of each P2/P3 episode lists those sources
- before the first publication, re-open each cited page and confirm the wording is still current. The research only saw search excerpts.
