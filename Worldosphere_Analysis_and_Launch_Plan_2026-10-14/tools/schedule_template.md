# 20 — Production schedule, dependencies and buffer plan

> Generated from `tools/schedule_template.md` by `tools/gen_schedule_tables.py`. The tables come from `tools/calendar_data.py`, the claim ledger and `data/calendar_fallback_launch_2026-11-09.csv`. Edit the template or the data, not this file.

**Status of these numbers:**
- Every hour figure is an **estimate** (12 §9). Nobody has made a Worldosphere episode yet.
- Staffing, weekly hours and budget are **assumptions**, stated in §10, because the owner's capacity was not provided and could not be measured.
- The plan is built so the first three productions measure real capacity before the launch decision (§5).

---

## 1. Readiness assessment (as of Wed 14 Oct 2026)

| Item | Status today | Needed before Day 1 |
|---|---|---|
| Creative system, calendar, 30 briefs, Day 1–3 packages | Done (planning documents) | — |
| Style frames + Fork/breath motion proof | Done (prototype renders, 11) | Production-quality rebuild in the chosen tool |
| Character rigs, kits, HUD templates in the production tool | **None** | Rigs for 4 leads + guest + Turned; kits K1–K4, K9, K10 |
| Narrator voice | **Not chosen, not recorded** | A decision (own voice, contracted actor or licensed synthetic) + test recording |
| Music and SFX library | **None**. YouTube Help pages conflict on claimed music in Shorts over 60 s, so no claimable music (22 §3) | Motif, 3 beds, core SFX; rights logged (22) |
| Real-world claims | **Verified 2026-10-14:** no BLOCKING rows remain (46 SUPPORTED, 20 QUALIFIED; one in-story detail) | Reopen cited pages at QA F-03 before each script lock |
| YouTube channel | Not inspected (no access). YPP status unknown | Channel exists, branding set, nothing published |
| Production capacity | **Unknown, never measured** | Pilot hours from Days 1–3 (§5) |

**Conclusion.** Publishing on the provisional Day 1 (**Wed 14 Oct 2026**) is **not feasible**: nothing can be shown without rigs, voice, sound and QA. The earliest credible launch is **Sat 31 Oct 2026**, and only with two people (Scenario A). Otherwise it is **Mon 9 Nov 2026** with a lean scope (Scenario B).

---

## 2. Capacity, the conflict, and the recommended scope

### 2.1 Demand
- **Episodes:** 6 H × ≈22 h + 20 M × ≈14 h + 4 L × ≈9 h = **≈450 h** for 30 episodes, about 15 h per publishing day (12 §9).
- **Library:** ≈60 h before launch, plus ≈20 h for the later kits (K5–K8, station, subway, depot).

### 2.2 Scenarios

| | **A. Two people (recommended)** | **B. Solo, lean scope** | **C. Solo, full scope** |
|---|---|---|---|
| Staffing assumption | An animator plus a producer (research, script, voice, edit, sound, QA). About 50 h/week each ≈ 14.3 h/day combined | One person, about 50 h/week ≈ 7.1 h/day | One person, about 50 h/week |
| Scope | As briefed | **Lean**: 48–56 s; narration-led; diagram-first; at most 3 short lip-synced lines; crowds as silhouettes; Both Endings share one setup. ≈0.7 × the hours (≈10.5 h average) | As briefed (≈15 h average) |
| Launch | **Sat 31 Oct 2026** | **Mon 9 Nov 2026** (WS-001 moves to Oct 2027; fallback order in §2.4) | No earlier than about **Mon 30 Nov 2026**, with the calendar re-dated and seasonal episodes swapped |
| Pre-launch hours available | Oct 15–30: ≈229 h | Oct 15–Nov 8: ≈179 h | Oct 15–Nov 29: ≈330 h |
| Pre-launch hours needed | Library 60 + Days 1–5 ≈81 + start of Days 6–7 ≈20 + Days 6–10 scripts ≈12 = **≈173 h** (≈56 h contingency) | Lean library ≈45 + a 10-episode bank ≈105 = **≈150 h** (≈29 h contingency) | Library 60 + a 16-episode bank ≈240 = **≈300 h** |
| Bank at launch | 5 episodes (Days 1–5), with Days 6–7 in progress | ≈10 episodes | ≈16 episodes |
| During the 30-day run | Capacity ≈429 h vs need ≈389 h (Days 6–30 + later kits). About 10% slack | Capacity ≈214 h ≈ 20 lean episodes; the bank covers the rest | Capacity ≈214 h ≈ 14 episodes; the bank covers the rest |
| Verdict | **Workable but tight.** Holds only if the pilot hours (§5) come in at or under the estimates | **Workable only if** the pilot shows ≤10.5 h per lean episode. No slack for illness or rework | Workable, but it loses the Halloween and Thanksgiving placements |

