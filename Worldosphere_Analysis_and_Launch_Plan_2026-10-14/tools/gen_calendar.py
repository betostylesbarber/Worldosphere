import sys, csv, datetime as dt
D=sys.argv[1]; sys.path.insert(0, D+"/tools"); from calendar_data import C, RESERVES
X = { # per-idea: fresh angle | strongest visual | why share | trend dependence
"WS-001":("The tell is breath fog, a physical rule viewers can check themselves","An infected hand on cold glass leaves no fog","'How would you tell?' and the rewatch hunt for the non-breathers","Halloween-dependent (fallback: move to reserve for next October)"),
"WS-002":("Shows why the door fails (pressure), not just 'use the window'","Headlights sinking away under black water","Share-to-protect: practical and memorable","Evergreen"),
"WS-003":("Attacks the most popular answer to 'where would you go'","Every headlight in town converging on one glowing store","Debate: 'my plan was the superstore'","Evergreen"),
"WS-004":("Myth correction with a visible consequence (the door swings)","The table 'walking' across the floor while Kai holds on","Share-to-correct a common belief","Evergreen; quake news spikes help"),
"WS-005":("The danger is invisible and comes from the helpful act (heat)","The violet Sphere seeping through a warm house","Share-to-protect before winter storms","Seasonal (winter)"),
"WS-006":("A barrier from cart physics instead of a fight","A wall of braked carts in a narrow aisle","'What would you do in seat 33C?'","Evergreen; holiday travel bump"),
"WS-007":("Shows both outcomes instead of arguing","The frame physically splitting into roof and basement","Viewers argue which they'd choose","Evergreen"),
"WS-008":("The 'shelter' everyone sees is the trap","Wind Sphere funnelling under the bridge","Share-to-correct","Seasonal (spring peak; Nov secondary [BK])"),
"WS-009":("Rule twist: no breath means the sea is a floor","Heads ringing the empty anchor spot at low tide","'I never thought of the tide'","Evergreen"),
"WS-010":("Ordered failure, not a list","The house cross-section going dark room by room","Useful checklist","Evergreen; storm season"),
"WS-011":("The stairwell door does the defending","Roof glowing with noise while floor 14 stays dark","Up-vs-down debate","Evergreen"),
"WS-012":("Side-by-side proof of a closed door","Two rooms, one ablaze, one intact","Share-to-protect","Heating season"),
"WS-013":("The loudest room in town hides the screams","Screaming face on screen, real panic in the seats","Irony + clever exit","Evergreen"),
"WS-014":("Tests early-leaving vs fortifying with both outcomes","Calendar flip; highways jamming in a split","Debate: city vs country","Evergreen"),
"WS-015":("The last clean place on Earth gets its first case","Plane on an ice runway at dusk","Cliff of a two-parter (measured test)","Evergreen"),
"WS-016":("The cold as the barrier","Frost spreading over a motionless Turned","Saga completion","Evergreen"),
"WS-017":("Instinct vs physics in one image","Overhead: swimmer stuck in a narrow channel","Share-to-protect","Summer peak; evergreen"),
"WS-018":("A real event's lesson most people never heard","Flash, delay, windows blowing inward","'I didn't know that' fact","Leonid-week curiosity (must not link showers to danger)"),
"WS-019":("The trap becomes the refuge","Feet in the door gap above the stuck car","Relatable fear + reversal","Evergreen"),
"WS-020":("Lineman's view of a spectacle","Green aurora over a town of filming phones","Big what-if","Space-weather news dependent"),
"WS-021":("Direction matters: back toward the ice that held you","Arms on ice, kicking, the roll away","Share-to-protect before ice season","Seasonal"),
"WS-022":("Darkness and a door type decide it","Faces at the latched door glass in emergency light","'Would you walk the tunnel?'","Evergreen"),
"WS-023":("Time cost of packing","Orange sky, half-packed truck","Share-to-protect","Season/news dependent"),
"WS-024":("A child notices what adults miss","Five faces in candlelight, one shivering","Guess-the-culprit comments","Evergreen"),
"WS-025":("The rescuers are your friends, not the ski patrol","Count-up clock over a snow field","Share-to-protect (ski season)","Seasonal"),
"WS-026":("Moving against a crowd","Crowd Sphere flowing to jammed doors","Holiday-travel relevance","Thanksgiving Eve"),
"WS-027":("The instinct (water) is the danger","Water-meets-oil flare preview","Share-to-protect on the day","Thanksgiving Day"),
"WS-028":("Pressure, not people","Red pressure Sphere in a crowd","Share-to-protect","Black Friday"),
"WS-029":("Both endings of the classic stranded choice","Plough lights finding the car","Debate + protect","Seasonal (winter)"),
"WS-030":("The cast unites; callbacks reward regulars","Gate arm dropping behind the bus at 11:58","Series payoff; forward to December","Month-end bridge"),
}
wd=lambda d: dt.date.fromisoformat(d).strftime("%a")
hdr=["Day","Date","Weekday","Topic and angle","Recommended title","Content pillar","Chosen hook","Main payoff","Target duration","Reason for placement","Production complexity","Main test","Brief ID"]
rows=[[c["day"],c["date"],wd(c["date"]),c["topic"],c["title"],c["pillar"],c["hook"],c["payoff"],c["dur"],c["placement"],c["complexity"],c["test"],c["id"]+"-BRIEF"] for c in C]
with open(D+"/data/calendar_30_days.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(hdr+["Lead","Recipe","Verdict","Kits","Claims","Reserve replacement"]); 
    for c,r in zip(C,rows): w.writerow(r+[c["lead"],c["recipe"],c["verdict"],c["kits"],c["claims"],c["reserve"]])
md=["# 17 — 30-day posting calendar (Worldosphere, YouTube Shorts)","",
"**Launch decision.** The provisional Day 1 was the execution date, **Wed 14 Oct 2026**. It is **not feasible**: no rigs, kits, voice, music library or finished episodes exist yet, and capacity has never been tested (20 §1). **Recommended Day 1: Saturday 31 October 2026 (Halloween)**, subject to a go/no-go gate on **Wed 28 Oct**: Days 1–5 exported and QA-passed, and Days 6–10 scripts locked. **If the gate fails, launch on Monday 9 November 2026** with the re-flowed order in `20_Production_Schedule_and_Buffer.md` §2.4: the seasonal episodes keep their dates (WS-026 to WS-028 around Thanksgiving), WS-001 (Halloween-specific) moves to October 2027, Day 1 becomes WS-003 (evergreen), and reserve R04 fills the free slot. Full readiness assessment: `20_Production_Schedule_and_Buffer.md`.",
"","**Timezone and posting time.** Dates are calendar dates. Publish daily at **12:00 US Eastern**. That is 16:00 UTC on 31 Oct, and 17:00 UTC from 1 Nov after US daylight saving time ends at 02:00 on 1 Nov. **This is an operational starting assumption to test, not a known best time.** YouTube publishes no best hour (appendix B §11, unverified). We had no audience data. Keep the time fixed for weeks 1–2 so it doesn't confound the content tests. Then use YouTube Analytics' 'When your viewers are on YouTube' card, once it appears, to test one alternative time (21, test T-10). Schedule uploads in YouTube Studio only when you decide to publish. Nothing has been scheduled.",
"","**Why Day 1 comes first.** It shows the entire promise in about 60 s: an ordinary place; a fresh, checkable rule (breath fog); a visible decision (the Fork); a clean resolution (the Verdict); and two of the four recurring characters. It does this on the day the premise is most relevant. Halloween is also a Saturday this year.",
"","**Sequence logic.**",
"- **Days 1–3:** fiction → real → fiction. Three different leads, settings and times of day, so new viewers immediately see the range: zombies, real disasters, the cast.",
"- **Week 1:** only high-clarity concepts with verified facts (Days 2, 4, 5). Heavy kits (Days 1, 3, 6) are built before launch.",
"- **Weeks 2–3:** introduce the formats to measure: hour-by-hour (Day 10), Both Endings on P3 (Day 14), and the saga test on the weekend pair (Days 15–16). Low-cost episodes (Days 19 and 24) protect capacity.",
"- **Week 4:** seasonal moments: Thanksgiving Eve travel (Day 26), Thanksgiving Day (Day 27), Black Friday (Day 28), winter (Days 29–30).",
"- Real Rule slots whose facts are still **UNVERIFIED** (Days 18, 20, 23, 25, 27, 28, 29) are placed **late on purpose**, so each has 2–4 weeks to be verified, with a named verified reserve ready.",
"- **Day 30** unites the cast and bridges into December ('The Long Winter'). It stays satisfying on its own.",
"- **Adjacency rules applied:** no lead appears on consecutive days (except the saga pair). No two water episodes are adjacent. No two Both Endings episodes are within 6 days. No primary location repeats on consecutive days. Days 29–30 deliberately share a winter-night road palette as the bridge into December (flagged, not accidental).",
"- **Claims to avoid:** we make **no** claim that this order 'trains the algorithm'. Ordering is for viewer experience and production risk only.",
"","## Calendar","",
"| "+" | ".join(hdr)+" |","|"+"---|"*len(hdr)]
for r in rows: md.append("| "+" | ".join(str(x).replace("|","/") for x in r)+" |")
from collections import Counter
pc=Counter(c["pillar"].split(" ")[0] for c in C); lc=Counter(c["lead"].split(" ")[0].replace(",","") for c in C)
md+=["",f"**Mix check:** P1 Outbreak {pc['P1']} · P2 Real Rule {pc['P2']} · P3 World Shift {pc['P3']}. Leads: "+", ".join(f"{k} {v}" for k,v in lc.items())+". Both Endings: Days 7, 14, 29. Saga: Days 15–16.",
"","Machine-readable copy: `data/calendar_30_days.csv`, which also includes the lead, recipe, Verdict, kits, claims and reserve for each day. The workbook `Worldosphere_Launch_Workbook.xlsx` has the same data in editable sheets."]
open(D+"/17_30_Day_Posting_Calendar.md","w").write("\n".join(md))
# ---- 16 selection
m=["# 16 — Selected 30 videos and 10 reserves","",
"Selection method:",
"1. Score all 94 premises with the rubric in 15.",
"2. Remove rejected premises (copies of the reference, sensitive subjects, unverifiable or off-brand ideas).",
"3. Fill slots for seasonality and sequence (17).",
"4. Balance pillars, leads, settings and production cost.",
"5. Keep 10 reserves. At least 4 reserves are **fact-verified P2s**, so any Real Rule slot that fails verification can be swapped in without delay.",
"","Each row answers the brief's questions: why someone cares immediately (hook and topic), what's fresh, the strongest visual, the decision, the payoff, fit, the share motive, trend dependence and feasibility.","",
"| ID | Date | Why care immediately | Fresh angle | Strongest visual | Central decision (Fork) | Payoff | Fit (pillar) | Why share / replay / subscribe | Trend dependence | Feasibility (complexity) |","|---|---|---|---|---|---|---|---|---|---|---|"]
import re
for c in C:
    fork=re.search(r"FORK: ([^.]*)\.",c["spine"]); fork=fork.group(1) if fork else "—"
    a,v,s,t=X[c["id"]]
    m.append("| "+" | ".join(x.replace("|","/") for x in [c["id"],c["date"],c["hook"],a,v,fork,c["payoff"],c["pillar"],s,t,c["complexity"]])+" |")
m+=["","## Reserves (ready to swap in; see change log rules in 21)","","| ID | Premise | Pillar | Working title | Claim status | Replaces | Story spine |","|---|---|---|---|---|---|---|"]
for r in RESERVES: m.append("| "+" | ".join(str(x).replace("|","/") for x in [r["id"],r["topic"],r["pillar"],r["title"],r["claims"],r["replaces"],r["spine"]])+" |")
m+=["","## Rejected or deferred (with reasons)","","Full list with scores: `15_Topic_Research_Pool.md` (decision = REJ/DEF). Main patterns:",
"- **Too close to the reference:** farm outbreaks (T001), the barking-dog dilemma (T050), the stranger-at-the-door trust dilemma (T082), the rural silo (T092).",
"- **Derivative of well-known films, TV or games:** hospital wake-up (T005), prison (T009), quarantine checkpoint (T035), spore outbreak (T044), theme park (T026).",
"- **Brand-safety or sensitivity:** school lockdown (T004), infants in peril (T094).",
"- **Hoax or health-misinformation risk:** outbreak science (T043), permafrost virus (T045).",
"- **Unverified facts:** deferred until verified (tsunami T054, nuclear alert T062, bear T069, volcano T060, lost hiker T066 and others).",
"- **Not a story:** polls and grids (T008, T084).",
"- **Seasonal mismatch:** deferred to the right month (gym T036 for January, heat wave T059 for June, Thanksgiving dinner outbreak T017 for 2027).",
"- **Strong evidence but needs a careful format:** real historical incidents minute by minute (T076, retrieved evidence: Zack D. Films' top videos). Recommended as a month-2 test with a sensitivity checklist."]
open(D+"/16_Selected_30_and_10_Reserves.md","w").write("\n".join(m))
print(pc, lc)
