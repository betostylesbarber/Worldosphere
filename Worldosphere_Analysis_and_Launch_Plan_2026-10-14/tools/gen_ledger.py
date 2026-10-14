# Regenerates 07_Survival_Logic_and_Facts/claim_ledger.csv and claim_ledger.md from tools/ledger_data.py.
# Usage: python3 -I tools/gen_ledger.py <deliverables root>
import sys, csv, collections, os
D = sys.argv[1]; sys.path.insert(0, D + "/tools")
from ledger_data import L
H = ["Claim ID","Claim","Class","Source (org, URL/ref)","Assumptions","Necessary qualification","Script wording","Visual implication","Verification status","Episodes"]
# Apply verification results recorded locally (07_Survival_Logic_and_Facts/verification_results.csv).
VR = os.path.join(D, "07_Survival_Logic_and_Facts", "verification_results.csv")
if os.path.exists(VR):
    idx = {r[0]: i for i, r in enumerate(L)}
    for v in csv.DictReader(open(VR, newline="")):
        cid = (v.get("Claim ID") or "").strip()
        if not cid: continue
        assert cid in idx, f"unknown Claim ID in verification_results.csv: {cid}"
        st = v["New status"].strip().upper()
        assert st in ("SUPPORTED", "QUALIFIED", "FALSE", "UNVERIFIED — BLOCKING", "UNVERIFIED"), f"{cid}: bad status {st}"
        if st in ("SUPPORTED", "QUALIFIED"):
            for k in ("Source URL", "Exact quote", "Access date", "Verified by"):
                assert v.get(k, "").strip(), f"{cid}: '{k}' is required to mark a claim {st}"
        r = list(L[idx[cid]])
        r[3] = r[3] + f" · VERIFIED {v['Access date'].strip()} by {v['Verified by'].strip()}: {v['Source URL'].strip()} — \"{v['Exact quote'].strip()}\""
        if v.get("Qualification", "").strip(): r[5] = v["Qualification"].strip()
        if v.get("New script wording", "").strip(): r[6] = v["New script wording"].strip()
        r[8] = st
        L[idx[cid]] = tuple(r)
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
