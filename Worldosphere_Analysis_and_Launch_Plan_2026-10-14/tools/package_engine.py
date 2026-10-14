# Package timing engine: computes provisional line timings from word counts at a target speaking rate,
# splits captions to the Worldosphere rules (<=7 words, <=2 lines of <=24 chars, min display 0.3+0.22*words),
# and writes shot list tables, ASS + SRT caption files and a cue sheet. All timings are PROVISIONAL until
# re-synced to the recorded voice-over.
import math, re

WPS = 2.85          # ~171 wpm narrator (target band 160-175 wpm)
COMMA = 0.18        # pause per comma/colon inside a line
STOP = 0.30         # pause per internal full stop / ellipsis
LEAD = 0.083        # captions appear 2 frames (24 fps) before the words

def clean(text):
    return re.sub(r"\s*\|\s*", " ", text).strip()

def line_dur(text):
    text = clean(text)
    w = len(text.split())
    c = text.count(",") + text.count(":") + text.count("—")
    s = max(0, len(re.findall(r"(?<!Mr)(?<!Mrs)(?<!Dr)[.?!…](?=\s)", text)))
    return w / WPS + c * COMMA + s * STOP

WEAK = {"a","an","the","to","of","his","her","their","its","and","or","on","in","at","with","for","from","by","into","your","my","our","is","was","be","than","that","as","you","can't","can"}
def _weak_end(seg):
    return seg.split()[-1].strip(",.:;!?…").lower() in WEAK

def wrap_ok(text, maxc=24):
    words = text.split()
    if len(text) <= maxc: return [text]
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if len(a) <= maxc and len(b) <= maxc:
            score = abs(len(b) - len(a)) * 0.5 + (0 if len(a) <= len(b) else 2) + (8 if _weak_end(a) else 0) - (6 if a.endswith((",", ":", ".", "—")) else 0)
            if best is None or score < best[0]: best = (score, [a, b])
    return best[1] if best else None

def _fits(words):
    return len(words) <= 7 and wrap_ok(" ".join(words)) is not None

def _split_part(words):
    if _fits(words): return [" ".join(words)]
    n = len(words); best = None
    for k in range(2, n + 1):
        # dynamic search over boundaries for k groups
        import itertools
        if k > 4: break
        for cuts in itertools.combinations(range(1, n), k - 1):
            segs = [words[a:b] for a, b in zip((0,) + cuts, cuts + (n,))]
            if not all(_fits(sg) for sg in segs): continue
            sizes = [len(sg) for sg in segs]
            score = (max(sizes) - min(sizes)) + sum(8 for sg in segs[:-1] if _weak_end(" ".join(sg))) + k * 3
            if best is None or score < best[0]: best = (score, segs)
        if best: break
    if not best: return [" ".join(words[i:i+5]) for i in range(0, n, 5)]
    return [" ".join(sg) for sg in best[1]]

def split_groups(text):
    if "|" in text:
        return [g.strip() for g in text.split("|") if g.strip()]
    """Split a spoken line into caption groups (<=7 words, <=2 lines of <=24 chars), preferring punctuation
    boundaries, balanced sizes and never ending a group on a weak word."""
    parts = re.split(r"(?<!\bMr\.)(?<!\bMrs\.)(?<!\bDr\.)(?<=[.?!…:])\s+", text.strip())
    groups = []
    for p in parts:
        sub = re.split(r"(?<=,)\s+", p)
        # keep comma parts together when the whole part fits
        if _fits(p.split()): groups.append(p); continue
        buf = []
        for sp in sub:
            cand = buf + sp.split()
            if _fits(cand): buf = cand
            else:
                if buf: groups.extend(_split_part(buf))
                buf = sp.split()
        if buf: groups.extend(_split_part(buf))
    return groups

