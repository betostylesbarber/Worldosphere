import sys, json, wave, numpy as np
v=sys.argv[1]; SP=sys.argv[2]
def load(p):
    with wave.open(p) as w:
        return np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768, w.getframerate()
a,sr=load(f"{SP}/media/{v}.22k.wav")
asr=json.load(open(f"{SP}/{v}.asr.json"))
# --- pitch per ASR segment, and per sentence chunk using token timestamps
def f0_track(x, sr, fmin=70, fmax=400):
    hop=int(0.01*sr); win=int(0.04*sr); out=[]
    for i in range(0, len(x)-win, hop):
        f=x[i:i+win]*np.hanning(win)
        if np.sqrt((f**2).mean())<0.01: continue
        ac=np.correlate(f,f,'full')[win-1:]
        lo=int(sr/fmax); hi=int(sr/fmin)
        if ac[0]<=0: continue
        seg=ac[lo:hi]; k=np.argmax(seg)+lo
        if ac[k]/ac[0]>0.45: out.append(sr/k)
    return np.array(out)
def chunk_f0(t0,t1):
    x=a[int(t0*sr):int(t1*sr)]; f=f0_track(x,sr)
    return (round(float(np.median(f)),1) if len(f)>5 else None, len(f))
# split tokens into phrases at gaps > 0.35s or sentence punctuation
phr=[]
for s in asr:
    toks=s["tokens"]; cur=[]; 
    for j,tk in enumerate(toks):
        cur.append(tk)
        end = (j==len(toks)-1) or (toks[j+1]["s"]-tk["s"]>0.6) or tk["t"].strip() in (".","?","!")
        if end:
            txt="".join(t["t"] for t in cur).replace("▁"," ").strip()
            t0=cur[0]["s"]; t1=(toks[j+1]["s"] if j+1<len(toks) else s["end"])
            phr.append((round(t0,2),round(min(t1,s["end"]),2),txt)); cur=[]
res=[]
for t0,t1,txt in phr:
    f,nv=chunk_f0(t0,t1); nw=len(txt.split())
    res.append({"t0":t0,"t1":t1,"text":txt,"f0_med":f,"voiced_frames":nv,"words":nw,"wps":round(nw/max(t1-t0,0.01),2)})
    print(f"{t0:6.2f}-{t1:6.2f} f0={f} n={nv:4d} w={nw:2d} wps={nw/max(t1-t0,0.01):4.1f} | {txt}")
# overall speech stats
tot_words=sum(r["words"] for r in res); speech_time=sum(s["end"]-s["start"] for s in asr)
dur=len(a)/sr
print(f"TOTAL words={tot_words} dur={dur:.2f}s speech_active={speech_time:.2f}s ({100*speech_time/dur:.0f}%) wpm_overall={60*tot_words/dur:.0f} wpm_during_speech={60*tot_words/speech_time:.0f}")
# --- gaps between VAD segments
gaps=[(round(asr[i]["end"],2), round(asr[i+1]["start"],2), round(asr[i+1]["start"]-asr[i]["end"],2)) for i in range(len(asr)-1)]
print("GAPS >0.4s:", [g for g in gaps if g[2]>0.4])
print("lead-in silence before first speech:", asr[0]["start"], " tail after last speech:", round(dur-asr[-1]["end"],2))
# --- spectral flux onsets
n=1024; hop=256; win=np.hanning(n)
S=np.array([np.abs(np.fft.rfft(a[i:i+n]*win)) for i in range(0,len(a)-n,hop)])
L=np.log1p(S*10)
flux=np.maximum(L[1:]-L[:-1],0).sum(1); flux=np.concatenate([[0],flux])
t=np.arange(len(flux))*hop/sr
on=[]
for i in range(5,len(flux)-5):
    w=flux[max(0,i-40):i+40]
    if flux[i]==flux[i-4:i+5].max() and flux[i]>np.median(w)+3.0*np.std(w):
        on.append(round(float(t[i]),2))
print("STRONG ONSETS:", on)
# low-freq (<120 Hz) energy and high-freq (>4k) energy per 0.5s
freqs=np.fft.rfftfreq(n,1/sr)
lf=S[:,freqs<120].sum(1); hf=S[:,freqs>4000].sum(1)
step=int(0.5*sr/hop)
print("LF/HF per 0.5s (relative dB):")
lfdb=20*np.log10(np.array([lf[i:i+step].mean() for i in range(0,len(lf),step)])+1e-6)
hfdb=20*np.log10(np.array([hf[i:i+step].mean() for i in range(0,len(hf),step)])+1e-6)
print("LF", " ".join(f"{x-lfdb.max():.0f}" for x in lfdb))
print("HF", " ".join(f"{x-hfdb.max():.0f}" for x in hfdb))
json.dump({"phrases":res,"gaps":gaps,"onsets":on,"lf":lfdb.round(1).tolist(),"hf":hfdb.round(1).tolist()},open(f"{SP}/{v}.audio.json","w"),indent=1)
