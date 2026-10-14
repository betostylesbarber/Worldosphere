# C. Topic demand, comparable creators and premise pool for Worldosphere

- Prepared for: Worldosphere, an original 2D-animated narrative survival Shorts channel
- Research and access date for every source below: **2026-10-14**
- Tools that worked: **WebSearch only**. Each search returned link titles, URLs and a machine-written summary of the result pages.
- Tools that did not work:
  - **WebFetch** failed DNS resolution for every host, including the neutral control hosts `example.com` and `en.wikipedia.org`.
  - **curl** was refused (CONNECT 403, egress policy) for youtube.com, socialblade.com, reddit.com and wikipedia.org.
  - The **WebSearch budget** (200 calls per turn, shared with the other research agents) ran out after 22 of my queries.
- **As a result, no YouTube, TikTok, Instagram, Reddit, Social Blade or Google Trends page was opened.** Every number below comes from a search-result summary of a third-party page. The page itself was not seen. Treat every number as a lead to check, not as a measurement.

## Read this first: evidence labels used throughout

| Label | Meaning | How far to trust it |
|---|---|---|
| **[R-Sxx]** | Retrieved this session. It appeared in a WebSearch result summary, and `Sxx` points to the source list (section E). | Moderate. The summary was machine-written from the page snippet, so wording and numbers can be compressed or wrong. Every page needs a click-through before publication. |
| **[BK]** | Background knowledge from the model's training data (to about mid-2026). **It was not verified in this session.** | Low to moderate. Use it as a hypothesis or a pointer, not a citation. No view counts or statistics are given under this label. |
| **[J]** | Creative or strategic judgment only. | None as evidence. It is opinion. |

Following the brief, each section keeps three things apart: **(1) evidence of audience interest**, **(2) evidence about execution** (what format or packaging seems to work), and **(3) judgment**.

---

## A. Comparable creators and channels

### A.1 How to read this table

- "Subs" figures are what a third-party tracker page showed, as quoted in a search-result summary. Snapshot dates are given where the summary stated one.
- **No per-video view count could be read from YouTube itself.** Where a view number appears, it comes from a tracker page (vidIQ, youtubers.me, SpeakRJ) or a non-YouTube page (TED.com), as summarized by the search tool.
- **"Vs typical" method.** No tracker page listing a channel's recent uploads could be opened, so medians could not be computed. Where both total views and total uploads were available, I used the **lifetime mean views per upload** (total views ÷ total uploads). This is a weak proxy: viral outliers skew the mean upward, and Shorts and long-form are mixed together. Where even that was not possible, the cell says so.

### A.2 Creators with retrieved data

