import json, csv, sys, statistics as st
sys.path.insert(0, sys.argv[1]+"/scripts")
from shots_data import REF01, REF02
from captions_data import REF01_CAPS, REF02_CAPS
SP=sys.argv[1]; D=sys.argv[2]
OVR={"REF01":{0.59:"Character (female; Mara, inferred)",12.68:"Character (female; Mara)",14.25:"Character (female; Mara)",15.37:"Character (female; Mara)",26.51:"Character (female; Mara)",37.39:"Character (female; Mara)",40.15:"Character (whispered; Mara, inferred — pitch unreliable)",55.96:"Character (female; Mara)",57.64:"Character (female; Mara)",59.72:"Character (female; Mara)",76.62:"Character (female range; likely Mara, inferred)"},
     "REF02":{15.71:"Narrator (emphatic; raised pitch)"}}
def voice(v,t0,f0):
    for k,val in OVR[v].items():
        if abs(k-t0)<0.15: return val
    return "Narrator (male)"
stats={}
for v,shots,caps in [("REF02",REF02,REF02_CAPS),("REF01",REF01,REF01_CAPS)]:
    words=json.load(open(f"{SP}/{v}.words.json")); aud=json.load(open(f"{SP}/{v}.audio.json"))
    # transcript
    with open(f"{D}/data/{v}_transcript_phrases.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["start_s","end_s","text","speaker_attribution","median_f0_Hz(measured)","words","words_per_s"])
        for p in aud["phrases"]:
            w.writerow([p["t0"],p["t1"],p["text"],voice(v,p["t0"],p["f0_med"]),p["f0_med"],p["words"],p["wps"]])
    with open(f"{D}/data/{v}_word_timings.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["word","start_s"]); [w.writerow([a,b]) for a,b in words]
    with open(f"{D}/data/{v}_captions.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["start_s","end_s","duration_s","caption_text","words","notes"])
        for a,b,t,n in caps:
            wc=0 if t.startswith("[") else len(t.replace("/"," ").split())
            w.writerow([a,b,round(b-a,2),t,wc,n])
    rows=[]
    for s in shots:
        sid,a,b,act,cs,cam,gfx,snd,edit,q,purp,rep=s
        sp=" ".join(wd for wd,t in words if a<=t<b) or "—"
        cp=" | ".join(t for c0,c1,t,n in caps if c0<b and c1>a) or "—"
        rows.append([sid,f"{a:.2f}–{b:.2f}",round(b-a,2),sp,act,cs,cam,cp+("" if gfx=="—" else f" || Graphics: {gfx}"),snd,edit,q,purp,rep])
    hdr=["Shot","Time range (s)","Dur (s)","Spoken words (ASR, word-timed)","Visible action","Character state","Camera & composition","On-screen text (captions || graphics)","Music & sound","Edit / transition","Viewer question / emotion","Narrative purpose","Reproduction notes"]
    with open(f"{D}/data/{v}_shot_timeline.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(hdr); w.writerows(rows)
    md=["| "+" | ".join(hdr)+" |","|"+"---|"*len(hdr)]
    for r in rows: md.append("| "+" | ".join(str(x).replace("|","/") if i!=7 else str(x).replace(" || "," ⟂ ").replace(" | "," / ") for i,x in enumerate(r))+" |")
    open(f"{SP}/{v}_timeline_table.md","w").write("\n".join(md))
    durs=[s[2]-s[1] for s in shots]
    real=[c for c in caps if not c[2].startswith("[")]
    cd=[c[1]-c[0] for c in real]; cw=[len(c[2].replace("/"," ").split()) for c in real]
    stats[v]={"shots":len(shots),"mean_shot":round(st.mean(durs),2),"median_shot":round(st.median(durs),2),"min_shot":round(min(durs),2),"max_shot":round(max(durs),2),
      "shots_le_1s":sum(d<=1.0 for d in durs),"shots_1_2s":sum(1<d<=2 for d in durs),"shots_2_3s":sum(2<d<=3 for d in durs),"shots_gt_3s":sum(d>3 for d in durs),
      "caption_groups":len(real),"cap_mean_s":round(st.mean(cd),2),"cap_median_s":round(st.median(cd),2),"cap_words_mean":round(st.mean(cw),2),"cap_words_max":max(cw),
      "two_line_groups":sum("/" in c[2] for c in real),"emphasised_groups":sum(bool(c[3]) and ("red" in c[3] or "yellow" in c[3]) for c in real),
      "cap_words_per_s_mean":round(st.mean([w_/d for w_,d in zip(cw,cd)]),2)}
json.dump(stats,open(f"{D}/data/reference_measured_stats.json","w"),indent=1)
print(json.dumps(stats,indent=1))
