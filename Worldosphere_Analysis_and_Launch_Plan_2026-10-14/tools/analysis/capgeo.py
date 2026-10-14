import sys, subprocess, numpy as np
from PIL import Image
v=sys.argv[1]; times=[float(x) for x in sys.argv[2].split(",")]
for t in times:
    raw=subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",v,"-frames:v","1","-pix_fmt","rgb24","-f","rawvideo","-"],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(1280,720,3).astype(int)
    # near-white or saturated caption colours inside y band 600-1000
    band=f[560:1000]
    white=(band.min(2)>225)
    rows=np.where(white.sum(1)>3)[0]; cols=np.where(white.sum(0)>1)[0]
    if len(rows)==0: print(t,"none"); continue
    # group rows into lines
    lines=[]; s=rows[0]; p=rows[0]
    for r in rows[1:]:
        if r-p>4: lines.append((s,p)); s=r
        p=r
    lines.append((s,p))
    lines=[(a+560,b+560) for a,b in lines if b-a>8]
    print(f"t={t}: lines(y0,y1,h)={[(a,b,b-a+1) for a,b in lines]} x-range=({cols.min()},{cols.max()}) width={cols.max()-cols.min()+1}px of 720 -> center_x={(cols.min()+cols.max())/2:.0f}")
