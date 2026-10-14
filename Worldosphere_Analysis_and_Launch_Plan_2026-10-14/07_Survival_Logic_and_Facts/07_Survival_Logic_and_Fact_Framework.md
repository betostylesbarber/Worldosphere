# 07 — Survival logic, world rules and fact-verification framework

Files in this folder:
- this framework, which includes the **Outbreak World Rules sheet** (§3)
- `claim_ledger.csv`, the master ledger (one row per claim, linked to episode IDs)
- `claim_ledger.md`, a readable copy of the ledger

## 1. Five kinds of statement, kept separate

| Class | Definition | On screen | Example |
|---|---|---|---|
| **FACT** | A real-world claim with an authoritative source in the ledger, verified before script lock | May appear as narration, a label or a REAL RULE. The source goes in the description | "In tests, cars floated about 15 seconds to a minute before water reached the side windows." |
| **QUALIFIED FACT** | True only under conditions, or varies | Must carry its qualifier in the wording | "About a foot of rushing water can float *most* cars." |
| **HYPOTHETICAL ASSUMPTION** | A premise we choose for a what-if (e.g. a week-long grid failure) | Framed as "if" or "in this scenario" | "In this scenario, the grid is down for a week." |
| **FICTIONAL RULE** | Outbreak-world mechanics (§3) | Shown as the world's behaviour, never as real advice. The description says "Fiction scenario" | "The Turned don't breathe." |
| **EXAGGERATION / COMEDY** | A deliberate joke | Must be unmistakable (visual gag, tone) | Mia's helmet fogging comically |

**Hard rule:** a fictional solution must never be framed as real-world safety advice. If a Real Rule episode uses fiction (characters, places), every *action that keeps them alive* must still be correct real-world guidance.

## 2. Verification process (per episode)

1. **Extract claims** from the brief: every number, safety action, timeline and causal statement, spoken *or* shown. That includes what the animation implies, such as a character surviving under an overpass.
2. **Look the claim up in the ledger.** Status must be SUPPORTED or QUALIFIED, from a source of the right kind:
   - government agencies (NWS/NOAA, USGS, FEMA/Ready.gov, CDC, CPSC, USDA FSIS, NPS, US Coast Guard)
   - recognised safety bodies (NFPA, UL FSRI, Red Cross)
   - peer-reviewed research
   - university extension services
   - manufacturer data, for product specifications only
3. **UNVERIFIED claims block script lock.** You may cut the claim, rewrite it as a hypothetical, or verify it and update the ledger with the URL, the exact quote and the access date.
4. **Write the qualifier into the line**, not only into the description.
5. **Visual check:** the storyboard must not imply a false cause, an impossible escape or a debunked action (a lightning crouch "saving" someone; a doorway "protecting" someone).
6. **Description:** list the sources, the access date, "Fiction scenario" where relevant, and a "not professional advice; follow local official guidance" line on Real Rule episodes.
7. **Post-publish:** monitor comments for factual corrections. A verified correction goes into the change log, with a pinned correction comment if it's material (21).

Ledger columns: `Claim ID | Claim | Class | Source (org, URL) | Assumptions | Necessary qualification | Script wording | Visual implication | Verification status | Episodes`.

### Research status at this cutoff (2026-10-14)
Direct page access was blocked and the shared search budget ran out. Verified claims come from **search-result extracts** of the cited agency pages, and their wording must be confirmed against the live page before publication. That confirmation is a QA item, not a reason to rewrite. Several Real Rule topics are therefore **scheduled later in the calendar**, giving time to verify; each has a reserve replacement if it fails (16).

## 3. Outbreak World Rules (fictional, fixed across all P1 episodes)

The rules are deliberately simple, physical and testable on screen, so the stories feel fair. **A rule never changes to rescue a character.** A new rule may be revealed only if it is consistent with all earlier ones, and it must be added here first.