**The conflict, stated plainly.** Thirty consecutive daily episodes at the quality standard in 08 §12 need about 15 focused hours per publishing day. One person cannot do that for 30 days. The options:
1. add a second person (A)
2. reduce the scope per episode and launch later with a bank (B)
3. keep the scope and launch much later (C)
4. keep the scope and publish 3–4 episodes per week instead of daily.

Lowering the QA bar is not one of the options.

**Recommendation.**
- Plan for **A** and run the pre-launch plan below.
- At the **Wed 28 Oct gate**, use the real pilot hours (§5) to confirm A, or switch to **B** (gate Wed 4 Nov) or **C**. The owner makes this decision.
- Nothing is published or scheduled by this plan.

### 2.3 Pre-launch plan, Scenario A (Thu 15 – Fri 30 Oct)

| Dates | Animator | Producer | Exit criterion |
|---|---|---|---|
| **Thu 15 – Sat 17 Oct** · Style lock + source-wording check | Model sheets for KAI, MIA, TESS, OWEN, the guest and the Turned (turnarounds, mouths, hands, brows); palette tokens in the tool | **Live-wording check (QA F-03)** of the Days 1–5 sources (claims already verified 2026-10-14). Safe-zone look in the Shorts editor (23 §2 P6). Voice decision + test read | Sheets approved; Days 1–5 source wording confirmed; voice chosen |
| **Sun 18 – Thu 22 Oct** · Library build | Rigs (Duik/RubberHose or Moho/Blender), walk/run/shamble cycles, FX-BREATH; Fork/Sphere/Verdict/T1 templates | Kits K1–K4 and K10 backgrounds (vector) with floor plans; the audio library (motif, 3 beds, Fork/Verdict SFX); **script lock Days 1–5** (Oct 18–20, re-timing the Day 1–3 packages after the claim sprint); animatics; **VO batch 1 (Days 1–5) Wed 21 – Fri 23 Oct** | Library v1 tagged; scripts and VO for Days 1–5 approved |
| **Fri 23 – Wed 28 Oct** · Produce Days 1–5 | Animation in this order: WS-001 (H), WS-002, WS-003 (H), WS-004, WS-005. Critical shots first | Edit, mix, caption re-timing and QA as each episode lands; claim checks for Days 6–10 (by Wed 21 Oct to T-10); scripts Days 6–7 (Oct 22–23); **K8 cabin kit** (Day 6) | **Gate (Wed 28 Oct):** Days 1–5 exported and QA-passed (including the playback section); Days 6–10 scripts locked; pilot hours logged |
| **Thu 29 – Fri 30 Oct** | WS-006 animation | WS-007 animatic; VO batch 2 (Days 6–10); upload packages Days 1–5 ready for the owner | Bank = 5; Days 6–7 in progress |
| **Sat 31 Oct** | — | — | **Launch, if the owner decides to publish** |

### 2.4 Scenario B: fallback launch Mon 9 Nov 2026 (re-flowed order)

Seasonal and structural pins:
- WS-026 stays on the day before Thanksgiving.
- WS-027 stays on Thanksgiving.
- WS-028 stays on Black Friday.
- WS-018 stays in Leonid week.
- The saga stays on a Saturday/Sunday pair.
- WS-030 stays the finale.

