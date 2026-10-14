import sys, json, wave, numpy as np
v=sys.argv[1]; SP=sys.argv[2]
with wave.open(f"{SP}/media/{v}.22k.wav") as w:
    a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768; sr=w.getframerate()
asr=json.load(open(f"{SP}/{v}.asr.json"))
def db(x): return 20*np.log10(np.sqrt((x**2).mean())+1e-9)
# 0.5 s RMS timeline
tl=[round(db(a[i:i+sr//2]),1) for i in range(0,len(a),sr//2)]
print("RMS dBFS per 0.5s:", " ".join(f"{x:.0f}" for x in tl))
# gaps (non-speech) levels incl. head/tail
segs=[(s["start"],s["end"]) for s in asr]
gaps=[(0,segs[0][0])]+[(segs[i][1],segs[i+1][0]) for i in range(len(segs)-1)]+[(segs[-1][1],len(a)/sr)]
for g0,g1 in gaps:
    if g1-g0>=0.3:
        x=a[int((g0+0.05)*sr):int((g1-0.05)*sr)]
        # spectral flatness (tonal vs noise) and dominant freq
        S=np.abs(np.fft.rfft(x*np.hanning(len(x))))+1e-9; f=np.fft.rfftfreq(len(x),1/sr)
        band=(f>60)&(f<4000); flat=np.exp(np.log(S[band]).mean())/S[band].mean()
        pk=f[band][np.argsort(S[band])[-5:]][::-1]
        print(f"gap {g0:6.2f}-{g1:6.2f} ({g1-g0:.2f}s) level={db(x):6.1f} dBFS flatness={flat:.3f} top_freqs={[int(p) for p in pk]}")
sp=np.concatenate([a[int(s*sr):int(e*sr)] for s,e in segs])
print(f"speech-segment RMS={db(sp):.1f} dBFS; whole-file RMS={db(a):.1f}")
