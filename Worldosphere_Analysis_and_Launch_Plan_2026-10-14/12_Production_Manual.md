# 12 — Production manual (how to make a Worldosphere episode)

**Purpose.** A producer can make any Worldosphere episode from its brief by following this manual, without re-watching or re-analysing the reference videos. It covers:
- the toolchain (§1) and render settings (§2)
- folders, naming and versioning (§3)
- the reusable asset library (§4, *Assets*)
- the 17-stage workflow with acceptance criteria (§5)
- animation technique and its limits (§6, *Animation*), including a reconstruction of how the reference's effects can be made
- the policy on generative tools (§7)
- the YouTube Shorts translation (§8)
- effort estimates (§9)
- the one-episode quick path (§10).

**Evidence labels.**
- Tool prices, versions and platform facts come from research appendices B and F (`22_Asset_Rights_and_Sources/research_appendices/`). Those were collected from search excerpts on 2026-10-14, without page fetches, and are flagged where unverified.
- Everything else in this manual is a RECOMMENDED production choice, not a ranking trick, and not something the reference creator is known to use.
- The reference creator's tools are **UNKNOWN**. §6 is labelled as a **reconstruction**.

---

## 1. Toolchain

### 1.1 Primary workflow (recommended for a one-video-per-day cadence)

| Stage | Tool | Why | Cost as seen 2026-10-14 (verify before buying; nothing was purchased) |
|---|---|---|---|
| Vector design: characters, kits, props | Adobe Illustrator, **or Affinity** (free since late 2025) | Vector model sheets and layered SVG/AI import | Illustrator: Creative Cloud plans (single app about US$22.99/mo, as seen). Affinity: free |
| Rigging + animation + HUD | **After Effects 26.x + Duik Ángela** (free, GPL) **+ RubberHose 3** (noodle limbs) | Expressions drive timers, counters and Sphere growth. Rigs and HUD templates are reusable. AE 26 imports SVG | AE single app about US$22.99/mo (as seen); Duik free; RubberHose 3 price not found |
| Alternative rig path | **Moho Pro 14** | Bone rigs, smart bones and auto lip-sync. Good if character acting dominates | US$399.99 perpetual (as seen) |
| Edit, captions, mix | **DaVinci Resolve Studio 21** (or the free Resolve 21) | Vertical timeline, subtitle track with SRT import/export, Fairlight loudness meter | Studio US$295 one-time (as seen); free version available |
| Caption timing | **Subtitle Edit** or **Aegisub** (both free) | Waveform timing; ASS styling (`09_Typography_and_Captions/worldosphere_caption_styles.ass`) | Free |
| Voice | The creator's own voice (safest), or a contracted actor with a written licence covering YouTube, monetization and term | Rights clarity (22 §4) | — |
| Music + SFX | Original/commissioned score; YouTube Audio Library; Sonniss GDC bundle (SFX); a subscription library only after confirming monetized-YouTube terms | Rights clarity (22 §3) | See 22 |
| Fonts | Big Shoulders Display, Atkinson Hyperlegible Next, JetBrains Mono (all SIL OFL 1.1) | Original type system (09); OFL allows commercial use and burn-in | Free |
| Prototyping (optional) | The procedural renderer in `tools/render/` (Node + Playwright + ffmpeg) | Fast style frames, HUD tests and caption checks without the main toolchain | Free |

### 1.2 Free fallback (when a paid tool isn't available)

| Stage | Tool | What you lose | How to compensate |
|---|---|---|---|
| Vector design | **Inkscape 1.4.x** or **Affinity** | Speed on complex files (Inkscape) | Keep kits as small SVG modules |
| Rigging + animation | **Blender 5.2 LTS Grease Pencil** (armatures, 3D-camera parallax) or **Tahoma2D/OpenToonz** | AE's expression ecosystem for HUD counters | Build HUD elements (Fork, Sphere, Verdict, T1 timer) once in Blender as linked library assets; or render the HUD with the procedural renderer in `tools/render/` and composite it in Resolve |
| Edit + mix | **DaVinci Resolve 21 (free)** | Studio-only AI transcription | Time captions in Subtitle Edit against the VO waveform |
| Captions | Subtitle Edit / Aegisub | — | — |
| Voice | Own voice, recorded in a treated small room or closet | — | A USB dynamic microphone is enough; record at 48 kHz/24-bit |
| Music + SFX | YouTube Audio Library, Sonniss GDC, Freesound **CC0/CC BY only**, own Foley | Library breadth | Use one recurring original pulse and motif (08 §10), which keeps the channel's sound consistent anyway |

**Avoid** (appendix F):
- starting a new pipeline in Adobe Animate (maintenance mode) or Synfig (no stable release since 2024)
- CapCut stock assets in monetized videos (terms concern)
- BBC RemArc sounds (no commercial use)
- Freesound CC BY-NC
- any free tier whose terms exclude commercial use.

---

## 2. Production format and render settings

