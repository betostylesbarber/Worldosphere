# 23 — Outstanding limitations and next actions

Everything here is something this session **could not** do or verify. Each item comes with the concrete action that closes it and when it is due. The dates assume Scenario A (launch Sat 31 Oct; 20 §2).

## 1. Access and environment limitations

| # | Limitation | Consequence | Next action | Owner | Due |
|---|---|---|---|---|---|
| L1 | **The "Worldosphere" folder on the Desktop was not inspected.** This work ran in a cloud container with no access to the owner's computer, and the repository was empty at the start (02 §1) | Existing scripts, assets, branding or past uploads there may already cover subjects in this plan, or contain things to preserve | When downloading this package, place it **inside** the Desktop "Worldosphere" folder as its own dated subfolder (it doesn't overwrite anything). Then run `python3 tools/desktop_intake.py "<path to Desktop/Worldosphere>"` from the package folder. It is read-only: it inventories every file, detects copies of the reference videos by MD5, and flags files that mention a planned episode's subject, writing a timestamped report into the package. Review the flags against the calendar (17) and the brand (08), and log any change in the change log | Owner | Before Oct 17 |
| L2 | **The reference account's online catalog was not accessible** (Instagram, YouTube, TikTok and the aggregators were blocked; no search result named the account; A §1) | Online coverage is 0 videos. Other uploads could share premises with Worldosphere's topics; no metrics or comments were analysed | ≈30 minutes in a normal browser: list the reference's video titles and dates; note any premise that matches a Worldosphere topic. A match doesn't require a change (premises are general), but every Worldosphere execution must stay original (05 §5) | Owner | Before Oct 17 |
| L3 | **Web pages could not be opened** (WebFetch DNS failure; proxy 403s). All research comes from search excerpts, and the shared search budget ran out | Platform facts, tool prices and claim sources need confirmation on the live pages | See §2 (platform) and the ledger sprint (20 §6) | Producer | Oct 15–21 |
| L4 | **The Worldosphere YouTube channel was not inspected** | Unknown: existing uploads, subscribers, YPP status, audience regions, branding | Check the channel in Studio; record the baseline in the workbook *Tracking* sheet before Day 1 | Owner | Before Oct 28 |
| L5 | **The GitHub repository `betostylesbarber/Worldosphere` is public** | Anyone can read the plans. Licensed audio, raw VO, contracts or reference media must never be committed there | Decide whether to make the repository private (GitHub > Settings > General > Danger Zone > Change visibility). Keep production media in a private store | Owner | Now |
| L6 | **No production capacity was measured** | Hour estimates are unproven (12 §9) | Run the pilot (20 §5) and decide at the Oct 28 gate | Owner + team | Oct 28 |

## 2. Platform requirements: checked on official YouTube and Google pages (2026-10-14)

Checked with official-domain web searches (support.google.com, blog.youtube) once the search budget reset. As with every source in this package, the wording came from search excerpts: reopen the page before relying on a detail.

| # | Item | Result (official source) | Effect on the plan |
|---|---|---|---|
| P1 | Shorts over 1 minute with an active Content ID claim | **Official pages conflict.** "Understand three-minute YouTube Shorts" (answer 15424877) says such Shorts are "blocked globally"; a newer "Create YouTube Shorts" page says they are "no longer automatically blocked and may remain playable" | Keep the conservative rule either way: **no claimable third-party music** (22 §3) |
| P2 | Audio Library terms for Shorts | **Confirmed** (answers 3376882, 13486873): Audio Library tracks aren't claimed through Content ID; YPP members can monetize them; Creative Commons tracks need the artist credit in the description; royalty-free Audio Library music in Shorts won't receive a Content ID claim. Creator Music can't be used in Shorts and is phasing out paid licences from Aug 2026 | The Audio Library is a safe free option |
| P3 | Analytics definitions | **Confirmed**: engaged views = "How many times viewers stayed to watch past the initial seconds, not including any loops"; "Viewed (vs swiped away)" is the percentage of feed impressions viewed rather than swiped (the Reach page labels it "Stayed to watch"); the YouTube Blog says CTR, average view duration and retention calculations are unchanged by the 24 Aug 2026 view-count change | 21 §1 holds |
| P4 | Shorts features | **Confirmed** (answers 14075157, 13748639, 1270709, 9080341): a related video can be added in Studio with advanced feature access (public or unlisted, from your channel); links in Shorts descriptions and comments are not clickable; Studio scheduling works for Shorts; Shorts can't be Premieres. Playlists and remix settings were not checked (low impact) | Saga Part 2 links to Part 1 via "related video"; description sources are plain text |
| P5 | YPP stance on AI narration | **Confirmed** (answers 1311392, 2801973, 14328491): AI use isn't disqualifying; mass-produced or repetitive content (generic templates, AI scripts over repetitive imagery) isn't monetizable; a synthetic voice that could be mistaken for a real person must be disclosed | 22 §4 stands |
| P6 | Organic Shorts safe zones | **Official guidance found**: the Shorts editor shows visual guides marking non-safe areas (answer 16215842); Google Ads Shorts guidance: keep text out of the top 10%, bottom 25% and right 10% | 09 §2 zones are consistent. A quick look in the Shorts editor, or a **private** upload viewed on your phone, is still a recommended local check (it needs your device) |
| P7 | Upload encoding | **Confirmed** (answer 1722171): stereo audio 384 kbps; AAC-LC or Opus at 48 kHz; BT.709 for SDR; upload at the recorded frame rate | 12 §2 audio bitrate raised from 320 to 384 kbps |