| # | Creator / platform | URL | Approx. size (source) | Typical format | Example videos (title, views as shown, where seen) | Vs typical (method, limits) |
|---|---|---|---|---|---|---|
| 1 | **Zack D. Films**. YouTube (Shorts only); Snapchat reposts exist under similar handles | https://www.youtube.com/@zackdfilms (not opened) | 27.7M subs, 72.2B views, 3,633 videos, "as of July 17, 2026" [R-S1]. 27.6M [R-S2]. About 28.7M subs, about 78.03B views, 4,025 videos, latest upload Oct 4, 2026 [R-S3]. About 28.9M (HypeAuditor, Oct 2026) [R-S4] | 3D-animated sub-60s explainers: real-world incidents, "what happens if", body facts, life hacks. OutlierKit says **Shorts are 100% of channel views** [R-S2] | 1) "Ohio's 1986 Balloon Disaster": **18.45M** (vidIQ "top videos" per search summary) [R-S3]<br>2) "The Pepsi Contest That Killed 5 People": **12.4M** (vidIQ, same) [R-S3]<br>3) "How To Make A Candle From An Orange 😮": **22,171,086** (youtubers.me table dated April 2026, per search summary) [R-S5]<br>4) "The Trick To Winning Tic Tac Toe 😮": **23,231,305** (same table) [R-S5]<br>5) Two unnamed July 2026 uploads (one plane-related, one about a catfish): about **16.7M** and about **16.9M** (SpeakRJ, titles not given) [R-S6] | Lifetime mean per upload is about **19.4M** (78.03B ÷ 4,025, vidIQ) or about **19.9M** (72.2B ÷ 3,633, SpeakRJ). Against the vidIQ mean: Balloon is about 0.95×, Candle about 1.14×, Tic Tac Toe about 1.20×. **Limits:** this is a mean, not a median. The snapshots are from different dates (April vs October 2026). The vidIQ "top videos" list ranks Balloon (18.45M) as top, which conflicts with youtubers.me's 22–23M figures, so the trackers measure differently. HypeAuditor's "about 6.43M views gained on Oct 8" [R-S4] is far below the lifetime average of about 43M/day (78.03B over 5 years), which suggests either a slowdown or a tracker artifact. Treat all of this as unverified. |
| 2 | **The Infographics Show**. YouTube (long-form plus Shorts) | https://www.youtube.com/@TheInfographicsShow (not opened) | About 15.5M subs, 6.84B views. Gained about 100K subs and about 29.51M views in the last 30 days. Channel started Feb 26, 2011 (vidIQ, 2026 snapshot) [R-S9]. 16M subs, 6.9B views, 6.3K videos (Social Blade, undated) [R-S8]. 15.5M (CreatorDB, refreshed Sep 24, 2026) [R-S10] | Flat-vector 2D animation with a narrator. Uses second-person "Could you survive…" and "YOU vs…" scenarios, plus military and true-story episodes. CreatorDB lists an **engagement rate of 1.8% against a category median of 1.5%** [R-S10] | 1) "Could You Survive A Zombie Attack?", aired **Oct 1, 2018**, 5 min. **Views not retrieved** [R-S11]<br>2) "YOU vs 1000 ZOMBIES - How To Defeat and Survive a Zombie Horde", aired **Jan 28, 2020**. **Views not retrieved** [R-S12]<br>3) Channel's most-viewed video (topic: what happens after death): "over 21 million", from an older promotional page [R-S13] | OutlierKit gives an **average of about 1.1M views per video** [R-S7]. That matches 6.9B ÷ 6.3K ≈ 1.09M. The zombie episodes cannot be compared because their view counts were not retrievable. |
| 3 | **TED-Ed**. YouTube and ed.ted.com (animated lessons and riddles) | https://ed.ted.com/lessons/can-you-solve-the-bridge-riddle-alex-gendler | Channel subs **not retrieved** | 4–5 min animated logic puzzles with a pause-and-solve beat. This is a **decision-under-time-pressure** format | 1) "Can you solve the bridge riddle? - Alex Gendler". You and friends must cross a bridge before zombies arrive. **24,088,563 views** (ed.ted.com counter, per search summary) [R-S15]. **24,359,925 plays** (TED.com page) [R-S16]. **21.4M** (Glasp mirror) [R-S17]<br>2) "Can you solve the virus riddle?" (not zombie, but outbreak-themed). Views not retrieved [R-S19]<br>3) "Can you solve the secret werewolf riddle?". Views not retrieved [R-S18 result set] | **Not computed.** No channel totals were retrieved. One educator roundup says it chose riddles "as measured by number of views and audience interaction" [R-S18], which is consistent with the bridge riddle being a standout. Note this is long-form, not Shorts. |
| 4 | **What If** (Underknown). YouTube, Snapchat, Facebook, Instagram, TikTok | https://underknown.com/news/thunderbird-entertainment-to-take-what-if-to-television/ | "Over 35 million subscribers across Snapchat, YouTube, Facebook, Instagram and TikTok", "monthly average of nearly 450 million views" (Underknown, 2021) [R-S20]. "250 million times a month", "more than six billion views in nine languages" (Business Wire, Oct 2020) [R-S21]. Spanish channel "Qué pasaría si - What If Español": 3.15M subs, 594.24M views (vidIQ, updated Apr 22, 2025) [R-S22] | 3D and 2D animated hypothetical-disaster explainers ("What if…"). Being adapted for TV (Thunderbird) [R-S21] | 1) "What If the Largest Asteroid Hit Earth" (a Shorty Awards entry). **Views not retrieved** [R-S23]<br>2) No "What If Zombies" title or view count was retrievable | Not computable. Execution signal: the franchise grew by **multi-platform distribution and localization into nine languages** [R-S21], and the Spanish spin-off alone shows 3.15M subs [R-S22]. |
| 5 | **ErrorMotion**. YouTube | https://outlierkit.com/channel/errormotion | 393.0K subs, 167.9M total views (OutlierKit, undated) [R-S24] | Serialized, high-volume "Among Us Zombie" survival animations that cross over with gaming-horror franchises [R-S24] | "Among Us Zombie" series, named by OutlierKit as the biggest hits. **Individual titles and views not retrieved** [R-S24] | Not computable (no upload count). OutlierKit flags two risks: a "93-day upload hiatus" and "heavy reliance on declining third-party IPs (Among Us)" [R-S24]. |
| 6 | **GameToons**. YouTube | https://beacons.ai/i/blog/gametoons-bio | "Over 12 million subscribers" (undated bio page) [R-S25] | Serialized animated parodies of trending games ("Among Us Logic", Poppy Playtime, Rainbow Friends). A fan wiki says it later expanded into supernatural horror and urban legends [R-S25, R-S26] | No zombie-specific title or view count retrieved | Not computable |
| 7 | **AsapSCIENCE**. YouTube | (channel not opened) | Not retrieved | Whiteboard-style science animation | "Zombie Apocalypse Science". Covered by Dread Central and Gizmodo. **Views not retrieved** [R-S34, R-S35] | Not computable |
| 8 | **Life Noggin**. YouTube | (channel not opened) | Not retrieved | 2D animated science explainers with a mascot (Blocko) | "We Need to Talk About the Zombie Cells Growing Inside You", Sep 9, 2022, 3 min. **Views not retrieved** [R-S54] | Not computable. An Invidious mirror showed unlabeled counts of 25K–108K on recent videos, which could not be tied to titles. |
| 9 | **StickTheMan**. YouTube | https://listofdeaths.fandom.com/wiki/Basics_In_Survival | Not retrieved | Stick-figure / flat animated series | "Basics In Survival", an animated apocalyptic-horror series (2024–2025) based on the web series *Fundamental Paper Education* [R-S28]. **Views not retrieved** | Not computable |
| 10 | **Puzzle Hunters**. TikTok and Gumroad | https://puzzlehunters.gumroad.com/l/ep1318 | Not retrieved | Serialized animated zombie story episodes | "7 Days Before Doomsday (EP13–18)": a zombie-virus outbreak that only the protagonist knows is coming [R-S29]. A related "TikTok-viral" story about a man reincarnated a week before a zombie outbreak [R-S29]. **Views not retrieved** | Not computable. The **"advance warning / second chance before the outbreak"** hook is described as viral on TikTok (qualitative claim only). |
| 11 | **Nutshell** and **FastAndCurious**. Snapchat | https://www.snapchat.com/topic/zombie-apocalypse-comedy | Not retrieved | Stick-figure and cartoon zombie-apocalypse comedy shorts | "Zombie Restaurant Chaos" and "Yuvi's School Hallway Escape Plan" (FastAndCurious). Nutshell's stick figure "finds humor in every single terrible situation" [R-S30]. **Views not retrieved** | Not computable |
| 12 | **Unidentified YouTube Shorts creators** (two Shorts surfaced by search) | https://www.youtube.com/shorts/HreuYoU9TbE and https://www.youtube.com/shorts/goqUSAOoSZk | Not retrieved | Direct-address "what would you do" zombie Shorts | "Would you survive a Zombie Apocalypse?" and "How to survive zombies! #Zombies #Survival #Shorts". One asks "What would be your first move in a zombie apocalypse?" with three options: fortify your house, head to the wilderness, or join a group. The other draws on the game *Project Zomboid* [R-S32, R-S33]. Which Short is which could not be confirmed. **Views not retrieved** | Not computable |
| 13 | **Final Refuge** and **Infection Zero**. YouTube (both 2026 launches) | vling.net pages [R-S27] | About 1.6K subs (Final Refuge) and about 286 subs (Infection Zero), per vling.net via search summary [R-S27] | Final Refuge: narrated zombie-outbreak and collapse survival stories over gameplay footage. Infection Zero: "immersive survival storytelling", covering zombie outbreaks, biological disasters and nuclear collapse [R-S27] | No titles or views retrieved | These are **new entrants in exactly this niche**. Their small size suggests the narrated-survival-story space is open to newcomers, not saturated (judgment). |
| 14 | **Zarigüeya: Zona Cero**. YouTube (Spanish) | https://outlierkit.com/channel/zarigueyazonacero | Not retrieved | Urban prepping and DIY survival [R-S49] | Not retrieved | Not computable. Signals a Spanish-language prepping audience (see What If Español above). |
| 15 | **Disney Channel: "ZOMBIES: The Re-Animated Series Shorts"**. YouTube and Disney+ | https://whatsondisneyplus.com/zombies-the-re-animated-series-shorts-coming-soon-to-disney-us/ | n/a (studio) | Animated short-form zombie series that premiered weekly on the Disney Channel YouTube channel (2023) [R-S47] | Not retrieved | Studio precedent for **weekly serialized animated zombie shorts on YouTube**. It is family-friendly, not survival. |
| 16 | **Machinima: "Bite Me"** (historical, live-action) | https://blog.youtube/creator-and-artist-stories/machinima-says-bite-me | n/a | Serialized zombie web series about gamers caught in a real outbreak | Early episodes "passed two million views" (YouTube blog, older) [R-S46] | Historical precedent only |

### A.3 Leads that could not be verified (no numbers given)

These are well-known channels in the "what if / how to survive" animated space [BK]. **No data was retrieved for them in this session.** Check them manually before including them in any competitive table.

- **Bright Side**: animated survival-tip and "how to survive…" videos [BK].
- **Kurzgesagt**: hypothetical disaster science [BK].
- **Alternate History Hub**: a search was attempted, but nothing about its zombie content was returned [R-S34–S39 result set].
- **City Prepping** and **Canadian Prepper**: prepper and current-events survival commentary, not animated [BK].
- **TikTok "POV: zombie apocalypse" creators**: no creator could be identified.
- **YouTube @BeanieSurvives1**: surfaced as "genre-adjacent" in sibling report A (search S5). It was not checked here.

Sibling report A also found **TikTok discover topic pages** titled:

- "you-are-a-farmer-trapped-in-a-zombie-apocalypse-pt3"
- "pov-youre-a-farmer-in-a-barn-during-a-zombie-outbreak"
- "farmer-part-3-story-zombie-in-english"

TikTok creates these pages around recurring searches or hashtags. That makes them **weak evidence that the "farmer in a zombie apocalypse, part N" premise is a recurring short-form trope**. Source: `A_reference_account.md`, section 4, "Excluded results". Not re-verified by me.

### A.4 Execution evidence pulled from section A (format and packaging)

1. **Real incidents retold as animated Shorts are the biggest earners at the largest comparable channel.** Zack D. Films' top-listed videos are real-world disaster stories ("Ohio's 1986 Balloon Disaster", "The Pepsi Contest That Killed 5 People"), not fictional scenarios [R-S2, R-S3].
2. **Second-person "Could you survive / YOU vs" framing is an established Infographics Show format.** The zombie entries date back to 2018 and 2020 [R-S11, R-S12]. One of them aired **Oct 1**, a pre-Halloween slot.
3. **The pause-and-decide puzzle with a zombie timer reached tens of millions** in long-form: the TED-Ed bridge riddle, about 24M by its own page counters [R-S15, R-S16].
4. **Serialized zombie-survival animation can build a mid-size channel, but borrowed IP is a stated risk.** ErrorMotion is the example [R-S24]. This argues for Worldosphere's original recurring characters (judgment).
5. **Localization multiplies reach.** What If runs in 9 languages, and its Spanish channel shows 3.15M subs [R-S21, R-S22].
6. **Hoax risk.** The 2022 "zombies in China" TikTok trend spread from a misread article [R-S40]. Label fiction clearly and avoid "breaking news" styling (judgment, based on [R-S40]).