| Setting | Value | Reason |
|---|---|---|
| Working canvas | **1080×1920, 9:16**, square pixels | Native vertical Shorts format; Shorts may be square or vertical and up to 3 minutes (appendix B §1) |
| Frame rate | **24 fps** project and export. Characters on twos; camera, Sphere and HUD on ones | Hand-made cadence; YouTube asks for upload at the native frame rate (B §2) |
| Duration | 48–72 s per the calendar (all ≤ 3:00) | Story needs (recipes); not a ranking rule |
| Master export (archive) | ProRes 422 HQ or DNxHR HQ .mov, plus a 48 kHz/24-bit WAV mix | Re-encode later without generation loss |
| **Upload export** | MP4; **H.264 High Profile**, yuv420p, closed GOP, 2 B-frames, VBR **12–16 Mbps** (above the 8 Mbps reference for 1080p at 24–30 fps); **AAC-LC 48 kHz stereo, 384 kbps**; `faststart` | Matches YouTube's recommended upload encoding (answer 1722171: stereo 384 kbps, BT.709 for SDR; checked 2026-10-14) |
| Loudness | **−14 LUFS integrated ±1, true peak ≤ −1.0 dBTP**, measured on the final mix | Common convention; **no official YouTube target was found** (B §3). The reference measured −14.1 LUFS / −1.0 dBTP |
| Captions | Burned-in (brand ASS styles) **plus** an SRT uploaded as a subtitle track | Readability muted plus accessibility |
| Colour | Rec.709, sRGB-matched UI, no HDR | Flat-colour animation; avoids conversion surprises |

**ffmpeg reference commands** (the Resolve presets should give the same result):

```bash
# Upload encode from a master (subtitles burned in from the ASS file)
ffmpeg -i WS-0NN_master_v03.mov -vf "ass=WS-0NN_captions_v03.ass" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r 24 -g 48 -bf 2 \
  -b:v 14M -maxrate 16M -bufsize 28M \
  -c:a aac -b:a 384k -ar 48000 -movflags +faststart WS-0NN_upload_v03.mp4

# Loudness and true-peak check (read the Summary block)
ffmpeg -hide_banner -i WS-0NN_upload_v03.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12

# Container/stream check, pasted into the QA log (U-01)
ffprobe -v error -show_entries stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,sample_rate,channels -show_entries format=duration -of compact WS-0NN_upload_v03.mp4
```

---

## 3. Folder structure, naming, versioning and backups

### 3.1 Library (shared by all episodes)
```
Worldosphere_Production/
  00_Library/
    Characters/   KAI/ MIA/ TESS/ OWEN/ GUEST/ TURNED/    (model sheet .ai/.svg, rig .aep/.moho/.blend, expressions, mouth sets)
    Kits/         K01_SuburbanStreet/ K02_VehicleRoadWater/ ... K10_CrowdGuestTurned/
    HUD/          FORK/ SPHERE/ VERDICT/ T1_TIMER/ L1_LABELS/ H1_HOOK/ G1_TAG/  (AE .mogrt or Blender library .blend)
    Type/         fonts (OFL + licence files), worldosphere_caption_styles.ass, typography_presets.json
    Audio/        MOTIF/ PULSE_BEDS/ SFX_ORIGINAL/ SFX_LICENSED/ (each licensed file paired with its licence PDF/receipt)
    Overlays/     safe_zone_overlay_1080x1920.png, paper_grain.png
    Licences/     asset_register.csv (see 22 §3)
  WS-001_The-Breath-Test/
    01_Brief/     WS-001_brief.md, claim extract
    02_Script/    WS-001_script_v01.md ... (timed read)
    03_Board/     WS-001_animatic_v01.mp4, storyboard frames
    04_Assets/    episode-only props and backgrounds
    05_Anim/      WS-001_S01_v01.aep ... (one comp per shot or scene)
    06_Audio/     VO/ raw takes + comp; SFX/; MUSIC/; STEMS/ (VO, DX, SFX, MUS, FX-HUD)
    07_Edit/      WS-001_edit_v01.drp, captions (WS-001_captions_v03.srt/.ass)
    08_Export/    WS-001_master_v03.mov, WS-001_upload_v03.mp4, preview_360x640.mp4
    09_Upload/    title/description/pinned comment, cover frame PNG
    10_QA/        WS-001_QA_v03.md, ffprobe + ebur128 logs
    11_Review/    24h/72h/7d notes (21)
```

### 3.2 Naming and IDs
- **Episode ID:** `WS-0NN` (calendar order; reserves `R01–R10` take a WS number only when scheduled).
- **Scene / shot ID:** `WS-0NN_S07` for scene 7. Optional sub-shot letters: `S07a`, `S07b`. The shot list in each package is the authority.
- **Files:** `WS-0NN_<stage>_<shot?>_v<2 digits>.<ext>` (e.g. `WS-002_S04_anim_v02.aep`). Never overwrite: increase the version. An `_APPROVED` suffix marks the locked version of each stage.
- **Assets:** `K03_store_dock_v02.svg`, `CH_TESS_rig_v05.aep`, `HUD_FORK_v03.mogrt`, `SFX_ORIG_door-slam-01.wav`, `SFX_LIC_SONNISS_<pack>_<file>.wav`.
- **Claims:** IDs from the claim ledger (`C-205`) are quoted in script margins and in the description sources.

### 3.3 Versioning and backup
- Keep `00_Library` and active episodes in a git repository (git LFS for media) **or** a synced cloud folder with version history. Back up nightly to a second location (3-2-1 rule: 3 copies, 2 media types, 1 off-site).
- Episode files are locked after export (`10_QA` sign-off). Changes after upload go into a new version and the change log.
- **This planning repo is public on GitHub.** Keep licensed audio, raw VO and any reference media out of public repositories (22).

