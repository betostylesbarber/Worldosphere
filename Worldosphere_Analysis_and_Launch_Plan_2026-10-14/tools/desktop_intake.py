#!/usr/bin/env python3
"""Read-only intake of the Desktop "Worldosphere" folder (run it on your own computer).

The cloud session that built this package could not see your Desktop. This script closes that gap.
It lists everything in the folder, detects copies of the two reference videos (by MD5), reads the text
of plain-text and .docx files, and flags files whose names or text mention the subject of a planned
episode (WS-001 to WS-030), so you can check for subjects you've already covered.

It never modifies, moves or deletes anything in the folder. It writes one new report file into this
package folder (a new timestamped name, so nothing is overwritten).

Usage (Python 3.8+, standard library only; ffprobe is optional, for video durations):
    python3 tools/desktop_intake.py "~/Desktop/Worldosphere"
    python3 tools/desktop_intake.py "C:\\Users\\<you>\\Desktop\\Worldosphere"      (Windows)
"""
import csv, datetime as dt, hashlib, os, re, shutil, subprocess, sys, zipfile

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF_MD5 = {"9213c9adc3d2bfbb9cd20e532137ba36": "REF01 (The Last Farm, Part 2)",
           "232bdcc43a43c29dd4afe9c396352d0c": "REF02 (The Last Farm, Part 1)"}
TYPES = {"video": {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}, "audio": {".wav", ".mp3", ".aac", ".m4a", ".flac", ".ogg"},
         "image": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".psd", ".svg", ".ai", ".tif", ".tiff"},
         "document": {".txt", ".md", ".docx", ".doc", ".pdf", ".rtf", ".pages", ".odt", ".csv", ".xlsx", ".srt", ".ass"},
         "project": {".aep", ".prproj", ".drp", ".moho", ".blend", ".tvpp", ".fla", ".kra", ".clip", ".afdesign", ".afphoto"},
         "font": {".ttf", ".otf", ".woff", ".woff2"}}
TEXT_EXT = {".txt", ".md", ".csv", ".srt", ".ass", ".rtf"}
# Distinctive subject keywords per planned episode (lower case; matched as whole words or phrases).
KEYWORDS = {
 "WS-001": ["halloween", "costume", "breath"], "WS-002": ["sinking car", "car in water", "submerged", "window punch", "seatbelt"],
 "WS-003": ["superstore", "costco", "warehouse store", "loading dock"], "WS-004": ["earthquake", "doorway", "drop, cover"],
 "WS-005": ["generator", "carbon monoxide"], "WS-006": ["airplane", "plane cabin", "flight", "row 31"], "WS-007": ["roof or basement", "attic"],
 "WS-008": ["tornado", "overpass"], "WS-009": ["boat", "harbor", "harbour", "can't swim"], "WS-010": ["power outage", "blackout", "freezer"],
 "WS-011": ["high-rise", "floor 14", "stairwell"], "WS-012": ["house fire", "close the door", "close before you doze"],
 "WS-013": ["theater", "theatre", "cinema"], "WS-014": ["seven days", "week of warning"], "WS-015": ["antarctic", "research station", "station zero"],
 "WS-016": ["station zero"], "WS-017": ["rip current"], "WS-018": ["meteor", "asteroid", "chelyabinsk"], "WS-019": ["elevator"],
 "WS-020": ["solar storm", "aurora", "carrington"], "WS-021": ["thin ice", "frozen pond", "fell through"], "WS-022": ["subway", "metro", "tunnel"],
 "WS-023": ["wildfire", "evacuation"], "WS-024": ["safe room", "who was bitten"], "WS-025": ["avalanche"], "WS-026": ["airport", "gate 22"],
 "WS-027": ["grease fire", "turkey fryer", "thanksgiving"], "WS-028": ["crowd crush", "black friday", "crowd surge"],
 "WS-029": ["blizzard", "snowed in", "stranded"], "WS-030": ["last bus", "bus depot"],
 "REFERENCE": ["the last farm", "stickocalypse", "eli", "rusty", "mara"],
}

def kind(ext):
    for k, v in TYPES.items():
        if ext in v: return k
    return "other"

def md5(path, limit=4 * 1024**3):
    if os.path.getsize(path) > limit: return "(skipped: >4 GB)"
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()

