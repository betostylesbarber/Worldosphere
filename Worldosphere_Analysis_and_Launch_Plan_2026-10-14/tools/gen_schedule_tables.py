# Builds 20_Production_Schedule_and_Buffer.md from tools/schedule_template.md, filling the computed tables
# ({{DEADLINES}}, {{CLAIMS}}, {{FALLBACK}}) from calendar_data.py, the claim ledger and the fallback calendar CSV.
# Usage: python3 -I tools/gen_schedule_tables.py <deliverables root>
import sys, csv, datetime as dt, re
D = sys.argv[1]; sys.path.insert(0, D + "/tools")
from calendar_data import C, RESERVES
P = lambda s: dt.date.fromisoformat(s)
f = lambda d: d.strftime("%a %d %b")
blocks = {}
out = []
# 1) Per-episode backward deadlines (Scenario A, launch 31 Oct). Days 1-7 follow the pre-launch plan.
pre = {1: "Oct 18", 2: "Oct 18", 3: "Oct 19", 4: "Oct 19", 5: "Oct 20", 6: "Oct 22", 7: "Oct 23"}
out += ["| Day | Publish | ID | Cx | Research start (T-14) | Claims verified (T-10) | Script lock + timed read (T-8) | Animatic + VO (T-7) | Assets ready (T-6) | Animation done (T-4) | Edit, mix, captions (T-3) | QA + export + package (T-3, end of day) |", "|" + "---|" * 12]
for c in C:
    d = P(c["date"]); t = lambda n: f(d - dt.timedelta(days=n))
    if c["day"] in pre:
        last = "**Wed 28 Oct (gate)**" if c["day"] <= 5 else t(3)
        claims = "Verified 14 Oct; wording check Sat 17 Oct" if c["day"] <= 5 else "Verified 14 Oct; wording check Wed 21 Oct"
        out.append(f"| {c['day']} | {f(d)} | {c['id']} | {c['complexity'].split()[0]} | pre-launch (§2.2) | {claims} | {pre[c['day']]} | Oct 21–23 (VO batch) | library (§2.2) | see §2.2 | see §2.2 | {last} |")
    else:
        out.append(f"| {c['day']} | {f(d)} | {c['id']} | {c['complexity'].split()[0]} | {t(14)} | {t(10)} | {t(8)} | {t(7)} | {t(6)} | {t(4)} | {t(3)} | {t(3)} |")
blocks["DEADLINES"] = "\n".join(out); out = []
# 2) Verification deadlines for unverified claims
dates = {c["id"]: P(c["date"]) for c in C}
res = {c["id"]: c["reserve"] for c in C}
out += ["| Claim | Status | Episode(s) | First publish date | Verify by (T-10, or the pre-launch sprint) | If not verified |", "|---|---|---|---|---|---|"]
for r in csv.DictReader(open(D + "/07_Survival_Logic_and_Facts/claim_ledger.csv")):
    st = r["Verification status"]
    if not st.startswith("UNVERIFIED"): continue
    eps = re.findall(r"WS-\d{3}", r["Episodes"])
    if not eps: continue
    first = min(dates[e] for e in eps)
    due = first - dt.timedelta(days=10)
    if first <= dt.date(2026, 11, 4): due_s = "**Sat 17 Oct** (pre-launch sprint)"
    elif due <= dt.date(2026, 10, 21): due_s = "**Wed 21 Oct** (pre-launch sprint)"
    else: due_s = f(due)
    act = ("Cut the line (the episode works without it)" if re.search(r"\bif\b", st) else "Swap to " + res[eps[0]])
    if "BLOCKING" not in st: act = "Keep it as an in-story fact only (no real-world claim)" if "in-story" in st else "Add one citable source (QA F-03); low risk"
    out.append(f"| {r['Claim ID']} | {st} | {', '.join(eps)} | {f(first)} | {due_s} | {act} |")
blocks["CLAIMS"] = "\n".join(out); out = []
# 3) Fallback calendar
out += ["| Day | Date | Weekday | Episode | Title | Lead | Original slot | Pinned reason |", "|---|---|---|---|---|---|---|---|"]
for row in csv.reader(open(D + "/data/calendar_fallback_launch_2026-11-09.csv")):
    if row[0] == "Day": continue
    out.append("| " + " | ".join(row) + " |")
blocks["FALLBACK"] = "\n".join(out)
t = open(D + "/tools/schedule_template.md").read()
for k, v in blocks.items():
    assert "{{" + k + "}}" in t, k
    t = t.replace("{{" + k + "}}", v)
open(D + "/20_Production_Schedule_and_Buffer.md", "w").write(t)
print("wrote 20_Production_Schedule_and_Buffer.md")
