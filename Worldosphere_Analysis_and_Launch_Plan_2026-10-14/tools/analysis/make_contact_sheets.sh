#!/usr/bin/env bash
# Rebuild the visual evidence for the supplied reference videos LOCALLY (not committed to the public repo).
# Usage: ./make_contact_sheets.sh /path/to/REF02.mp4 REF02 [outdir]
# Requires: ffmpeg, ImageMagick (convert, montage)
set -euo pipefail
V="$1"; ID="$2"; OUT="${3:-./evidence_$ID}"; mkdir -p "$OUT/s1" "$OUT/lab" "$OUT/f10"
ffmpeg -v error -i "$V" -vf "fps=1,scale=360:-1" "$OUT/s1/%03d.jpg"
for f in "$OUT"/s1/*.jpg; do b=$(basename "$f" .jpg); t=$((10#$b - 1));
  convert "$f" -resize 288x512 -gravity North -background black -splice 0x26 -fill yellow -pointsize 22 -annotate +0+2 "$ID t=${t}s" "$OUT/lab/$b.jpg"; done
ls "$OUT"/lab/*.jpg | split -l 10 - "$OUT/grp_"
for g in "$OUT"/grp_*; do montage $(cat "$g") -tile 5x2 -geometry +4+4 -background gray20 "$OUT/sheet_$(basename "$g").jpg"; rm "$g"; done
ffmpeg -v error -i "$V" -t 3.2 -vf "fps=10,scale=216:-1" "$OUT/f10/%03d.jpg"
montage "$OUT"/f10/*.jpg -tile 8x4 -geometry +3+3 -background gray20 "$OUT/opening_10fps.jpg"
echo "Done: $OUT"
