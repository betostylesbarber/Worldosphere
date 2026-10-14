# 11 — Style frames and motion proof (inspected prototypes)

**What these are.** Original Worldosphere prototypes rendered in this session from procedural vector code (`tools/render/ws_draw.js` + `tools/render/pages/*.html`, rendered with headless Chromium through `tools/render/render.js`). They test the *look* and the *signature techniques*. They are **not** final production art and **not** a finished episode. Each one was opened and inspected after rendering. Defects found were fixed and re-rendered, and the remaining limitations are listed below.

| File | Represents | Inspection result |
|---|---|---|
| `SF1_hook_WS-001_frame0.png` | **Hook.** WS-001 frame 0: original city-alert phone card, costume crowd breathing, the planted Turned (no breath) under the far streetlight, Mia's fogging helmet, H1 "WHO'S IN COSTUME?", G1 tag, N1 caption in lane A | **Pass (prototype).** H1, alert text and caption are readable at phone scale. Breath puffs are visible after a fix (first render: puffs too faint; opacity and size raised). The Turned is the only figure without breath, which reads at a glance. First-render fixes: crowd arms crossed faces (re-posed forward), figures too small and lower third empty (re-staged). **Known limitation:** two crowd figures still overlap at the arms (silhouette tangle). Production staging must separate them by at least 40 px |
| `SF2_escalation_WS-001_fork.png` | **Escalation.** The Fork: amber crack at 12°, the bright street (chosen, "STREET" Amber chip) vs the dark alley ("ALLEY" Ink chip), an ambiguous figure far down the alley, N1 caption on its tag above the crack | **Pass (prototype).** The split, chips and caption read clearly. The caption tag sits above the crack layer as specified (09 §6, revised). **Known limitation:** Kai's hood shape reads like a helmet at small size. Simplify the hood silhouette in the turnaround |
| `SF3_payoff_WS-001_verdict.png` | **Payoff.** Exterior reverse angle: Kai and Mia behind the warm window, two breath-fog patches on the glass with Mia's smiley, Pell's grey-green hand flat on the glass with **no fog**, frame darkened 20%, V1/V2 Verdict card | **Pass (prototype) after one fix.** First render put the fog patches over Kai's head (confusing); they were moved to chest and mouth height on the glass. The Verdict card is fully legible. **Known limitation:** the fog patches are subtle against the warm interior. Raise to 85% in production and add a faint edge highlight |
| `MP1_fork_and_breath_motion_proof_1080x1920_24fps.mp4` | **Motion proof** of the two techniques WS-001 depends on: (1) the **breath emitter** (living characters puff on staggered cycles; Mia's visor fogs and clears); (2) the **Fork transition**: freeze → crack draws in 4 frames → panels separate → chips slide in → hold → chosen panel wipes to full frame in 8 frames → action resumes with a walk | **Pass (prototype) after three fixes**, all found by frame inspection: (a) the 2-line caption overlapped Kai's head during the hold → Kai re-staged lower and smaller (the subject-box rule); (b) the split hold ran 1.7 s, over spec → set to 1.5 s (chips visible about 1.3 s); (c) a 1-frame bare-ink flash at the split → frozen base layer added. **Specs:** H.264 High, 1080×1920, 24 fps, 120 frames, 5.0 s, yuv420p, faststart, CRF 18. **Silent by design:** this is a visual technique proof. No audio or voice was produced, so it was **not** given a "complete viewing with sound" review |
| `MP1_keyframes_contact_sheet.jpg` | Frames 0, 40, 80, 119 of the motion proof | Reference |
| `../09_Typography_and_Captions/type_specimen_1080x1920.png`, `verdict_card_specimen_1080x1920.png` | Typography presets rendered with the licensed fonts | Pass after two fixes (CSS shrink-to-fit bug caused 3-line captions; an L1 label crossed into the right UI column) |

## What the prototypes prove, and what they don't
- **Proved (inspected):**
  - The palette, outline weight, bean heads with brows, noodle limbs and two-tone shading are readable at phone size.
  - The caption, hook, chip and Verdict typography renders correctly from the OFL fonts.
  - The Fork transition timing (crack 4 frames, hold about 1.3–1.5 s, wipe 8 frames) reads clearly.
  - Breath puffs can carry an entire story mechanic when opacity is about 85–95% at the core.
  - Every text element stays inside the conservative safe zones.
- **Not proved:**
  - Full character animation quality: walk cycles here are a simple leg swing, with no lip-sync and no secondary motion.
  - Lighting and FX at production level.
  - Audio, mix and voice.
  - Compression behaviour after YouTube re-encoding. Test with a private upload; publish nothing.
  - Performance with viewers.

## How to use these in production
1. Treat SF1–SF3 as **composition and value references**. Rebuild the characters as proper rigs (After Effects + Duik / Moho / Blender Grease Pencil; see 12) from the turnaround specs in 08 §4.
2. Re-use the **breath emitter logic** and the **Fork timing** exactly, or improve them. Keep the frame counts.
3. Re-render SF1 with the production rigs as the Day 1 thumbnail candidate, and check it on a phone at 30% brightness.

## Re-rendering
```
cd tools/render
node render.js pages/sf1_hook.html out.png
node render.js pages/mp1_fork.html frames/ --frames 120 --fps 24
ffmpeg -framerate 24 -i frames/%04d.png -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 -movflags +faststart out.mp4
```
Requires Node + Playwright (Chromium). The fonts are bundled in `tools/render/fonts/` (OFL licences included).