Other changes:
- WS-001 (Halloween) moves to October 2027.
- Reserve R04 fills the slot, with **Tess as lead** (her delivery-driver job suits a 2 a.m. fuel stop; the reserve note had Kai), so that no lead appears on two consecutive days.
- WS-002 keeps its story, but its "first evening after the clocks change" line becomes "the first week after".
- **Gate (Wed 4 Nov):** a bank of at least 8 episodes exported and QA-passed; Days 9–14 scripts locked.

{{FALLBACK}}

### 2.5 Scenario C
Keep the briefs and the order, and re-date the calendar so Day 1 is the first Monday after the bank reaches 16 episodes (about Mon 30 Nov 2026 at 50 h/week). Then:
- Move the Halloween (WS-001) and Thanksgiving (WS-026, WS-027, WS-028) episodes to their 2027 dates.
- Replace them with reserves R03, R04, R07 and R09 (P1), or with winter-relevant P2 topics after verification.
- Alternatively, keep the Oct 31 launch and publish 3–4 episodes per week until the bank allows daily posting.

---

## 3. Backward deadlines per episode (Scenario A)

Steady-state offsets from publication (T = publish day, 12:00 US Eastern):

| Stage (12 §5) | Deadline |
|---|---|
| Topic GO and research start | T-14 |
| Claims verified, or reserve swap decided | **T-10** |
| Script lock + timed read | T-8 |
| Animatic approved + VO recorded (batched) | T-7 |
| Episode-specific assets ready | T-6 |
| Animation done | T-4 |
| Edit, mix, caption re-timing | T-3 |
| QA (including playback), export, upload package → **banked** | T-3, end of day |

For Scenario B, apply the same offsets to the fallback dates in §2.4.

{{DEADLINES}}

---

## 4. Buffer rules (the bank)
1. **Bank target:** at least **3** finished, QA-passed episodes ahead of the publishing date at all times (QA CAL-04). Scenario A starts with 5.
2. **Bank = 2:** simplify the next M episode to a lean treatment (12 §6 simplifications), or swap it for a cheaper reserve (R04 single set; R03 bunker) and log it.
3. **Bank = 1:** pause all optional tests. Produce only lean episodes until the bank reaches 3.
4. **Bank = 0, or a QA hard stop:** **skip the day** rather than publish an unchecked episode, and log it. A missed day costs less than a wrong safety fact or a broken story. Never repost an old video to fill a gap.
5. Use at least one rest day per person per week. The capacity figures assume 50 h/week, not 7 × 10 h.

## 5. Pilot: measuring real capacity before committing
- Log hours per stage for WS-001, WS-002 and WS-003 in the workbook *Schedule* sheet (columns: stage, estimate, actual, notes).
- At the gate, compute the actual hours per tier: `actual H = (WS-001 + WS-003)/2`, `actual M = WS-002`. Multiply out across the calendar mix (§2.1).
- If actual > 1.15 × estimate, Scenario A has no slack left. Move to B or C, or add help (voice/sound/captions can be contracted out more easily than animation).
- Re-run this check at the Days 7 and 14 reviews (21 §5) with the larger sample.

## 6. Claim-verification deadlines

**Status 2026-10-14:** every BLOCKING claim was checked against official or primary sources (`07_Survival_Logic_and_Facts/verification_results.csv`, CL-013). What remains is the **live-page wording check** (QA F-03): reopen each cited URL by the episode's T-10 date in §3, because the research saw search excerpts. The table below lists any claim still not fully verified.

If a live page contradicts a claim, only three reserves are verified P2 substitutes (R01, R02, R08). If several P2 claims fail in the same week:
- use P1 reserves (R03, R04, R07, R09) and accept a temporary pillar imbalance
- note it in the change log.

Verification is mostly 20–40 minutes per claim with web access (find the agency page, quote it, record the URL and date). Do it in weekly batches (§8).

{{CLAIMS}}

## 7. Asset dependencies and build deadlines