---

## 4. Assets: the reusable library (build before launch)

| Asset | Contents | Built by (gate) | First used | Reuse count in the 30-day plan |
|---|---|---|---|---|
| Character rigs | KAI, MIA, TESS, OWEN: turnaround (front, 3/4, side, back), 6 mouth shapes, 4 hands, brow set, walk/run/shamble cycles, rest poses | Oct 21 | WS-001 to WS-003 | Kai 11 leads, Owen 9, Tess 9, plus cameos |
| GUEST rig | Swappable heads (6), hair (8), tops (8), colourways | Oct 21 | WS-001 | Every episode |
| TURNED variant | Pose shift, grey-green overlay, pale eyes; breath emitter **disabled**; can push but not pull, climb, swim or work handles (WR-04) | Oct 21 | WS-001 | All P1 |
| FX-BREATH | Breath emitter (spec: WS-001 package §17); glass-fog patch | Oct 19 | WS-001 | WS-001, 009, 015, 016, 030 |
| HUD kit (K9) | FORK (crack, panels, chips), SPHERE (4 colours, rim, distance tick), VERDICT (V1–V3), T1 timer, L1 labels, H1 hook, G1 tag, C1 card | Oct 18 | All | All 30 |
| Kits K1–K10 | Modular backgrounds (08 §9) in 4 depth planes, each with a top-down floor plan for geography | K1–K4, K9, K10 by Oct 21; others 5 days before first use (20) | — | See calendar "Kits" column |
| Crowd system | 3 depth bands, cycle offsets of 3–11 frames, background silhouettes | Oct 21 | WS-001, WS-003 | WS-003, 006, 013, 022, 026, 028 |
| Audio library | Motif (0.8 s), 3 pulse beds (70/76/90 BPM), Fork whoosh + tick, Verdict paper slide + boom, Sphere bloom, room tones | Oct 21 | All | All |
| Templates | Script, storyboard, shot list, cue sheet, QA, upload, review (`13_Templates/`) | Done (this package) | All | All |

**Consistent references.** Every rig folder holds a one-page model sheet PNG (silhouette test at 120 px, colour hexes from 08 §4.2) that is pinned in the animation workspace. Every kit has a floor plan PNG with exits, threat entry side and screen direction.

---

## 5. The 17-stage workflow

The stages run in this order:

> **Topic selection → research → scenario rules → hook development → script → timed read → storyboard → assets → animation → voice → editing → sound mix → captions → quality review → export → upload packaging → performance review**

Deadlines for each stage, counted back from publication, are in `20_Production_Schedule_and_Buffer.md` §3.

### 5.1 Topic selection
- **Inputs:** calendar row (17), brief (18), the last review's decisions (21), reserve list.
- **Actions:**
  - Confirm the slot's topic still fits: no clash with news (sensitivity) and no BLOCKING claim unresolved at T-10.
  - Check it doesn't repeat an angle already covered (topic pool 15; for the future, the channel's own uploads).
- **Tools:** workbook *Calendar* sheet.
- **Output:** "GO" or "SWAP → Rxx" logged in the change log.
- **Acceptance:** the topic has a decision, a fair rule and a payoff in one sentence each.
- **Failure modes → fix:**
  - A real disaster in the news that matches the topic → swap with a reserve; never exploit a live tragedy.
  - A claim can't be verified → use the reserve.
- **Handoff:** brief ID + status to research.

### 5.2 Research and claim verification
- **Inputs:** brief fields 7–8, claim ledger rows.
- **Actions:**
  - For each real-world claim, find a primary source (government agency, standards body, peer-reviewed study, manufacturer). Record publisher, title, URL, access date and exact supporting wording in `claim_ledger.csv`.
  - Set the status to SUPPORTED, QUALIFIED (with the qualifier), FALSE (cut it) or still UNVERIFIED. P1 fiction rules cite the world-rules sheet instead.
- **Tools:** browser, ledger CSV, workbook *Claims* sheet.
- **Output:** updated ledger rows; the description "Sources" block.
- **Acceptance:** QA F-01 to F-05 can pass. No UNVERIFIED-BLOCKING claims remain in the script.
- **Failure modes → fix:**
  - Secondary sources only → find the primary, or soften to "can"/"about".
  - Sources disagree → state the safer instruction; keep numbers off screen.
- **Handoff:** the claim list with approved wording, to the scriptwriter.

### 5.3 Scenario rules
- **Inputs:** world rules WR-01…WR-12 (07 §3), kit floor plan.
- **Actions:**
  - Write a 5-line rules box for the episode: location geography (exits, threat entry side, screen direction), time of day and weather, which world rules matter, what the Turned can and can't do here, and the fair clue the viewer can see before the answer.
- **Output:** a "Rules" block at the top of the script.
- **Acceptance:** a viewer could, in principle, guess the right choice from what is shown (fair play).
- **Failure modes → fix:**
  - The solution relies on information never shown → plant it in the first 30%.
- **Handoff:** to hook development and script.