def duration(path):
    if not shutil.which("ffprobe"): return ""
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        return f"{float(out):.2f} s" if out else ""
    except Exception:
        return ""

def text_of(path, ext):
    try:
        if ext in TEXT_EXT:
            with open(path, "r", encoding="utf-8", errors="ignore") as f: return f.read(2_000_000)
        if ext == ".docx":
            with zipfile.ZipFile(path) as z:
                xml = z.read("word/document.xml").decode("utf-8", "ignore")
            return re.sub(r"<[^>]+>", " ", xml)
    except Exception:
        return ""
    return ""

def hits(text):
    t = " " + re.sub(r"\s+", " ", text.lower()) + " "
    found = {}
    for ep, words in KEYWORDS.items():
        m = [w for w in words if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", t)]
        if m: found[ep] = m
    return found

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    root = os.path.abspath(os.path.expanduser(sys.argv[1]))
    if not os.path.isdir(root):
        sys.exit(f"Not a folder: {root}")
    titles = {}
    cal = os.path.join(PKG, "data", "calendar_30_days.csv")
    if os.path.exists(cal):
        for r in csv.DictReader(open(cal, newline="", encoding="utf-8")):
            titles[f"WS-{int(r['Day']):03d}"] = f"{r['Date']} · {r['Recommended title']}"
    rows, overlaps, refs, counts = [], {}, [], {}
    pkg_name = os.path.basename(PKG)
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d != pkg_name and not d.startswith(".")]   # skip this package if it was copied in
        for fn in sorted(fns):
            if fn.startswith("."): continue
            p = os.path.join(dp, fn); rel = os.path.relpath(p, root); ext = os.path.splitext(fn)[1].lower(); k = kind(ext)
            st = os.stat(p); counts[k] = counts.get(k, 0) + 1
            note = ""
            if k == "video":
                h = md5(p); d = duration(p)
                if h in REF_MD5: refs.append((rel, REF_MD5[h])); note = f"= {REF_MD5[h]} (reference; keep separate)"
                note = (note + " " + d).strip()
            found = hits(fn.replace("_", " ").replace("-", " ") + " " + text_of(p, ext))
            for ep, w in found.items(): overlaps.setdefault(ep, []).append((rel, w))
            rows.append((rel, k, f"{st.st_size/1_048_576:.2f}", dt.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d"), note))
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    out = os.path.join(PKG, f"Desktop_Folder_Intake_Report_{stamp}.md")
    L = [f"# Desktop folder intake report ({stamp})", "", f"Folder scanned (read-only): `{root}`", "",
         "Nothing in the scanned folder was changed. Review each flagged item and log decisions in the change log (21 §8).", "",
         "## Summary", "", "| Type | Files |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(counts.items())] + [""]
    L += ["## Copies of the reference videos", ""] + ([f"- `{r}` = {n}. Keep it out of the public repository (22 §1)." for r, n in refs] or ["- None found."]) + [""]
    L += ["## Possible overlaps with planned episodes", "",
          "A keyword match only means the subject *may* already be covered. Open the file and decide: keep the episode (the angle differs), adjust its angle, or swap in a reserve (16).", ""]
    if overlaps:
        L += ["| Episode | Planned | File | Matched words |", "|---|---|---|---|"]
        for ep in sorted(overlaps):
            for rel, w in overlaps[ep]:
                L.append(f"| {ep} | {titles.get(ep, 'reference material' if ep == 'REFERENCE' else '')} | `{rel}` | {', '.join(w)} |")
    else:
        L.append("- No keyword matches.")
    L += ["", "## Full inventory", "", "| File | Type | Size (MB) | Modified | Notes |", "|---|---|---|---|---|"]
    L += [f"| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} | {r[4]} |" for r in rows]
    L += ["", "## Next steps", "- Existing brand assets (logos, fonts, characters) → compare with 08/09 and decide what to keep.",
          "- Existing scripts or videos on a planned subject → check the angle against the brief; log any swap.",
          "- Existing published-video list → add it to the workbook *Tracking* sheet as the channel baseline (23 L4)."]
    with open(out, "x", encoding="utf-8") as f: f.write("\n".join(L) + "\n")
    print(f"Scanned {len(rows)} files. Report: {out}")

if __name__ == "__main__":
    main()