| Asset | First use (Scenario A) | Build by (≥ T-8 of first use) | Reused in |
|---|---|---|---|
| Rigs (4 leads, guest, Turned), FX-BREATH, HUD | WS-001 · Sat 31 Oct | Thu 22 Oct (library v1) | All |
| K1 street, K2 vehicle/road/water, K3 store/dock, K4 interiors, K10 crowd | WS-001 to WS-005 | Thu 22 Oct | Throughout |
| K8 plane cabin (modular row) | WS-006 · Thu 5 Nov | Wed 28 Oct | WS-026 (terminal + plane) |
| K6 wilderness (open plains first) | WS-008 · Sat 7 Nov | Fri 30 Oct | WS-014, WS-015/016, WS-021, WS-023, WS-025 |
| K7 coast (harbour/boat) | WS-009 · Sun 8 Nov | Sat 31 Oct | WS-017 |
| K5 tower (stairwell/corridor/office/apartment) | WS-011 · Tue 10 Nov | Mon 2 Nov | WS-014, WS-018 |
| Theater interior (simple tiers) | WS-013 · Thu 12 Nov | Wed 4 Nov | — |
| Station Zero interior + snow/ice | WS-015 · Sat 14 Nov | Fri 6 Nov | WS-016, WS-025, WS-029/030 snow |
| Elevator interior | WS-019 · Wed 18 Nov | Tue 10 Nov | — |
| K8 subway car/tunnel | WS-022 · Sat 21 Nov | Fri 13 Nov | — |
| Depot + bus | WS-030 · Sun 29 Nov | Sat 21 Nov | December winter content |

## 8. Batching plan (weekly rhythm in steady state, Scenario A)

| Day | Producer | Animator |
|---|---|---|
| Mon | Claim-verification batch for the episodes publishing in 10–16 days; topic GO decisions | Animation (episode T-4) |
| Tue | Scripts + timed reads for 2–3 episodes | Animation |
| Wed | Animatics; **VO batch** (3–5 episodes in one session for a consistent voice) | Next kit pieces (§7) |
| Thu | Edit + mix + caption re-timing | Animation |
| Fri | QA playback reviews; upload packages | Animation |
| Sat | Performance reviews (21: 24 h, 72 h and 7-day checkpoints); change log | Animation / fixes |
| Sun | Rest (rotating) | Rest (rotating) |

Batch compatible work, but never the storytelling. Each episode still gets its own hook test, its own fair clue and its own payoff check.

## 9. The most expensive steps, and how to simplify them without weakening the episode
| Episode | Expensive element | Simplification that keeps the viewer experience |
|---|---|---|
| WS-001 | Costume crowd + breath on every figure | Breath only on figures in the light pools; background crowd as silhouettes with cycle offsets |
| WS-003 | Town-scale crowd and cars | Map view with dots (WR-07) carries the scale; only the dock scenes need full animation |
| WS-006 | Plane cabin with passengers | A modular row instanced ×10; passengers as guest-rig variations; the aisle camera stays locked |
| WS-007 / WS-014 / WS-029 | Both Endings = two stories | A shared setup (first 40%) and a mirrored second branch reusing camera setups |
| WS-015 / WS-016 | A new station kit | Build once and reuse it fully for Part 2 and the later snow episodes |
| WS-022 | A dark subway tunnel | Darkness + sound design (the episode's test) means less to draw: torch pools, silhouettes |
| WS-030 | Ensemble of four leads + depot | Lines spread across scenes so no shot animates more than two leads in close-up |

General rules (12 §6):
- threat off-screen via sound plus a reaction
- diagrams in place of complex action
- held drawings plus camera moves
- narration-led scripts
- kit reuse.

## 10. Staffing, tool, time and budget assumptions
- **Staffing:** Scenario A assumes two people with 2D animation, editing and audio skills, about 50 h/week each. Scenario B assumes one such person. Neither has been confirmed.
- **Tools:** the primary or the free fallback toolchain (12 §1). The free fallback has zero licence cost. Paid options are listed with prices as seen on 2026-10-14 and must be checked. **Nothing has been purchased.**
- **Time:** the estimates are for a fluent operator with the library built. First-week productions usually take longer than steady state, which is why the pilot exists.
- **Budget:** unknown. The plan does not depend on paid tools, paid voice or paid music. Original audio and the free libraries (22) are enough.
- **Publishing:** the owner publishes manually. This plan schedules nothing.
