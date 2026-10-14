# B. YouTube platform requirements for original 2D-animated narrative Shorts (45–90 s)

> **Update 2026-10-14 (later the same day):** many items marked UNVERIFIED or NOT VERIFIED below were later checked with official-domain searches. See `../../07_Survival_Logic_and_Facts/verification_results.csv` and `../../23_Limitations_and_Next_Actions.md` §2. This appendix is kept as the original research record.

Access date for every row: **2026-10-14**.

## READ FIRST: how this evidence was collected (and its limits)

- **No page could be fetched directly.** `WebFetch` failed for every host with `getaddrinfo ENOTFOUND` (support.google.com, blog.youtube, support-google-com.translate.goog, and also third-party sites). A direct `curl` to support.google.com was refused by the egress proxy (`CONNECT tunnel failed, response 403`, "connect_rejected"). web.archive.org could not be fetched either.
- **All evidence below comes from WebSearch result excerpts.** The search tool returns a summary plus fragments of page text. The text in the "Exact quote" column is the wording the search tool presented as quoted from the page. It was **not checked against the live page**, may be truncated, and may differ from the current text. Rows where the tool only paraphrased are marked "(paraphrase from search summary)".
- **The search budget ran out partway through.** The 200-search limit per turn is shared with other agents. Topics **9, 11 and 12**, and parts of **5** (most analytics metric definitions) and **6** (AI voices, Shorts revenue sharing and music), could **not** be researched. Those sections list what to verify and do not make claims. A follow-up run with search budget (or with access to support.google.com) is needed.
- **Official? column.** "Yes": the URL is a YouTube or Google property (support.google.com, blog.youtube, business.google.com). "Yes (via secondary)": official wording that only reached me through a third-party site quoting it. "No": a third-party source.

---

## 1. Shorts eligibility (length, aspect ratio, identification)

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| A Short is a square or vertical video up to 3 minutes long, uploaded on or after 15 Oct 2024 | "Videos uploaded on or after October 15, 2024 with a square or vertical aspect ratio, up to three minutes long, are categorized as Shorts." | https://support.google.com/youtube/answer/15424877?hl=en ("Understand three-minute YouTube Shorts") | 2026-10-14 | Yes | Two separate searches returned this wording, but I could not fetch the page. Both conditions apply: the length (3 min or less) **and** the shape (square or vertical). |
| Videos uploaded before 15 Oct 2024 keep the old classification | "Uploads from before 15 October 2024 stay classified as long-form videos." (paraphrase from search summary) | https://support.google.com/youtube/answer/15424877?hl=en | 2026-10-14 | Yes | Not relevant to new uploads. |
| You can upload 3-minute Shorts from the app and from Studio | "Three-minute Shorts can be uploaded through the YouTube app and YouTube Studio." (paraphrase from search summary) | https://support.google.com/youtube/answer/15424877?hl=en | 2026-10-14 | Yes | — |
| Official Artist Channels have a different cutoff date (8 Dec 2025) | (no verbatim quote returned) | https://support.google.com/youtube/answer/15424877?hl=en | 2026-10-14 | Yes | **Conflict:** one search summary said this Dec 8, 2025 cohort applies to "standard channels" and is monetized under the creator's agreement rather than Shorts revenue sharing. Another summary tied it only to Official Artist Channels. The OAC reading seems more likely, but this needs checking on the live page. It probably does not affect a standard fiction channel. |
| Landscape videos are long-form, however short they are | "upload something 16:9 and it is a regular video no matter how brief." | (third-party guide in search results for the Shorts-length query; site not individually identified) | 2026-10-14 | No | Follows from the official square-or-vertical rule. |
| The #Shorts tag is not needed to classify a video as a Short | "YouTube does not need it to identify an eligible Short." | (third-party hashtag guide; e.g. https://taskant.com/youtube-hashtags-guide/) | 2026-10-14 | No | No official statement found within the search budget. |
| Rights-holder note on 3-minute Shorts | Three-minute Shorts uploaded before Oct 15, 2024 "don't appear under the Shorts filter in Studio Content Manager" (paraphrase from search summary) | https://support.google.com/youtube/answer/13053317?hl=en ("Manage Shorts as a rights holder") | 2026-10-14 | Yes | Only an excerpt was available. |
| Recommended size is 1080×1920 (9:16) | (no official quote) | e.g. https://postfa.st/sizes/youtube/shorts | 2026-10-14 | No | Standard industry advice. The official Help text I could see says only "square or vertical". |

