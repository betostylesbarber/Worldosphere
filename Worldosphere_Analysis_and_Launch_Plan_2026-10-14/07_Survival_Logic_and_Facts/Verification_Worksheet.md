# Verification worksheet: closing every open claim and platform fact

**Why this exists.** The cloud session could not open web pages: WebFetch failed DNS for every host, and the egress policy refused government and YouTube Help sites with 403. Its search budget also ran out. So **15 claims are UNVERIFIED — BLOCKING**, 3 are low-risk UNVERIFIED, and 7 platform facts are unconfirmed. In a normal browser, each item takes about 10–30 minutes. This worksheet gives the exact procedure. The results flow into the ledger, the schedule and the workbook automatically.

## Results of the 2026-10-14 check (completed in the cloud session once the search budget reset)
- **Section A (15 BLOCKING claims): all closed.** 9 SUPPORTED and 6 QUALIFIED, from official or primary sources (NWS/NOAA, CDC/CPSC, NASA/ESA/AMS, USAP/BAS, Minnesota DNR, NFPA/USFA, CAL FIRE, Ready.gov, FCC, peer-reviewed papers). Every row, with its URL, excerpt and qualification, is in `verification_results.csv`. The ledger is regenerated from it.
- **Section B:** C-101 SUPPORTED (NWS) and C-207 SUPPORTED (AAA tests reported in an NHTSA ESV paper). C-1101 stays an in-story detail with no real-world claim.
- **Section C:** P1 checked, and the YouTube Help pages contradict each other, so the conservative "no claimable music" rule stays. P2, P3, P4 (related video, scheduling), P5 and P7 are confirmed. P6 has official guidance (the editor's safe-area guides; the ads zones); a look on your own phone is still recommended. Details: 23 §2.
- **Script changes the evidence forced:**
  - WS-002: power window, not a punch tool
  - WS-020: no transformer-hum claim; the 1989 blackout lasted "for hours"
  - WS-025: no "Only Rescue" title
  - WS-028: "toward where the crowd thins", not "diagonally"
  - WS-027: the NFPA caution on oil turkey fryers goes in the description.
- **What remains:** reopen each cited page before the episode's script lock (QA F-03), because the check used search excerpts. The procedure below stays the process for any new claim.

## How to record a result (one row per claim)
1. Open the source page and find the sentence that supports or contradicts the claim. Copy it **exactly**.
2. Add a row to `07_Survival_Logic_and_Facts/verification_results.csv` with these columns:
   - `Claim ID`
   - `New status` (SUPPORTED / QUALIFIED / FALSE)
   - `Source URL`
   - `Exact quote`
   - `Access date` (YYYY-MM-DD)
   - `Verified by`
   - optional `Qualification`, `New script wording`, `Notes`.
3. Regenerate the outputs (from the package root):
   ```bash
   python3 -I tools/gen_ledger.py "$PWD"            # ledger CSV + readable copy (refuses SUPPORTED/QUALIFIED without URL, quote, date, name)
   python3 -I tools/gen_schedule_tables.py "$PWD"   # deadline tables in 20
   python3 -I tools/gen_workbook.py "$PWD"          # workbook (save your filled-in copy under another name first)
   ```
4. **If the result is FALSE, or nothing authoritative supports the claim,** use the fallback in the table: cut the line, or swap to the named reserve. Log it in the change log (21 §8).

**Source rule:** a government agency, a standards body, peer-reviewed research or the original program's own page. News articles and blogs may point you to a source but never count as one (07 §2).

---

## A. BLOCKING claims (must be closed by the deadline, or the episode uses its fallback)

| Claim | Episode · publish | Verify by | Where to check (from research appendices D1/D2) | What exactly must be confirmed | If confirmed → | If not → |
|---|---|---|---|---|---|---|
| **C-205** Belt/window order when a car is in water | WS-002 · Sun 1 Nov | **Sat 17 Oct** | U. Manitoba Giesbrecht page (umanitoba.ca/kinesiology-recreation-management/faculty-staff/gordon-giesbrecht); Giesbrecht's published protocol; the 2013 review PDF cited in D1 §6 | Which comes first in **current** guidance: "Seatbelts off → Windows" or "Window → Seatbelt"? | Lock Version A ("Belt off. Window.") or Version B ("Window. Belt off."), both already in the WS-002 package §3 and §9 | If sources conflict, use the order the researcher's own current page gives. If none can be found: swap to **R02** (verified) |
| **C-506** CO suspected → fresh air first, then call for help | WS-005 · Wed 4 Nov | **Sat 17 Oct** | CDC carbon-monoxide pages (cdc.gov, "carbon monoxide poisoning", the "what to do" / FAQ section); CPSC CO safety guide (cpsc.gov, search "carbon monoxide") | Agency wording that people with suspected CO poisoning should get to fresh air immediately and call 911 or emergency services | Status SUPPORTED; keep "Fresh air first. Then call for help." | Swap to **R08** (verified) |
| **C-505** Battery-backed CO alarms (only if used) | WS-005 | Sat 17 Oct | CPSC CO alarm guidance; CDC CO prevention page | That agencies advise installing battery-operated or battery-backup CO alarms | Optional line may be used | Cut the alarm line (the episode doesn't need it) |
| **C-1003** Cell sites / fuel pumps need power (only if stated) | WS-010 · Mon 9 Nov | Fri 30 Oct | FCC or CISA backup-power pages; Ready.gov power-outage page | That cell sites rely on backup power for a limited time and fuel pumps need electricity | May state it without hour figures | **Cut** (the calendar already says cut unless verified) |
| **C-1501** Inland Antarctic winter temperatures (only if a number is shown) | WS-015/016 · Sat 14 Nov | Wed 4 Nov | British Antarctic Survey or the US Antarctic Program (NSF) station climate pages | A typical winter low at an inland station well below −30 °C (for the −41 °C readout) | Show the readout | Use a gauge with no number (the WS-016 brief fallback) |
| **C-1704** What a rip current looks like (only if shown) | WS-017 · Mon 16 Nov | Fri 6 Nov | NWS rip-current safety pages (weather.gov/safety/ripcurrent); NOAA Ocean Today | The listed visual signs (gaps in breaking waves, churning or discoloured water, foam moving seaward) | Animate the signs | Don't animate them (the episode works without) |
| **C-1801** Chelyabinsk 2013: flash then delayed shock wave; injuries mostly from glass | WS-018 · Tue 17 Nov | **Sat 7 Nov** | NASA (CNEOS / Planetary Defense) and ESA pages on the Chelyabinsk event | The date (15 Feb 2013), the delay between flash and shock wave, about 1,500 injuries, and that most were from broken glass | REAL RULE "A bright flash in the sky? Stay away from windows." becomes usable if an agency source supports the advice; otherwise state only the history | Swap to **R01** (verified) |
| **C-1802** Leonids 2026 peak date; shower meteors are harmless dust | WS-018 | **Sat 7 Nov** | American Meteor Society 2026 meteor-shower calendar; IMO calendar; NASA meteor pages | The 2026 peak date; that shower meteors are tiny particles that burn up | State "harmless dust"; **keep the date off screen** unless confirmed | Drop the Leonid line (the brief already keeps the date off screen) |
| **C-2001** Carrington 1859; Quebec 13 Mar 1989 (~9 h); May 2024 G5; transformer damage risk | WS-020 · Thu 19 Nov | Mon 9 Nov | NOAA SWPC (swpc.noaa.gov, including the NOAA space-weather scales page); NASA; Hydro-Québec | Each date and figure used on screen; SWPC's G5 description | Use SWPC's G5 wording verbatim | Swap to **R01** (named in the calendar) |
| **C-2104** Minimum ice thickness (only if a number is shown) | WS-021 · Fri 20 Nov | Tue 10 Nov | Minnesota DNR ice-thickness guidelines; Wisconsin/Michigan DNR | The minimum thickness of new clear ice for walking | Show the number with "new clear ice" | No number on screen (the brief's default) |
| **C-2301** Ready, Set, Go!: leave early when told; embers travel ahead of the fire | WS-023 · Sun 22 Nov | Thu 12 Nov | Ready.gov wildfires page (ready.gov/wildfires); IAFC Ready, Set, Go! program; CAL FIRE; NFPA Firewise | "Leave when told / don't wait" wording; that embers can ignite homes ahead of the flame front (no distance) | REAL RULE draft "Wildfire: leave as soon as you're told to. Sooner if you feel unsafe." | Swap to **R02** |
| **C-2501** Avalanche survival falls sharply after ~15–18 min; companion rescue with beacon, probe and shovel | WS-025 · Tue 24 Nov | Sat 14 Nov | avalanche.org (US National Avalanche Center); Haegeli et al., CMAJ 2011; Brugger et al. survival-curve papers | The shape of the survival curve (keep "15 minutes" off screen unless the source states it); companion rescue as the main chance | REAL RULE draft "Avalanche: your partners are the rescue team. Speed is everything." | Swap to **R08** |
| **C-2701** Thanksgiving = peak day for home cooking fires; no water on grease fires; fryer outdoors and away from buildings; thawed turkey | WS-027 · Thu 26 Nov | Mon 16 Nov | NFPA Thanksgiving cooking-fire pages; USFA cooking-fire and turkey-fryer guidance; UL | Each of the four statements, with NFPA/USFA wording | Use the agency wording for the REAL RULE | Swap to **R01** |
| **C-2801** Crowd crush risk at high density; individual guidance (stay upright, protect the chest, move diagonally toward gaps) | WS-028 · Fri 27 Nov | Tue 17 Nov | Peer-reviewed crowd-safety research (e.g. G. Keith Still's work); any official event-safety guidance; **plus the sensitivity review** (23 C4) | Individual guidance from a credible source; **no density numbers on screen** unless sourced | Proceed after the sensitivity sign-off | Swap to **R02** |
| **C-2901** Stranded in a winter storm: stay with the car, keep the tailpipe clear, run the engine in short bursts, make the car visible | WS-029 · Sat 28 Nov | Wed 18 Nov | NWS winter safety (weather.gov/safety/winter); Ready.gov winter weather; CDC winter weather | Each step, and the agency's own interval wording if any interval is mentioned (the brief keeps the number off screen) | Use the agency wording | Swap to **R02** |

## B. Low-risk UNVERIFIED claims (add a source before publishing; they don't block the script)
| Claim | Episode | Where to check | Action |
|---|---|---|---|
| C-101 Breath visible in cold air (no temperature threshold) | WS-001 (by Sat 17 Oct) | Any NOAA/NWS or university atmospheric-science explainer on condensation | Add the citation to the description sources (QA F-03) |
| C-207 Laminated side glass may resist punch tools | WS-002 | NHTSA, or the tool or vehicle manufacturer | Description caveat only |
| C-1101 Stairwell door direction | WS-011, WS-013 | — | Kept as an in-story fact about one building; no real-world claim is made |

## C. Platform facts (from 23 §2), checked in a normal browser and in YouTube Studio
| # | Fact to confirm | Where | Record in |
|---|---|---|---|
| P1 | Is a Short over 1 minute with an active Content ID claim blocked? | YouTube Help: Shorts music and rights pages (search Help for "Shorts longer than 1 minute Content ID") | 22 §3 rule 2; if confirmed, keep "no claimable music"; if not, relax it |
| P2 | Audio Library licence types, attribution format and any Shorts length limit | YouTube Help answer 3376882; Studio > Audio Library | 22 §3 table |
| P3 | Analytics definitions after the 24 Aug 2026 view-count change (engaged views; the "Stayed to watch" label; the AVD/APV denominators) | YouTube Analytics Help glossary; Studio > Analytics (Advanced mode) | 21 §1 table |
| P4 | Shorts features: related-video link, playlists, pinned comments, scheduling, remix settings | YouTube Help | 21 T-12; `13_Templates/Upload_Package_Template.md` |
| P5 | The YPP stance on AI narration (only if a synthetic voice is chosen) | YPP monetization policies (answer 1311392) | 22 §4 |
| P6 | Organic Shorts safe zones on current iPhone and Android apps | Upload the safe-zone overlay **as a private video**, view it in the Shorts player on both phones, screenshot it | 09 §2; adjust the lanes if the UI covers them |
| P7 | Upload encoding details (audio bitrate, colour space) | YouTube Help answer 1722171 | 12 §2 |

**Done means:** every Section A row has a recorded result or an applied fallback before its deadline, Section B citations are in the descriptions, and P1–P7 are recorded with the date checked.