---

## B. Evidence of audience demand for specific topics

### B.1 Search-suggest phrasing: NOT ACCESSIBLE

`suggestqueries.google.com` failed DNS through WebFetch. YouTube autocomplete could not be loaded. **No autocomplete data was collected.**

The phrasings below are hypotheses to test by typing them into the YouTube search bar on a logged-out browser. They are **[J]**, not evidence:

- "how to survive a zombie apocalypse"
- "best place to hide in a zombie apocalypse"
- "what to do if a zombie apocalypse happens"
- "zombie apocalypse in school"
- "would you survive"
- "what to do if you fall through ice"
- "what to do if your car goes into water"
- "what to do in an earthquake"
- "what to do if a tornado"
- "what to do if you see a bear"
- "how to survive a nuclear bomb"
- "how to survive a blackout"
- "what happens if the grid goes down"

### B.2 Reddit: NOT ACCESSIBLE

WebFetch could not load reddit.com or old.reddit.com ("unable to fetch"). curl got a 403. Sibling report A recorded that WebSearch rejects reddit.com as a domain filter ("not accessible to our user agent"). **No Reddit thread, upvote count or comment was retrieved.**

Threads worth checking manually [BK, not verified]:

- r/AskReddit: "What's your zombie apocalypse plan?" and "Where would you go?" type threads
- r/zombies: "best location" and "best weapon" threads
- r/preppers: grid-down and winter-storm threads
- r/WritingPrompts: zombie-outbreak prompts
- r/NoStupidQuestions and r/whatif: hypothetical survival questions

### B.3 Recurring debate questions (with what evidence exists)

| Debate question | Retrieved evidence | Notes |
|---|---|---|
| **Where do you go or hide?** (city vs countryside; upper floor vs bunker) | A Stylist article describes **viewers debating where they'd hide**: one picks "a second-floor plan", another a bunker [R-S38]. The 2015 Cornell model, as reported: starting in "a big city like New York or Atlanta" means "you are basically screwed from the start"; ideally escape to "an almost empty region like the Rocky Mountains" [R-S36]. An outbreak simulator lets you "watch the infection spread like wildfire across America" [R-S37] | This is the strongest retrieved demand signal for **location-choice** content. The classic location debates (mall, prison, boat, island, Costco, Home Depot, farm) are **[BK]**. They are long-running staples of zombie fandom, popularized by *Dawn of the Dead* (mall), *The Walking Dead* (farm, prison) and Max Brooks' *Zombie Survival Guide* (boats and islands), but no thread or engagement figure was retrieved for them. |
| **What is your first move?** | A YouTube Short asks "What would be your first move in a zombie apocalypse?" with three choices: fortify your house, head to the wilderness, or join a group [R-S32/S33] | This maps directly onto a three-choice decision Short with a poll or comment prompt (judgment). |
| **Would you survive?** | A Gizmodo piece, "Would you survive the zombie apocalypse" (interactive "The Outbreak") [R-S42]. A YouTube Short, "Would you survive a Zombie Apocalypse?" [R-S32]. Infographics Show, "Could You Survive A Zombie Attack?" [R-S11] | This is a recurring title formula across a decade of content. |
| **How would the outbreak actually spread? Is it scientifically possible?** | AsapSCIENCE: "Dying and coming back from the dead? Not so likely. But a virus that induces zombie-like qualities of rage and the incessant need to eat human flesh, hypothetically? Yes" (as quoted by Dread Central, rendered in the search summary) [R-S34]. A critique of the Cornell model, as rendered in the search summary: "bitten and infected people would drive cars and hop planes and do all sorts of other dumb stuff to increase the speed of infection" [R-S36–S39 result set; exact page not determinable] | Expect **science and plot-hole debate** in comments (see section D). |
| **Is it real?** (hoax appetite) | Aug 2022: "zombies in China" trended on TikTok. "Many people treated a work of fiction as a real forecast" [R-S40] | This shows appetite, and also a reputational risk. |
| **Fighting a horde** (numbers games) | "YOU vs 1000 ZOMBIES" (Infographics Show) [R-S12] | The broader "X vs Y" debates ("100 men vs 1 gorilla", "man vs bear") went viral in 2024–2025 [BK]. Not verified here. |
| **"First 24 hours"** framing | SYFY's *Day of the Dead* "set during the first 24 hours of a ghoulish outbreak", with episodes put free on SYFY's YouTube [R-S43] | Supports "Hour 1 / Hour 6 / Hour 24" timer overlays (judgment). |

### B.4 Seasonal signals (dates for 2026 computed from calendar rules; rules are [BK])