## 2. Recommended upload encoding settings

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| Container: MP4, with the moov atom at the front | "Container: MP4 ..." (moov atom at the front of the file: paraphrase from search summary) | https://support.google.com/youtube/answer/1722171?hl=en | 2026-10-14 | Yes | This is the "fast start" flag, e.g. `-movflags +faststart` in ffmpeg. |
| Audio codec: AAC-LC, Opus or Eclipsa Audio | "Audio codec: AAC-LC or Opus or Eclipsa Audio" | https://support.google.com/youtube/answer/1722171?hl=en | 2026-10-14 | Yes | Fragment from search excerpt. |
| Audio sample rate: 48 kHz | "Sample rate: 48kHz" | https://support.google.com/youtube/answer/1722171?hl=en | 2026-10-14 | Yes | Fragment from search excerpt. |
| Frame rate: keep the native rate (24/25/30/48/50/60) and deinterlace first | "Content should be encoded and uploaded in the same frame rate it was recorded. Common frame rates include: 24, 25, 30, 48, 50, 60 frames per second" | https://support.google.com/youtube/answer/1722171?hl=en | 2026-10-14 | Yes | For animation, render and export at the project frame rate (e.g. 24 or 30) and do not convert it. |
| Video codec: H.264 High Profile, CABAC, 2 consecutive B-frames, closed GOP, variable bitrate | "Video codec: H.264 ... High Profile ... 2 consecutive B frames ... Closed GOP" | https://support.google.com/youtube/answer/1722171?hl=en | 2026-10-14 | Yes | CABAC and VBR came from the search summary. |
| No bitrate limit is required; the page gives recommended reference values | "no bitrate limit is required, although it gives recommended values for reference" | (summary of the official page as relayed by a third-party; e.g. https://swarmify.com/blog/what-you-need-to-know-about-the-video-bitrate/) | 2026-10-14 | Yes (via secondary) | — |
| SDR 1080p bitrates: 8 Mbps at 24–30 fps, 12 Mbps at 48–60 fps (4K: 35–45 / 53–68 Mbps) | "1080p 8 Mbps, 12 Mbps" | Third-party pages citing Google (e.g. https://swarmify.com/blog/what-you-need-to-know-about-the-video-bitrate/, https://josephnilo.com/blog/best-target-bitrate-for-youtube/) | 2026-10-14 | No (cites official) | I could not see the official SDR table. The excerpt I could see was the HDR table. |
| Audio bitrate (e.g. stereo 384 kbps) | — | — | 2026-10-14 | **Not verified** | The search tool explicitly could not confirm 384 kbps stereo from the official page. Check it on the page. |
| Colour space / BT.709, resolution table | — | https://support.google.com/youtube/answer/1722171?hl=en | 2026-10-14 | **Not verified** | Not returned by search. |

## 3. Loudness normalization

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| **I found no official YouTube Help page that documents loudness normalization or a LUFS target** | — | — | 2026-10-14 | — | The search returned only third-party pages. I could not search further within the budget, so this is "not found", not "does not exist". |
| −14 LUFS is the commonly cited YouTube reference level | "as of 2026, YouTube uses -14 LUFS as its target loudness level" / "-14 LUFS ... a useful starting point, but it is not a universal rule or a guarantee" | Third-party (e.g. https://www.criticallisteninglab.com/en/learn/loudness/youtube, https://audioforgepro.com/blog/youtube-lufs-normalization-guide) | 2026-10-14 | **No** | Community consensus that comes from observed behaviour. One source says it was lowered from −13 LUFS. |
| "Stats for nerds" shows the playback gain adjustment ("Volume / Normalized", "content loudness") | "a reading of 6dB means your video is 6dB louder than YouTube's Distribution Loudness level" | https://productionadvice.co.uk/stats-for-nerds/ | 2026-10-14 | No | This is a feature of the YouTube player, but my source for how to read it is a third party. |
| YouTube turns loud content down but reportedly does not raise quiet content | (paraphrase from search summary: "YouTube doesn't turn up quieter videos") | Third-party loudness guides (see above) | 2026-10-14 | No | — |
| The displayed values are not publicly specified | "not documented in a public spec" (paraphrase from search summary) | https://github.com/yuliskov/SmartTube/issues/5653 | 2026-10-14 | No | — |

## 4. Titles, descriptions, hashtags, Shorts thumbnails

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| Title limit: 100 characters | "YouTube caps video titles at 100 characters, but search results and suggested-video cards truncate around 60-70" | Third-party (e.g. https://www.limitora.com/blog/youtube-character-limits-2026, https://howmanywords.app/blog/youtube-character-limits) | 2026-10-14 | No | No official Help page came up. The figure is widely consistent. Truncation lengths are estimates. |
| Description limit: 5,000 characters | "A YouTube video description can contain up to 5,000 characters." | Third-party (as above) | 2026-10-14 | No | One outlier source says 1,000, which is outdated or refers to the channel description. |
| More than 60 hashtags: every hashtag on the video is ignored | "If a video or playlist has more than 60 hashtags, we'll ignore each hashtag on that content. Over-tagging may result in the removal of your video from your uploads or from search." | Help text quoted by third-party (e.g. https://taskant.com/youtube-hashtags-guide/); official page is the YouTube Help hashtag article (support.google.com/youtube/answer/6390658, URL from memory, not fetched) | 2026-10-14 | Yes (via secondary) | The count reportedly covers the title and description together ("This includes hashtags in both the title and description combined", third-party). |
| Up to 3 description hashtags appear near the title | "up to three from the description appear beside the title" | Third-party (as above) | 2026-10-14 | No | — |
| The "15 hashtag" cap is not on YouTube's pages | "The 15-hashtag cap that circulates on other sites is not on any YouTube page read for this table." | Third-party (hashtag guide in search results) | 2026-10-14 | No | — |
| Custom thumbnails for Shorts: rolled out from July 2026 to YPP creators, expanding over time | (paraphrase from search summary) "YouTube Partner Program creators can start uploading custom thumbnails for Shorts", with expansion "to more creators over time" | https://blog.youtube/news-and-events/youtube-studio-custom-thumbnail-updates/ | 2026-10-14 | Yes | Neal Mohan announced it on 24 Jul 2026 ("one of the most requested features from @YouTubeCreators", via https://www.tubefilter.com/2026/07/24/youtube-shorts-custom-thumbnails-neal-mohan-feature-update/). Some outlets date the rollout to 25 Jul 2026. |
| Desktop upload only, no A/B testing for Shorts thumbnails; on desktop you can pick from 3 suggested frames | "Access begins with Partner Program channels... There is no A/B testing for Shorts thumbnails. And the upload path is desktop only." / "Creators will also be able to choose one of three 'suggested thumbnail frames'" | https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/ ; https://www.tubefilter.com/2026/07/24/youtube-shorts-custom-thumbnails-neal-mohan-feature-update/ | 2026-10-14 | No | Sources disagree on whether it is strictly desktop-only. Before YPP, the fallback is choosing a frame in the mobile app. |
| Choosing a frame on mobile still works | "Picking a completely custom frame from the video itself remains a mobile function." | https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/ | 2026-10-14 | No | — |
| Shorts thumbnails may render at roughly 3:2 on some surfaces | "A Shorts thumbnail renders at roughly 3:2, not at the 9:16 of the video." | https://www.relevantaudience.com/social-media-marketing/youtube-shorts-custom-thumbnails-no-ab-testing/ | 2026-10-14 | No | Not confirmed officially. Keep key art centred so it survives crops. |

## 5. View counting and Shorts analytics

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| From 31 Mar 2025, a Shorts view counts each time the Short starts or replays, with no minimum watch time | (paraphrase from search summary) a view "registers each time a Short starts or replays, with no minimum watch time" | Third-party: https://ppc.land/youtube-changes-how-shorts-views-are-counted-from-march-31/ , https://vidiq.com/blog/post/youtube-view-count-update/ | 2026-10-14 | No | No official Help text came up for the 2025 change. Many outlets agree on it. |
| From 24 Aug 2026, public views on **all** formats count from the first frame. The old definition is now "engaged views" | "An engaged view is defined as clicking to watch or watching past the initial seconds, and this has been how creators qualify to earn, as long as the content is public." | https://blog.youtube/inside-youtube/engaged-views-youtube-explained/ (YouTube Blog; reported date 19 Aug 2026) | 2026-10-14 | Yes | Third parties report a Help Community announcement on 17 Aug 2026 titled "An update to how we count public views across YouTube" (https://www.newsshooter.com/2026/08/17/..., https://routenote.com/blog/youtube-view-count-change/). It was not retroactive. |
| Definition of engaged views in Studio | "How many times viewers stayed to watch past the initial seconds, not including any loops." | Help/Studio text quoted by third-party: https://adaptlypost.com/blog/youtube-engaged-views | 2026-10-14 | Yes (via secondary) | YouTube does not publish the number of seconds. The metric is in Analytics "Advanced Mode". |
| YPP earnings and eligibility still use engaged views | (paraphrase from search summary) "earnings and Partner Program eligibility are unaffected", and "still depend on Engaged Views" | https://vidiq.com/blog/post/youtube-view-count-update/ ; blog.youtube (as above) | 2026-10-14 | Partly | Secondary sources differ slightly in wording. |
| "Viewed vs. swiped away" (Content tab, Shorts): the share of feed impressions where viewers stayed rather than swiping away | "highlights the percentage of times that viewers viewed your Shorts versus swiped away" | Help text quoted by third-party: https://1of10.com/blog/youtube-shorts-analytics/ (and similar) | 2026-10-14 | Yes (via secondary) | One secondary source says the label is now "Stayed to watch": "The percentage of times viewers stayed to watch past the initial seconds of a Short" (https://adaptlypost.com/blog/youtube-engaged-views). YouTube publishes no "good" threshold. The "70%" figures circulating are unverified. |
| Average view duration, average percentage viewed, audience retention, shares, subscribers gained, returning/new viewers: official definitions | — | — | 2026-10-14 | **Not verified** | Search budget ran out. Verify in the YouTube Analytics Help glossary (Analytics metrics definitions) and in Studio. After 24 Aug 2026, check which view definition each ratio uses as its denominator. Secondary sources say engaged views still drive AVD and retention. |

## 6. Monetization / YPP policies

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| From 15 Jul 2025 the "repetitious content" policy was renamed "inauthentic content" and clarified to cover mass-produced or repetitive content | "We're making a minor update to our 'repetitious content' policy to better clarify that this includes content that is repetitive or mass-produced." | Official statement quoted by secondary sources (e.g. https://www.searchenginejournal.com/youtube-targets-mass-produced-content-in-monetization-update/550337/, https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/). Official home: YPP monetization policies, support.google.com/youtube/answer/1311392 (not fetched) | 2026-10-14 | Yes (via secondary) | Creator Liaison Rene Ritchie described the main change as the renaming (secondary). The policy is applied at channel level. YouTube has published no exhaustive definition of "mass-produced". |
| The reused content policy was unchanged | "no change to our reused content policy" | Same secondary sources | 2026-10-14 | Yes (via secondary) | Reused content covers other people's material without "significant original commentary or substantive modifications" (paraphrase). |
| Using AI is not itself the target; the policy targets scale and sameness | (paraphrase from search summary) "Enforcement focuses on scale and sameness, not on the tools used." | Third-party (e.g. https://www.tubebuddy.com/blog/youtube-ai-monetization-best-practices/) | 2026-10-14 | No | This is interpretation by secondary sources. |
| One source claims channel-level detection in 2026 | (paraphrase from search summary) | https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline | 2026-10-14 | No | Single source, unverified. A third-party headline also mentions "new monetization rules" in July 2026 (https://outlierkit.com/blog/youtube-updates-july-2026). Its content was not checked, so a follow-up is needed. |
| AI voices / synthetic narration guidance; Shorts revenue sharing (pool, music-licensing share) | — | — | 2026-10-14 | **Not verified** | Search budget ran out. Verify: YPP monetization policies (answer 1311392), YouTube Shorts monetization policies, and the Shorts revenue-sharing terms in the YPP terms. |

## 7. Altered or synthetic content disclosure

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| Animated or clearly unrealistic content does not need disclosure | "We're not requiring creators to disclose content that is clearly unrealistic, animated, includes special effects, or has used generative AI for production assistance." | https://blog.youtube/news-and-events/disclosing-ai-generated-content/ | 2026-10-14 | Yes | YouTube Blog, March 2024. This is the key line for stylized 2D animation. |
| Example of exempt content | "Clearly unrealistic content, such as animation or someone riding a unicorn through a fantastical world" | https://blog.youtube/news-and-events/disclosing-ai-generated-content/ | 2026-10-14 | Yes | — |
| Help page examples: beauty filters do not need disclosure; replacing a real person's face does | "Applying beauty filters" / "Digitally generating or altering content to replace the face of one individual with another's" | https://support.google.com/youtube/answer/14328491 (seen only through a translate.goog mirror excerpt) | 2026-10-14 | Yes | Truncated. I could not see the full list of what needs disclosure (realistic people, events, places) or the voice-cloning examples. Verify on the live page. |
| Production uses such as scripts, ideas and auto-captions are exempt | (paraphrase from search summary) excludes "generating scripts, content ideas, or automatic captions" | https://blog.youtube/news-and-events/disclosing-ai-generated-content/ | 2026-10-14 | Yes | — |

## 8. Violence, gore, horror, age restriction, "made for kids"

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| Fictional or animated dramatized violence is generally not removed | "Generally, we do not remove dramatized violence when the content or metadata lets us know that the content is fictional, or when it's apparent from the content itself, such as with animated content or video games." | https://support.google.com/youtube/answer/2802008?hl=en (Violent or graphic content policies) | 2026-10-14 | Yes | The search reported this under the "Age-restricted content and EDSA exceptions" section. "Not removed" does not mean "not age-restricted". |
| Animation is treated differently from live-action dramatized violence | "We make a distinction between dramatized violence featuring real human actors and content featuring animations" (truncated) | https://support.google.com/youtube/answer/2802008?hl=en | 2026-10-14 | Yes | The rest of the sentence was not returned. |
| Fiction without enough context can still violate the policy | "Dramatized or fictional footage of content prohibited by these guidelines where the viewer is not given enough context to understand that the footage is dramatized or fictional." | https://support.google.com/youtube/answer/2802008?hl=en | 2026-10-14 | Yes | Relevant to realistic "breaking news" disaster framing. |
| Age-restriction trigger: focusing only on the goriest part | (paraphrase from search summary) "violent or gory imagery, such as focusing solely on the most graphically violent part of a film or video game" | https://support.google.com/youtube/answer/2802167?hl=en (Age-restricted content) | 2026-10-14 | Yes | Age-restricted videos cannot be viewed by users under 18 or signed out, which reduces reach. |
| From 17 Nov 2025, gaming content with realistic human characters in mass violence or torture is age-restricted. Duration and prominence are weighed | (paraphrase) "realistic human characters" in "mass violence against non-combatants" or torture | News: https://www.gamespot.com/articles/youtube-is-changing-its-guidelines-for-graphic-violence-in-gaming/1100-6535801/ , https://www.ghacks.net/2025/10/30/... | 2026-10-14 | No (reporting on an official change) | Applies to games, but it shows the factors YouTube weighs (duration, zoom/prominence, realism). |
| Advertiser-friendly guidelines (ad suitability for violence/gore) | — | https://support.google.com/youtube/answer/6162278?hl=en | 2026-10-14 | **Not verified** | The page came up in results but its content was not returned. Gore can reduce ads ("limited ads") even when the video stays up. Verify the "Violence" and "Shocking content" sections. |
| Made-for-kids test: the intent to target children | "If a video features actors, characters, activities, games, songs, stories, or other subject matter that reflects an intent to target children, it's likely made for kids." | https://support.google.com/youtube/answer/9528076?hl=en | 2026-10-14 | Yes | — |
| Violence, mature themes and age-restricted videos are examples of "not made for kids" | (paraphrase from search summary) "content with sexual themes, violence, obscene, or other mature themes; and age-restricted videos" | https://support.google.com/youtube/answer/9528076?hl=en | 2026-10-14 | Yes | — |
| Having some factors (e.g. animated characters) does not automatically make content MFK; mixed-audience content can still be MFK | (paraphrase) "including some of these factors does not automatically mean it's made for kids"; "Children are not the primary audience, but the video is still directed to children ... known under COPPA as 'mixed audience' content." | https://support.google.com/youtube/answer/9528076?hl=en ; https://support.google.com/youtube/answer/9684541?hl=en | 2026-10-14 | Yes | The FTC (Nov 2019) said animation can appeal to all ages and is not automatically child-directed (via Wikipedia summary; FTC blog https://www.ftc.gov/business-guidance/blog/2019/11/youtube-channel-owners-your-content-directed-children). |
| Creators must set the audience themselves | "While it might be tempting to rely on YouTube's machine learning algorithm to determine your Audience, there may be legal consequences if it gets it wrong." | YouTube Help MFK pages (excerpt) | 2026-10-14 | Yes (attribution to the exact page uncertain) | — |

## 9. Music and audio: NOT VERIFIED (search budget exhausted)

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| Shorts longer than 1 minute with an active Content ID claim are blocked | (no verbatim quote) | Mentioned by a third-party blog (https://1of10.com/blog/how-long-can-youtube-shorts-be/) and in a search summary that linked it to the YouTube Help rights-holder page https://support.google.com/youtube/answer/13053317 | 2026-10-14 | Unconfirmed | **Do not rely on this until it is verified.** If true, any claimed music in a 61–90 s Short blocks the video worldwide. |
| YouTube Audio Library license terms (attribution and Creative Commons tracks; usable in monetized videos) | — | https://support.google.com/youtube/answer/3376882 (not fetched) | 2026-10-14 | **Not verified** | Verify, including whether Audio Library tracks are usable in Shorts longer than 60 s. |
| Shorts sounds library / remixing (Remix audio) and how they interact with the 60 s limit | — | — | 2026-10-14 | **Not verified** | Background (model recollection, not cited): many licensed Shorts sounds were limited to 60 s of use. Verify. |

## 10. Shorts UI safe zones

| Fact | Exact quote | Source URL | Access date | Official? | Notes/uncertainty |
|---|---|---|---|---|---|
| Google's Shorts **ads** guidance: keep text, logos and CTAs out of the top 10%, bottom 25% and right 10%, where the channel name, caption and engagement buttons sit | (paraphrase from search summary) keep text, logos, and CTAs out of the "red zones": "the top 10%, bottom 25%, and right-hand 10%" | https://business.google.com/us/ad-solutions/youtube-ads/shorts-ads/ | 2026-10-14 | Yes (Google, ads context) | At 1080×1920 this is about **192 px top, 480 px bottom, 108 px right, 0 px left**. This is advertiser guidance, not organic-Shorts creator guidance, but the overlay UI is the same. |
| Stricter "all YouTube placements" zone: top 15%, bottom 35%, right 17.78%, left 4.44% (288/672/192/48 px) | (paraphrase) "measured from Google's official overlay PNG" | https://www.solidlabs.com/social-safe-zones , https://www.solidlabs.com/ad-specs/youtube | 2026-10-14 | No (claims derivation from a Google template) | Not confirmed on a Google page. |
| Third-party UI templates differ widely (e.g. 180/350/40/120 px; 241/381/201 px) | "figures online disagree by up to 2.8×" (paraphrase) | e.g. https://adkit.so/tools/safe-zones/youtube , https://www.poster.ly/tools/youtube-shorts-safe-zone-checker | 2026-10-14 | No | No official organic-Shorts safe-zone document was found within the budget. |
| Google Ads Help "YouTube Shorts ads: Asset specs and best practices" | — | https://support.google.com/google-ads/answer/16041697 | 2026-10-14 | Yes (exists) | It came up in results, but its safe-zone figures were not returned. Verify. |

## 11. Features for a serialized channel: NOT VERIFIED (search budget exhausted)

No facts verified. Check these on YouTube Help:
- "Related video" link on Shorts: what it can link to and whether it can be set after upload.
- Playlists and Series playlists for Shorts.
- Pinned comments.
- Scheduling Shorts uploads in Studio.
- Collab or co-creator features.
- Remix permissions (allow or disallow remixing of your content).
- Any official statement on best posting time or frequency. Expected result: YouTube generally says there is no best time. **Not confirmed in this session.**

## 12. Official statements on Shorts recommendations: NOT VERIFIED (search budget exhausted)

No quotes collected.
- Indirectly related: the 2026 YouTube Blog post on engaged views (section 5) says secondary outlets reported that YouTube said the view-count change "does not change recommendations, CTR, average view duration, audience retention, YPP earnings or YPP eligibility". That wording comes from a third party (https://ascendants.in/industry_events/youtube-engaged-views-explained-view-counting-change/) and was not verified on blog.youtube.
- To verify: YouTube's "How YouTube's recommendation system works" pages (youtube.com/howyoutubeworks) and Creator Insider / Creator Liaison statements about the Shorts feed (viewed vs. swiped away, satisfaction surveys).

---

## Implications for production (INTERPRETATION, not platform fact)

- **Length and format:** 45–90 s at 1080×1920 (9:16) sits well inside the official "square or vertical, up to 3 minutes" rule. A landscape master would be treated as long-form.
- **Encode:** MP4 with faststart, H.264 High Profile with closed GOP and VBR, at the native animation frame rate (24 or 30 fps; do not convert). Use AAC-LC at 48 kHz. Around 8 Mbps or more for 1080p at 24–30 fps is a reasonable floor, based on third-party copies of Google's table. Exporting at a higher bitrate costs little.
- **Loudness:** YouTube publishes no official target. Mixing narration to about −14 LUFS integrated with true peak at or below −1 dBTP is a widely used convention, not a requirement. The practical risk is being too loud (turned down) rather than too quiet. Check "Stats for nerds" after upload.
- **Music risk:** Treat any third-party or claimable track as dangerous in Shorts over 60 s until the "over 1 minute + Content ID claim = blocked" rule is verified. Prefer original or commissioned scores, or Audio Library tracks after confirming their terms.
- **AI disclosure:** Stylized 2D animation is officially exempt ("animated", "clearly unrealistic"). Disclosure would be relevant only for photorealistic synthetic footage of realistic events or places (e.g. fake "news footage" of a disaster) or a cloned real person's voice.
- **Monetization:** The inauthentic-content policy targets mass-produced or near-duplicate output at channel level. A serialized format should vary stories, scripts, visuals and edits meaningfully from episode to episode, not reuse templates with swapped text or voice. Whether AI narration is acceptable was not verified.
- **Violence:** Animated or fictional zombie violence is generally not removed. Close-ups that dwell on gore can trigger age restriction, which cuts reach to under-18 and signed-out viewers, and may also trigger limited ads. Make the fiction obvious (stylized art, story framing, metadata) and avoid lingering gore shots.
- **Made for kids:** With violence, horror and death as core themes, the content should normally be set **Not made for kids**. Cartoon style alone does not make it MFK, but avoid child-targeted elements (nursery-style songs, child-directed language, kid-character branding) that would create a "mixed audience" case. The creator is legally responsible for the setting.
- **Layout:** Keep subtitles, captions, title cards and faces out of roughly the bottom 25% (480 px), top 10% (192 px) and right 10% (108 px) of a 1080×1920 frame. That is Google's ads guidance and the only official numeric source found. A more conservative layout (bottom 35%, right ~18%) also protects against UI changes.
- **Thumbnails and metrics:** Custom Shorts thumbnails need YPP (desktop upload). Before YPP, design a strong in-video frame to choose on mobile. Watch "Viewed vs. swiped away / Stayed to watch" for hook quality and engaged views for earnings. Since 24 Aug 2026, public view counts are inflated relative to engaged views, so compare like with like.
- **Follow-up needed:** Re-run research for sections 9, 11 and 12 and the missing parts of 2, 5 and 6 when search budget or direct access to support.google.com is available.
