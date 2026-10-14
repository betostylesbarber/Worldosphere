# 02 — Source inventory and coverage report

**Research cutoff / observation date:** 2026-10-14 (all times in this document are UTC unless stated).
**Evidence labels used across this package:** OBSERVED · MEASURED (method stated) · INFERRED · RECOMMENDED · UNKNOWN. "NOT ACCESSIBLE" means we could not inspect it. It does **not** mean it doesn't exist or is zero.

## 1. Where the materials were looked for

| Location requested | What was found | Status |
|---|---|---|
| "Worldosphere" folder on the Desktop of the current computer | This assignment ran in a **cloud container**, not on your computer. The container has no Desktop (`/root/Desktop` does not exist), and none was redirected. The only Worldosphere folder is the Git repository `betostylesbarber/Worldosphere`, cloned to `/home/user/Worldosphere`. It was **empty**: no commits and no files on any branch (checked with `git ls-remote`). | **ACCESS GAP.** None of your local Desktop materials could be inspected: production guides, recipes, brand rules, earlier analyses, scripts, storyboards, captions, research, topic lists, existing Worldosphere videos, character sheets, backgrounds, props, animation projects, templates or audio. |
| Files attached to the session | Two MP4 files (REF01, REF02) | Fully inspected (see §2) |
| Reference account `instagram.com/stickocalypse_shorts` | The network policy here blocks instagram.com, youtube.com, tiktok.com, reddit.com and analytics sites (proxy 403). The page-fetch tool failed DNS for every host. Web search returned **no** result about the account. | **NOT ACCESSIBLE.** Profile facts, catalog, dates, captions, metrics and comments are unknown. |
| Official YouTube channel of the reference creator | None found by search | **NOT FOUND / NOT ACCESSIBLE** (a channel may still exist) |

**What this means for the plan.**
1. Every creative finding about the reference rests on **two videos**: Parts 1 and 2 of one three-part story. That is enough to reverse-engineer the format, the craft and the production system. It is **not** enough to describe the whole account's niche, its range or why any video performed. Those claims are marked INFERRED or UNKNOWN throughout.
2. We could not check which subjects Worldosphere has **already covered**. Before you lock the calendar, compare the 30 topics with your local Worldosphere folder. That check is listed in `23_Limitations_and_Next_Actions.md`.
3. If your local folder has existing brand rules or character designs, this package's brand bible (08) is a **proposal** to reconcile with them, not an automatic replacement. Nothing local was overwritten. Nothing local was readable.

## 2. Inventory: local (supplied) files

| ID | Filename (as uploaded) | Local path in session | Title / description | Platform & publication date | Observed | Duration | Aspect / resolution / fps | Subject & format | Main characters & setting | Opening hook | Central conflict | Final payoff | Public metrics | Visuals fully inspected | Audio fully inspected | Duplicate / version | Status / limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REF01 | 888bf781-snapgram.io_download-file-2log5rc1.mp4 | /root/.claude/uploads/…/888bf781-….mp4 (session only) | "The Last Farm", Part 2 | Instagram (inferred from the downloader name); date NOT ACCESSIBLE | 2026-10-14 | 87.12 s | 9:16 · 720×1280 · 30 fps | Serialized zombie-survival narrative with narrator + dialogue | Eli (farmer), Mara (neighbor), Rusty (dog); farm barn, fields, creek | A voice in the dark barn says "Eli?" → "The thing inside Eli's barn knew his name." | Trust (is Mara bitten?) → consequence of generator noise → fence breach | One infected is already inside; a horde beyond; "too big to defend"; teaser for Part 3 | NOT ACCESSIBLE | Yes (1 fps full run, 10 fps opening and endings, every cut and caption event) | Yes, by machine (2 ASR models, pitch, loudness, gap spectra, onsets). No human listening | Unique; sequel to REF02 | Complete. Original quality and date unknown |
| REF02 | e0450760-snapgram.io_download-file-4baz726m.mp4 | /root/.claude/uploads/…/e0450760-….mp4 (session only) | "The Last Farm", Part 1 | Instagram (inferred); date NOT ACCESSIBLE | 2026-10-14 | 61.04 s | 9:16 · 720×1280 · 30 fps | Second-person survival explainer that turns into a narrative | Eli, Rusty; farm (kitchen, fields, shed, porch, barn) | "If the zombie apocalypse starts while you're on a farm, don't run to town." | Prepare the farm in about 30 minutes without making noise | Supplies look good "on paper", but "someone was already inside the fence"; teaser for Part 2 | NOT ACCESSIBLE | Yes | Yes, by machine | Unique; prequel to REF01 | Complete |