### 5.4 Hook development
- **Inputs:** brief fields 9–14, playbook patterns HP01–HP14 (14).
- **Actions:**
  - Draft the three hooks from the brief as **frame-0 thumbnails plus a spoken line plus H1** (≤6 words).
  - Do the 3-second muted test with someone who doesn't know the script: can they say what is happening and what the question is?
- **Output:** the selected hook (frame-0 sketch, line, H1).
- **Acceptance:**
  - QA S-01, S-02 and S-05: no promise the episode doesn't keep.
  - The first word lands ≤0.3 s.
  - The protagonist and the anomaly are both in frame 0.
- **Failure modes → fix:**
  - A vague question ("What would you do?") with no concrete image → add the specific contradiction or clock.
  - A hook that gives the answer away → move the mechanism later.
- **Handoff:** the hook goes into the script header.

### 5.5 Script
- **Inputs:** brief, recipe (`13_Templates/Production_Recipes.md`), claim wording, hook.
- **Actions:**
  - Write in the script template (`13_Templates/Script_Template.md`): shot-by-shot lines, speaker, emphasis marks, " | " caption breaks, on-screen text events.
  - Hit the word budget for the target duration (recipes: 50 s ≈ 120–135 words … 70 s ≈ 170–185).
  - Put the Fork at the recipe's position.
  - Every line must do at least one of: reveal, change, raise or resolve stakes, deepen a character (QA S-03).
- **Tools:** text editor, or `tools/package_engine.py` (the shot-dict format in `tools/package_ws001.py`).
- **Output:** `WS-0NN_script_v0N.md`.
- **Acceptance:** read-aloud test passes; character lines ≤7 words; the Verdict factor ≤8 words; REAL RULE ≤14 words; all claims match the ledger wording.
- **Failure modes → fix:**
  - Over budget → cut adjectives and repeated explanations, not the setup of the fair clue.
  - Explaining a visible action → delete the line and let the picture carry it.
- **Handoff:** script v-locked → timed read.

### 5.6 Timed read
- **Inputs:** locked script.
- **Actions:**
  - Read it aloud at performance pace with a stopwatch, or run the engine (`python3 -I tools/gen_package.py <D> package_ws0NN <outdir>`). The engine produces a shot list with estimated durations (2.85 words/s, comma 0.18 s, stop 0.30 s), caption groups and provisional SRT/ASS.
  - Compare with the target duration.
- **Output:** the timed script table, a provisional caption file, and the shot durations for the animatic.
- **Acceptance:** total within ±3 s of target. Every caption group meets the minimum display time. Emphasis spacing ≥3 s.
- **Failure modes → fix:**
  - Long → trim words (not pauses before reveals).
  - Short → add a hold on the decisive visual, not filler words.
- **Handoff:** durations to the storyboard.

### 5.7 Storyboard and animatic
- **Inputs:** timed script, kit floor plan, model sheets.
- **Actions:**
  - Thumbnail every shot on `13_Templates/Storyboard_Template.md` (frame, camera, action, text lane, continuity).
  - Build an animatic: stills on the timed read (scratch VO is fine) with HUD placeholders.
  - Check the subject box against the caption lane for every shot.
- **Tools:** paper or tablet, then Resolve/AE for the animatic.
- **Output:** `WS-0NN_animatic_v0N.mp4`, the shot list CSV (`13_Templates/Shot_List_Template.csv`).
- **Acceptance:**
  - A muted watch of the animatic communicates the story (S-01).
  - Geography is consistent with the floor plan (F-08).
  - Captions never overlap faces or the decisive action (W-05).
- **Failure modes → fix:**
  - Talking heads → replace with action or diagram shots.
  - Unclear threat position → add an establishing top-down or a Sphere.
- **Handoff:** approved animatic = animation contract (shot IDs and durations frozen; changes need a new version).

### 5.8 Assets
- **Inputs:** animatic, brief field 20.
- **Actions:**
  - Pull kits and rigs from `00_Library`.
  - Build only the episode-specific props and backgrounds, in 4 depth planes (08 §6.4) with no background outlines.
  - Update the floor plan.
  - Register any third-party asset in the licence register.
- **Tools:** Illustrator/Affinity/Inkscape.
- **Output:** `04_Assets/` files; library updates (versioned).
- **Acceptance:** silhouette test at 120 px; palette tokens only; layers named for rigging.
- **Failure modes → fix:**
  - Over-detailed backgrounds compete with characters → drop one value step and remove texture.
  - New props with no hand-contact points → add a pivot and grip point.
- **Handoff:** assets to animation.

### 5.9 Animation
- **Inputs:** animatic, rigs, assets, HUD kit.
- **Actions:**
  - Block key poses per shot (anticipation, action, follow-through, settle).
  - Add the HUD (Fork, Sphere, timers) from templates.
  - Add effects (breath, rain, fog).
  - Work shot by shot in animatic order, critical shots first: hook, Fork, payoff, Verdict.
  - Techniques and limits: §6.
- **Tools:** AE + Duik/RubberHose, Moho, or Blender Grease Pencil.
- **Output:** `05_Anim/` project files; per-shot ProRes renders or a direct comp.
- **Acceptance:**
  - 08 §12 accept/reject list.
  - QA V-01 to V-09.
  - Planted feet locked.
  - Props parented to hands.
  - Reactions 4–6 frames after the stimulus.
