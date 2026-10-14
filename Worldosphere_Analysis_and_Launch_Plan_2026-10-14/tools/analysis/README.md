# Analysis tools (reproducible evidence)

These scripts produced every MEASURED number in the breakdowns. They run on your **local copies** of the reference videos; the videos and frame grabs are intentionally **not** committed (the GitHub repository is public and the videos belong to another creator).

| Script | What it measures | Notes |
|---|---|---|
| `make_contact_sheets.sh` | 1 fps labelled contact sheets + 10 fps opening sheet | ffmpeg + ImageMagick |
| `cuts.py` | Frame-by-frame difference + histogram distance → candidate cuts | Candidates were then verified by eye (`cutsheet.py`) |
| `cutsheet.py` | Before/after frame pairs for each candidate cut | Visual verification |
| `asr.py` | Speech-to-text with VAD; Parakeet-TDT 0.6B v2 (token timestamps) + Whisper small.en (cross-check) | `pip install sherpa-onnx`; models from github.com/k2-fsa/sherpa-onnx/releases (asr-models) |
| `audio.py` | Per-phrase median pitch (autocorrelation), words/s, gaps, onsets, low/high-band energy | Pitch is an estimate; unreliable on very short or whispered phrases |
| `levels.py` | RMS timeline, level and spectral flatness of every speech gap | Used to detect music drop-outs |
| `captions.py` | Detects every caption change in the caption band and builds readable crop sheets | Captions were then transcribed by eye |
| `capgeo.py` | Caption line positions, heights and widths in pixels | — |
| `shots_data.py`, `captions_data.py`, `gen_breakdowns.py` | Hand-logged shot data + caption list → CSV timelines and stats | Re-run to regenerate `../../data/*` |

Loudness: `ffmpeg -i FILE -af ebur128=peak=true -f null -` (integrated, LRA, true peak).