## 3. Content and fact limitations

| # | Limitation | Next action | Due |
|---|---|---|---|
| C1 | **Closed 2026-10-14: no claim is UNVERIFIED — BLOCKING.** All 15 were checked against official or primary sources (NWS/NOAA, CDC/CPSC, NASA/ESA, USAP/BAS, MN DNR, NFPA/USFA, CAL FIRE, Ready.gov, peer-reviewed papers): 9 SUPPORTED, 6 QUALIFIED (`07_Survival_Logic_and_Facts/verification_results.csv`; CL-013). Four scripts changed because of the evidence: WS-002 (power window, not a punch tool), WS-020 (no transformer-hum claim; "for hours"), WS-025 (no "Only Rescue"), WS-028 (no "move diagonally"). Only C-1101 stays an in-story detail with no real-world claim | Process for future claims stays the same (`Verification_Worksheet.md`) | — |
| C2 | All claims, including the newly verified ones, were checked through search excerpts | Re-open each cited page before the episode's script lock (QA F-03); the URLs are in the ledger | T-10 |
| C3 | **Closed 2026-10-14:** every [PENDING VERIFICATION] marker in the briefs was resolved and replaced by the claim's checked status | — | — |
| C4 | WS-028 (crowd surge) needs a **sensitivity review** beyond fact-checking (real crowd tragedies) | A second reader checks tone, framing and the absence of real-event imagery; or swap to R02 | T-10 (Tue 17 Nov) |
| C5 | Days 4–30 have briefs, not full packages (by design: only Days 1–3 were to be fully developed) | Produce a package per episode using the Day 1–3 packages as examples and the pipeline in `tools/` (12 §5) | T-8 per episode |
| C6 | The Day 1–3 caption timings are **provisional** (modelled at 2.85 words/s) | Re-time to the recorded VO (QA W-01) | At edit |

## 4. Prototype limitations (11)
- The style frames and motion proof are procedural prototypes, not production art. Walk cycles are basic; there is no lip-sync and no audio.
- The motion proof is silent, so it was **not** given a complete-viewing-with-sound review. Its compression after a YouTube re-encode was not tested.
- Known fixes for production:
  - separate the tangled crowd silhouettes in SF1
  - simplify Kai's hood silhouette
  - raise the fog-patch opacity in SF3.

## 5. Next actions, in order (the first two weeks)
1. **Now:** decide the repository visibility (L5). Read `01_Executive_Overview.md` and `20_Production_Schedule_and_Buffer.md` §2, and decide the staffing scenario (A, B or C).
2. **Oct 15–17:**
   - open the cited pages for the Days 1–5 claims and confirm the wording (QA F-03; the URLs are in the ledger)
   - Desktop folder and reference catalog checks (L1, L2)
   - channel baseline (L4)
   - voice decision (22 §4).
3. **Oct 18–22:**
   - the library build (12 §4)
   - script lock for Days 1–5 (re-time the Day 1–3 packages)
   - VO batch 1
   - the device safe-zone check (P6: the Shorts editor guides or a private upload).
4. **Oct 23–28:** produce Days 1–5 with full QA, including the playback section, and log the pilot hours.
5. **Wed Oct 28:** the go/no-go gate (20 §2.3). The owner decides whether and when to publish. Nothing has been published or scheduled.
