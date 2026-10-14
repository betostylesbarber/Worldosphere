# Re-embed regenerated tables into an assembled package document (idempotent).
import sys, os, glob, re
pdir=sys.argv[1]; md=glob.glob(pdir+"/*_Production_Package.md")[0]
s=open(md).read().split("\n")
def block(start_pred):
    for i,l in enumerate(s):
        if start_pred(l):
            j=i
            while j < len(s) and s[j].strip()!="": j+=1
            return i,j
    return None
for pred,fn in [(lambda l:l.startswith("**Runtime (provisional)"),"_script_table.md"),(lambda l:l.startswith("| Shot | Start |"),"_shot_table.md"),(lambda l:l.startswith("| # | In | Out |"),"_caption_table.md")]:
    b=block(pred)
    if b:
        new=open(os.path.join(pdir,fn)).read().split("\n")
        s=s[:b[0]]+new+s[b[1]:]
open(md,"w").write("\n".join(s)); print("refreshed",os.path.basename(md))