Hashes: REF01 `9213c9adc3d2bfbb9cd20e532137ba36` · REF02 `232bdcc43a43c29dd4afe9c396352d0c`. The two are **not duplicates** and not alternate edits. They are consecutive parts of one story.

## 3. Inventory: online references (catalog at research cutoff)

| ID | Item | Source | Status |
|---|---|---|---|
| ONL-01 | `stickocalypse_shorts` Instagram profile (bio, followers, posts, link) | instagram.com | NOT ACCESSIBLE |
| ONL-02 | Other reels in the account (including "The Last Farm" Part 3) | instagram.com | NOT ACCESSIBLE; Part 3 not found by search |
| ONL-03 | Linked YouTube / TikTok channels | search | NOT FOUND. A name collision exists: "Stickocalypse" is also an unrelated 2014 Flash game (see `22_…/research_appendices/A_reference_account.md`) |
| ONL-04 | Third-party analytics (Social Blade etc.) | search | NOT FOUND / NOT ACCESSIBLE |
| ONL-05 | Viewer comments | — | NOT ACCESSIBLE: no comment evidence for the reference |

## 4. Coverage totals (reconciled)

| Set | Items known | Unique videos | Fully inspected (visual + audio) | Partly inspected | Not accessible |
|---|---|---|---|---|---|
| Local supplied files | 2 | 2 | **2** (audio by machine analysis) | 0 | 0 |
| Online reference catalog | Unknown size | Unknown | **0** | 0 | Whole catalog |
| Total analysed | — | **2** | **2** | — | — |

Reconciliation: 2 supplied files = 2 unique videos = 2 complete breakdowns (`03_Video_Breakdowns/REF01…`, `REF02…`). No online video was viewed. **No claim in this package describes the whole account.**

## 5. Progress ledger (what was done, in order)

1. Located the materials. Confirmed there is no Desktop and the repository is empty.
2. Probed and hashed both videos. Extracted frames at 1 fps (148 frames) and at 10 fps for 0–3.2 s.
3. Detected cuts in every frame (109 candidates). Verified each one visually.
4. Transcribed with two speech models. Agreement was near-verbatim. The only differences were punctuation and "Two Farms East" capitalization.
5. Measured audio: loudness (EBU R128), per-phrase pitch, speech gaps, spectral flatness, onsets.
6. Read every caption change from the caption band (261 events in total).
7. Wrote the shot-by-shot timeline (80 shots) and the component analysis A–J.
8. Ran online research in six parallel threads: account, platform rules, topic demand, two fact ledgers, tools and licensing. All were limited by blocked page access and an exhausted shared search budget. See the access logs in `22_Asset_Rights_and_Sources/research_appendices/`.
9. Built the creative system: niche and pillars (05), the brand and animation bible (08), typography and captions (09), and the survival-logic framework with its claim ledger (07).
10. Scored 94 premises (15), selected 30 and 10 reserves (16), and dated the calendar (17).
11. Wrote the Day 1–3 production packages with the caption and timing engine (`tools/package_engine.py`) (19).
12. Rendered the style frames and the Fork/breath motion proof, then inspected them frame by frame and fixed the defects found (11).
13. Three parallel writers drafted the briefs for Days 4–30. Every brief was then checked by script (fields 1–29; title, Verdict, duration and reserve match the calendar; no lane-B captions during a Fork) and edited for consistency (change log CL-005 to CL-010 in 21 §8).
14. Wrote the production manual (12), master QA checklist and templates (13), improvement audit (10), performance hypotheses (06), schedule and buffer plan (20), measurement plan (21), asset-rights record (22), limitations (23), the next-video checklist (24), the workbook and the index (00).
