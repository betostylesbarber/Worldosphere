import sys, subprocess, numpy as np, json
from PIL import Image, ImageDraw, ImageFont
v, out = sys.argv[1], sys.argv[2]
Y0,Y1=780,904
raw=subprocess.run(["ffmpeg","-v","error","-i",v,"-vf",f"crop=720:{Y1-Y0}:0:{Y0}","-pix_fmt","rgb24","-f","rawvideo","-"],capture_output=True).stdout
fr=np.frombuffer(raw,np.uint8).reshape(-1,Y1-Y0,720,3)
# caption mask: bright near-white OR saturated red/yellow text pixels
def mask(f):
    f=f.astype(int); r,g,b=f[...,0],f[...,1],f[...,2]
    white=(f.min(2)>215)
    red=(r>170)&(g<90)&(b<90)
    yel=(r>200)&(g>150)&(b<80)
    return white|red|yel
ms=[mask(f) for f in fr]
cnt=np.array([m.sum() for m in ms])
events=[]; prev=None; start=0
def sig(m): return m
for i,m in enumerate(ms):
    on = cnt[i]>150
    if prev is None:
        prev=(on,m); start=i; continue
    pon,pm=prev
    changed = (on!=pon) or (on and pon and (np.logical_xor(m,pm).sum() > 0.35*max(m.sum(),pm.sum())))
    if changed:
        events.append((start,i-1,pon)); start=i
    prev=(on,m)
events.append((start,len(ms)-1,prev[0]))
# merge tiny events (<3 frames) into neighbors
ev=[e for e in events if e[1]-e[0]>=2 or e[2]]
caps=[(s,e) for s,e,on in ev if on]
print(len(caps),"caption events")
json.dump([(s/30,(e+1)/30) for s,e in caps],open(out+".json","w"))
font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",18)
H=Y1-Y0; per=40
for k in range(0,len(caps),per):
    chunk=caps[k:k+per]
    img=Image.new("RGB",(2*(720+150), ((len(chunk)+1)//2)*(H//1+4)),(30,30,30)); d=ImageDraw.Draw(img)
    for j,(s,e) in enumerate(chunk):
        mid=(s+e)//2; x=(j%2)*(870); y=(j//2)*(H+4)
        d.text((x+4,y+H//2-10),f"{s/30:5.2f}-{(e+1)/30:5.2f}",fill=(255,255,0),font=font)
        img.paste(Image.fromarray(fr[mid]),(x+150,y))
    img.save(f"{out}_{k//per+1}.jpg",quality=85); print(f"{out}_{k//per+1}.jpg")
