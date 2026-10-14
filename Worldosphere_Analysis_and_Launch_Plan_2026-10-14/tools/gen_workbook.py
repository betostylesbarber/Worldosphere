# Builds Worldosphere_Launch_Workbook.xlsx from the package's data files.
# Usage: python3 -I tools/gen_workbook.py <deliverables root>
import sys, csv, glob, os, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
D = sys.argv[1]; sys.path.insert(0, D + "/tools")
from calendar_data import C, RESERVES
HDR = PatternFill("solid", fgColor="161A22"); HF = Font(bold=True, color="F2EBDD")
INPUT = PatternFill("solid", fgColor="FFF4D6")
def sheet(wb, name, header, rows, widths=None, wrap=True):
    ws = wb.create_sheet(name); ws.append(header)
    for r in rows: ws.append(list(r))
    for c in ws[1]: c.fill = HDR; c.font = HF; c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, h in enumerate(header, 1):
        w = (widths or {}).get(h) or min(60, max(10, int(max(len(str(h)), *(len(str(r[i-1])) for r in rows)) * 0.9) if rows else len(h) + 4))
        ws.column_dimensions[get_column_letter(i)].width = w
    if wrap:
        for row in ws.iter_rows(min_row=2):
            for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "B2"; ws.auto_filter.ref = ws.dimensions
    return ws
read = lambda p: list(csv.reader(open(os.path.join(D, p), newline="")))
wb = Workbook(); ws = wb.active; ws.title = "README"
for line in [
 "Worldosphere launch workbook — generated from the planning package (tools/gen_workbook.py). Editable: add your own rows freely.",
 "Sheets: Calendar · Fallback calendar · Briefs · Reserves · Topic pool · Claims · Schedule · Pilot hours · Tracking · QA log · Change log · Asset register.",
 "Yellow cells are for you to fill in. Formula columns (rates per 1,000 engaged views) calculate automatically.",
 "Definitions and denominators: 21_Measurement_and_Iteration_Plan.md §1. Nothing in this workbook is a prediction or a published metric.",
 "Source of truth for regenerated sheets: tools/calendar_data.py, tools/ledger_data.py, data/*.csv. If you edit those, re-run the generator into a NEW file name so your filled-in sheets are not overwritten.",
 f"Generated: {dt.date(2026,10,14).isoformat()} (planning date).",
]: ws.append([line])
ws.column_dimensions["A"].width = 150
# Calendar
cal = read("data/calendar_30_days.csv"); sheet(wb, "Calendar", cal[0], cal[1:], {"Topic and angle": 45, "Chosen hook": 45, "Main payoff": 45, "Reason for placement": 50, "Verdict": 40, "Claims": 35})
fb = read("data/calendar_fallback_launch_2026-11-09.csv"); sheet(wb, "Fallback calendar", fb[0], fb[1:])
# Briefs summary
rows = []
for c in C:
    f = glob.glob(os.path.join(D, "18_Daily_Briefs", f"{c['id']}_{c['date']}_*.md"))
    pkg = glob.glob(os.path.join(D, "19_Production_Packages_Days_1-3", f"{c['id']}_*"))
    rows.append([c["day"], c["date"], c["id"], c["title"], c["pillar"], c["recipe"], c["lead"], c["verdict"], c["dur"], c["complexity"], c["test"], c["claims"], c["reserve"],
                 os.path.relpath(f[0], D) if f else "MISSING", os.path.relpath(pkg[0], D) if pkg else "—"])
sheet(wb, "Briefs", ["Day", "Date", "ID", "Title", "Pillar", "Recipe", "Lead", "Verdict", "Duration", "Complexity", "Main test", "Claims", "Reserve", "Brief file", "Full package"], rows, {"Title": 45, "Verdict": 45, "Main test": 40, "Claims": 35, "Brief file": 55})
sheet(wb, "Reserves", ["ID", "Topic", "Pillar", "Title", "Claims", "Replaces", "Spine"], [[r.get(k, "") for k in ("id", "topic", "pillar", "title", "claims", "replaces", "spine")] for r in RESERVES], {"Spine": 70, "Topic": 45})
tp = read("data/topic_pool.csv"); sheet(wb, "Topic pool", tp[0], tp[1:], {"Premise": 50, "Evidence of interest / factual support": 50, "Reason / note": 50})
cl = read("07_Survival_Logic_and_Facts/claim_ledger.csv"); sheet(wb, "Claims", cl[0] + ["Verified by", "Verified on", "Exact quote (paste)", "URL"], [r + ["", "", "", ""] for r in cl[1:]], {"Claim": 50, "Source (org, URL/ref)": 40, "Script wording": 35, "Visual implication": 30, "Exact quote (paste)": 40})
# Schedule (Scenario A deadlines)
P = dt.date.fromisoformat; rows = []
for c in C:
    d = P(c["date"]); t = lambda n: (d - dt.timedelta(days=n)).isoformat()
    pre = c["day"] <= 7
    rows.append([c["day"], c["date"], c["id"], c["complexity"].split()[0], "pre-launch" if pre else t(14), "2026-10-17" if c["day"] <= 5 else ("2026-10-21" if pre else t(10)),
                 "see 20 §2.3" if pre else t(8), "see 20 §2.3" if pre else t(7), "see 20 §2.3" if pre else t(6), "see 20 §2.3" if pre else t(4),
                 "2026-10-28" if c["day"] <= 5 else t(3), "", "", ""])
