# Script template (copy as `WS-0NN_script_v01.md`)

Worked examples: the script sections of the Day 1–3 packages (`19_Production_Packages_Days_1-3/*/WS-00N_Production_Package.md` §3). For the machine-readable version used by the timing engine, copy `tools/package_ws001.py` and edit its `SHOTS` list.

```
# WS-0NN — <Title> — script v01
Recipe: R-_ · Pillar: P_ · Target: __–__ s · Word budget: ___ (Production_Recipes.md)
Lead: ____ · Fork position target: __% · Verdict: <STATUS> — <factor ≤8 words>
Claims used (ledger IDs + status): C-___ (SUPPORTED) …   World rules used: WR-__ …

## Rules box (12 §5.3)
- Geography / exits / screen direction:
- Threat position and entry side:
- Time of day, weather, light source:
- The fair clue the viewer can see before the answer (and the shot where it is planted):
- What the Turned can / cannot do here (WR-04):

## Hook (frame 0)
- Frame 0 image:
- H1 (≤6 words, one Amber keyword):
- Opening line (first word ≤0.3 s):

## Script
| Shot | Speaker | Line (use " | " to force a caption break; mark the one emphasised word as *word* or *word!* for threat) | On-screen text event | Purpose (reveal / change / stakes / character) |
|---|---|---|---|---|
| 01 | NARR | | H1 … · G1 SCENARIO 0NN | Hook |
| 02 | | | | |
| … | | | | |
| FORK | — | (no line during the 1.0–1.6 s hold) | F1 chips: LEFT / RIGHT | Decision |
| … | | | | |
| END | — | (Verdict is not voiced) | V1/V2(/V3) | Resolution |

## Checks before lock
- [ ] Every line has a purpose (QA S-03); no line describes what the picture already shows
- [ ] Character lines ≤7 words; Verdict factor ≤8 words; REAL RULE ≤14 words in ledger wording
- [ ] Claims match ledger "Script wording"; no UNVERIFIED-BLOCKING claim (QA F-01/F-02)
- [ ] Timed read within ±3 s of target (engine or stopwatch); emphasis ≥3 s apart
- [ ] The title, H1 and opening line promise only what the ending delivers (QA S-05)
```
