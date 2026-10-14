# A. Reference account research: Stickocalypse (`stickocalypse_shorts`)

- Target: https://www.instagram.com/stickocalypse_shorts/
- Research and access date for every item below: **2026-10-14**
- Tools used: WebSearch (standard and extended modes), WebFetch, `curl` through the container's agent proxy.
- **Headline result:** No public information about the target account could be retrieved or found. The account's own pages could not be reached by any method. No search engine result referenced the handle, the "Stickocalypse" account name in a social-media context, or the series "The Last Farm" with characters Eli, Mara or Rusty. Every metric field below is either **NOT ACCESSIBLE** (could not be reached) or **NOT FOUND** (reachable searches returned nothing). None of them should be read as zero.

---

## 1. Access log

### 1a. Direct page fetches

| # | Method | URL | Result |
|---|---|---|---|
| 1 | WebFetch | https://www.instagram.com/stickocalypse_shorts/ | **NOT ACCESSIBLE**: `getaddrinfo ENOTFOUND www.instagram.com` |
| 2 | WebFetch | https://www.youtube.com/@stickocalypse | **NOT ACCESSIBLE**: `getaddrinfo ENOTFOUND www.youtube.com` |
| 3 | WebFetch | https://www.tiktok.com/@stickocalypse_shorts | **NOT ACCESSIBLE**: `getaddrinfo ENOTFOUND www.tiktok.com` |
| 4 | WebFetch | https://socialblade.com/instagram/user/stickocalypse_shorts | **NOT ACCESSIBLE**: `getaddrinfo ENOTFOUND socialblade.com` |
| 5 | WebFetch | https://www.picuki.com/profile/stickocalypse_shorts | **NOT ACCESSIBLE**: `getaddrinfo ENOTFOUND www.picuki.com` |
| 6 | WebFetch | https://imginn.com/stickocalypse_shorts/ | **NOT ACCESSIBLE**: `getaddrinfo ENOTFOUND imginn.com` |
| 7 | WebFetch (control test) | https://en.wikipedia.org/wiki/YouTube_Shorts | **FAILED**: `getaddrinfo ENOTFOUND en.wikipedia.org` |
| 8 | WebFetch (control test) | https://example.com/ | **FAILED**: `getaddrinfo ENOTFOUND example.com` |
| 9 | curl via proxy | https://www.instagram.com/stickocalypse_shorts/ | **NOT ACCESSIBLE**: `curl: (56) CONNECT tunnel failed, response 403` (egress policy denial) |
| 10 | curl via proxy | https://www.youtube.com/@stickocalypse | **NOT ACCESSIBLE**: `CONNECT tunnel failed, response 403` |
| 11 | curl via proxy | https://www.tiktok.com/@stickocalypse_shorts | **NOT ACCESSIBLE**: `CONNECT tunnel failed, response 403` |
| 12 | curl via proxy | https://socialblade.com/instagram/user/stickocalypse_shorts | **NOT ACCESSIBLE**: `CONNECT tunnel failed, response 403` |
| 13 | curl via proxy | https://www.picuki.com/profile/stickocalypse_shorts | **NOT ACCESSIBLE**: `CONNECT tunnel failed, response 403` |
| 14 | curl via proxy | https://imginn.com/stickocalypse_shorts/ | **NOT ACCESSIBLE**: `CONNECT tunnel failed, response 403` |

Interpretation:
- **WebFetch does not work at all in this session.** It failed DNS resolution for every host tried, including the neutral control hosts wikipedia.org and example.com. The failure is therefore a tool or environment problem, not a block specific to Instagram or YouTube.
- **curl** reaches the proxy, but the egress policy refuses CONNECT (403) to instagram.com, youtube.com, tiktok.com, socialblade.com, picuki.com and imginn.com. Per the proxy README, 403s are policy denials. They were reported here and not retried or routed around.
- Because of this, **no page from any platform was actually loaded.** Everything in this report comes from search-engine result titles and snippets only.

### 1b. WebSearch queries (all on 2026-10-14)

