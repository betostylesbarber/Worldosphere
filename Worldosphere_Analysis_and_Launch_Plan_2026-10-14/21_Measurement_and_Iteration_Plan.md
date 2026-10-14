# 21 — Measurement and iteration plan

**What this is.** A working method for learning from Worldosphere's own results: what to measure, when, how to compare, how to diagnose problems, and how to change the plan without guessing.
- **No result is predicted here.** There are no view targets and no "viral" thresholds, because no Worldosphere data exists yet and the reference account's metrics were not accessible (02).
- **Organic posts are not experiments.** Each video differs in topic, day, audience mood and how the platform distributes it. Comparisons between them are **observational**: they suggest; they don't prove. The decision rules below need a consistent pattern across several comparisons before anything changes.

---

## 1. Metric definitions and denominators

Platform definitions come from research appendix B §5 and were confirmed on YouTube Help and the YouTube Blog on 2026-10-14 (23 §2 P3). **Still check each label in your own Studio before the first review**, and note any differences in the change log.

| Metric | Definition used in this plan | Where to find it | Cautions |
|---|---|---|---|
| **Views (public count)** | Since 24 Aug 2026, counted from the first frame on all formats (B §5) | Video page / Studio | Inflated relative to engaged views. **Never use it as a denominator** |
| **Engaged views** | Views where the viewer stayed past the initial seconds, excluding loops (Studio definition as quoted in B §5) | Studio Analytics (Advanced mode) | YouTube doesn't publish the number of seconds. **This is the denominator for every derived rate below** |
| **Stayed to watch %** (formerly "Viewed vs. swiped away") | The share of Shorts-feed impressions where the viewer stayed rather than swiping away | Studio > Content (Shorts) | Measures **viewing choice** (frame 0 + first seconds). YouTube publishes no "good" threshold; the circulating "70%" figures are unverified |
| **Average view duration (AVD)** | Average watch time per view | Studio | Its denominator (views vs engaged views) must be checked in Studio after the 24 Aug 2026 change |
| **Average percentage viewed (APV)** | AVD ÷ video length | Studio | **Not a completion rate.** Loops can push it above 100%. A long video can have a lower APV with more total watch time |
| **Audience retention curve** | The % of viewers still watching at each moment | Studio > video > Retention | A spike can mean rewatching, scrubbing or looping. **It does not prove intentional rewatching** without other evidence (e.g. comments citing the moment) |
| **Shares** | Share actions | Studio | Count shares only from the video's own analytics |
| **Subscribers gained** | Subscriptions attributed to the video | Studio | Small numbers early; aggregate weekly |
| **Returning vs new viewers** | Where available | Studio > Audience | May need a minimum audience before it shows |
| **Comments** | Count + coded content (§4) | Studio > Comments | A self-selected sample, not a survey |

**Derived rates (all per 1,000 engaged views):**
- **Share rate** = shares ÷ engaged views × 1,000
- **Subscribe rate** = subscribers gained ÷ engaged views × 1,000
- **Comment rate** = comments ÷ engaged views × 1,000
- **Correction rate** = valid factual corrections ÷ total comments × 100 (per 100 comments)
- **Confusion rate** = comments asking what happened or why ÷ total comments × 100

**Comparison windows.** Compare videos at the same age (24 h with 24 h, 7 days with 7 days). Prefer **medians** of a group over single videos. Record every value in the workbook *Tracking* sheet at the checkpoint, not later from memory.

## 2. Baselines
There is no prior baseline.
- **Provisional baseline:** the median of Days 1–7 on each metric at the 7-day checkpoint.
- **Rolling baseline:** from Day 14, the median of the previous 14 published videos at the same age.
- The first week mixes three pillars and novel formats on purpose (17), so treat the early baseline as rough.
- Channel age is a confounder: a new channel's early videos can behave differently from later ones for reasons that have nothing to do with content.

## 3. The tests