ws = sheet(wb, "Schedule", ["Day", "Publish", "ID", "Cx", "Research start", "Claims verified", "Script lock", "Animatic + VO", "Assets ready", "Animation done", "QA + export (banked)", "Actual banked date", "Bank level that day", "Notes"], rows)
for r in range(2, len(rows) + 2):
    for col in "LMN": ws[f"{col}{r}"].fill = INPUT
# Pilot hours
stages = ["Topic + research + claims", "Rules + hook + script + timed read", "Storyboard / animatic", "Assets", "Animation", "Voice", "Edit + captions", "Sound + mix", "QA + export + package"]
est = {"L": [0.5, 1.5, 0.75, 0.5, 3, 0.5, 1, 0.75, 0.75], "M": [1, 2, 1, 1.5, 5, 0.75, 1.25, 1, 0.75], "H": [1.5, 2.5, 1.5, 4, 8, 1, 1.5, 1.5, 1]}
cx = {"WS-001": "H", "WS-002": "M", "WS-003": "H"}
rows = []
for ep, k in cx.items():
    for s, e in zip(stages, est[k]): rows.append([ep, k, s, e, "", ""])
ws = sheet(wb, "Pilot hours", ["Episode", "Tier", "Stage (12 §5)", "Estimate (h)", "Actual (h)", "Notes"], rows)
n = len(rows) + 1
for r in range(2, n + 1): ws[f"E{r}"].fill = INPUT
ws[f"C{n+2}"] = "Total estimate / actual"; ws[f"D{n+2}"] = f"=SUM(D2:D{n})"; ws[f"E{n+2}"] = f"=SUM(E2:E{n})"
ws[f"C{n+3}"] = "Actual ÷ estimate (if >1.15, see 20 §5)"; ws[f"E{n+3}"] = f'=IFERROR(E{n+2}/D{n+2},"")'
# Tracking
hdr = ["ID", "Publish date", "Checkpoint", "Public views", "Engaged views", "Stayed to watch %", "AVD (s)", "APV %", "Ret. 3 s %", "Ret. 50% %", "Ret. at Fork %", "Shares", "Subscribers gained", "Comments", "Valid corrections", "Confusion comments",
       "Share rate /1k engaged", "Subscribe rate /1k engaged", "Comment rate /1k engaged", "Correction rate /100 comments", "Confusion rate /100 comments", "Notes"]
rows = [[c["id"], c["date"], cp] + [""] * 13 + [""] * 5 + [""] for c in C for cp in ("24 h", "72 h", "7 d")]
ws = sheet(wb, "Tracking", hdr, rows, {"Notes": 40}, wrap=False)
for r in range(2, len(rows) + 2):
    for col in "DEFGHIJKLMNOP": ws[f"{col}{r}"].fill = INPUT
    ws[f"Q{r}"] = f'=IFERROR(L{r}/E{r}*1000,"")'; ws[f"R{r}"] = f'=IFERROR(M{r}/E{r}*1000,"")'; ws[f"S{r}"] = f'=IFERROR(N{r}/E{r}*1000,"")'
    ws[f"T{r}"] = f'=IFERROR(O{r}/N{r}*100,"")'; ws[f"U{r}"] = f'=IFERROR(P{r}/N{r}*100,"")'
# QA log
rows = [[c["id"], "", "", "", "", "", "", "", "", "", "", ""] for c in C]
ws = sheet(wb, "QA log", ["ID", "Export file + version", "Reviewer", "Device", "Date", "S", "F", "V", "W", "A", "P (playback on export)", "U / notes"], rows, wrap=False)
dv = DataValidation(type="list", formula1='"PASS,FAIL,N/A"', allow_blank=True); ws.add_data_validation(dv)
for r in range(2, len(rows) + 2):
    for col in "BCDEFGHIJKL": ws[f"{col}{r}"].fill = INPUT
    for col in "FGHIJK": dv.add(f"{col}{r}")
# Change log (pre-launch entries from 21 §8)
import re
txt = open(os.path.join(D, "21_Measurement_and_Iteration_Plan.md")).read()
cls = [[x.strip() for x in m.split("|")[1:-1]] for m in re.findall(r"^\| CL-\d{3} .*\|$", txt, re.M)]
sheet(wb, "Change log", ["ID", "Date", "Change", "Why (evidence)", "Files"], cls + [["CL-014", "", "", "", ""]], {"Change": 60, "Why (evidence)": 60, "Files": 30})
ar = read("22_Asset_Rights_and_Sources/asset_register.csv"); sheet(wb, "Asset register", ar[0], ar[1:], {"Asset": 40, "Notes": 50})
out = os.path.join(D, "Worldosphere_Launch_Workbook.xlsx"); wb.save(out); print("wrote", out, [s.title for s in wb.worksheets])
