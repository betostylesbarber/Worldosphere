import sys, os, glob, csv, re
pdir=sys.argv[1]; md=glob.glob(pdir+"/*_Production_Package.md")[0]; pre=os.path.basename(pdir).split("_")[0]
s=open(md).read()
for key,fn in [("{{SCRIPT}}","_script_table.md"),("{{SHOTS}}","_shot_table.md"),("{{CAPTIONS}}","_caption_table.md")]:
    if key in s: s=s.replace(key,open(os.path.join(pdir,fn)).read())
# emphasis check
cap=open(os.path.join(pdir,"_caption_table.md")).read().splitlines()[2:]
em=[(float(r.split("|")[2]),r.split("|")[8].strip()) for r in cap if r.split("|")[8].strip()!="—"]
gaps=[round(b[0]-a[0],2) for a,b in zip(em,em[1:])]
s=re.sub(r"Emphasis budget: \d+ emphasised groups",f"Emphasis budget: {len(em)} emphasised groups",s)
open(md,"w").write(s)
# sound cues csv from the cue table in section 10
rows=[]; inside=False
for line in s.splitlines():
    if line.startswith("| Time (s, provisional) | Cue"): inside=True; continue
    if inside:
        if not line.startswith("|"): break
        if line.startswith("|---"): continue
        rows.append([c.strip().replace("**","") for c in line.strip("|").split("|")])
with open(os.path.join(pdir,f"{pre}_sound_cues.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["time_s_provisional","cue","level_note"]); w.writerows(rows)
print(pre,"emphasis groups",len(em),"min gap",min(gaps) if gaps else None,"cues",len(rows))
