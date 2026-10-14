# D1 Claim Ledger: Natural-Hazard Survival Facts

> **Update 2026-10-14 (later the same day):** many items marked UNVERIFIED or NOT VERIFIED below were later checked with official-domain searches. See `../../07_Survival_Logic_and_Facts/verification_results.csv` and `../../23_Limitations_and_Next_Actions.md` §2. This appendix is kept as the original research record.

Access date for every source below: **2026-10-14**.

## How this was checked, and what's missing

- **How sources were read.** Direct page fetches failed this session. WebFetch could not resolve any host, and direct HTTPS was refused by the egress proxy under organization policy (weather.gov, ready.gov, usgs.gov, nasa.gov, noaa.gov, pubmed and avalanche.org were all refused). Every quote below comes from the page extracts the web-search tool returned for the cited URL.
  - Text in "quotes" is wording the search tool returned as the page's own words.
  - Text marked *(paraphrase)* is the search tool's summary, not the page's wording.
  - Before anything goes on screen as a direct quote, open the live URL and confirm the wording.
- **Topics left unchecked.** The shared web-search budget ran out (200 searches per turn, shared across agents) partway through. These topics are therefore **UNVERIFIED**:
  - TSUNAMI, WILDFIRE, HURRICANE, BLIZZARD/WINTER STORM, HEAT, AVALANCHE, VOLCANO, SPACE WEATHER and ASTEROID.
  - The primary abstract for one sinking-car paper.
  - For these I list the claim as you supplied it, the source to check, and the qualifications to look for. No numbers were added.