def build(shots, fps=24):
    """shots: list of dict(id, min, pre, lines=[(speaker,text,emph,lane)], post, ...). Returns timed shots, captions, total."""
    t = 0.0; out = []; caps = []
    for s in shots:
        start = t; cur = t + s.get("pre", 0.0); timed = []
        for (spk, text, emph, lane) in s.get("lines", []):
            d = line_dur(text); ls, le = cur, cur + d
            timed.append((spk, clean(text), round(ls, 2), round(le, 2)))
            groups = split_groups(text); wc = [len(g.split()) for g in groups]; tot = sum(wc)
            gs = ls
            for g, n in zip(groups, wc):
                gd = d * n / tot
                ge = gs + gd
                caps.append(dict(start=max(0, gs - LEAD), end=ge + 0.10, text=g, spk=spk, lane=lane,
                                 emph=[e for e in (emph or []) if e.rstrip("!").lower() in g.lower()]))
                gs = ge
            cur = le + s.get("gap", 0.25)
        end = max(start + s["min"], cur - s.get("gap", 0.25) + s.get("post", 0.3))
        s2 = dict(s); s2.update(start=round(start, 2), end=round(end, 2), dur=round(end - start, 2), timed=timed)
        out.append(s2); t = end
    # enforce min display: extend a caption until the next one starts, if needed (never overlap)
    for i, c in enumerate(caps):
        need = max(0.5, 0.3 + 0.22 * len(c["text"].split()))
        nxt = caps[i + 1]["start"] if i + 1 < len(caps) else c["end"] + 5
        if c["end"] - c["start"] < need: c["end"] = min(c["start"] + need, nxt - 0.02)
        c["end"] = min(c["end"], nxt - 0.02)
        c["ok"] = (c["end"] - c["start"]) >= need - 0.05
    return out, caps, round(t, 2)

def ts_srt(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
def ts_ass(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

SPK = {"KAI": "&H30C2F2&", "MIA": "&HE08EB4&", "TESS": "&H288CF2&", "OWEN": "&H50A67F&", "GUEST": "&HB6B39F&"}
def write_captions(caps, srt_path, ass_path, ass_header, extras=()):
    with open(srt_path, "w") as f:
        for i, c in enumerate(caps, 1):
            lines = wrap_ok(c["text"]) or [c["text"]]
            spk = "" if c["spk"] == "NARR" else f"[{c['spk']}] "
            f.write(f"{i}\n{ts_srt(c['start'])} --> {ts_srt(c['end'])}\n{spk}{chr(10).join(lines)}\n\n")
    with open(ass_path, "w") as f:
        f.write(ass_header)
        for (a, b, style, text) in extras:
            f.write(f"Dialogue: 2,{ts_ass(a)},{ts_ass(b)},{style},,0,0,0,,{text}\n")
        for c in caps:
            lines = wrap_ok(c["text"]) or [c["text"]]
            txt = r"\N".join(lines)
            for e in c["emph"]:
                tint = r"{\1c&H7A8AFF&}" if e.endswith("!") else r"{\1c&H47C2FF&}"
                w = e.rstrip("!")
                txt = re.sub(re.escape(w), lambda m, t=tint: t + m.group(0) + "{\\1c&HFFFFFF&}", txt, count=1, flags=re.I)
            lane = c["lane"]
            if c["spk"] == "NARR":
                style = "N1_LaneB" if lane == "B" else "N1_Narration"
                f.write(f"Dialogue: 0,{ts_ass(c['start'])},{ts_ass(c['end'])},{style},,0,0,0,,{{\\fad(83,0)}}{txt}\n")
            else:
                style = "D1_Right" if lane.endswith("right") else "D1_Left"
                chip_style = "S1_Chip"
                col = SPK.get(c["spk"], SPK["GUEST"])
                f.write(f"Dialogue: 1,{ts_ass(c['start'])},{ts_ass(c['end'])},{chip_style},,0,0,{742 + (71 if len(lines) > 1 else 0)},,{{\\3c{col}\\4c{col}}}{c['spk']}\n")
                f.write(f"Dialogue: 0,{ts_ass(c['start'])},{ts_ass(c['end'])},{style},,0,0,0,,{{\\fad(83,0)}}{txt}\n")
