import sys, subprocess, numpy as np, json
v=sys.argv[1]; W,H=72,128
raw=subprocess.run(["ffmpeg","-v","error","-i",v,"-vf",f"scale={W}:{H}","-pix_fmt","rgb24","-f","rawvideo","-"],capture_output=True).stdout
fr=np.frombuffer(raw,np.uint8).reshape(-1,H,W,3).astype(np.float32)
n=len(fr); fps=30
# metrics: mean abs diff, and histogram (per-channel 16 bins) chi distance
d=np.zeros(n); hd=np.zeros(n)
def hist(f): return np.concatenate([np.histogram(f[...,c],bins=16,range=(0,256))[0] for c in range(3)])/(W*H)
hs=[hist(f) for f in fr]
for i in range(1,n):
    d[i]=np.abs(fr[i]-fr[i-1]).mean()
    hd[i]=0.5*np.abs(hs[i]-hs[i-1]).sum()
# local-peak detection
cands=[]
for i in range(1,n):
    lo=max(1,i-15); hi=min(n,i+16)
    med=np.median(d[lo:hi])
    if d[i]>max(6, 3.0*med) and d[i]==d[max(1,i-2):min(n,i+3)].max():
        cands.append((i, round(i/fps,3), round(float(d[i]),1), round(float(hd[i]),3)))
json.dump({"n":n,"d":d.round(2).tolist(),"hd":hd.round(3).tolist(),"cands":cands},open(sys.argv[2],"w"))
print(n, "frames;", len(cands),"candidate cuts")
for c in cands: print(c)
# motion: fraction of frames with any visible change (mean abs diff > 0.5)
print("frames with change>0.5:", round(float((d[1:]>0.5).mean()),3), " >2:", round(float((d[1:]>2).mean()),3))