- **Failure modes → fix:** see the §6 table.
- **Handoff:** picture-locked shots to the edit.

### 5.10 Voice
- **Inputs:** locked script, voice direction (08 §10; package §11).
- **Actions:**
  - Record at 48 kHz/24-bit in a quiet treated space, 3 takes per line.
  - Comp the best takes.
  - Edit breaths only where distracting.
  - Character lines recorded separately (or by guest actors, with a written licence).
- **Tools:** Resolve Fairlight / any DAW; dynamic microphone; pop filter.
- **Output:** `06_Audio/VO/WS-0NN_VO_comp_v0N.wav` plus raw takes.
- **Acceptance:**
  - Intelligible on a phone speaker.
  - No clipping; noise floor ≤ −60 dBFS between phrases.
  - Pace 160–175 wpm with planned pauses before reveals.
- **Failure modes → fix:**
  - Rushed reads → mark pauses in the script.
  - Room echo → record in a closet or under a duvet.
  - Inconsistent day-to-day tone → batch-record 3–5 episodes per session.
- **Handoff:** the VO comp to the edit, and to caption re-timing.

> In practice, **voice can be recorded right after the timed read** (before animation) and the animation timed to it. This is the recommended order when one person does both.

### 5.11 Editing
- **Inputs:** animation renders, VO comp, animatic.
- **Actions:**
  - Assemble on a 1080×1920, 24 fps timeline.
  - Cut to the VO. Hard cuts by default; branded transitions only (Fork split, Sphere expand-to-cut, Verdict slide, at most one match wipe).
  - Hold the decisive visuals.
  - Place the drop.
- **Tools:** Resolve.
- **Output:** `07_Edit/WS-0NN_edit_v0N.drp`; picture lock.
- **Acceptance:**
  - Duration within the target range.
  - Average shot length about 1.6–2.2 s, with suspense holds 2.5–5 s (08 §7).
  - The final image holds ≥1.5 s before the Verdict.
- **Failure modes → fix:**
  - Constant motion with no holds → add a held beat on the reveal.
  - Cutting on every word → let story beats breathe.
- **Handoff:** the locked cut to the sound mix and captions.

### 5.12 Sound mix
- **Inputs:** locked cut, VO, cue sheet (`13_Templates/Sound_Cue_Sheet_Template.csv`; packages §10).
- **Actions:**
  - Lay ambience first (it is always present), then SFX on sync points, then the music bed (70–90 BPM), the drop, the Fork whoosh and tick, and the Verdict motif and boom.
  - Mix the VO to sit 14–18 dB above the bed in gaps.
  - Export stems (VO, DX, SFX, MUS, HUD-FX) and the full mix.
- **Tools:** Fairlight (Resolve), with its loudness meter.
- **Output:** `06_Audio/STEMS/*`, `WS-0NN_mix_v0N.wav`.
- **Acceptance:**
  - −14 LUFS ±1 integrated; ≤ −1.0 dBTP.
  - Dialogue never masked.
  - The drop lands on the frame.
  - QA A-01 to A-08.
- **Failure modes → fix:**
  - Music fights the voice → cut the 1–4 kHz band in the music by 3–6 dB under speech.
  - A booming end card clips → use a limiter at −1.0 dBTP.
- **Handoff:** the final mix to captions and export.