| # | Query | Domain filter | Result |
|---|---|---|---|
| S1 | `stickocalypse_shorts instagram` | none | NOT FOUND: unrelated results (Wikipedia "YouTube Shorts", NPR "Stick Nation"/@officialstickreviews articles) |
| S2 | `Stickocalypse youtube shorts` | none | NOT FOUND: unrelated (Wikipedia, eklipse.gg blog, thisiscolossal "Stickmatch", lilys.ai article on "AI apocalypse of YouTube Shorts", vling.net channel UCXo83oYpiqYoGasp7RKt3qg described as "Stick & Paw Stories") |
| S3 | `"stickocalypse"` (extended) | none | Only hits are an **unrelated 2014-era Flash browser game "Stickocalypse"** (stickmangames.altervista.org, stickmangames247.com, gamekb.com, nicholasjdamato.com portfolio). No social account found. |
| S4 | `"The Last Farm" zombie animation shorts Eli Rusty Mara` | none | NOT FOUND: unrelated (The Last Farmer Steam game, Icelandic live-action short "The Last Farm", "Malas Hierbas" student short) |
| S5 | `stickocalypse instagram animated survival stories zombie` (extended) | none | NOT FOUND: genre-adjacent only (TikTok discover "zombie-apocalypse-animation", YouTube @BeanieSurvives1, the Flash game) |
| S6 | `"stickocalypse_shorts"` (extended) | none | NOT FOUND: Flash game, StickDeath, Stickpage, unrelated YouTube playlists |
| S7 | `stickocalypse` | instagram.com | **No links returned** |
| S8 | `stickocalypse` | youtube.com | NOT FOUND: unrelated stick channels (@Stickylollies, @StickoExplains, StickVerse, Stickology) and a video titled "STICK apocalypse" (https://www.youtube.com/watch?v=IfPmNV5mEDM). The snippet showed "posted 101 days ago". The uploader was not shown, and **nothing links this video to Stickocalypse**. |
| S9 | `stickocalypse` | tiktok.com | NOT FOUND: unrelated (Stickfellas, Sticky Loco, @officialstickreviews) |
| S10 | `"The Last Farm" "Part 2" "Something is in the barn"` (extended) | none | NOT FOUND: results about *The Last of Us Part II* "The Farm" chapter |
| S11 | `"the last farm" zombie apocalypse farm shorts part 3 "survive the night"` | none | NOT FOUND: The Last Farmer game, unrelated shorts |
| S12 | `"STICK apocalypse" youtube IfPmNV5mEDM` | none | Could not identify the uploader or content of IfPmNV5mEDM |
| S13 | `"@stickocalypse"` (extended) | none | NOT FOUND: only the Flash game |
| S14 | `Stickocalypse facebook animated zombie survival shorts page` | none | NOT FOUND |
| S15 | `"follow to survive" "the last farm" animation` | none | NOT FOUND |
| S16 | `stickocalypse` | reddit.com | **NOT ACCESSIBLE**: `API Error: 400 The following domains are not accessible to our user agent: ['reddit.com']` |
| S17 | `stickocalypse` | x.com, twitter.com, threads.net, threads.com, facebook.com | **NOT ACCESSIBLE** for threads.net: `API Error: 400 ... not accessible to our user agent: ['threads.net']` (whole query rejected) |
| S18 | `stickocalypse` | x.com, twitter.com, facebook.com | NOT FOUND: unrelated (@stickchronicles, Stick CMF, Stickopolis, @stickpagenews, stickK) |
| S19 | `stickocalypse_shorts` | socialblade.com, hypeauditor.com, picuki.com, imginn.com, dumpor.com, picnob.com, inflact.com, greatfon.com, pixwox.com, storynavigation.com | NOT FOUND: only two unrelated Social Blade pages (YouTube channel UCfmFQaCPo3uZeby48CaEgLQ "Shorts"/@premaakter5304, and @shorts) |
| S20 | `stickocalypse shorts survival animation reels "end of the world"` (extended) | none | NOT FOUND: genre-adjacent only |
| S21 | `"Stickocalypse" animation channel 2026` (extended) | none | NOT FOUND |
| S22 | `"stickocalypseshorts" OR "stickocalypse.shorts" OR "#stickocalypse"` (extended) | none | NOT FOUND: only the Flash game (credited to Nicholas D'amato) |
| S23 | `zombie apocalypse farm animated short farmer Eli dog Rusty "someone was already inside the fence"` (extended) | none | NOT FOUND: unrelated ("Steadfast Stanley" CalArts short, TikTok discover pages on farmer/zombie POV stories) |
| S24 | `"The Last Farm" zombie shorts youtube "part 1"` | youtube.com, tiktok.com, instagram.com, facebook.com | NOT FOUND: one unrelated hit, "The Last Farmer - PART 1" (https://www.youtube.com/watch?v=jJEKYO6GnyA), described as Hindi-language gameplay by channel "Nade Flick" |
| S25 | `"You Are A Farmer Trapped in A Zombie Apocalypse" tiktok animation part 3` (extended) | none | Unrelated: TikTok discover page tied to @secondateupdate8 / "HoneyReels" drama app, not to Stickocalypse |
| S26 | `"Pov you're a farmer" barn zombie outbreak animation tiktok creator` | none | NOT FOUND |
| S27 | `"Stickocalypse Shorts"` (extended) | none | NOT FOUND |
| S28 | `"stick-ocalypse" OR "stick o calypse" animated zombie shorts` | none | NOT FOUND |
| S29 | `"stickocalypse" instagram reels` | instagram.com, picuki.com, imginn.com, dumpor.com, picnob.com, pixwox.com, inflact.com | NOT FOUND: only generic Instagram and Inflact help pages |
| S30 | `"STICK apocalypse" youtube video stick figure animation` | youtube.com | NOT FOUND: unrelated stick-figure apocalypse videos |
| S31 | `stickocalypse` | socialblade.com, hypeauditor.com, playboard.co, vling.net, noxinfluencer.com, viewstats.com, speakrj.com, socialcounts.org | NOT FOUND: unrelated "Stick"/"Sticky" channel stat pages |
| S32 | `"the last farm" part 2 barn zombie shorts animation generator infected west fence` | none | NOT FOUND |
| S33 | `"Survive the night" "the finale" "the last farm" part 3` | youtube.com, tiktok.com, instagram.com, facebook.com | NOT FOUND: unrelated Roblox and game "Survive the Night(s)" videos |

---

## 2. Profile facts (Instagram)

Source: https://www.instagram.com/stickocalypse_shorts/ (access attempted 2026-10-14)

| Field | Value |
|---|---|
| Display name | **NOT ACCESSIBLE** (WebFetch DNS failure; curl 403 policy denial) |
| Bio text | **NOT ACCESSIBLE**. The brief's description ("animated survival stories, zombie scenarios and end-of-the-world chaos") could **not** be verified. |
| Follower count | **NOT ACCESSIBLE** |
| Following count | **NOT ACCESSIBLE** |
| Post count | **NOT ACCESSIBLE** |
| Link in bio | **NOT ACCESSIBLE** |
| Account creation date ("About this account") | **NOT ACCESSIBLE**. This field normally needs a logged-in app view in any case. |
| Linked YouTube / TikTok / Facebook | **NOT ACCESSIBLE** from the profile. **NOT FOUND** through search (S1–S33). |

Search engines also returned **no indexed snippet** of the profile (S7: zero results on instagram.com for "stickocalypse"). The account may be too new or too small to be indexed, or not indexed at all. No conclusion about its size can be drawn.

---

## 3. Linked channels

| Platform | Candidate handle(s) tried | Status | Subscribers/followers | # videos | Creation date |
|---|---|---|---|---|---|
| YouTube | @stickocalypse (direct); search "stickocalypse", "Stickocalypse Shorts", "@stickocalypse" | Direct page **NOT ACCESSIBLE**. Search: **NOT FOUND** (no channel by that name surfaced) | NOT ACCESSIBLE / NOT FOUND | NOT ACCESSIBLE / NOT FOUND | NOT ACCESSIBLE / NOT FOUND |
| TikTok | @stickocalypse_shorts (direct); search "stickocalypse" | Direct page **NOT ACCESSIBLE**. Search: **NOT FOUND** | — | — | — |
| Facebook | search only | **NOT FOUND** | — | — | — |
| X / Twitter | search only | **NOT FOUND** | — | — | — |
| Threads | search only | **NOT ACCESSIBLE** (WebSearch rejected threads.net) | — | — | — |

**Name collision to be aware of:** "Stickocalypse" is also the title of an older, unrelated stick-figure zombie **Flash browser game** (listing dated December 2014 on stickmangames.altervista.org; developer credited as Nicholas D'amato on nicholasjdamato.com/portfolio and gamekb.com). Nothing found connects that game to the Instagram account. The name collision is the main reason searches for "Stickocalypse" return no social-media results.
- http://stickmangames.altervista.org/blog/en/archives/stickocalypse-2 (search snippet only, 2026-10-14)
- http://www.stickmangames247.com/game/stickocalypse.html (search snippet only, 2026-10-14)
- https://www.gamekb.com/games/1730386-stickocalypse (search snippet only, 2026-10-14)
- https://www.nicholasjdamato.com/portfolio/ (search snippet only, 2026-10-14)

---

## 4. Video catalog

No video or reel attributable to `stickocalypse_shorts` or to any Stickocalypse-branded channel could be found or opened.

| ID | Platform | URL | Title / first line | Date | Views | Likes | Comments | Source / access date |
|---|---|---|---|---|---|---|---|---|
| V1 | Instagram (local copy only) | NOT FOUND online | "THE LAST FARM" Part 1 (per brief; end card "PART 2 – SOMETHING IS IN THE BARN – FOLLOW TO SURVIVE DAY 1") | NOT ACCESSIBLE | NOT ACCESSIBLE | NOT ACCESSIBLE | NOT ACCESSIBLE | Local file described in brief; no online match in S4, S10, S15, S23, S24 (2026-10-14) |
| V2 | Instagram (local copy only) | NOT FOUND online | "THE LAST FARM" Part 2 (per brief; end card "THE LAST FARM PART 3 SURVIVE THE NIGHT THE FINALE") | NOT ACCESSIBLE | NOT ACCESSIBLE | NOT ACCESSIBLE | NOT ACCESSIBLE | Local file described in brief; no online match in S10, S32 (2026-10-14) |
| V3 | unknown | **NOT FOUND** | "THE LAST FARM" Part 3 / "Survive the Night" / finale | NOT FOUND | — | — | — | S11, S33 (2026-10-14). Whether Part 3 has been published is unknown. |
| — | Other series by this creator | **NOT FOUND** | — | — | — | — | — | All searches (2026-10-14) |

**Excluded results.** These are not attributed to the target and are listed only so nobody mistakes them for it:
- https://www.youtube.com/watch?v=IfPmNV5mEDM, "STICK apocalypse" (search snippet: "posted 101 days ago"). Uploader unknown. No evidence it is Stickocalypse.
- https://www.youtube.com/watch?v=jJEKYO6GnyA, "The Last Farmer - PART 1". Channel "Nade Flick", Hindi gameplay. Unrelated.
- https://www.tiktok.com/discover/you-are-a-farmer-trapped-in-a-zombie-apocalypse-pt3. TikTok topic page tied by the search snippet to @secondateupdate8 / "HoneyReels". Unrelated short-drama content, though it shows the "farmer in a zombie apocalypse, part N" premise is a recurring short-form trope.
- https://www.tiktok.com/discover/pov-youre-a-farmer-in-a-barn-during-a-zombie-outbreak and https://www.tiktok.com/discover/farmer-part-3-story-zombie-in-english. Topic pages only. Creators were not identified and the pages could not be opened.

---

## 5. Comments

**NOT ACCESSIBLE / NOT FOUND.** No viewer comments on any Stickocalypse video could be retrieved:
- Instagram reel pages could not be loaded (WebFetch DNS failure; curl 403). Instagram comments also generally need a login.
- No YouTube or TikTok uploads by the creator were found, so there was nothing to pull comments from.
- Reddit is not reachable through WebSearch (400, domain not accessible to user agent).

No comments are quoted here, and none have been paraphrased or invented. No evidence was found either way on viewer attachment to Eli, Mara or Rusty, on confusion, on corrections, or on requests for Part 3.

---

## 6. Third-party data

All of the following are **estimates by design** where they exist, and none were found for this account.

| Source type | Result |
|---|---|
| Social Blade (Instagram / YouTube) | Direct URL **NOT ACCESSIBLE** (WebFetch DNS; curl 403). Domain-filtered search: **NOT FOUND** (only unrelated channels) |
| HypeAuditor, Playboard, vling, NoxInfluencer, ViewStats, SocialCounts, speakrj | Domain-filtered search: **NOT FOUND** |
| Picuki / Imginn / Dumpor / Picnob / Pixwox / Inflact / Greatfon / StoryNavigation (Instagram viewers) | Picuki and Imginn direct URLs **NOT ACCESSIBLE**. Domain-filtered search: **NOT FOUND** |
| Reddit | **NOT ACCESSIBLE** (WebSearch 400 for reddit.com) |
| News / blogs | **NOT FOUND** |

---

## 7. Limitations

1. **No page was actually loaded.** WebFetch failed DNS for every host (including example.com and wikipedia.org), and the egress proxy refuses CONNECT (403) to Instagram, YouTube, TikTok, Social Blade, Picuki and Imginn. All findings come from search-result titles and snippets.
2. **Search coverage of Instagram is thin.** A domain-filtered search on instagram.com returned zero results for "stickocalypse". "Not found in search" does **not** mean the account lacks followers, posts or linked channels. It means the search index exposes none of it.
3. **Name collision.** The 2014-era "Stickocalypse" Flash game dominates results for the name and may hide a small social account.
4. **Login walls.** Even with network access, Instagram follower and comment data and the "About this account" creation date usually need a logged-in session. That would need to be gathered manually.
5. **Reddit and Threads** could not be searched (WebSearch domain restriction).
6. **Unverified brief claims.** The bio description in the brief ("animated survival stories, zombie scenarios and end-of-the-world chaos") and the existence or publication of "The Last Farm" Part 3 remain **unverified**.

**Recommended manual follow-up.** Someone with a logged-in browser should open the Instagram profile and record its display name, bio, counts, link-in-bio and "About this account" date. They should also open each "The Last Farm" reel and copy its view, like and comment counts and the top comments, then check whether the link-in-bio points to a YouTube or TikTok channel.
