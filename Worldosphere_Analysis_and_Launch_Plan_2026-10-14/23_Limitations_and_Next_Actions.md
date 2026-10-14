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

## 2. Platform requirements to verify on official YouTube pages before launch

The step-by-step procedure and where to record each result: `07_Survival_Logic_and_Facts/Verification_Worksheet.md` §C.

| # | Item | Why it matters | Where (from appendix B) |
|---|---|---|---|
| P1 | Whether a Short over 1 minute with an active Content ID claim is blocked | Decides whether any third-party music is safe in 61–72 s episodes | YouTube Help, rights-holder / Shorts music pages (B §9) |
| P2 | YouTube Audio Library terms for Shorts (including any length limits) and CC BY attribution format | Free music option | support.google.com/youtube/answer/3376882 |
| P3 | Analytics metric definitions after the 24 Aug 2026 view-count change (which denominator AVD and APV use; the "Stayed to watch" label) | The measurement plan's denominators (21 §1) | YouTube Analytics Help glossary; Studio |
| P4 | Shorts features: related-video link, playlists, pinned comments, scheduling, remix permissions | Saga linking (T-12), the CTA plan, posting logistics | YouTube Help (B §11) |
| P5 | The YPP stance on AI narration (only if a synthetic voice is chosen) | Monetization eligibility | YPP monetization policies (B §6) |
| P6 | Organic Shorts safe zones on current iPhone and Android apps | Caption and hook placement (09 §2) | A private test upload of the safe-zone overlay (09 §2 device check); **private only, never public** |
| P7 | The upload encoding page (audio bitrate, colour space) | Export settings (12 §2) | support.google.com/youtube/answer/1722171 |

## 3. Content and fact limitations

| # | Limitation | Next action | Due |
|---|---|---|---|
| C1 | **15 claims are UNVERIFIED — BLOCKING** (ledger; 20 §6 lists each with a deadline and a reserve). C-1205 and C-1206 were re-classed QUALIFIED from the USFA excerpt in appendix D2 §3c (CL-012) | Follow `07_Survival_Logic_and_Facts/Verification_Worksheet.md`: record each result in `verification_results.csv` and regenerate (the ledger, 20 and the workbook update automatically) | Days 1–5 claims by Sat 17 Oct; the rest at T-10 |
| C2 | Even SUPPORTED claims were checked through search excerpts only | Re-open each cited page before the episode's script lock (QA F-03) | T-10 |
| C3 | Ten briefs carry [PENDING VERIFICATION] markers on specific lines: WS-012, WS-016, WS-018, WS-020, WS-023, WS-025, WS-027, WS-028, WS-029, WS-030. WS-005 depends on BLOCKING row C-506 (field 8) | Treat the marked lines as placeholders; swap to the named reserve if not verified | T-10 per episode |
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
   - the claim sprint for Days 1–5 (C1)
   - platform checks P1–P3
   - Desktop folder and reference catalog checks (L1, L2)
   - channel baseline (L4)
   - voice decision (22 §4).
3. **Oct 18–22:**
   - the library build (12 §4)
   - script lock for Days 1–5 (re-time the Day 1–3 packages)
   - VO batch 1
   - the device safe-zone test (P6, private upload).
4. **Oct 23–28:** produce Days 1–5 with full QA, including the playback section, and log the pilot hours.
5. **Wed Oct 28:** the go/no-go gate (20 §2.3). The owner decides whether and when to publish. Nothing has been published or scheduled.