### 5.13 Captions
- **Inputs:** final VO, provisional captions from the timed read (5.6), ASS styles.
- **Actions:**
  - Re-time every caption group to the recorded VO (Subtitle Edit waveform, or Resolve's subtitle track).
  - Keep the groups, breaks and emphasis from the script.
  - Apply styles: N1 lane A; D1 + S1 speaker chips; H1/L1/T1/F1/V1–V3 from 09 §3.
  - Export the SRT (upload track) and the ASS (burn-in).
- **Tools:** Subtitle Edit / Aegisub, Resolve.
- **Output:** `WS-0NN_captions_v0N.srt/.ass`.
- **Acceptance:**
  - Word-for-word match (W-01).
  - Reading time, line length, emphasis and lane rules (W-02 to W-08; 09 §4–§8).
- **Failure modes → fix:**
  - Groups that break a phrase awkwardly → use " | " markers and avoid a weak word at a line end (the engine's rules).
  - A caption over the action → move the action (subject-box rule), not the caption.
- **Handoff:** captions to QA and export.

### 5.14 Quality review
- **Inputs:** a full-quality render with captions and mix.
- **Actions:**
  - Run the master checklist (`13_Templates/QA_Checklist.md`) and the episode checklist (brief/package §18).
  - The playback section (P-01 to P-06) must be done on the **actual export file**: complete viewing with sound, muted viewing, phone-size viewing, critical transitions frame by frame, and continuity points.
- **Output:** `10_QA/WS-0NN_QA_v0N.md` with sign-off.
- **Acceptance:** all items pass or are N/A with a reason; no hard-stop (★) failures.
- **Failure modes → fix:**
  - Late-found factual issue → fix it or swap to the reserve; never ship with a known error.
- **Handoff:** pass → export packaging.

### 5.15 Export
- **Inputs:** the QA-passed timeline.
- **Actions:**
  - Render the master (ProRes/DNxHR) and the upload MP4 (§2).
  - Make a 360×640 preview for the phone check.
  - Run ffprobe and ebur128 and paste the results into the QA log.
- **Output:** `08_Export/`.
- **Acceptance:** U-01; loudness confirmed on the upload file (not just the timeline).
- **Failure modes → fix:**
  - Banding in gradients → raise the bitrate or add a 1–2% static grain.
  - Wrong frame rate → re-export at 24; never convert.
- **Handoff:** files to upload packaging.

### 5.16 Upload packaging (prepare only; publishing is the owner's decision)
- **Inputs:** export, brief fields 3, 25 and 26, ledger sources.
- **Actions:**
  - Fill `13_Templates/Upload_Package_Template.md`: title (≤100 characters, key words in the first ~60), description (summary, "Fiction scenario" or sources, attributions), ≤3 hashtags, pinned comment, cover frame.
  - Settings: **Not made for kids**; altered/synthetic content **No** (stylized animation); SRT attached.
- **Output:** `09_Upload/WS-0NN_upload_package.md` + cover PNG.
- **Acceptance:** U-02 to U-08; the title represents the video.
- **Failure modes → fix:**
  - Clickbait drift ("You won't believe…") → rewrite to the actual decision and payoff.
- **Handoff:** to the owner for go / no-go.

### 5.17 Performance review
- **Inputs:** YouTube Studio analytics at 24 h, 72 h and 7 days; comments.
- **Actions:**
  - Fill `13_Templates/Performance_Review_Template.md` and the workbook *Tracking* sheet.
  - Compare with videos at a similar age.
  - Classify the result with the diagnosis guide (21 §6).
  - Log decisions in the change log.
- **Output:** review notes; any calendar change (reserve swap) with a reason.
- **Acceptance:** each decision cites a measure and a comparison. No change is made on a single slow result.
- **Failure modes → fix:**
  - Over-reacting to one video → wait for the planned checkpoint (Days 7, 14, 21 and 30).
- **Handoff:** decisions to topic selection for upcoming slots.

---

## 6. Animation: techniques, limits, typical defects (with a reconstruction of the reference's effects)

The reference creator's tools and methods are **UNKNOWN**. The "reference observation" column describes what is visible (OBSERVED, from the breakdowns). The "likely method" column is our **RECONSTRUCTION**: one practical way to produce that look, not a claim about how it was made.

| Area | Reference observation | Likely method (reconstruction) | Worldosphere method | Limits and typical defects | Fix |
|---|---|---|---|---|---|
| Turnarounds + expressions | Consistent simple characters (round head, dot eyes, thin limbs) | Vector model sheet + limited expression set | Model sheet with front, 3/4, side and back; 6 mouths; brow library; Turned variant (08 §4–§5) | Off-model drift between shots; heads changing size | Rig from one master file; scale-lock heads; check against the sheet ±3% |
| Proportions + line weights | Uniform line weight, no outlines on backgrounds | Vector strokes at a fixed width | 6 px outlines, 3 px detail; no background outlines | Strokes scale with layers, so lines get thinner on zoomed-out shots | Use non-scaling strokes or a "stroke compensate" expression |
| Skeletons, rigs, pivots, parenting | Limb swings, reaches, kneel-and-pull | Cutout rig with parented layers or IK | Duik/RubberHose IK limbs; parent hierarchy torso → upper arm → forearm → hand; pivots at joints | Elbow popping at full extension; pivot drift | Soft-IK; lock pivots in a template; avoid fully straight limbs |
| Pose libraries + cycles | Run cycle, walk, crouch | Saved cycles reused | Walk/run/shamble/crowd-idle cycles on twos; pose library per character | Cycles look mechanical; repeated identically in crowds | Offset 3–11 frames; vary one parameter per copy (speed or arm swing) |
| Hand-to-object contact | Phone in hand, generator switch | Prop parented to the hand | Prop parented to the hand null for the whole hold; grip-pose swap on contact frame | Props sliding in hands; "floating" hands near the target | Parent to the hand; contact frame keyed exactly; check at 50% speed |
| Feet + ground contact | Mostly side-on runs; feet partly hidden by grass | Foreground occlusion hides contact | Planted frames locked with IK; foreground grass only where the story allows | Foot slide; skating cycles | Lock the foot controller; match cycle stride to the background move speed |
| Prop layers, occlusion, depth | Dog in front, tractor behind, etc. | Layer stacking | Named depth layers per kit (FG, subject, MG, BG) | Hands rendering behind props they should hold | Depth-order check frame on every contact |
| Reusable backgrounds + modular sets | Repeated farm, shed, barn sets across parts | Reused painted backgrounds | Kits K1–K10, with floor plans | Locations feel samey | One distinctive landmark per episode (pumpkins, dock doors, waterline) |
| Crowd + creature variation | Groups of 5–6 dark hunched infected | Duplicated figures, offset | GUEST rig swaps; 3 depth bands; background silhouettes | Clones obvious; tangles | Swap heads and colourways; separate silhouettes by ≥40 px |
| Parallax + camera | Slow pushes, simulated depth of field | Layered 2.5D camera | 4 planes at 1.6/1.0/0.6/0.3×; slow drift ≤2%/s; push-ins for realisations; no constant zoom | Wobbly parallax; motion sickness | Keep moves slow and motivated; cut instead of whip-panning |
| Weather, smoke, dust, debris | Dust motes, haze, rain | Particle/overlay layers | Rain, fog, breath, snow as reusable FX comps under 25% of frame | Effects covering the action; compression mush | Keep FX low-contrast; reduce particle count; test the upload encode |
| Infographics (maps, cutaways, counters) | Blueprint plan, satellite aerial, cutaway diagrams, counters | Motion-graphics templates | The Sphere, T1 timer, L1 labels, map scale; cutaway labels | Clutter; numbers inconsistent with time | ≤2 domes; T1 driven by real time (expression) |
| Scene-to-scene continuity | Some time-of-day jumps (REF02 52–56 s; REF01 1.9–3.1 s) | — | Continuity column in every shot list; light only changes with a visible cause | Time jumps; prop states reset | Continuity pass (QA F-08) |
| Compositing + grading | Soft gradients, cast shadows, haze | Gradient fills, blur layers | Flat base + one shadow tone + rim light; paper grain 3% static; fog on far planes | Banding in gradients after YouTube encoding | Static grain; higher bitrate |
| Captions | Dense short captions, semantic colour (F05) | Burn-in, likely in an editor (UNKNOWN) | The original 09 system (lanes, tags, emphasis budget) | Captions over faces; mismatched words (REF01 defects) | Subject-box rule; re-time to the final VO |
| Sound + render | −14.1 LUFS, drop-outs as punctuation (MEASURED) | Mixed to a streaming convention | −14 LUFS ±1, ≤ −1 dBTP; one drop per episode | Music masking speech | EQ and sidechain the bed under speech |

**Why controlled 2D.** The format depends on exact readable details: breath puffs, a waterline, push versus pull on a door, chip labels. Controlled 2D rigs reproduce those details identically in every shot. 3D, photorealism or generative video would add cost and inconsistency without helping the viewer read the decision (§7).

**Cheapest ways to keep quality (simplifications that don't weaken the viewer experience):**
1. Off-screen threat conveyed by sound plus a reaction. It is cheaper to make and often scarier.
2. A diagram or cutaway shot instead of a complex action shot (the reference relies on this, F02).
3. Held drawings plus a camera move for suspense holds.
4. Crowds as cycles plus silhouettes; only the foreground band is fully animated.
5. Narration-led episodes with few lip-synced lines (character lines ≤7 words).
6. Reuse of the kits: the calendar groups kits (K3 store on Days 3 and 28; K8 transit on Days 6 and 26).

---

## 7. Generative tools (optional helpers only)
- **Allowed:** ideation thumbnails; background texture or plate drafts that are then **redrawn or traced as vector** in the kit style; sound-design ideation. Nothing generative is used for characters, text, the HUD or the narrator's identity.
- **If generated plates are used:**
  - **Reference consistency:** feed the kit's palette and a style frame (SF1–SF3) as reference. Reject any output whose palette or line style differs.
  - **Shot constraints:** a static camera or a single slow push, a maximum of 2 s per clip, no human figures and no lettering.
  - **Temporal checks:** check every frame for "boiling" shapes, drifting perspective and lights that move.
  - **Correction:** paint out the drift, or replace the clip with a held still plus a 2.5D camera move.
- A good still does not prove its animation will stay consistent: judge the moving clip.
- **Disclosure and policy:** stylized animation is exempt from the altered/synthetic disclosure ("clearly unrealistic, animated"; B §7). The inauthentic-content policy targets mass-produced, repetitive output (B §6), so every episode must have its own story, script, staging and edit.
- **Voice:** do not clone any real person's voice. A synthetic narrator is allowed only on a commercial plan, with the terms saved (22 §4). Whether YouTube treats AI narration differently for monetization was **not verified** (B §6).

---

## 8. Translating the format to YouTube Shorts

| Topic | What transfers from the reference (Instagram) | What must adapt for YouTube Shorts | Source / status |
|---|---|---|---|
| **First-frame viewing choice** | Frame 0 contains the protagonist and an anomaly (F01, F14) | Shorts viewers choose in the feed: frame 0 must work as a still with the H1 hook (QA S-01, P-06). "Stayed to watch" (formerly "Viewed vs. swiped away") is the metric to watch | B §5 (via secondary sources) |
| **Clarity for new viewers** | Each beat re-explained (REF01 works cold) | Every episode stands alone (anthology rule). Sagas resolve Part 1 (S-09) | Design choice |
| **Mobile framing + UI clearance** | Captions at 62–65% height in the reference (MEASURED) | Conservative zones: text box x 144–936; hook lane y 220–620; caption lane A y 1100–1300; nothing important at y ≥ 1400 or x ≥ 936 from y 700 down. Based on Google's Shorts ads guidance (top 10%, bottom 25%, right 10%); no official organic-Shorts spec was found | B §10; check on a device |
| **Titles** | Instagram captions unknown (not accessible) | Searchable titles that state the scenario (≤100 characters, key words in the first ~60, truncation estimated) | B §4 (third-party) |
| **Descriptions** | — | Summary + "Fiction scenario" or sources + attributions; ≤3 hashtags (more than 60 makes all of them ignored) | B §4 |
| **Cover selection** | Typographic end cards | Choose a cover frame in the app; custom Shorts thumbnails were rolling out to YPP creators from July 2026 (desktop). Design frame 0 or the payoff frame as the cover; keep key art centred (3:2 crops reported) | B §4 |
| **Captions** | Burned-in captions | Burned-in **plus** an SRT subtitle track | Design choice |
| **Standalone satisfaction** | Reference ends on cliffhangers + "follow" CTAs (F08) | **Resolution first** (the Verdict); an optional forward line after it. No "follow to find out" | 08 §8.3 |
| **Subscriber / returning reasons** | Serial story | A recurring benefit: a new decidable scenario daily, a fair rule, a Verdict; a recognisable cast | 14 Part 3 |
| **Audio licensing** | The reference's music is unidentified; Instagram licences do **not** carry over | Use only original or YouTube-cleared audio. YouTube Help pages conflict on whether Shorts over 1 minute with a Content ID claim are blocked (23 §2 P1), so use no claimable music in any episode | YouTube Help, checked 2026-10-14; 22 §3 |
| **Clean original exports** | Downloaded references were 720×1280 re-encodes | Upload from our own 1080×1920 master; never upload a re-download or a watermarked file | §2 |
| **Length** | 61 s and 87 s references | Shorts allow up to 3 minutes (uploads on or after 15 Oct 2024); the plan uses 48–72 s for story reasons | B §1 |
| **Made for kids** | — | Set **Not made for kids** (violence and horror themes; the creator is legally responsible). Mia (8) is a sibling character in a teen/adult story; avoid child-directed elements (nursery songs, kid branding) | B §8 |
| **Violence / age restriction** | Implied violence, blood on Mara (REF01) | No gore focus; fiction made clear; avoid realistic "breaking news" framing of fiction | B §8 |
| **AI disclosure** | — | Not required for clearly animated content; required if realistic synthetic people, places or events are ever used | B §7 |
| **Metrics** | Instagram metrics don't predict YouTube results | From 24 Aug 2026, public views count from the first frame; engaged views keep the old definition. Compare like with like (21 §2) | B §5 |
| **Monetization policy** | — | Inauthentic (mass-produced/repetitive) content is not monetizable; keep episodes meaningfully different | B §6 |

**Platform requirements checked on official pages (2026-10-14):** the Content ID rule (the pages conflict, so the conservative rule stays), the Audio Library terms, the analytics definitions, related video and scheduling, the AI-voice stance and the encoding settings. Results and effects are in 23 §2. Still worth a local look: the safe zones in the Shorts editor on your phone (P6).

---

## 9. Effort estimates (assumptions stated; capacity is unproven)

**Assumptions:**
- An experienced 2D animator-editor who is fluent in the chosen toolchain.
- The library (§4) is already built.
- 48–72 s episodes, as planned.
- Hours are focused working hours.
- None of these figures has been measured on this project yet. Days 1–3 are the time pilots: log actual hours per stage in the workbook *Schedule* sheet and recalculate (20 §5).

| Stage | L (single set, little crowd) | M (typical) | H (new kit or crowd-heavy) |
|---|---|---|---|
| Topic check + research and claims | 0.5 | 1.0 | 1.5 |
| Scenario rules + hook + script + timed read | 1.5 | 2.0 | 2.5 |
| Storyboard / animatic | 0.75 | 1.0 | 1.5 |
| Assets (episode-specific) | 0.5 | 1.5 | 4.0 (new kit) |
| Animation incl. HUD and FX | 3.0 | 5.0 | 8.0 |
| Voice (record + comp) | 0.5 | 0.75 | 1.0 |
| Edit + captions | 1.0 | 1.25 | 1.5 |
| Sound + mix | 0.75 | 1.0 | 1.5 |
| QA + export + upload package | 0.75 | 0.75 | 1.0 |
| **Total per episode** | **≈9 h** | **≈14 h** | **≈22 h** |

**One-time library build:**
- 4 lead rigs + guest + Turned: ≈24 h.
- Kits K1–K4, K9, K10: ≈30 h.
- Audio library: ≈6 h.
- Templates: done.
- Total **≈60 h**; the later kits (K5–K8) add ≈20 h, spread before first use.

**Totals for the 30-day plan:**
- The calendar's mix is 6 H, 20 M and 4 L (one M/H counted as M).
- That is ≈6×22 + 20×14 + 4×9 = **≈450 h for 30 episodes**, about **15 h per publishing day**.
- **This exceeds one person working full time.** The consequences and the recommended staffing and launch date are in `20_Production_Schedule_and_Buffer.md` §1–§2.

---

## 10. Making one episode without re-analysing the reference library
Everything needed is already distilled:
1. Open the brief (`18_Daily_Briefs/WS-0NN_*.md`) and its recipe (`13_Templates/Production_Recipes.md`).
2. Check the claims in `07_Survival_Logic_and_Facts/claim_ledger.csv`.
3. Use the brand rules (08), type rules (09), the playbook (14) and the templates (13).
4. Follow §5 stages 5.1–5.16, using the Day 1–3 packages (19) as worked examples.
5. QA with `13_Templates/QA_Checklist.md`.

The one-page version is `24_Make_the_Next_Worldosphere_Video_Checklist.md`. The reference videos are needed only for an optional re-study, and the analysis tools in `tools/analysis/` can regenerate every measurement from local copies.