| Date (2026) | Event | Status | Premise hooks |
|---|---|---|---|
| **Sat Oct 31** | Halloween falls on a **Saturday**, which means party night | Weekday computed. **[R]** scheduling precedents: an Infographics Show zombie episode aired **Oct 1** (2018) [R-S11]; SYFY's *Day of the Dead* premiered in mid-October [R-S43]; a 2021 ShortsTV **Halloween campaign** told a zombie outbreak "across a series of 14 short videos" (search summary; source attribution uncertain) [R-S48] | Halloween party where every guest is in zombie makeup; trick-or-treat outbreak |
| **Sun Nov 1, 2:00 a.m.** | US daylight saving time ends ("first Sunday of November" rule [BK]) | Date computed | "Darkness comes an hour early tonight": a dusk-timed outbreak; a lost hour of daylight on a hike |
| **About Nov 17–18** | Leonid meteor shower peak (typical window [BK]; check 2026 specifics with the American Meteor Society or IMO) | [BK] | Meteor-night outbreak (an homage to *Night of the Comet* [BK]); a "something landed" story |
| **Thu Nov 26** | US Thanksgiving (4th Thursday) | Date computed | Thanksgiving-dinner outbreak; turkey-fryer fire. NFPA has repeatedly identified Thanksgiving as the peak day for US home cooking fires [BK]. Verify with NFPA before citing. |
| **Fri Nov 27** | Black Friday | Date computed | Doorbuster crowd and zombie horde; crowd-crush physics |
| **Mon Nov 30** | End of the Atlantic hurricane season (NOAA's official June 1–Nov 30 [BK]) | Date computed | "Last storm of the season" story |
| **Dec–Feb** | Winter storms and cold snaps; **Mon Dec 21** solstice (longest night) | [BK] | Blizzard stranding, carbon monoxide during a blackout, falling through ice, "longest night" outbreak |

**Google Trends for "zombie": NOT ACCESSIBLE.** trends.google.com could not be loaded, and no article describing zombie search seasonality was found before the search budget ran out. Hypothesis **[BK]**: search interest in "zombie" has historically risen each October around Halloween, and spiked around *The Walking Dead* premieres and *The Last of Us* (2023). **Check it at** https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=zombie (and with `gprop=youtube` for YouTube search).

**Other trend hooks [BK, unverified; confirm dates before using]:**

- Zombie releases in 2026: *28 Years Later: The Bone Temple* (January), *Resident Evil Requiem* (game, February), and a new *Resident Evil* feature film slated for September 2026.
- Real-event disaster interest:
  - May 2024 G5 geomagnetic storm (auroras)
  - Asteroid 2024 YR4 "city-killer" risk headlines (early 2025)
  - Iberian Peninsula blackout (April 28, 2025)
  - Kamchatka M8.8 earthquake and Pacific tsunami warnings (July 2025)
  - Los Angeles wildfires (January 2025)
  - Hawaii false missile alert (2018)
  - "Zombie" science headlines: permafrost "zombie virus" (2022–23), chronic wasting disease ("zombie deer disease", 2024), Cordyceps after *The Last of Us* (2023)
- The CDC's 2011 "Preparedness 101: Zombie Apocalypse" blog post is widely reported to have overwhelmed the CDC blog with traffic.

---

## C. Candidate premise pool (84 premises)

Column key:

- **Evidence**: [R-Sxx] retrieved; [BK] background knowledge (unverified); [J] creative judgment only.
- **Season/trend**: E = evergreen; H = Halloween; T = Thanksgiving / Black Friday; W = winter; S = news-spike dependent; D = DST; L = Leonids.
- **Comparable**: existing works are named so the channel can differentiate. Views are given **only** where retrieved; "views n/r" means not retrieved.

### C.1 Zombie outbreak in a specific everyday location (36)

| # | One-line premise | Evidence of interest | Season/trend | Comparable existing work |
|---|---|---|---|---|
| 1 | Outbreak starts while you're on a remote **farm**: fences, livestock noise, a generator, the barn | [R] TikTok topic pages "you-are-a-farmer-trapped-in-a-zombie-apocalypse-pt3" and "pov-youre-a-farmer-in-a-barn-during-a-zombie-outbreak" exist (sibling report A). [R-S36] Cornell model favors sparse rural areas | E | *The Walking Dead* S2 farm [BK]. The reference account's "The Last Farm" |
| 2 | **City vs countryside**: Hour 0 in a downtown apartment, and you must reach low-density land before the bridges close | [R-S36] Cornell: a big city means "basically screwed", head for the Rockies. [R-S37] spread simulator | E | Cornell simulator coverage (IFLScience, Uproxx) [R-S36, S37] |
| 3 | **High-rise apartment**: stay on floor 2 or climb to 30? The water and stairwell math | [R-S38] viewers debate a "second-floor plan" vs a bunker | E | *#Alive* (2020 film) [BK] |
| 4 | **School** lockdown turns into an outbreak during 3rd period: hallway escape plan | [R-S30] FastAndCurious "Yuvi's School Hallway Escape Plan" (views n/r) | E (back-to-school Aug–Sep) | *All of Us Are Dead* (Netflix) [BK] |
| 5 | Waking up alone in a **hospital** ward on day 9 of the outbreak | [J] | E | *28 Days Later*; *TWD* pilot [BK] |
| 6 | **Shopping mall**: the classic stronghold, but the glass doors and the food court are traps | [BK] long-running "best location" debate | E | *Dawn of the Dead* (1978/2004) [BK] |
| 7 | **Costco / warehouse club**: endless food, terrible doors. Can you hold it? | [BK] "Costco in the apocalypse" is a common meme and debate. No thread retrieved | E, T (Black Friday tie-in) | Not identified |
| 8 | **Hardware superstore** vs Costco: which one do you barricade? (poll Short) | [BK] | E | Not identified |
| 9 | **Prison**: walls are perfect, but who is already inside? | [BK] | E | *TWD* S3 prison [BK] |
| 10 | **Sailboat / houseboat**: zombies can't swim (can they?), but fresh water runs out | [BK] boat and island strategy in Max Brooks' guide | E | *Zombie Survival Guide* [BK] |
| 11 | **Small island**: safe until the ferry arrives with one infected passenger | [BK] | E, summer | Not identified |
| 12 | **Cruise ship**: 3,000 cabins, one sick passenger, 4 days from port | [J]. [BK] cruise-ship outbreak news (norovirus, COVID-era quarantines) | E | Not identified |
| 13 | **Airplane** at 35,000 ft: someone in row 31 was bitten before boarding | [J] | E (holiday travel spike in late Nov) | *World War Z* plane sequence [BK] |
| 14 | **Subway** car stalls in a tunnel and the lights go out | [J] | E | *Train to Busan* (train) [BK] |
| 15 | **Gas station** at 2 a.m.: fuel, snacks and one locked bathroom | [J] | E | Not identified |
| 16 | **Ski resort** lodge snowed in: zombies are slow in the cold. Or are they? | [J] | W | Not identified |
| 17 | **Thanksgiving dinner**: Grandpa "isn't feeling well" before the turkey is carved | [J] + calendar (Nov 26) | T | Not identified |
| 18 | **Black Friday** doorbuster: the crowd at the doors is not shoppers | [J] + calendar (Nov 27) | T | Not identified |
| 19 | **Halloween party**: everyone is in zombie makeup, so who is real? | [J] + calendar (Sat Oct 31) + [R-S48] Halloween serialized zombie campaign precedent | H | Not identified |
| 20 | **Trick-or-treat** route: the houses with lights on are the dangerous ones | [J] | H | Not identified |
| 21 | **Wedding** reception: the best man was bitten at the bachelor party | [J] | E (summer and fall wedding season) | Not identified |
| 22 | **Office tower** on a Monday morning: badge-locked doors become a trap | [J] | E | Not identified |
| 23 | **Fast-food kitchen** during the lunch rush: the walk-in freezer as a panic room | [R-S30] Snapchat "Zombie Restaurant Chaos" (views n/r) | E | FastAndCurious [R-S30] |
| 24 | **Submarine** on patrol: the outbreak happens on the surface. Surface, or stay down for 90 days? | [J] | E | Not identified |
| 25 | **Antarctic research station**: the last uninfected place on Earth, until the supply plane lands | [J] | W (southern summer = station season) | *The Thing* vibe [BK] |
| 26 | **Theme park** after closing: rides as barricades, the park as a maze | [J] | E | *Zombieland* (Pacific Playland) [BK] |
| 27 | **Zoo** outbreak: are the animals infected too? | [R-S51] the animated feature *Zombies im Zoo* ("Madagascar meets The Walking Dead") exists | E | *Zombies im Zoo* [R-S51] |
| 28 | **Movie theater** during a zombie movie: the screams are not from the film | [J] | H | Not identified |
| 29 | **Stadium** at a sold-out game: 70,000 people, 12 exits | [J] | E (football season) | Not identified |
| 30 | **Highway evacuation gridlock**: abandon the car or wait? | [J]. [R-S36–S39] critique notes cars and planes would accelerate spread | E | Not identified |
| 31 | **Prepper bunker** with 30 days of supplies: a knock on the hatch on day 12 | [R-S38] bunker choice in the hiding debate. [R-S49] prepping channels | E | Not identified |
| 32 | **Space station** crew watches the outbreak from orbit: when do you come home? | [J] | S (crewed-spaceflight news) | Not identified |
| 33 | **Lighthouse / remote cabin** in the woods: perfect isolation, one road in | [J] | E | Not identified |
| 34 | **Elevator** stuck between floors as the outbreak begins outside the doors | [J] | E | Not identified |
| 35 | **Military checkpoint / quarantine zone**: you're healthy, but the scanner says otherwise | [J] | E | *The Last of Us* QZs [BK] |
| 36 | **Gym / fitness center**: strongest people, weakest doors (glass walls) | [J] | E (January resolutions) | Not identified |

### C.2 Zombie scenario twists and mechanics (14)

| # | One-line premise | Evidence of interest | Season/trend | Comparable existing work |
|---|---|---|---|---|
| 37 | **The bridge**: you have 17 minutes to get 4 survivors across before the horde arrives (puzzle Short) | **[R-S15/S16/S17] TED-Ed zombie bridge riddle: about 24.1M (ed.ted.com) / about 24.4M (TED.com) / 21.4M (Glasp)** | E | TED-Ed "Can you solve the bridge riddle?" [R-S15] |
| 38 | **Your first move**: fortify the house, head for the wilderness, or join a group? (three endings) | [R-S32/S33] a YouTube Short asks exactly this | E | Unidentified Shorts [R-S32/S33] |
| 39 | **You get 7 days of warning** before the outbreak, and nobody believes you | [R-S29] Puzzle Hunters "7 Days Before Doomsday"; "TikTok-viral" reincarnation-before-outbreak story | E | Puzzle Hunters [R-S29] |
| 40 | **You vs a 1,000-zombie horde** with 1 car, 1 radio, 1 rooftop | [R-S12] Infographics Show "YOU vs 1000 ZOMBIES" title exists (views n/r) | E | The Infographics Show [R-S12] |
| 41 | **Would you survive?** Five questions decide whether you reach Day 30 | [R-S11, R-S32, R-S42] recurring title formula | E | Infographics Show; Gizmodo "The Outbreak" |
| 42 | **Hidden infected**: one of the 5 survivors in the safe room was bitten. Who? | [R-S24] ErrorMotion's top hits are serialized "Among Us Zombie" survival animations (an imposter-style hidden-infected mechanic) | E | ErrorMotion [R-S24] |
| 43 | **Rage virus through the nose**: how an outbreak could plausibly start (science-framed) | [R-S34, S35] AsapSCIENCE "Zombie Apocalypse Science" covered by Dread Central and Gizmodo | E | AsapSCIENCE (views n/r) |
| 44 | **Fungal (Cordyceps-style) outbreak**: no bites, just spores | [BK] *The Last of Us*-driven Cordyceps interest (2023) | S | *The Last of Us* [BK] |
| 45 | **The permafrost virus**: a melting Siberian thaw releases something old | [BK] 2022–23 "zombie virus" permafrost headlines | S | Not identified |
| 46 | **Outbreak on Leonid night**: everyone outside watching the meteors | [J] + [BK] Leonids mid-Nov | L | *Night of the Comet* (1984) [BK] |
| 47 | **The night clocks fall back**: darkness arrives at 5 p.m. on Day 1 | [J] + calendar (DST ends Nov 1) | D | Not identified |
| 48 | **Blizzard plus zombies**: do the infected freeze solid? | [J] | W | Not identified |
| 49 | **Day 1,000**: what the world actually looks like after 3 years (infrastructure decay overlay) | [J]. [BK] "Life After People"-style decay content is a known genre | E | Not identified |
| 50 | **The pet question**: your dog barks at every zombie. Keep him or not? | [J]. The reference series includes a dog (Rusty, per sibling report A) | E | Not identified |

### C.3 Real-world disaster survival stories (26)

These are educational-adjacent. Every factual claim in them must pass fact-check; see sibling report D2.

| # | One-line premise | Evidence of interest | Season/trend | Comparable existing work |
|---|---|---|---|---|
| 51 | **Earthquake** while you're on the 20th floor: drop, cover, hold on, not the doorway | [BK] recurring "doorway myth" corrections; Japan megaquake advisory (2024) and Kamchatka M8.8 (2025) headlines | S | Not identified |
| 52 | **Tornado** siren while driving: why the highway overpass is a death trap | [BK] long-standing NWS myth-busting | Spring (Mar–Jun), Nov secondary season [BK] | Not identified |
| 53 | **Flash flood**: your car stalls in 12 inches of water | [BK] NWS "Turn Around Don't Drown" | Summer, S | Not identified |
| 54 | **Tsunami**: the ocean suddenly pulls back at the beach | [BK] 2025 Pacific tsunami warnings | S | Not identified |
| 55 | **Wildfire evacuation** with one road out | [BK] LA fires (Jan 2025) | Summer–fall, S | Not identified |
| 56 | **Blizzard**: stranded in your car overnight. Stay with the car, clear the exhaust pipe | [BK] | W | Not identified |
| 57 | **Avalanche** at a ski resort: the first 15 minutes | [BK] | W | Not identified |
| 58 | **Hurricane**: stay or evacuate? The storm-surge decision | [BK] Hurricane Helene and Milton (2024), Melissa (2025) coverage | Jun–Nov 30 | Not identified |
| 59 | **Heat wave** plus power outage in a top-floor apartment | [BK] | Summer | Not identified |
| 60 | **Volcanic eruption**: ash fall 30 km away. What actually kills you? | [BK] Iceland Reykjanes eruptions (2023–25) | S | Not identified |
| 61 | **Solar storm**: the grid goes dark for a week (supply counter) | [BK] May 2024 G5 storm; Iberian blackout (Apr 2025) | S | Not identified |
| 62 | **Nuclear alert** on your phone: you have 15 minutes. Get inside, go deep, stay in | [BK] Hawaii false alert (2018) | S | Not identified |
| 63 | **Sinking car**: seatbelt, window, out. The 60-second rule | [BK] widely shared rescue-tool advice | E | Not identified |
| 64 | **House fire at 3 a.m.**: why closing the door buys you minutes | [BK] UL "Close Before You Doze" campaign | W (heating season), T (cooking) | Not identified |
| 65 | **Rip current** pulls you out: swim parallel, don't fight | [BK] NOAA and USLA guidance | Summer | Not identified |
| 66 | **Lost in the woods** at dusk: stay put and make yourself findable | [BK] "Hug-a-Tree" program | Fall hunting season, D (early dark) | Not identified |
| 67 | **Stuck in an elevator**: why prying the doors is the dangerous move | [BK] (see sibling report D2 §4 for checked facts) | E | Not identified |
| 68 | **Carbon monoxide during a blackout**: the generator in the garage | [BK] CDC post-storm CO warnings; Texas Feb 2021 | W | Not identified |
| 69 | **Bear encounter**: black vs brown bear rules | [BK] "man vs bear" debate went viral in 2024 | E, fall (bears foraging) | Not identified |
| 70 | **Falling through ice**: the 1-10-1 rule | [BK] | W | Not identified |
| 71 | **Turkey-fryer fire** on Thanksgiving | [BK] NFPA: Thanksgiving is the peak day for home cooking fires (verify) | T | Not identified |
| 72 | **Crowd crush** at a Black Friday door, concert or festival: how to survive the surge | [BK] Itaewon 2022 and Astroworld 2021 (sensitive) | T | Not identified |
| 73 | **City-killer asteroid** is announced: 7 years of warning. What do you do? | [R-S23] What If "What If the Largest Asteroid Hit Earth" (award entry; views n/r). [BK] 2024 YR4 headlines | S, L | What If [R-S23] |
| 74 | **Plane ditching** on water: brace, leave the bags, inflate the vest outside | [BK] | E (holiday travel) | Not identified |
| 75 | **Lost at sea in a life raft**: water, sun, signal | [BK] | E | Not identified |
| 76 | **Real disaster retold minute by minute**: an animated historical incident in the Zack D. style | [R-S2, R-S3] Zack D. Films' top-listed videos are real incidents ("Ohio's 1986 Balloon Disaster" 18.45M; "The Pepsi Contest That Killed 5 People" 12.4M) | E | Zack D. Films [R-S3] |

### C.4 Survival myths and mistakes (5)

| # | One-line premise | Evidence of interest | Season/trend | Comparable |
|---|---|---|---|---|
| 77 | **3 earthquake, tornado and flood myths** that get people killed (doorway, overpass, "a little water is fine") | [BK] standard NWS and USGS myth lists | E | Not identified |
| 78 | **"Eat snow for water"** and **"alcohol warms you up"**: winter myths | [BK] | W | Not identified |
| 79 | **"Play dead"** works for one bear and gets you killed with another | [BK] | E | Not identified |
| 80 | **Zombie-movie rules that would actually get you killed** (shooting a gun, splitting up, the noisy car) | [J]. [R-S36–S39] audiences already argue the logic of spread models | E, H | Not identified |
| 81 | **Movie quicksand vs real quicksand** | [BK] (see sibling report D2 §9: unverified) | E | Not identified |

### C.5 Decision-and-consequence dilemmas (3; more dilemmas are embedded in #3, #8, #30, #38, #50, #58)

| # | One-line premise | Evidence of interest | Season/trend | Comparable |
|---|---|---|---|---|
| 82 | **A stranger at the door on Day 5** asks for help. Let them in? (supply counter shows the cost) | [J] | E | Not identified |
| 83 | **Your friend hides a bite.** Tell the group? | [J]. Related to [R-S24] hidden-infected mechanic | E | Not identified |
| 84 | **Pick 3 items only** from a 12-item grid to survive 72 hours (comment-bait) | [J] | E | Not identified |

**Total: 84 premises** (36 + 14 + 26 + 5 + 3 = 84).

### C.6 Premise ranking by strength of retrieved evidence (judgment applied to the labels above)

| Rank | # | Premise | Why it ranks here |
|---|---|---|---|
| 1 | 37 | Zombie bridge / timed-escape puzzle | The only per-video number directly tied to zombie content: about 24M views on TED-Ed's own counters [R-S15, S16] |
| 2 | 76 | Real disaster retold minute by minute | The largest comparable channel's top-listed videos are real incidents at 12–18M [R-S3] |
| 3 | 2 | City vs countryside, first 24 hours | Cornell model coverage across several outlets [R-S36, S37, S38]; SYFY "first 24 hours" [R-S43] |
| 4 | 3 | High-rise: second floor vs bunker | A viewer hiding debate reported directly [R-S38] |
| 5 | 31 | Prepper bunker, knock on Day 12 | Bunker side of the same debate [R-S38]; prepping channels exist [R-S49]; new 2026 survival channels [R-S27] |
| 6 | 1 | Farm outbreak | TikTok topic pages for "farmer in zombie apocalypse pt3" (sibling A); Cornell rural-safety logic [R-S36] |
| 7 | 42 | Hidden infected in the group | ErrorMotion's serialized "Among Us Zombie" hits [R-S24] |
| 8 | 38 | First move: house, wild or group? | An existing Short asks exactly this [R-S32/S33] |
| 9 | 41 | Would you survive? | A recurring title formula across three sources [R-S11, S32, S42] |
| 10 | 40 | You vs a 1,000-zombie horde | Existing Infographics Show title [R-S12] (views n/r) |
| 11 | 39 | 7 days of warning | Described as "TikTok-viral" [R-S29] |
| 12 | 4 | School outbreak escape | Snapchat precedent [R-S30] |
| 13 | 73 | City-killer asteroid with years of warning | What If award entry [R-S23] |
| 14 | 19 | Halloween party: who's real? | Halloween zombie scheduling precedents [R-S11, S43, S48]; Halloween is a Saturday |
| 15 | 43 | How an outbreak could plausibly start (science) | AsapSCIENCE coverage [R-S34, S35]; "zombies in China" hoax appetite [R-S40] |

Seasonal premises (17, 18, 46, 47, 64, 68, 70, 71) have **calendar certainty but no retrieved demand data**. They rank lower on evidence, but they may be the best scheduling bets for Oct–Dec 2026 (judgment).

---

## D. Recurring audience comment themes

### D.1 What could be retrieved

**No verbatim viewer comments from YouTube, TikTok, Instagram or Reddit were retrieved.** All of those hosts were unreachable, and WebSearch does not index comment text. The items below are the closest available material: article descriptions of audience behavior, and creator or critic quotes as rendered in search summaries. They are **not** viewer comments.

| Theme | What was found | Source |
|---|---|---|
| **Arguing about where to hide** | Stylist describes people debating hiding spots: "a second-floor plan" vs a bunker | [R-S38] |
| **Plot-hole and logic policing of outbreak models** | Critique of the Cornell model, as rendered in the search summary: "bitten and infected people would drive cars and hop planes and do all sorts of other dumb stuff to increase the speed of infection" | [R-S36–S39 result set; exact page not determinable] |
| **Science plausibility** | Transmission caveat (paraphrased in the summary): direct-contact spread would normally be "quite an inefficient method" compared with airborne spread, but zombies "actively try to bite", which spreads it faster | [R-S39, sciencefocus.com or physicsworld.com; attribution uncertain] |
| **Fiction taken as fact** | "Many people treated a work of fiction as a real forecast" ("zombies in China", 2022) | [R-S40] |
| **Comedy appetite** | A stick figure who "finds humor in every single terrible situation" (description of the Nutshell Snapchat content) | [R-S30] |

### D.2 Likely comment themes to plan for (hypotheses: [BK]/[J], not evidence)

These are **unverified expectations** based on general familiarity with the genre. Check them by reading the top 100 comments on 5–10 comparable Shorts once access is available.

- **Praise:** art style and character design; the narrator's voice; cliffhangers ("Part 2?"); the infographic overlays (maps, timers, counters).
- **Arguments:**
  - Location choice (mall vs Costco vs boat vs prison)
  - Fast vs slow zombies
  - Gunshots attracting the horde
  - "Why didn't he just…" solutions
  - "I would survive because…" self-insertion
- **Factual corrections** (especially on the real-disaster premises):
  - Doorway and overpass myths
  - Car-window and seatbelt order
  - Hypothermia and alcohol
  - Bear-type rules
  - Generator placement
  - Ammunition and weapon realism
- **Requests:** "do one in my country, school or job"; "what if it happened in [location]"; "part 2"; a named character's backstory.
- **Infographics Show-style criticism:** viewers and Reddit threads have often criticized animated explainer channels for factual inaccuracies [BK]. This is a reason to keep a fact-check ledger (see sibling report D2).

### D.3 Execution implications (judgment)

1. End every zombie Short with a **forced choice** (2–3 options), because the strongest retrieved debates are location and first-move choices.
2. Build in a **visible "why not X?" rebuttal beat** (for example: "the boat looked safe, but…"). This pre-empts plot-hole policing.
3. For real-disaster premises, use **only fact-checked actions**. Corrections in comments are likely, and an error damages trust in the whole channel.
4. Add an "**original fiction**" cue on zombie Shorts that use news-style overlays, given the hoax precedent [R-S40].

---

## E. Source list (all accessed 2026-10-14, via WebSearch result summaries only; no page was opened)

| ID | URL | What the search summary said it shows |
|---|---|---|
| S1 | https://www.speakrj.com/audit/report/zackdfilms/youtube | Zack D. Films: 27.7M subs, 72.2B views, 3,633 videos, as of Jul 17, 2026 |
| S2 | https://outlierkit.com/channel/zackdfilms | 27.6M subs. Shorts are 100% of views. Top videos are real-world stories (Balloon Disaster, Pepsi Contest) |
| S3 | https://vidiq.com/youtube-stats/channel/@zackdfilms/ | About 28.7M subs, about 78.03B views, 4,025 videos, latest upload Oct 4, 2026. Top videos: "Ohio's 1986 Balloon Disaster" 18.45M; "The Pepsi Contest That Killed 5 People" 12.4M |
| S4 | https://hypeauditor.com/youtube/UCvz84_Q0BbvZThy75mbd-Dg/ | About 28.9M subs (Oct 2026). Oct 8: about 6.43M views gained; 4,009 videos |
| S5 | https://us.youtubers.me/zack-d-films/youtube-videos-stats | April 2026 table: "How To Make A Candle From An Orange 😮" 22,171,086; "The Trick To Winning Tic Tac Toe 😮" 23,231,305; about 65B total (April 2026) |
| S6 | https://www.speakrj.com/audit/report/UCvz84_Q0BbvZThy75mbd-Dg/youtube/media-stats/ | Recent uploads (Jul 2026): plane-related about 16.7M, catfish about 16.9M (titles not given) |
| S7 | https://outlierkit.com/channel/theinfographicsshow | 15.5M subs, 6.8B views, about 1.1M average views per video, $64K–$209K/month estimate |
| S8 | https://socialblade.com/youtube/handle/theinfographicsshow/achievements | 16M subs, 6.9B views, 6.3K videos (undated) |
| S9 | https://vidiq.com/youtube-stats/channel/@theinfographicsshow/ | About 15.5M subs, 6.84B views. +100K subs and 29.51M views in the last 30 days. Started Feb 26, 2011 |
| S10 | https://creatordb.app/creatorstats/theinfographicsshow/ | Refreshed Sep 24, 2026: 15.5M. Engagement 1.8% vs category median 1.5% |
| S11 | https://thetvdb.com/series/infographics/episodes/7936248 | "Could You Survive A Zombie Attack?", aired Oct 1, 2018, 5 min |
| S12 | https://thetvdb.com/series/the-infographics-show/episodes/8727710 | "YOU vs 1000 ZOMBIES - How To Defeat and Survive a Zombie Horde", aired Jan 28, 2020 |
| S13 | https://videoexplainers.com/?p=2335 | Infographics Show's most-viewed video (after-death topic): over 21M (older promotional page) |
| S14 | https://www.spotterstudio.com/creator-stories/the-infographics-show | Infographics Show title-ideation case study ("2hrs to 2min"). Execution context only |
| S15 | https://ed.ted.com/lessons/can-you-solve-the-bridge-riddle-alex-gendler | Bridge (zombie) riddle: 24,088,563 views |
| S16 | https://www.ted.com/talks/alex_gendler_can_you_solve_the_bridge_riddle | 24,359,925 plays |
| S17 | https://glasp.co/youtube/7yDmGnA8Hw0 | 21.4M views. Zombies pursue you across a bridge; about 4 min |
| S18 | https://www.educatorstechnology.com/2023/01/6-of-best-ted-ed-riddles-to-use-with.html | TED-Ed riddles picked "as measured by number of views and audience interaction" |
| S19 | https://thekidshouldseethis.com/post/can-you-solve-the-virus-riddle | TED-Ed virus riddle exists |
| S20 | https://underknown.com/news/thunderbird-entertainment-to-take-what-if-to-television/ (also underknown.com/?p=401, ?p=711) | What If: 35M+ subscribers across platforms; about 450M monthly views (2021); 14M followers (2019) |
| S21 | https://www.businesswire.com/news/home/20201007005242/en/Thunderbird-Entertainment-to-Take-the-Multi-Billion-View-Social-Media-Sensation-What-If-to-Television | What If: 250M views/month; 6B+ views in nine languages (Oct 2020) |
| S22 | https://vidiq.com/youtube-stats/channel/UC5BW1w7JyJW3r8rpR3BhqKA | "Qué pasaría si - What If Español": 3.15M subs, 594.24M views (updated Apr 22, 2025) |
| S23 | https://shortyawards.com/15th/what-if-what-if-the-largest-asteroid-hit-earth | What If asteroid video (award entry) |
| S24 | https://outlierkit.com/channel/errormotion | ErrorMotion: 393.0K subs, 167.9M views. "Among Us Zombie" hits; 93-day hiatus; IP risk |
| S25 | https://beacons.ai/i/blog/gametoons-bio | GameToons: 12M+ subs (undated); launched March 2020 |
| S26 | https://shapes.inc/fandom/gametoons | Fan wiki: expansion into supernatural horror |
| S27 | https://vling.net/en/channel/UCyo4F-KFqdLA1sOw7iGDrBw/channel-info, https://vling.net/en/channel/UCgO7SwesMCpsbaY9oHg2osQ/channel-info, https://vling.net/en/channel/UChH9wnwpgNPZ0fECf_Dctlg/channel-info | Final Refuge about 1.6K subs; Infection Zero about 286 subs (2026 channels). Which ID maps to which name was not confirmed |
| S28 | https://listofdeaths.fandom.com/wiki/Basics_In_Survival | StickTheMan, "Basics In Survival" (2024–25) |
| S29 | https://puzzlehunters.gumroad.com/l/ep1318 ; https://puzzlehunters.gumroad.com/l/ugusj | "7 Days Before Doomsday"; TikTok-viral reincarnation-before-outbreak story |
| S30 | https://www.snapchat.com/topic/zombie-apocalypse-comedy | Nutshell; FastAndCurious "Zombie Restaurant Chaos", "Yuvi's School Hallway Escape Plan" |
| S31 | https://www.tiktok.com/discover/animated-zombie-short-films | TikTok topic page: *Love, Death & Robots* "Mini Zombie Apocalypse"; "Nova: The Deadly Zombie Crisis" |
| S32 | https://www.youtube.com/shorts/HreuYoU9TbE | "Would you survive a Zombie Apocalypse?" |
| S33 | https://www.youtube.com/shorts/goqUSAOoSZk | "How to survive zombies! #Zombies #Survival #Shorts" |
| S34 | https://www.dreadcentral.com/news/38977/form.php?id=12 | AsapSCIENCE "Zombie Apocalypse Science" quote |
| S35 | https://gizmodo.com/zombies-could-actually-exist-sort-of-5955741 | AsapSCIENCE summary: a *28 Days Later*-like virus |
| S36 | https://www.iflscience.com/editors-blog/if-the-zombie-apocalypse-happens-this-is-where-scientists-say-you-should-go/ | Cornell 2015: big city means "screwed"; flee to the Rockies |
| S37 | https://uproxx.com/?p=1226275 | Zombie outbreak simulator across America |
| S38 | https://stylist.co.uk/life/zombie-apocalypse-plan-survival-what-to-do-scientists-expert-advice/185520 | Viewers debating where they'd hide (second floor vs bunker); Cornell simulation |
| S39 | https://www.sciencefocus.com/science/how-to-stop-a-zombie-apocalypse-with-science ; https://physicsworld.com/?p=11658 ; https://pjmedia.com/print/159900 | Epidemiology and critique snippets (attribution among these not determinable) |
| S40 | https://meaww.com/why-is-zombies-in-china-trending-on-tiktok ; https://www.publimetro.co/entretenimiento/2022/08/31/tiktokers-estan-completamente-convencidos-que-hay-un-apocalipsis-zombie-secreto-en-china-en-este-momento/ | Aug 2022 "zombies in China" hoax trend |
| S41 | https://www.abs-cbn.com/advertorial/life/02/04/22/tiktokers-use-hs-lessons-to-survive-a-zombie-apocalypse | 2022 brand campaign using zombie-survival framing on TikTok |
| S42 | https://gizmodo.com/would-you-survive-the-zombie-apocalypse-5055847 | "Would you survive" interactive ("The Outbreak") |
| S43 | https://www.syfy.com/syfy-wire/day-of-the-dead-syfy-how-to-watch-free | *Day of the Dead* set in the first 24 hours; free episodes on YouTube; mid-October premiere |
| S44 | https://www.dreadcentral.com/news/266845/zombie-apocalypse-infects-lego-stop-motion-film | FK Films LEGO lab-outbreak short |
| S45 | https://laughingsquid.com/isolated-animated-sci-fi-short-about-a-taxi-driver-who-crashes-wakes-up-in-a-zombie-outbreak/ | *Isolated*, an animated zombie-outbreak short |
| S46 | https://blog.youtube/creator-and-artist-stories/machinima-says-bite-me | "Bite Me": early episodes passed 2M views |
| S47 | https://whatsondisneyplus.com/zombies-the-re-animated-series-shorts-coming-soon-to-disney-us/ | Disney animated zombie shorts on YouTube (2023) |
| S48 | Search-summary item in the query "zombie apocalypse day 1 animated series…". Likely https://www.passionateinmarketing.com/?p=422429 | A 2021 ShortsTV Halloween campaign: a zombie outbreak told across 14 short videos (attribution uncertain) |
| S49 | https://outlierkit.com/channel/zarigueyazonacero | Spanish urban prepping and DIY survival channel |
| S50 | https://outlierkit.com/channel/extinctzoo | Prehistory told through a survival-horror lens |
| S51 | https://www.filmstarts.de/nachrichten/1000206542.html | *Zombies im Zoo* animated film trailer |
| S52 | https://rephonic.com/podcasts/100-ways-to-survive-a-zombie-apocalypse | Podcast "100 ways to survive a zombie apocalypse" |
| S53 | https://pro.imdb.com/title/tt5844556 | 2014 animated short "What to do in case of a Zombie Apocalypse" |
| S54 | https://thetvdb.com/series/life-noggin/episodes/9343491 | Life Noggin "Zombie Cells" episode (Sep 9, 2022) |
| S55 | https://www.dreadcentral.com/news/30460/the-zombie-apocalypse-now-in-hilarious-cartoon-variety/ | *Zombie Murder Explosion Die!* (Machinima cartoon) |
| S56 | https://thetvdb.com/series/board-af/episodes/11232560 | "Surviving the Zombie Apocalypse" (2016) |
| S57 | https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/289331/como-sobrevivir-a-un-apocalipsis-zombi.pdf | Spanish-language zombie survival book |
| S58 | https://craigdilouie.com/my-top-10-list-of-apocalyptic-short-films/ ; https://www.shortoftheweek.com/news/9-great-zombie-shorts/ | Curated apocalyptic and zombie short-film lists |
| Sib-A | `A_reference_account.md` (sibling agent, same date) | TikTok discover topic pages on the farmer-zombie trope; Reddit blocked for WebSearch |

---

## F. Access log (2026-10-14)

### F.1 WebSearch queries (22 executed, then budget exhausted)

| # | Query | Mode | Useful output |
|---|---|---|---|
| 1 | "If the zombie apocalypse starts" shorts animated channel | std | Puzzle Hunters; *Zombie Murder Explosion Die!*; Disney ZOMBIES shorts |
| 2 | zombie apocalypse animation YouTube shorts channel survival story "you" farm | std | StickTheMan "Basics In Survival"; Final Refuge; Infection Zero; FK Films |
| 3 | Zack D. Films YouTube Shorts subscribers 3D animated "what happens if" survival | std | S1, S2 |
| 4 | The Infographics Show subscribers 2026 zombie apocalypse episode views | std | S7, S8, S11, S12 |
| 5 | animated zombie apocalypse shorts channel millions of views 2025 TikTok series… | std | S46, S47 |
| 6 | outlierkit channel zombie apocalypse survival animation shorts | std | S24, S49, S50, S45 |
| 7 | "zombie apocalypse" animated shorts channel "subscribers" survival scenarios "what would you do" | ext | S30, S31, S32, S33 |
| 8 | outlierkit Zack D. Films top videos views survival "what happens if" | std | S6 |
| 9 | site:youtube.com "zombie apocalypse" shorts animation "if you" survive | std | S53, S56, S42 |
| 10 | TED-Ed "zombie bridge riddle" views | std | S15, S16, S17 |
| 11 | WhatIf channel "What If Zombies" video views subscribers Underknown | std | S20–S23 |
| 12 | "zombie apocalypse" "day 1" animated series shorts youtube channel 2026 | std | S43, S48 |
| 13 | GameToons zombie apocalypse animation shorts subscribers views | std | S25, S26 |
| 14 | Life Noggin "zombie apocalypse" video views | std | S54 |
| 15 | tiktok discover "zombie apocalypse animation" survival story | std | S41; hoax items |
| 16 | tiktok discover "if the zombie apocalypse happened" animation where would you go | std | S38, S40, S29 |
| 17 | vidiq youtube-stats The Infographics Show subscribers views | std | S9 |
| 18 | "Infographics Show" "YOU vs 1000 ZOMBIES" OR "Could You Survive A Zombie Attack" views | std | No views; confirmed S11, S12 |
| 19 | TED-Ed "zombie" riddle videos list "Can you solve the" zombie island cure views | std | S18, S19 |
| 20 | AsapSCIENCE OR "Alternate History Hub" zombie apocalypse video views how would it spread | std | S34–S39 |
| 21 | speakrj "The Infographics Show" top YouTube videos media-stats | std | S10, S13, S14 |
| 22 | speakrj Zack D Films media-stats recent videos views list | ext | S3, S4, S5 |
| 23–25 | Zack D. Films survival-video queries; Infographics youtubers.me query | — | **Refused: "web search budget is used up (limit: 200 WebSearch calls per turn, shared by every agent in it)"** |

### F.2 WebFetch attempts

| URL | Result |
|---|---|
| https://www.youtube.com/@TheInfographicsShow/shorts | `getaddrinfo ENOTFOUND www.youtube.com` |
| https://socialblade.com/youtube/handle/theinfographicsshow | `ENOTFOUND socialblade.com` |
| https://www.reddit.com/r/zombies/top/?t=all | "unable to fetch from www.reddit.com" |
| https://old.reddit.com/r/zombies/top/?t=all | "unable to fetch from old.reddit.com" |
| https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=how+to+survive+a+zombie | `ENOTFOUND` |
| https://en.wikipedia.org/wiki/The_Infographics_Show | `ENOTFOUND` (control) |
| https://vling.net/en/channel/UCyo4F-KFqdLA1sOw7iGDrBw/channel-info | `ENOTFOUND` |
| https://example.com/ | `ENOTFOUND` (control). This confirms WebFetch was non-functional for all hosts |

### F.3 curl through the agent proxy

youtube.com, socialblade.com, reddit.com and en.wikipedia.org all failed with `CONNECT tunnel failed, response 403` (egress policy denial). Per the proxy README, these were not retried or routed around.

---

## G. Limitations

1. **No primary platform data.** No YouTube, TikTok, Instagram or Reddit page was opened. All view and subscriber numbers come from search-tool summaries of third-party tracker pages, whose dates and methods differ. Where trackers disagree (Zack D. Films' "top video" vs per-video tables), both figures are shown.
2. **Medians not computable.** "Vs typical" uses lifetime mean views per upload where totals were available (Zack D. Films, The Infographics Show). It could not be computed for anyone else.
3. **Search budget exhausted early** (22 queries, shared cap). Not done as a result:
   - Reddit thread engagement
   - Google Trends seasonality
   - Autocomplete phrasing
   - Bright Side, Kurzgesagt and prepper-channel stats
   - TikTok creator identification
   - Per-video views for zombie-specific titles
   - Verbatim viewer comments
4. **[BK] items are unverified.** They include release dates, disaster events, NFPA/CDC/NOAA claims, and the location-debate staples. They are hypotheses and pointers only.
5. **Quotes** in sections B and D are as rendered in search-result summaries. Exact page wording and attribution could not be confirmed (attribution is explicitly uncertain for S39 and S48).
6. **Section C evidence is thin for most premises.** About 20 of 84 premises have any retrieved evidence. The rest rest on background knowledge or judgment, and are labeled that way.
7. **Sensitive real events.** Premises on crowd crushes, floods and recent disasters touch real deaths. Avoid naming or depicting specific recent tragedies without care (judgment).

### Recommended manual checks (about 30 minutes in a normal browser)

1. Google Trends for "zombie" (5 years, US, plus YouTube Search), and for "earthquake", "power outage" and "blizzard".
2. YouTube autocomplete for the phrasings in B.1.
3. Social Blade or vidIQ for Bright Side, Kurzgesagt, TED-Ed and ErrorMotion. Sort each channel's videos by "Popular" and note the zombie and survival titles' views against the channel median of its last 30 uploads.
4. Reddit search for "zombie apocalypse plan", "best place zombie apocalypse" and "Costco zombie". Record the top threads' upvotes and comment counts.
5. The top 100 comments on 5 comparable Shorts, to replace section D.2's hypotheses with real quotes.
