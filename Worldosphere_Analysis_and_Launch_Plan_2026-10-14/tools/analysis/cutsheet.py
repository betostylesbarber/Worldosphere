import sys, json, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
v, cj, out = sys.argv[1], sys.argv[2], sys.argv[3]
c = json.load(open(cj))["cands"]
W,H=110,196
raw=subprocess.run(["ffmpeg","-v","error","-i",v,"-vf",f"scale={W}:{H}","-pix_fmt","rgb24","-f","rawvideo","-"],capture_output=True).stdout
fr=np.frombuffer(raw,np.uint8).reshape(-1,H,W,3)
font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
per=24; cols=6
for s in range(0,len(c),per):
    chunk=c[s:s+per]; rows=(len(chunk)+cols-1)//cols
    img=Image.new("RGB",(cols*(2*W+12),rows*(H+20)),(40,40,40)); dr=ImageDraw.Draw(img)
    for k,(i,t,dd,hh) in enumerate(chunk):
        x=(k%cols)*(2*W+12); y=(k//cols)*(H+20)
        img.paste(Image.fromarray(fr[i-1]),(x,y+18)); img.paste(Image.fromarray(fr[i+1 if i+1<len(fr) else i]),(x+W+2,y+18))
        dr.text((x+2,y+1),f"#{s+k+1} {t:.2f}s",fill=(255,255,0),font=font)
    img.save(f"{out}_{s//per+1}.jpg",quality=88)
    print(f"{out}_{s//per+1}.jpg")