**Rules:**
- **One main variable per test.**
- Hold the other variables steady where the calendar allows: the posting time stays at 12:00 ET through Day 14; the caption style stays fixed except in T-05.
- Each test names its comparison set in advance (from the calendar's "Main test" column, 17).

| ID | Area | Hypothesis | Variable | Primary measure | Quality guardrail | Comparison method | Review window | Decision rule |
|---|---|---|---|---|---|---|---|---|
| **T-01** | Hook wording + first frame | Hooks that show a concrete contradiction or clock in frame 0 earn more viewing choice than verbal-only questions | Hook pattern (HP01 diegetic contradiction, HP02 clock, HP03 "Everyone says…", HP04 wrong instinct, question titles): see the playbook (14) | Stayed to watch % | 3-second retention must not fall while Stayed to watch rises (a hook that over-promises loses viewers just after) | Group episodes by hook pattern; compare medians at 7 days; within-pillar pairs (Day 4 vs Day 8 myth-busting; Day 2 vs Day 23 clocks) | 7 days per video; pooled at Days 14 and 30 | Adopt a pattern as the default when its median beats the other patterns in **both** pillars it was used in **and** the guardrail holds. Otherwise keep rotating |
| **T-02** | Topic + scenario selection | P2 Real Rule episodes earn higher share rates; P1 Outbreak episodes earn higher comment rates | Pillar (P1 / P2 / P3) | Share rate (P2 hypothesis); comment rate (P1) | Correction rate (P2); Stayed to watch must stay within the channel's range | Medians by pillar at 7 days; weekly | Days 14 and 30 | Shift up to 2 future slots toward the stronger pillar **only** if the gap holds at both Day 14 and Day 21 |
| **T-03** | Character attachment | Recurring leads raise returning viewers and subscriptions over time | Lead (Kai/Mia, Tess, Owen; ensemble on Day 30) and callbacks (WS-009, WS-030) | Subscribe rate; returning viewers (if shown); comments naming characters | No drop in Stayed to watch on ensemble or callback episodes (they must stand alone) | Medians by lead; coded comments mentioning a cast member | Days 21 and 30 | Give the lead with the stronger subscribe rate and named-character comments one extra slot in the next month. Never drop a lead on one result |
| **T-04** | Script density | Slightly lower density (about −10% words, more held visuals) keeps more viewers in the middle | Words per second (default ≈2.85 at a 171 wpm read vs ≈2.55) | Retention at 50% of the duration | Confusion rate must not rise | Week 3: three episodes written lean, compared with matched-recipe episodes from weeks 1–2 at 7 days | Day 21 | Adopt lean density for that recipe if 50% retention is higher in **all three** pairs, or in 2 of 3 with no guardrail breach |
| **T-05** | Caption treatment | Shorter caption groups (3–4 words, close to the reference's measured 3.4) are easier to follow than up to 7 | Caption group length (casing stays sentence case; a later T-05b may test casing) | Retention in the first 15 s | Muted review score (QA P-02) and the reading-time rule must still pass | Days 15–21 (except the saga) at 3–4 words vs Days 8–14 at ≤7; same caption styling otherwise | Day 21 | Switch the default if the first-15 s retention median is higher and comment complaints about captions don't rise |
| **T-06** | Animation clarity | Sphere and diagram shots reduce confusion about invisible mechanisms | Mechanism visual present vs minimal (Violet Sphere WS-005; water Sphere WS-017; count-up timer WS-025; low-cost single set WS-019) | Confusion rate; retention around the mechanism shot | Production hours (from the *Schedule* sheet) | Compare confusion comments and the retention slope around the mechanism shot with episodes that have no Sphere | Days 14 and 30 | Keep a technique if confusion is lower and the retention slope is flat or better. Drop costly techniques that show no benefit |
| **T-07** | Sound + voice direction | An audio-led suspense episode (WS-022) and the planned "drop" hold attention | Sound-led design; drop placement | Retention through the drop (±3 s) vs the episode median slope | Comments on audio problems ("can't hear", "too loud") | Per-episode curve check at the drop moment | 7 days per episode; Day 30 pooled | If the curve consistently dips at drops, shorten them to ≤1.5 s or move them nearer the payoff |
| **T-08** | Payoff timing / Fork placement | An earlier Fork (≈33–45%) holds viewers better than a late one (WS-003 at 55%) | Fork position (% of duration) | Retention at the Fork moment and at 75% | The payoff must still land with ≥1.5 s before the Verdict (QA S-06) | WS-003 vs WS-001 and other R-A episodes at similar ages; **indicative only** (topics differ) | Days 7 and 14 | Keep the Fork at 33–45% unless late-Fork episodes match or beat that in at least 2 comparisons |
| **T-09** | CTA placement | No CTA, or one natural share line after the Verdict, does no harm to retention and lifts shares on P2 | CTA type: none (default), spoken share line (WS-002), forward line (WS-030) | Share rate (share line); subscribe rate (forward line) | Retention in the last 5 s; no comments complaining about "begging" | Compare P2 episodes with and without the share line at 7 days | Days 14 and 30 | Keep the share line on P2 if the share-rate median is higher and the last-5 s retention doesn't drop. Never make subscribing a condition for the ending |
| **T-10** | Duration + publication time | (a) Story-needed duration (48–72 s) has no fixed best length. (b) A posting time aligned with the audience's active hours helps early viewing choice | (a) Duration band; (b) posting time (12:00 ET baseline until Day 14) | (a) APV and AVD **together**; (b) engaged views at 24 h | (a) No cutting of payoff holds to chase APV; (b) consistency of the publishing rhythm | (a) Short (≤56 s) vs long (≥64 s) medians within the same recipe; (b) from Day 15, test one alternative time on 5 consecutive episodes, chosen from Studio's "When your viewers are on YouTube" card once it appears | Days 21 and 30 | (a) Prefer the duration band where AVD is higher **without** an APV collapse, per recipe. (b) Change the posting time only if the alternative's 24-h engaged-view median is higher on most of the 5 days **and** day-of-week mix is similar |
| **T-11** | Format: Both Endings | Showing both outcomes (WS-007, WS-014, WS-029) raises comments and replays | Format | Comment rate; retention through the "rewind" | Confusion rate | Three data points vs the same-pillar median | Day 30 | Keep it as a monthly format if 2 of 3 beat the median on comment rate with no confusion rise |
| **T-12** | Format: Two-part saga | A resolved Part 1 plus a forward line lifts Part 2 viewing without hurting Part 1 | Saga structure (WS-015/016) | Part 2 ÷ Part 1 engaged views at 7 days; Part 2 retention for cold viewers (first 10 s) | Part 1's own completion and its comments ("unfinished?" complaints) | Single comparison against the channel's 7-day median | Day 21 | One saga is too little evidence: run a second saga next month before adopting it. Stop if Part 1 draws "unfinished" complaints |

## 4. Comment coding (a self-selected sample)
At 72 h and 7 days, read and code up to 200 comments per video into:
- **enjoyed moment** (cite the timestamp)
- **confusion**
- **factual correction** (valid / invalid)
- **character attachment**
- **follow-up request**
- **decision debate** ("I'd pick left")
- **share intent** ("sending this to…")
- **other**

Log the counts in the *Tracking* sheet. Treat them as signals to investigate, never as a survey of the whole audience.

## 5. Review checkpoints (working intervals, not algorithm deadlines)

| Checkpoint | What to look at | Allowed actions |
|---|---|---|
| **24 h** (each video) | Stayed to watch %, early retention (first 3–5 s), comments for **errors** (a factual mistake, a broken caption, an audio fault) | Fix real errors only: pin a correction, update the description. **No other changes, no deletion, no reposting** |
| **72 h** (each video) | Retention curve shape, engaged views vs similar-age peers, comment coding | Note hypotheses; adjust **unproduced** scripts only if a problem is clearly diagnosed (e.g. confusion at a specific beat type) |
| **7 days** (each video) | All §1 metrics recorded in *Tracking*; comment coding | Feed the test comparisons in §3 |
| **Day 7 review** (calendar) | Provisional baselines; hook-pattern spread; **capacity vs the pilot** (20 §5); bank level | Confirm or adjust Days 15–21 (scripts are still open); re-plan capacity |
| **Day 14 review** | Pillar comparison (T-02); T-01, T-06, T-08 first reads; posting-time test set-up (T-10b) | Up to 2 reserve swaps for Days 22–30, each with a reason in the change log |
| **Day 21 review** | T-04, T-05, T-10a, T-12 (saga), T-03 first read | Adjust the default caption length / density; plan next month's formats |
| **Day 30 review** | Everything; pooled medians; all comment coding | Next month's calendar: what to keep, change and retire, with evidence for each |

## 6. Diagnosis guide

| Symptom | What it suggests | Check first | Likely fixes (for future episodes) |
|---|---|---|---|
| **Poor viewing choice** (low Stayed to watch vs baseline) | Frame 0 or the first second doesn't make a reason to watch | Is the protagonist + anomaly visible in frame 0? Is H1 ≤6 words and readable on a phone? Does the first word land ≤0.3 s? | A more concrete first-frame contradiction (HP01/HP02); a shorter H1; start mid-event |
| **Early abandonment** (a steep drop in the first 3–5 s after a good Stayed to watch) | The hook promise and the next beat disconnect, or the setup is slow | The first 5 s of the retention curve; the line right after the hook | Pay off a piece of the hook by 5 s; cut setup lines; move the clock or threat earlier |
| **Mid-video confusion** (a dip at a specific beat + confusion comments) | Missing cause and effect, unclear geography or rule | That beat in the shot list; floor plan; muted review | Add a Sphere/diagram or an L1 label; simplify to one action per shot; re-explain the rule in 5 words |
| **Unsatisfying ending** (a drop before the Verdict; "that's it?" comments) | The payoff isn't earned or lands too fast | Payoff hold ≥1.5 s; Verdict factor matches the story | Plant the fair clue earlier; hold the final image; make the Verdict factor specific |
| **Strong retention, limited reach** | Good content; weak viewing choice or a narrow topic | Stayed to watch %; topic breadth | Test hooks/frame 0 (T-01) and broader topics (T-02). **Don't** change the story structure that is retaining |
| **High views, weak subscriber conversion** | One-off curiosity without a reason to return | Does the ending show the format (Fork + Verdict) and the cast? Is the channel identity visible? | Strengthen the recurring benefit (14 Part 3): the cast, the "daily scenario" promise in the description, a forward line on strong episodes. No subscribe begging |
| **High engagement driven mainly by factual objections** | A claim is wrong, over-stated or ambiguous | Correction rate; the ledger row; the exact wording on screen | If valid: pin a correction, update the ledger (FALSE/QUALIFIED), fix the wording rule for future scripts, log it in the change log. **Never** seed controversy deliberately. If invalid: pin the source |

**Never:** panic-delete a slow video, repost the same video, or change several variables at once after a single result.

## 7. Using reserves to revise the calendar
- A slot may be swapped for a reserve (R01–R10, 16) when one of these applies:
  - a BLOCKING claim isn't verified by T-10
  - a QA hard stop can't be fixed in time
  - a sensitive real-world event makes the topic inappropriate
  - a scheduled review (Days 14 or 21) shows consistent evidence that favours a different pillar or format.
- Each swap gets a change-log line.
- Reserve pairings are in 16 and the brief field 29 of each episode.

## 8. Change log
Keep it in the workbook (*Change log* sheet) with: ID · date · what changed · why (evidence) · decided by · affected files and IDs.

Pre-launch entries from this planning session:

| ID | Date | Change | Why | Files |
|---|---|---|---|---|
| CL-001 | 2026-10-14 | All Fork-time captions moved to lane A (tag drawn above the crack) | Lane B overlapped the Fork chips (found while prototyping) | 09 §6, packages |
| CL-002 | 2026-10-14 | 13 Verdict factors shortened to ≤8 words | The V2 rule (≤8 words) was broken in the first calendar draft | calendar_data, briefs |
| CL-003 | 2026-10-14 | Day 1 script trimmed to 121 words; read rate set to 2.85 words/s | The first draft implied ≈250 wpm windows | WS-001 package |
| CL-004 | 2026-10-14 | WS-002 countdown made real time (T1 per-second events) | The first draft showed a time inconsistent with screen time (a false countdown) | WS-002 package |
| CL-005 | 2026-10-14 | WS-005 REAL RULE shortened from 16 to 14 words | The V3 limit is ≤14 words | calendar, WS-005 brief |
| CL-006 | 2026-10-14 | WS-026 title no longer says "Busiest Travel Day" | No ledger source; replaced by a plain calendar fact ("the Day Before Thanksgiving") | calendar, WS-026 brief |
| CL-007 | 2026-10-14 | SAFE added as a Verdict status; WS-010 "OK" changed to SAFE | Real Rule outcomes needed a truthful status that isn't "escaped" | 08 §8.3, 09 V1, calendar |
| CL-008 | 2026-10-14 | WR-04 extended: no climbing over waist-high barriers | WS-006's cart barrier needed the rule stated before use (rules never change to rescue a character) | 07 §3, WS-006 brief |
| CL-009 | 2026-10-14 | Ledger rows C-506 (CO first response) and C-1206 (second way out) added as BLOCKING | Scripts used these instructions without ledger rows | ledger, WS-005, WS-012 |
| CL-010 | 2026-10-14 | Fallback launch order re-flowed so seasonal episodes keep their dates | "Same order, 9 days later" would have mis-dated the Thanksgiving and Black Friday episodes | 17, 20 §2.4 |
| CL-011 | 2026-10-14 | WS-003 target duration revised from 62–66 s to 58–62 s; Verdict statuses normalised to the fixed set (CONTAINED/READY/OUT/FOUND mapped to SURVIVED/SAFE/ESCAPED) | The timed package reads 58.0 s; one status vocabulary keeps the Verdict ritual consistent | calendar, WS-003/015/020/021/023/025 briefs |
| CL-012 | 2026-10-14 | C-1205 re-worded to the evidence and re-classed QUALIFIED; C-1206 re-classed QUALIFIED; a verification-results pipeline and worksheet added | The USFA escape-planning excerpt already in appendix D2 §3c ("if the door is hot, keep it closed and use your second way out") meets the same evidence standard as other SUPPORTED rows; the "back of the hand" detail had no evidence and was removed | ledger, WS-012 brief, calendar, 07 Verification_Worksheet |
| CL-013 | 2026-10-14 | All 15 BLOCKING claims verified (9 SUPPORTED, 6 QUALIFIED) and platform facts P1–P7 checked on official pages; WS-002 shows the power window instead of a punch tool; WS-020 drops the transformer-hum claim and says "for hours"; WS-025 title drops "Only Rescue"; WS-028 says "toward where the crowd thins" instead of "diagonally"; six REAL RULE lines finalised; upload audio bitrate 384 kbps | Official and primary sources found once the search budget reset (verification_results.csv; 23 §2). Laminated side glass defeats punch tools (AAA/NHTSA ESV); the hum, "only rescue" and "diagonal" wordings had no source | ledger, calendar, 12 briefs, WS-002 package, 12, 20, 22, 23, 00, 01 |

## 9. Templates
- Per-video review: `13_Templates/Performance_Review_Template.md`.
- Workbook sheets: *Tracking* (metrics by checkpoint), *Change log*, *Schedule* (pilot hours), *Calendar*, *Claims* (`Worldosphere_Launch_Workbook.xlsx`).
