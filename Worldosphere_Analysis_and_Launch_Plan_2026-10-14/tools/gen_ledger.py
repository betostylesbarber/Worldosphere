# Regenerates 07_Survival_Logic_and_Facts/claim_ledger.csv and claim_ledger.md from tools/ledger_data.py.
# Usage: python3 -I tools/gen_ledger.py <deliverables root>
import sys, csv, collections
D = sys.argv[1]; sys.path.insert(0, D + "/tools")
from ledger_data import L
H = ["Claim ID","Claim","Class","Source (org, URL/ref)","Assumptions","Necessary qualification","Script wording","Visual implication","Verification status","Episodes"]
ids = [r[0] for r in L]
assert len(ids) == len(set(ids)), "duplicate Claim IDs"
assert all(len(r) == 10 for r in L), "every row needs 10 fields"
with open(D + "/07_Survival_Logic_and_Facts/claim_ledger.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(H); w.writerows(L)
def cat(s):
    s = s.upper()
    if s.startswith("UNVERIFIED"): return "UNVERIFIED-BLOCKING" if "BLOCKING" in s else "UNVERIFIED"
    if s.startswith("DESIGN"): return "DESIGN"
    return s.split()[0].strip("—;,")
cnt = collections.Counter(cat(r[8]) for r in L)
esc = lambda x: x.replace("|", "\\|")
md = ["# Claim ledger (readable copy of `claim_ledger.csv`)", "",
"Status key: SUPPORTED · QUALIFIED · FALSE · FICTION · DESIGN RULE · **UNVERIFIED — BLOCKING** (must be verified with URL + quote + access date, or cut, before script lock). Full source URLs are in `../22_Asset_Rights_and_Sources/research_appendices/D1_facts_natural.md` and `D2_facts_home_outdoor.md`. Verified rows were confirmed from search-result extracts on 2026-10-14: confirm the live page wording before publication (QA F-03).", "",
"| " + " | ".join(H) + " |", "|" + "---|" * len(H)]
md += ["| " + " | ".join(esc(x) for x in r) + " |" for r in L]
md += ["", "Counts: " + ", ".join(f"{k}: {v}" for k, v in sorted(cnt.items()))]
open(D + "/07_Survival_Logic_and_Facts/claim_ledger.md", "w").write("\n".join(md) + "\n")
print(len(L), dict(sorted(cnt.items())))