| ID | Rule | Shown how | Used in |
|---|---|---|---|
| **WR-01 Transmission** | Bites transmit; scratches, blood contact and air do not. Fever within about 10 minutes. The person turns 30–90 minutes after the bite (it varies by person; state the window when it matters) | A bandage, sweat, shivers. Never the bite itself | WS-024, WS-026, WS-030 |
| **WR-02 No breath** | The Turned do not breathe: no breath fog in cold air, no chest movement, no fog on glass. They cannot drown; they sink and can walk on the bottom of shallow water | Breath puffs on living characters; their absence on the Turned | **WS-001**, WS-009, WS-016 |
| **WR-03 Senses** | Hearing first: they turn toward sudden or loud sounds. How far they react follows real acoustics (a loud engine carries hundreds of metres in quiet country; a whisper doesn't carry across a room). Motion second: they notice movement within about 30 m in good light. Sight in darkness is no better than a person's. No sense of smell beyond a person's | The **Amber Sphere** shows how far a sound carries | WS-003, WS-006, WS-013, WS-022 |
| **WR-04 Bodies** | Walk at about a normal human walking pace. Lurch to about 1.4× when they see a target. Cannot run, swim, climb ladders, or work handles, latches, locks or keys. **Can push** a door open with their weight; **cannot pull** a door open. Climb stairs slowly | Push/pull door logic is drawn with arrows | WS-001, WS-003, WS-011, WS-013, WS-019 |
| **WR-05 Endurance** | They never tire or sleep and do not heal. Worldosphere never shows combat or injuries to them; stories are about avoidance, barriers and escape | — | All |
| **WR-06 Cold** | Below about −20 °C (−4 °F) they slow sharply. Below about −30 °C (−22 °F) they stiffen and stop moving within an hour, and recover if warmed. No effect above freezing | Frost on their skin; slow-motion shamble | WS-015/016 |
| **WR-07 Herding** | They follow other Turned and moving crowds. A moving crowd pulls in more of them | Red dots streaming on maps | WS-003, WS-014, WS-026 |
| **WR-08 Timeline** | Day 1: dense places fall first. Phone networks overload within hours. Power becomes unreliable over **1–3 days** (not minutes) | Day/Time HUD | All P1 |
| **WR-09 No cure, no immunity** | Nobody is immune. There is no cure | — | All P1 |
| **WR-10 Humans** | Competent but fallible. Skills match the cast sheet (08 §4.2). No superhuman feats. Injuries have consequences | — | All |
| **WR-11 Anthology** | Each episode is a separate scenario unless marked SAGA. The rules are constant across scenarios | "SCENARIO 0NN" tag | All |
| **WR-12 Labelling** | Outbreak episodes are labelled "Fiction scenario" in the description. Real-world physics inside fiction must still be true (e.g. breath fog needs cold air) | — | All P1 |

### Consistency checks for every P1 script
- Does any escape rely on the Turned pulling a door, climbing a ladder or swimming? (Not allowed.)
- Does a sound draw them from farther away than real acoustics allow? (Check against C-012/C-013.)
- Does someone turn faster than WR-01 allows?
- Do threat positions stay consistent across cuts? (Use the floor-plan sheet in the storyboard template.)

## 4. Real-disaster standards (P2) and hypotheticals (P3)
- Fictional characters, real physics.
- **Show the wrong instinct, then why it fails, then the right action.** Never leave the wrong action as the last image.
- The REAL RULE line comes from the ledger word for word (shortened only if the source's meaning survives).
- No medical instructions beyond first-response agency guidance ("call emergency services", "move to fresh air").
- Grief and real tragedies: never depict identifiable real victims. Historical events (e.g. the 2013 Chelyabinsk airburst) are named factually, without dramatised deaths.
- P3 hypotheticals: state the assumption on screen ("In this scenario…"). Real mechanisms used inside them (food safety times, CO) must be ledger-verified.

## 5. Reference audit, applying the same standard
- REF02's "WATER 73 GAL ✓ … could survive here for weeks" fails (C-020). REF01's three-mile generator audibility is doubtful (C-021).
- Lesson for Worldosphere: **any number on a card is a factual claim**, even inside fiction.
