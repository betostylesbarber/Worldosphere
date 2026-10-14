import sys, csv, importlib
D=sys.argv[1]; mod=sys.argv[2]; outdir=sys.argv[3]
sys.path.insert(0, D+"/tools")
from package_engine import build, write_captions, wrap_ok
S=importlib.import_module(mod).SHOTS
shots, caps, total = build(S)
head=open(D+"/09_Typography_and_Captions/worldosphere_caption_styles.ass").read().split("[Events]")[0]+"[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
import os; os.makedirs(outdir, exist_ok=True)
pre=os.path.basename(outdir).split("_")[0]
extras=[]
for sh in shots:
    for (ra, rb, style, text) in sh.get("txt", []):
        a = sh["start"] + ra; b = sh["start"] + rb if rb is not None else sh["end"]
        extras.append((a, b, style, text))
T=getattr(importlib.import_module(mod),"TIMER",None)
if T:
    st={s["id"]:s for s in shots}; t0=st[T["start_shot"]]["start"]; t1=st[T["end_shot"]]["end"]; v=T["start_value"]; tt=t0
    while tt < t1 - 0.01:
        nxt=min(tt+1.0,t1); extras.append((tt,nxt,"T1_Timer",f"{T['prefix']}{int(v)//60}:{int(v)%60:02d}")); v-=1; tt=nxt
write_captions(caps, f"{outdir}/{pre}_captions_PROVISIONAL.srt", f"{outdir}/{pre}_captions_PROVISIONAL.ass", head, extras)
# shot list csv + md
hdr=["Shot","Start","End","Dur","Camera & composition","Action / performance","Spoken (speaker: line @ start–end)","Graphics / on-screen text","Sound","Transition","Continuity / notes"]
rows=[]
for s in shots:
    spoken=" / ".join(f"{spk}: \"{t}\" @{a:.2f}–{b:.2f}" for spk,t,a,b in s["timed"]) or "— (no line)"
    rows.append([s["id"],f"{s['start']:.2f}",f"{s['end']:.2f}",f"{s['dur']:.2f}",s["cam"],s["act"],spoken,s["gfx"],s["snd"],s["trans"],s["cont"]])
with open(f"{outdir}/{pre}_shot_list.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(hdr); w.writerows(rows)
md=["| "+" | ".join(hdr)+" |","|"+"---|"*len(hdr)]
for r in rows: md.append("| "+" | ".join(str(x).replace("|","/").replace("\n"," ") for x in r)+" |")
open(f"{outdir}/_shot_table.md","w").write("\n".join(md))
# captions table
cm=["| # | In | Out | Dur | Speaker | Lane | Caption (as it breaks) | Emphasis | Reading-time rule met |","|---|---|---|---|---|---|---|---|---|"]
for i,c in enumerate(caps,1):
    lines=" / ".join(wrap_ok(c["text"]) or [c["text"]])
    cm.append(f"| {i} | {c['start']:.2f} | {c['end']:.2f} | {c['end']-c['start']:.2f} | {c['spk']} | {c['lane']} | {lines} | {', '.join(e.rstrip('!')+(' (threat tint)' if e.endswith('!') else ' (amber)') for e in c['emph']) or '—'} | {'yes' if c['ok'] else 'NO — extend or rewrite'} |")
open(f"{outdir}/_caption_table.md","w").write("\n".join(cm))
# script with reading estimate
words=sum(len(t.split()) for s in shots for _,t,_,_ in s["timed"]); speech=sum(b-a for s in shots for _,_,a,b in s["timed"])
sc=[f"**Runtime (provisional): {total:.1f} s · spoken words: {words} · speaking time ≈ {speech:.1f} s ({60*words/max(speech,1):.0f} wpm while speaking; {60*words/total:.0f} wpm overall) · reading model: {__import__("package_engine").WPS} words/s + 0.18 s per comma/colon + 0.30 s per internal stop.**","","| Time | Speaker | Line |","|---|---|---|"]
for s in shots:
    for spk,t,a,b in s["timed"]: sc.append(f"| {a:05.2f}–{b:05.2f} | {spk} | {t} |")
    if not s["timed"]: sc.append(f"| {s['start']:05.2f}–{s['end']:05.2f} | — | *(no dialogue: {s['cam'][:90]}…)* |")
open(f"{outdir}/_script_table.md","w").write("\n".join(sc))
bad=[c for c in caps if not c["ok"]]
print("total",total,"words",words,"speech",round(speech,1),"caption groups",len(caps),"rule failures",len(bad))
for c in bad: print("  FAIL",c)
