# tools/ — scripts that build and check this package

Run everything with the package root as the argument, e.g. `python3 -I tools/gen_calendar.py "$PWD"` from inside `Worldosphere_Analysis_and_Launch_Plan_2026-10-14/`. Python 3.10+; `openpyxl` for the workbook; Node + Playwright + ffmpeg for rendering.

| Script | Reads | Writes |
|---|---|---|
| `calendar_data.py` | — (source of truth for the 30 days + reserves) | — |
| `gen_calendar.py` | calendar_data | `16_…md`, `17_…md`, `data/calendar_30_days.csv` |
| `ledger_data.py` | — (source of truth for claims) | — |
| `gen_ledger.py` | ledger_data | `07_…/claim_ledger.csv`, `claim_ledger.md` (checks unique IDs) |
| `topic_pool_data.py` | — (94 scored premises and rubric weights; matches `data/topic_pool.csv` and 15) | — (the pool tables were generated once; edit the data, CSV and 15 together if the pool changes) |
| `gen_schedule_tables.py` | calendar_data, claim ledger, fallback CSV, `schedule_template.md` | `20_Production_Schedule_and_Buffer.md` |
| `gen_workbook.py` | all data above + `21` change log + asset register | `Worldosphere_Launch_Workbook.xlsx` (write to a new name if you have filled one in) |
| `package_engine.py` | — | caption splitting, timing model (2.85 words/s), SRT/ASS writer |
| `package_ws00N.py` | — (shot-by-shot script data for Days 1–3) | — |
| `gen_package.py` | `package_ws00N` | captions, shot list CSV, script/shot/caption tables in a package folder |
| `assemble_package.py`, `refresh_package.py` | package folder | re-embeds generated tables into the package document; writes `_sound_cues.csv` |
| `render/` | `pages/*.html`, `ws_draw.js`, `ws.css`, fonts | style frames, specimens, motion-proof frames (`node render/render.js page.html out.png`) |
| `analysis/` | **local** reference video copies (not in the repo) | every measurement in `data/` and `03` (see `analysis/README.md`) |

To make a package for a new episode: copy `package_ws001.py` to `package_ws0NN.py`, replace `SHOTS`, run `gen_package.py`, then fill the package document using a Day 1–3 package as the model (12 §5).