- **How to finish.** Send a follow-up message, or raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`, to complete the unverified sections.

Verdict key:
- **SUPPORTED:** an authoritative source states it.
- **QUALIFIED:** true, but the wording, a number or the framing needs adjusting.
- **FALSE:** an authoritative source contradicts it.
- **UNVERIFIED:** could not be confirmed this session.

---

## 1. EARTHQUAKE

| Claim | Verdict | Exact quote | Source (org, URL) | Access date | Script-safe wording | Visual implication |
|---|---|---|---|---|---|---|
| Drop, Cover, and Hold On is the recommended action | SUPPORTED | "federal, state, and local emergency management experts and other official preparedness organizations all agree that 'Drop, Cover, and Hold On' is the appropriate action" (Earthquake Country Alliance handout hosted by Alaska DHS&EM). USGS separately advises getting "under a sturdy piece of furniture like a strong desk or table" *(paraphrase)* | State of Alaska DHS&EM, https://ready.alaska.gov/Documents/Earthquake%20Safety%20Handout_4%20pages.pdf ; USGS, https://www.usgs.gov/faqs/what-should-i-do-during-earthquake | 2026-10-14 | "Drop to your hands and knees. Cover your head and neck, under a sturdy table if you can. Hold on until the shaking stops." | Character drops to hands and knees, crawls under a table, holds a table leg with one hand and shields the head and neck with the other arm. If there's no table, crouch against an interior wall with arms over the head. |
| Doorways are not safer in modern homes | SUPPORTED | USGS: "in modern homes doorways are no stronger than any other parts of the house and usually have doors that will swing and can injure you." FEMA: "a doorway does not provide protection from falling or flying objects and you likely will not be able to remain standing." | USGS, https://www.usgs.gov/programs/earthquake-hazards/earthquake-facts-earthquake-fantasy ; FEMA P-530, https://www.fema.gov/sites/default/files/2020-08/fema_earthquakes_fema-p-530-earthquake-safety-at-home-march-2020.pdf | 2026-10-14 | "In a modern house, a doorway is no stronger than any other wall, and the door can swing shut on you." | Show the doorway as a myth: the door swings and hits the character, or a myth-vs-fact split screen. The myth comes from old California adobe houses where only the door frames were left standing (USGS), which works as an optional flashback. |
| Running outside during shaking is dangerous (falling debris) | QUALIFIED | USGS *(paraphrase)*: don't "run downstairs or rush outside while the building is shaking or while there is danger of falling and hurting yourself or being hit by falling glass or debris." USGS HVO *(paraphrase)*: running outside risks that "you could easily lose your balance and fall." | USGS, https://www.usgs.gov/faqs/what-should-i-do-during-earthquake ; USGS HVO, https://www.usgs.gov/observatories/hvo/news/volcano-watch-practice-key-protecting-yourself-during-earthquake | 2026-10-14 | "Don't run outside while the ground is shaking. Falling glass and debris near exits injure people. Once the shaking stops, if the building is damaged, get out and move away from it." | Glass and facade pieces falling near the exits. **Qualification:** Ready.gov says that *after* shaking, if you're in a damaged building, go outside and move quickly away. If you're already outdoors, stay in the open, away from buildings, power lines and chimneys. |
| Aftershocks follow | SUPPORTED | FEMA *(paraphrase)*: aftershocks "can occur in the first hours, days, weeks, or even months after the quake." USGS *(paraphrase)*: aftershocks generally taper off over time, and "it is best just to be prepared and aware that they may happen." Ready.gov *(paraphrase)*: be ready to Drop, Cover and Hold On if you feel an aftershock. | FEMA, https://www.fema.gov/sites/default/files/2020-07/fema_earthquakes_what-to-do-before-during-and-after-an-earthquake-fact-sheet.pdf ; USGS, https://www.usgs.gov/faqs/foreshocks-aftershocks-whats-difference ; Ready.gov, https://www.ready.gov/earthquakes | 2026-10-14 | "Aftershocks can hit for hours, days, even months. They're usually smaller, but they can bring down buildings the first quake weakened. Each time, drop, cover and hold on again." | A second, smaller shake while characters are leaving a cracked building. Repeat the drop, cover and hold on pose. |

---

## 2. TORNADO

| Claim | Verdict | Exact quote | Source (org, URL) | Access date | Script-safe wording | Visual implication |
|---|---|---|---|---|---|---|
| Highway overpasses are dangerous shelters | SUPPORTED | NWS Birmingham: "Do not take shelter under a highway overpass, where wind speeds can increase due to a tunneling effect." NWS Mobile: an overpass "does not provide adequate shelter during a tornado and can cause increased wind speeds due to a tunneling effect." A NOAA report on the May 3, 1999 outbreak *(paraphrase)* says the event confirmed that overpasses do not provide good shelter. | NWS BMX, https://www.weather.gov/bmx/sps_torsafetyrules ; NWS MOB, https://www.weather.gov/mob/Severe_Tornado ; NOAA, https://www.nssl.noaa.gov/about/history/may3rd/noaareport.pdf | 2026-10-14 | "Never hide under a highway overpass. It can funnel the wind and the flying debris right at you." | Don't show an overpass as a refuge. If a driver is caught out, show the options NWS offices describe: drive out of the storm's path if possible, or get down in a ditch or culvert, lower than the road, and cover the head (NWS MOB/MKX *(paraphrase)*). |
| Best shelter is a basement, or an interior room on the lowest floor | SUPPORTED | NWS–Red Cross Joint Statement: "the best options are to go to an underground shelter, basement or safe room." Without one, a "small windowless interior room or hallway on the lowest level of a sturdy building." Ready.gov *(paraphrase)*: "small, interior, windowless room or basement on the lowest level of a sturdy building." | NWS/American Red Cross, https://www.weather.gov/media/safety/NWS-ARC-Revised-Joint-Statement-on-Tornado-Safety_062209.pdf ; Ready.gov, https://www.ready.gov/tornadoes | 2026-10-14 | "Get underground: a basement, storm cellar or safe room. If you can't, go to a small interior room with no windows on the lowest floor, and put as many walls between you and the outside as you can." | Family in an interior bathroom or closet, crouched low with arms over their heads, maybe a mattress or helmets. No windows in the shot. NWS Mobile advises "as many walls between yourself and the outside as possible." |
| Mobile homes are unsafe | SUPPORTED | NWS Springfield: "Mobile homes provide absolutely no protection from tornadoes!" Ready.gov *(paraphrase)*: a mobile home is not a safe shelter, so seek a substantial building. | NWS SGF, https://www.weather.gov/media/sgf/TornadoSafetyTipSheet.pdf ; Ready.gov, https://www.ready.gov/tornadoes | 2026-10-14 | "A mobile home offers almost no protection. Leave early for a sturdy building or shelter you picked out ahead of time." | Characters leave the trailer for a neighbor's basement or a community shelter *before* the tornado arrives. NWS advises picking that building in advance. |
| "A tornado sounds like a freight train" (anecdotal) | QUALIFIED. It's more than anecdote: officials list it as a warning sign. | Ready.gov *(paraphrase)* lists "a loud roar like a freight train" as a sign. SPC FAQ *(paraphrase)*: the most common sound is "a continuous rumble, like a nearby train," but tornadoes can also sound like a waterfall or rushing air. NSSL *(paraphrase)*: survivors describe "a jet engine or freight train." | Ready.gov, https://www.ready.gov/tornadoes ; NOAA SPC, https://www.spc.noaa.gov/faq/tornado/ ; NOAA NSSL, https://www.nssl.noaa.gov/education/svrwx101/tornadoes/faq/ | 2026-10-14 | "Many survivors describe a roar like a freight train. Don't wait to hear it, though. By then you should already be in shelter." | Rising rumble on the soundtrack. **Qualification:** NWS Boston notes strong downbursts can sound the same, and the sound varies, so the roar alone shouldn't be what triggers sheltering. |
| Watch vs. warning | SUPPORTED | NWS: "A Tornado WATCH means Be Prepared. A Tornado WARNING means Take Action!" NWS *(paraphrase)*: a warning is issued when a tornado is happening or about to happen: "Immediately seek shelter in your safe place!" | NWS WRN, https://www.weather.gov/wrn/tornado-sm ; NOAA, https://www.noaa.gov/stories/tornadoes-101 | 2026-10-14 | "A watch means conditions could produce tornadoes, so get ready. A warning means a tornado is happening or about to, so take shelter now." | Phone alert graphic: WATCH in yellow (plan) vs WARNING in red (act). The Storm Prediction Center issues watches over large areas; local NWS offices issue warnings. NOAA cites an average warning lead time of about 13 minutes. Treat that as approximate, since the figure may be dated. |

---

## 3. FLASH FLOOD

| Claim | Verdict | Exact quote | Source (org, URL) | Access date | Script-safe wording | Visual implication |
|---|---|---|---|---|---|---|
| "Turn Around Don't Drown" | SUPPORTED | It's NWS's registered campaign name ("Turn Around Don't Drown®"). The NWS states "it is NEVER safe to drive or walk into flood waters." | NWS, https://www.weather.gov/safety/flood-turn-around-dont-drown | 2026-10-14 | "Turn around, don't drown. Never drive or walk into floodwater." | Car stops at a flooded dip and reverses. A road-sign graphic works. |
| 6 inches of moving water can knock an adult down | SUPPORTED | "A mere 6 inches of fast-moving flood water can knock over an adult." | NWS, https://www.weather.gov/safety/flood-turn-around-dont-drown | 2026-10-14 | "Just six inches of fast-moving water can knock an adult off their feet." | Ankle-to-shin-deep current sweeps a hiker's feet out. |
| 12 inches can carry away a small car | QUALIFIED. The NWS headline page says "most cars." | "It takes just 12 inches of rushing water to carry away most cars." Other NWS materials say "12 inches of rushing water to carry away a small car." NWS Tulsa *(paraphrase)*: a foot of water will float many vehicles. | NWS, https://www.weather.gov/safety/flood-turn-around-dont-drown ; NWS TSA, https://www.weather.gov/tsa/hydro_tadd | 2026-10-14 | "About a foot of rushing water can float and carry away most cars." | Water at hubcap or bumper height lifts the car until it drifts. |
| 2 feet of rushing water can carry away most vehicles, including SUVs and trucks | SUPPORTED | "2 feet of rushing water can carry away SUVs and trucks." Some NWS office materials say "18-24 inches of fast-moving water can carry away most large SUVs, vans and trucks." | NWS, https://www.weather.gov/safety/flood-turn-around-dont-drown | 2026-10-14 | "Two feet of rushing water can sweep away SUVs and pickup trucks." | Pickup truck pushed sideways off a low-water crossing. |
| Flooding is a leading cause of weather deaths, many of them in vehicles | QUALIFIED. Heat ranks higher. | NWS, citing CDC: "over half of all flood-related drownings occur when a vehicle is driven into hazardous flood water. The next highest percentage of flood-related deaths is due to walking into or near flood waters." NWS social kit: "More than 50% of all flood fatalities are vehicle-related." A NOAA/NWS page *(paraphrase)* says flooding causes more deaths than any weather hazard **except heat**, with a 30-year average of 88 flood deaths a year (page attribution from the search extract; confirm before use). A 1996–2014 study of 1,075 flash-flood deaths, summarized by NSSL, found >60% vehicle-related. | NWS, https://www.weather.gov/safety/flood-turn-around-dont-drown ; NWS WRN, https://www.weather.gov/wrn/flood-sm ; NOAA JetStream, https://www.noaa.gov/jetstream/thunderstorms/flood ; NOAA NSSL, https://inside.nssl.noaa.gov/nsslnews/2016/08/significant-paper-a-situation-based-analysis-of-flash-flood-fatalities-in-the-united-states/ | 2026-10-14 | "Floods are among the deadliest weather hazards in the U.S. Over the long term only heat kills more, and more than half of flood deaths happen in vehicles." | Don't call floods "the #1 killer." Over 30 years heat ranks higher (see the NWS hazard statistics, https://www.weather.gov/media/hazstat/80years.pdf). An older NOAA JetStream line says "nearly half." Use "more than half," the CDC figure via NWS. |

---

## 4. LIGHTNING

| Claim | Verdict | Exact quote | Source (org, URL) | Access date | Script-safe wording | Visual implication |
|---|---|---|---|---|---|---|
| "When thunder roars, go indoors" | SUPPORTED | It's the NWS slogan, used as a page title: "When Thunder Roars, Go Indoors!" CDC uses the same title. | NWS JKL, https://www.weather.gov/jkl/lightningsafety ; CDC, https://blogs.cdc.gov/yourhealthyourenvironment/2016/06/30/when-thunder-roars-go-indoors-2/ | 2026-10-14 | "When thunder roars, go indoors." | First rumble → characters head inside right away. |
| No place outside is safe | SUPPORTED (the wording is a paraphrase) | NWS *(paraphrase)*: outdoor locations offer no protection, and if you hear thunder you are likely within striking distance. Only substantial buildings and hard-topped vehicles count as safe; "rain shelters, small sheds, and open vehicles" do not. Lightning "can sometimes strike 10 miles or more" from a storm. | NWS, https://www.weather.gov/safety/lightning-safety-overview ; https://www.weather.gov/safety/lightning-safety | 2026-10-14 | "There's no safe place outdoors in a thunderstorm. If you can hear thunder, you're close enough to be struck." | A picnic pavilion, tent or golf shelter is **not** safe. Show a lightning strike from a storm that still looks distant. |
| Wait 30 minutes after the last thunder | SUPPORTED | "Immediately move to safe shelter: a substantial building with electricity or plumbing or an enclosed, metal-topped vehicle with windows up. Stay in safe shelter at least 30 minutes after the last sound of thunder." | NOAA JetStream, https://www.noaa.gov/jetstream/lightning/lightning-safety | 2026-10-14 | "Stay inside until 30 minutes after the last thunder." | On-screen timer resetting at each new rumble. |
| The lightning crouch is a last resort and isn't protective | QUALIFIED / partly FALSE. "Not protective" is right. The "last resort" framing is what NWS dropped. | NWS: "The National Weather Service (NWS) stopped recommending the crouch in 2008." NWS *(paraphrase)*: the crouch "simply doesn't provide a significant level of protection," and presenting it even as a last resort can suggest some action prevents a strike. NOAA FAQ: the crouch "will not significantly lower your risk of being killed or injured from a nearby lightning strike." | NWS, https://www.weather.gov/safety/lightning-crouch ; NOAA JetStream FAQ, https://www.noaa.gov/jetstream/lightning/frequently-asked-questions | 2026-10-14 | "Crouching won't save you. The only real protection is getting inside a building or a hard-topped car." If caught out: get off peaks and ridges, away from isolated trees and water, never lie flat, and keep moving toward shelter. | Don't show the crouch as the hero's solution. NOAA says lying flat is worse because ground current can spread "up to 100 feet." Some older NWS office pages still show the crouch; they are outdated. |
| Cars with metal roofs are relatively safe because of the metal shell, not the rubber tires | SUPPORTED | NWS: "rubber-soled shoes and rubber tires provide NO protection from lightning." NWS: "the steel frame of a hard-topped vehicle provides increased protection if you are not touching metal." NWS Melbourne: "The vehicle's metal shell conducts the lightning around and away from you." | NWS, https://www.weather.gov/safety/lightning-myths ; NWS MLB, https://www.weather.gov/mlb/lightning_safety | 2026-10-14 | "A hard-topped car protects you because of its metal shell, not the rubber tires. Keep the windows up and your hands off the metal." | Current flows around the car body. Convertibles, motorcycles, bikes and fiberglass-shell vehicles give **no** protection (NWS offices). |

---

## 5. RIP CURRENTS

| Claim | Verdict | Exact quote | Source (org, URL) | Access date | Script-safe wording | Visual implication |
|---|---|---|---|---|---|---|
| Swim parallel to shore, or float | SUPPORTED | NWS Mount Holly: "If caught in a rip current, relax and float and do not swim against the current. If able, swim parallel to the shoreline. If unable to escape, face the shore and call or wave for help." NOAA NOS *(paraphrase)*: swim parallel because "most rip currents are less than 80 feet wide." | NWS PHI, https://forecast.weather.gov/product.php?site=NWS&issuedby=PHI&product=CFW ; NOAA NOS, https://oceanservice.noaa.gov/education/tutorial_currents/03coastal3.html | 2026-10-14 | "Don't panic, and don't fight it. Float to save energy, swim parallel to the beach until you're out of the pull, then angle back to shore. If you can't, face the shore and wave for help." | Overhead shot: the swimmer moves sideways out of a narrow channel, then curves back in. NWS Wilmington's treadmill analogy: "step to the side of it." |
| Don't swim against it | SUPPORTED | Same quote as above ("do not swim against the current"). NWS *(paraphrase)*: swimming straight against it only drains your energy. | NWS, https://www.weather.gov/news/242205-rip-current-safety | 2026-10-14 | "Swimming straight back to shore against the current wears out even strong swimmers." | A tired swimmer making no progress toward shore. |
| US rip current deaths per year (approx.) | QUALIFIED. It's an estimate, and the counts vary. | NOAA Ocean Today *(paraphrase)*: "it is estimated that 100 people are killed by rip currents annually." NWS Wilmington, citing USLA: about 100 drownings a year, and rip currents account for "over 80%" of lifeguard rescues. The NWS 2024 hazard summary counted 74 rip current deaths that year. | NOAA, https://oceantoday.noaa.gov/ripcurrent/ ; NWS ILM, https://www.weather.gov/ilm/ripcurrents ; NWS, https://www.weather.gov/media/hazstat/sum24.pdf | 2026-10-14 | "Rip currents are estimated to kill about 100 people a year in the U.S." | Rescuers shouldn't go in without a flotation device; call 911 or a lifeguard. **Not verified this session:** the visual cues for spotting a rip (gaps in breaking waves, discolored or churning water). Check NOAA before animating one. |

---

## 6. COLD WATER

| Claim | Verdict | Exact quote | Source (org, URL) | Access date | Script-safe wording | Visual implication |
|---|---|---|---|---|---|---|
| Cold water shock | SUPPORTED | Peer-reviewed *(paraphrase)*: sudden skin cooling triggers tachycardia, vasoconstriction, hypertension, an inspiratory gasp and hyperventilation, raising the risk of inhaling water. It peaks in the first minute. NWS *(paraphrase)*: cold shock can cause panic and loss of muscle control, which makes self-rescue very hard. | NIH/PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC5904285/ ; NIH/PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC13512758/ ; NWS, https://www.weather.gov/safety/coldwater | 2026-10-14 | "The first killer in cold water isn't hypothermia. It's the gasp. Sudden cold makes you gasp and breathe fast, and if your face is underwater, you breathe in water." | Character gasps and hyperventilates on entry. Show them deliberately slowing their breathing and keeping the face up. A life jacket helps. |
| 1-10-1: 1 minute to control breathing, 10 minutes of meaningful movement, 1 hour before hypothermia causes unconsciousness | QUALIFIED. It's a teaching rule of thumb. | NPS Point Reyes *(paraphrase)*: about one minute to regain control of breathing, about ten minutes of meaningful movement, about one hour before hypothermia causes unconsciousness; a flotation device can extend survival. The origin is Gordon Giesbrecht, a University of Manitoba thermophysiology professor (McGill Office for Science and Society *(paraphrase)*). Giesbrecht *(paraphrase)*: it "actually takes at least half an hour for hypothermia to develop." | NPS, https://www.nps.gov/pore/planyourvisit/yoursafety_hypothermia.htm ; McGill OSS, https://www.mcgill.ca/oss/article/medical-did-you-know/professor-popsicles-physiological-proof | 2026-10-14 | "Experts teach '1-10-1': about a minute to get your breathing under control, about ten minutes of useful movement to get yourself out, and up to roughly an hour before the cold knocks you unconscious. These are rough guides, not guarantees." | **Qualifications:** times vary with water temperature, clothing, life jacket, body size and waves. A peer-reviewed study (PMC, cold-induced stress) says cold shock commonly lasts **up to about 3 minutes**. A USCG survival-course outline gives looser times: coordination loss within about 15 minutes, hypothermia beginning within 30–60 minutes (https://www.dco.uscg.mil/Portals/9/DCO%20Documents/5p/CG-5PC/CG-CVC/CVC3/cfsac/meetings/2016/Finalchapter2.pdf). The "1 hour" is to unconsciousness, not death, and it assumes the head stays above water. |
| Falling through ice: turn back the way you came, kick, roll away | SUPPORTED (state natural-resource agency sources) | Minnesota DNR: "Turn toward the direction you came. That's probably the strongest ice." *(paraphrase)* "Kick your feet and dig in your ice picks to work your way back onto the solid ice." Wisconsin DNR *(paraphrase)*: lie flat until you're completely out, then roll away from the hole. Michigan DNR *(paraphrase)*: crawl, don't stand, until you're clear of the weak spot. | MN DNR, https://www.dnr.state.mn.us/safety/ice/survival.html ; WI DNR, https://dnr.wisconsin.gov/Education/OutdoorSkills/IceSafety ; MI DNR, https://www.michigan.gov/dnr/education/safety-info/ice | 2026-10-14 | "Turn back toward the way you came, where the ice held you. Get your arms onto the ice, kick your legs like you're swimming, and slide yourself out. Then roll away from the hole and don't stand up until you're on solid ice." | Keep winter clothing on; trapped air adds flotation (MN DNR *(paraphrase)*). Ice picks worn on the chest. Afterwards, get to warmth and medical care. |

---

## 7. SINKING CAR

| Claim | Verdict | Exact quote | Source (org, URL) | Access date | Script-safe wording | Visual implication |
|---|---|---|---|---|---|---|
| Escape sequence: Seatbelts off, Windows open, Children out, Out (SWOC) | QUALIFIED. It's an expert protocol, and the step order may have been revised. | University of Manitoba (Giesbrecht faculty page) *(paraphrase)*: "Seatbelts off, Windows open or broken, Out immediately, Children first (oldest to youngest)." A protocol described in JEMS *(paraphrase)*: unfasten seatbelts, open windows, release children and hold them near an adult, then exit with children first, oldest to youngest. CBS (2024) *(paraphrase)*: Giesbrecht "has now reversed the order" of unbuckling and opening the window. Neither the new order nor the reason could be confirmed. | U. Manitoba, https://www.umanitoba.ca/kinesiology-recreation-management/faculty-staff/gordon-giesbrecht ; JEMS (trade journal, secondary), https://www.jems.com/patient-care/a-tried-and-true-approach-to-escaping-from-sinking-vehicles-and-the-guy-behind-the-testing/ ; CBS (news, secondary), https://www.cbsnews.com/sanfrancisco/news/expert-explains-how-to-escape-from-a-submerged-car-with-children | 2026-10-14 | "Don't waste time calling for help. Act in the first minute: get the seatbelt off and the side window open (or broken), unbuckle the kids, and push them out the window, oldest first, then follow." | Show the side window opening early, while the car is still floating. **Confirm whether "window first" is now the recommended order before locking the scene.** The 2013 review advises against calling for help during the escape window. |
| Why opening the door is hard | SUPPORTED | Giesbrecht & McDonald 2010 field tests *(paraphrase)*: in one exit attempt started during the sinking phase, "it was impossible to open the doors or windows until the vehicle was completely full of water." U. Manitoba *(paraphrase)*: water pressure "will press the window against the door frame, making it impossible to open." | Aviat Space Environ Med 2010 (PubMed), https://pubmed.ncbi.nlm.nih.gov/20681239/ ; U. Manitoba (as above) | 2026-10-14 | "Once water is pressing on the outside of the car, it pins the doors shut. Usually they won't open until the car is almost full of water, and by then it's too late. Go out the window." | A character shoves the door and it won't budge, while water rises outside the glass. |
| A car floats roughly 30–120 s, depending on the vehicle | QUALIFIED. The tested floating window was shorter. | Peer-reviewed: "Vehicles floated for 15 s (H) to 63 s (I) before the water reached the bottom of the side windows." Escape is easiest "during the initial Floating Phase." U. Manitoba *(paraphrase)*: a vehicle "may float on the water surface for up to 3 minutes, but you only have 1 minute to exit the vehicle safely." A 2011 heavy-truck study *(paraphrase)*: "a heavy vehicle will sink before surface exit is possible." | Aviat Space Environ Med 2010 (PubMed), https://pubmed.ncbi.nlm.nih.gov/20681239/ ; PubMed, https://pubmed.ncbi.nlm.nih.gov/21235107/ ; U. Manitoba (as above) | 2026-10-14 | "In tests, cars stayed afloat only about 15 seconds to a minute before water reached the side windows. That's your escape window: about one minute." | A countdown overlay of about 60 s. The car tips nose-down because the engine is heavy, the front sinks first, and water climbs the side glass. Don't show a slow two-minute float. |
| Window-breaking tools | QUALIFIED | McDonald & Giesbrecht 2013 review *(paraphrase)*: side windows are hard to break without a center punch or rescue hammer, so mount one within the driver's reach. Giesbrecht via CBS *(paraphrase)*: don't try the windshield, because the front sinks first. | Aviat Space Environ Med 2013 review, PDF hosted by Kids and Cars, https://www.kidsandcars.org/document_center/download/vehicle-submersion/studies/Vehicle-Submersion-A-Review-of-the-Problem-Associated-Risks-and-Survival-Information-1.pdf | 2026-10-14 | "Keep a window-breaking tool where the driver can reach it, and aim for a side window, not the windshield." | Spring-loaded punch or rescue hammer on the keychain or console, hitting the corner of a side window. **UNVERIFIED this session:** whether laminated side glass on some newer vehicles defeats these tools. Check NHTSA or the manufacturer before scripting a window-smash scene. |
| Source quality | NOTE | A pilot study *(paraphrase)* says vehicle submersions have "one of the highest fatality rates of any type of single motor-vehicle accident, accounting for up to 10% of all drownings in high-income countries." | NIH/PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC6545703 | 2026-10-14 | — | The timing data come from small peer-reviewed field tests (a few vehicles, calm water, trained subjects). SWOC is guidance from one researcher, not a federal agency standard; no NHTSA or USCG page was verified this session. The PubMed 20681239 abstract was read through search extracts only, so confirm the 15–63 s wording. |

---

## 8. TSUNAMI: UNVERIFIED (search budget exhausted, direct fetch blocked)

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Natural warning signs: strong or long shaking, ocean receding, loud roar | UNVERIFIED | — | NWS/NOAA, https://www.weather.gov/safety/tsunami ; https://www.tsunami.gov | not accessed | "If you feel a strong or long earthquake near the coast, see the sea pull back, or hear a roar from the ocean, don't wait for an official warning. Move." | Confirm each sign is on the NOAA list, and that NOAA says a natural warning means leaving right away without waiting for an official one. |
| Go to high ground or inland | UNVERIFIED | — | as above; Ready.gov, https://www.ready.gov/tsunamis | not accessed | "Get to high ground or as far inland as you can." | Confirm wording and any distance or height guidance. Don't add numbers until confirmed. |
| Multiple waves; the first may not be the largest | UNVERIFIED | — | NOAA/NWS tsunami pages; USGS | not accessed | "A tsunami is a series of waves. The first is often not the biggest, so stay away until officials say it's safe." | Confirm, along with any NOAA statement on how long the danger lasts. |
| Vertical evacuation | UNVERIFIED | — | FEMA P-646 (vertical evacuation structures); NOAA | not accessed | "If you can't get to high ground in time, go to an upper floor of a tall, sturdy concrete building." | Confirm that FEMA/NOAA frame this as a last resort when there's no time to reach high ground. |

## 9. WILDFIRE: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Ready, Set, Go! | UNVERIFIED | — | Ready.gov, https://www.ready.gov/wildfires ; IAFC's Ready, Set, Go! program; CAL FIRE | not accessed | "Ready: prepare your home and plan. Set: pack and stay alert. Go: leave early." | Confirm who owns the program and the exact definitions of the three stages. |
| Evacuate early | UNVERIFIED | — | Ready.gov; CAL FIRE | not accessed | "Leave as soon as you're told to, or sooner if you feel unsafe." | — |
| If trapped in a car | UNVERIFIED | — | CAL FIRE "Ready for Wildfire"; NWCG | not accessed | Hold until verified. | Confirm the agency's exact steps (where to park, windows and vents, getting low, calling 911) before scripting. |
| Embers can travel far | UNVERIFIED (no distance given) | — | NFPA Firewise; USFS; CAL FIRE | not accessed | "Wind can carry burning embers far ahead of the fire and start new fires." | **Don't script a specific distance until it's verified.** |

## 10. HURRICANE: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Storm surge is the deadliest part | UNVERIFIED | — | NOAA NHC, https://www.nhc.noaa.gov/surge/ | not accessed | "Storm surge, the ocean pushed ashore, is often the most dangerous part of a hurricane." | Confirm NHC's current wording, which may be "greatest threat to life," and any statistic on deaths by cause. |
| The eye is a false calm | UNVERIFIED | — | NWS/NHC hurricane safety pages | not accessed | "If it suddenly goes calm, you may be in the eye. The other side of the storm is coming, so stay put." | Confirm. |
| Atlantic season runs June 1–Nov 30 | UNVERIFIED (high-confidence prior knowledge, not confirmed this session) | — | NOAA NHC | not accessed | "The Atlantic hurricane season officially runs from June 1 to November 30." | Confirm, and add the caveat that storms can form outside the season. |

## 11. BLIZZARD / WINTER STORM: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Stay in the vehicle if stranded | UNVERIFIED | — | NWS, https://www.weather.gov/safety/winter ; CDC winter weather; Ready.gov | not accessed | "If you're stranded, stay with your car. It's shelter, and rescuers can spot it more easily." | Confirm. |
| Clear the exhaust pipe to prevent carbon monoxide | UNVERIFIED | — | NWS; CDC | not accessed | "Keep snow cleared from the tailpipe, and crack a window when the engine runs." | Confirm. |
| Run the engine about 10 minutes per hour | UNVERIFIED | — | NWS; CDC | not accessed | Hold the number until verified. | Confirm the exact interval. |
| Hypothermia and frostbite signs | UNVERIFIED | — | CDC, winter weather / hypothermia pages | not accessed | Hold until verified. | Pull CDC's sign lists verbatim. |

## 12. HEAT: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Heat stroke signs; it's a medical emergency | UNVERIFIED | — | CDC, heat-related illness page (cdc.gov/extreme-heat) | not accessed | "Heat stroke is a medical emergency. Call 911." | Pull CDC's list of signs verbatim. |
| Vecellio et al. 2022: wet-bulb limit lower than 35 °C | UNVERIFIED | — | Vecellio DJ et al., J Appl Physiol 2022 (PSU HEAT project) | not accessed | Hold the numbers. Possible wording: "Lab studies suggest the humid-heat limit for young, healthy people is lower than the long-assumed 35 °C wet-bulb." | **Qualifications to confirm:** young, healthy volunteers; a controlled lab study with light activity; the endpoint was the point where core temperature stopped stabilizing, not death; limits differ in hot-dry vs warm-humid air; and the limits are likely lower for older or sick people. |

## 13. AVALANCHE: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Survival falls sharply after about 15–18 min buried (Brugger/Haegeli) | UNVERIFIED | — | Haegeli P et al., CMAJ 2011 (Canada vs Switzerland survival curves); Brugger H et al. | not accessed | "For a buried victim, survival drops quickly after the first few minutes. Speed is everything." | **Check whether the time to the steep drop differs between the Canadian and Swiss datasets** before using "15" or "18" minutes. |
| Beacon, probe and shovel; companion rescue | UNVERIFIED | — | avalanche.org (National Avalanche Center) | not accessed | "Everyone carries a beacon, probe and shovel, and knows how to use them. Your partners are the rescue team." | Confirm that avalanche.org says companion rescue beats waiting for organized rescue. |

## 14. VOLCANO: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Ash hazards | UNVERIFIED | — | USGS Volcano Hazards Program (volcanoes.usgs.gov, ash pages) | not accessed | Hold until verified. | Confirm the health, roof-load, machinery and aviation hazards. |
| Pyroclastic flow speed | UNVERIFIED | — | USGS VHP, pyroclastic flows page | not accessed | "Pyroclastic flows move far faster than anyone can run." | **Don't use a number until it's verified.** |
| Yellowstone supereruption annual probability about 1 in 730,000; USGS calls it very unlikely | UNVERIFIED | — | USGS Yellowstone Volcano Observatory FAQ | not accessed | Hold the number. | Confirm the figure and whether USGS defines it as a large caldera-forming eruption. |

## 15. SPACE WEATHER: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Carrington Event, 1859 | UNVERIFIED | — | NOAA SWPC; NASA | not accessed | Hold until verified. | Confirm the dates and the telegraph effects. |
| 1989 Quebec blackout | UNVERIFIED | — | NOAA SWPC; NASA | not accessed | Hold until verified. | Confirm the date, how long the outage lasted and how many people lost power. |
| May 2024 G5 storm | UNVERIFIED | — | NOAA SWPC | not accessed | Hold until verified. | Confirm the date and whether it was the first G5 in about 20 years. |
| What a severe storm could realistically do to the grid | UNVERIFIED | — | NOAA SWPC, G-scale page (swpc.noaa.gov/noaa-scales-explanation) | not accessed | Hold until verified. | Use SWPC's G5 description verbatim. Avoid "the grid goes down for months" unless an authoritative source says so. |
| Leonid meteor shower 2026 peak date | UNVERIFIED | — | American Meteor Society / IMO 2026 calendar; NASA | not accessed | Hold. **Don't guess a date.** | — |

## 16. ASTEROID: UNVERIFIED

| Claim | Verdict | Exact quote | Source to check | Access date | Script-safe wording (pending) | Visual implication / what to confirm |
|---|---|---|---|---|---|---|
| Apophis close approach April 13, 2029; NASA says no impact risk for at least 100 years | UNVERIFIED (consistent with prior knowledge, not confirmed this session) | — | NASA/JPL CNEOS; NASA Apophis news (2021) | not accessed | Hold until verified. | Confirm the date, the miss distance, and the exact NASA wording on ruling out impact risk. |

---

### Searches to run next (priority order)
1. NHC storm surge "greatest threat to life", plus the season dates.
2. NOAA/NWS tsunami natural warnings and "first wave".
3. NWS/CDC: stranded in a vehicle in winter, exhaust, minutes per hour of running the engine.
4. CDC heat stroke signs, and the Vecellio 2022 J Appl Physiol abstract.
5. CMAJ 2011 Haegeli/Brugger avalanche survival curve.
6. USGS YVO probability and pyroclastic flow speed.
7. NOAA SWPC G5 description, the May 2024 storm and the 1989 event.
8. NASA Apophis 2029.
9. Leonids 2026 peak (AMS/IMO).
10. CAL FIRE / Ready.gov: trapped in a car during a wildfire, and ember distance.
11. PubMed 20681239 abstract wording.
12. Giesbrecht's current SWOC order.
13. NHTSA guidance on laminated side glass.
