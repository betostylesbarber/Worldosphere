// Worldosphere SVG drawing kit for style frames and motion proofs (original artwork; prototype quality).
// All shapes are procedural vectors in the brand palette. Characters follow the bible: bean head + brows, noodle limbs, ink outline.
const INK = "#161A22", TEAL = "#1F3A44", SLATE = "#3D5560", FOG = "#9FB3B6", PAPER = "#F2EBDD",
  AMBER = "#F5A524", RED = "#E5483B", CYAN = "#4FC3D9", GREEN = "#6BBF59";
const NS = "http://www.w3.org/2000/svg";
function el(tag, attrs, parent) { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
function shade(hex, f) { const n = parseInt(hex.slice(1), 16); let r = n >> 16, g = (n >> 8) & 255, b = n & 255;
  r = Math.round(r * f); g = Math.round(g * f); b = Math.round(b * f); return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1); }
function mix(a, b, t) { const pa = parseInt(a.slice(1), 16), pb = parseInt(b.slice(1), 16);
  const c = [16, 8, 0].map(s => Math.round(((pa >> s) & 255) * (1 - t) + ((pb >> s) & 255) * t)); return "#" + c.map(v => v.toString(16).padStart(2, "0")).join(""); }

function defs(svg) {
  const d = el("defs", {}, svg);
  const lg = (id, stops, x2 = 0, y2 = 1) => { const g = el("linearGradient", { id, x1: 0, y1: 0, x2, y2 }, d); stops.forEach(([o, c, a]) => el("stop", { offset: o, "stop-color": c, "stop-opacity": a ?? 1 }, g)); };
  const rg = (id, stops) => { const g = el("radialGradient", { id }, d); stops.forEach(([o, c, a]) => el("stop", { offset: o, "stop-color": c, "stop-opacity": a ?? 1 }, g)); };
  lg("sky", [[0, "#13242c"], [0.55, TEAL], [1, "#2c4a55"]]);
  lg("cone", [[0, AMBER, 0.55], [1, AMBER, 0]]);
  rg("pool", [[0, AMBER, 0.45], [1, AMBER, 0]]);
  rg("puff", [[0, "#ffffff", 0.95], [0.55, PAPER, 0.6], [1, PAPER, 0]]);
  rg("fog", [[0, "#ffffff", 0.75], [0.7, "#ffffff", 0.35], [1, "#ffffff", 0]]);
  rg("window", [[0, "#FFD48A", 1], [1, "#E8A54B", 1]]);
  lg("warmroom", [[0, "#6b4a2e"], [1, "#3a2a1e"]]);
  const f = el("filter", { id: "blur6", x: "-20%", y: "-20%", width: "140%", height: "140%" }, d); el("feGaussianBlur", { stdDeviation: 6 }, f);
  const f2 = el("filter", { id: "blur14", x: "-30%", y: "-30%", width: "160%", height: "160%" }, d); el("feGaussianBlur", { stdDeviation: 14 }, f2);
  const f3 = el("filter", { id: "grain", x: 0, y: 0, width: "100%", height: "100%" }, d);
  el("feTurbulence", { type: "fractalNoise", baseFrequency: 0.9, numOctaves: 2, seed: 7, result: "n" }, f3);
  el("feColorMatrix", { type: "matrix", values: "0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0.035 0", in: "n" }, f3);
  return d;
}

// ---------- environment ----------
function nightStreet(g, opts = {}) {
  const W = 1080, H = 1920, hz = opts.horizon ?? 760;
  el("rect", { x: 0, y: 0, width: W, height: H, fill: "url(#sky)" }, g);
  for (let i = 0; i < 26; i++) el("circle", { cx: (i * 397) % W, cy: 60 + ((i * 211) % 420), r: 1.6, fill: PAPER, opacity: 0.35 }, g);
  el("circle", { cx: 860, cy: 230, r: 46, fill: PAPER, opacity: 0.9 }, g);
  el("circle", { cx: 878, cy: 218, r: 46, fill: "#13242c" }, g); // crescent
  // far houses (slate silhouettes)
  const far = el("g", { opacity: 0.85 }, g);
  [[-40, 230, 300], [230, 200, 260], [470, 240, 280], [740, 210, 300], [960, 230, 260]].forEach(([x, w, h]) => {
    el("rect", { x, y: hz - h * 0.55, width: w, height: h * 0.55, fill: "#2a4450" }, far);
    el("polygon", { points: `${x - 10},${hz - h * 0.55} ${x + w / 2},${hz - h * 0.85} ${x + w + 10},${hz - h * 0.55}`, fill: "#2a4450" }, far);
    for (let k = 0; k < 2; k++) el("rect", { x: x + 30 + k * (w - 90), y: hz - h * 0.45, width: 34, height: 40, rx: 3, fill: "url(#window)", opacity: 0.75 }, far);
  });
  // near houses left/right
  [[-60, 330, 520], [760, 380, 560]].forEach(([x, w, h]) => {
    el("rect", { x, y: hz + 40 - h * 0.62, width: w, height: h * 0.62, fill: SLATE }, g);
    el("polygon", { points: `${x - 18},${hz + 40 - h * 0.62} ${x + w / 2},${hz + 40 - h} ${x + w + 18},${hz + 40 - h * 0.62}`, fill: "#33495410" }, g);
    el("polygon", { points: `${x - 18},${hz + 40 - h * 0.62} ${x + w / 2},${hz + 40 - h} ${x + w + 18},${hz + 40 - h * 0.62}`, fill: "#2f4752" }, g);
    el("rect", { x: x + 60, y: hz + 40 - h * 0.48, width: 70, height: 84, rx: 4, fill: "url(#window)" }, g);
    el("rect", { x: x + w - 140, y: hz + 40 - h * 0.48, width: 70, height: 84, rx: 4, fill: "url(#window)", opacity: 0.85 }, g);
  });
  // ground: road + sidewalk
  el("rect", { x: 0, y: hz, width: W, height: H - hz, fill: "#24343c" }, g);
  el("polygon", { points: `0,${hz + 60} ${W},${hz + 30} ${W},${hz + 330} 0,${hz + 420}`, fill: "#2d424b" }, g);
  el("rect", { x: 0, y: hz + 420, width: W, height: 40, fill: "#20303a", opacity: 0.6 }, g);
  // fog band
  el("rect", { x: 0, y: hz - 80, width: W, height: 160, fill: FOG, opacity: 0.12, filter: "url(#blur14)" }, g);
}
function streetlight(g, x, groundY, h = 560, poolW = 260) {
  el("polygon", { points: `${x - 18},${groundY - h + 30} ${x + 18},${groundY - h + 30} ${x + poolW / 2},${groundY} ${x - poolW / 2},${groundY}`, fill: "url(#cone)", opacity: 0.55 }, g);
  el("ellipse", { cx: x, cy: groundY + 6, rx: poolW * 0.62, ry: 40, fill: "url(#pool)" }, g);
  el("rect", { x: x - 6, y: groundY - h, width: 12, height: h, fill: INK }, g);
  el("path", { d: `M ${x} ${groundY - h} q 0 -26 30 -26 h 10`, stroke: INK, "stroke-width": 10, fill: "none" }, g);
  el("rect", { x: x - 22, y: groundY - h + 8, width: 44, height: 18, rx: 6, fill: "#FFE2A6" }, g);
}
function pumpkin(g, x, y, s = 1) {
  el("ellipse", { cx: x, cy: y, rx: 34 * s, ry: 26 * s, fill: "#E07B2A", stroke: INK, "stroke-width": 4 }, g);
  el("path", { d: `M ${x - 14 * s} ${y - 6 * s} l 6 -8 l 6 8 z M ${x + 2 * s} ${y - 6 * s} l 6 -8 l 6 8 z`, fill: "#FFD27A" }, g);
  el("path", { d: `M ${x - 16 * s} ${y + 8 * s} q ${16 * s} ${10 * s} ${32 * s} 0`, stroke: "#FFD27A", "stroke-width": 4, fill: "none" }, g);
  el("rect", { x: x - 3 * s, y: y - 34 * s, width: 6 * s, height: 10 * s, fill: "#4c6b3a" }, g);
}

// ---------- characters ----------
// spec: {x, y (feet), h, skin, hair, top, bottom, shoe, face:{brows:'calm'|'worried'|'up'|'angry', mouth:'rest'|'o'|'smile'|'tight'}, turned, facing, extra:[fn(g,ctx)], arms:{l:[a1,a2], r:[a1,a2]}, legs:{l,r}, paint (zombie paint colour)}
function limb(g, x, y, a1, a2, L1, L2, col, w) {
  const r = Math.PI / 180, x1 = x + Math.sin(a1 * r) * L1, y1 = y + Math.cos(a1 * r) * L1, x2 = x1 + Math.sin(a2 * r) * L2, y2 = y1 + Math.cos(a2 * r) * L2;
  const d = `M ${x} ${y} Q ${x1} ${y1} ${x2} ${y2}`;
  el("path", { d, stroke: INK, "stroke-width": w + 10, "stroke-linecap": "round", fill: "none" }, g);
  el("path", { d, stroke: col, "stroke-width": w, "stroke-linecap": "round", fill: "none" }, g);
  return [x2, y2];
}
function character(g, s) {
  const H = s.h / 5, x = s.x, y = s.y, f = s.facing || 1;
  const grp = el("g", {}, g);
  const skin = s.turned ? "#8A9A86" : s.skin;
  const legW = H * 0.26, armW = H * 0.2;
  const hipY = y - H * 2.2, shY = y - H * 3.75, neckY = y - H * 3.9, headCY = y - H * 4.45;
  const L = s.legs || { l: [8, -4], r: [-8, 4] }, A = s.arms || { l: [12, 4], r: [-12, -4] };
  // legs
  const fl = limb(grp, x - H * 0.18, hipY, L.l[0], L.l[1], H * 1.1, H * 1.05, s.bottom, legW);
  const fr = limb(grp, x + H * 0.18, hipY, L.r[0], L.r[1], H * 1.1, H * 1.05, s.bottom, legW);
  [fl, fr].forEach(([fx, fy]) => el("ellipse", { cx: fx + 10 * f, cy: fy + 4, rx: H * 0.26, ry: H * 0.13, fill: s.shoe || "#2a2a2a", stroke: INK, "stroke-width": 5 }, grp));
  // back arm
  const bh = limb(grp, x - H * 0.42, shY + H * 0.1, A.l[0], A.l[1], H * 0.85, H * 0.8, s.top, armW);
  el("ellipse", { cx: bh[0], cy: bh[1], rx: H * 0.15, ry: H * 0.17, fill: skin, stroke: INK, "stroke-width": 5 }, grp);
  // torso (tapered)
  const tw = H * 0.95, bw = H * 0.78;
  el("path", { d: `M ${x - tw / 2} ${shY} Q ${x} ${shY - H * 0.18} ${x + tw / 2} ${shY} L ${x + bw / 2} ${hipY + H * 0.1} Q ${x} ${hipY + H * 0.22} ${x - bw / 2} ${hipY + H * 0.1} Z`, fill: s.top, stroke: INK, "stroke-width": 6, "stroke-linejoin": "round" }, grp);
  el("path", { d: `M ${x + f * tw * 0.12} ${shY + 6} L ${x + f * bw * 0.45} ${hipY + H * 0.08} L ${x + f * tw * 0.46} ${shY + 4} Z`, fill: shade(s.top, 0.78), opacity: 0.9 }, grp); // one shadow tone
  if (s.extraTorso) s.extraTorso(grp, { x, H, shY, hipY, f, tw, bw });
  // neck + head (bean)
  el("rect", { x: x - H * 0.12, y: neckY - H * 0.05, width: H * 0.24, height: H * 0.28, fill: skin, stroke: INK, "stroke-width": 5 }, grp);
  const tilt = s.turned ? 17 * f : (s.tilt || 0);
  const hg = el("g", { transform: `rotate(${tilt} ${x} ${neckY})` }, grp);
  if (s.hairBack) s.hairBack(hg, { x, H, cy: headCY, f });
  el("rect", { x: x - H * 0.42, y: headCY - H * 0.5, width: H * 0.84, height: H, rx: H * 0.4, fill: s.paint || skin, stroke: INK, "stroke-width": 6 }, hg);
  el("path", { d: `M ${x + f * H * 0.08} ${headCY - H * 0.46} q ${f * H * 0.36} ${H * 0.1} ${f * H * 0.3} ${H * 0.86}`, stroke: shade(s.paint || skin, 0.82), "stroke-width": H * 0.16, fill: "none", opacity: 0.55, "stroke-linecap": "round" }, hg);
  // face
  const ex = H * 0.16, ey = headCY - H * 0.04, fx = x + f * H * 0.06;
  if (s.turned) {
    [-1, 1].forEach(k => el("ellipse", { cx: fx + k * ex, cy: ey, rx: H * 0.075, ry: H * 0.09, fill: "#E9EFD8", stroke: INK, "stroke-width": 3 }, hg));
    el("path", { d: `M ${fx - H * 0.1} ${ey + H * 0.24} q ${H * 0.1} ${H * 0.07} ${H * 0.2} 0`, stroke: INK, "stroke-width": 4, fill: "#2a2f35" }, hg);
  } else {
    [-1, 1].forEach(k => { el("ellipse", { cx: fx + k * ex, cy: ey, rx: H * 0.06, ry: H * 0.085, fill: INK }, hg); el("circle", { cx: fx + k * ex + H * 0.02, cy: ey - H * 0.03, r: H * 0.022, fill: "#fff" }, hg); });
    const b = s.face?.brows || "calm", by = ey - H * 0.15;
    const ang = { calm: [0, 0], worried: [-14, 14], up: [-6, 6], angry: [14, -14] }[b];
    [-1, 1].forEach((k, i) => el("rect", { x: fx + k * ex - H * 0.09, y: by - H * 0.025, width: H * 0.18, height: H * 0.05, rx: H * 0.025, fill: s.browCol || INK, transform: `rotate(${ang[i]} ${fx + k * ex} ${by})` }, hg));
    const m = s.face?.mouth || "rest", my = ey + H * 0.22;
    if (m === "o") el("ellipse", { cx: fx, cy: my, rx: H * 0.055, ry: H * 0.075, fill: "#3a1f1f", stroke: INK, "stroke-width": 3 }, hg);
    else if (m === "smile") el("path", { d: `M ${fx - H * 0.11} ${my - 2} q ${H * 0.11} ${H * 0.1} ${H * 0.22} 0`, stroke: INK, "stroke-width": 5, fill: "none", "stroke-linecap": "round" }, hg);
    else if (m === "tight") el("path", { d: `M ${fx - H * 0.08} ${my} h ${H * 0.16}`, stroke: INK, "stroke-width": 5, "stroke-linecap": "round" }, hg);
    else el("path", { d: `M ${fx - H * 0.07} ${my} q ${H * 0.07} ${H * 0.03} ${H * 0.14} 0`, stroke: INK, "stroke-width": 4, fill: "none", "stroke-linecap": "round" }, hg);
  }
  if (s.hairFront) s.hairFront(hg, { x, H, cy: headCY, f });
  // front arm + hand
  const fh = limb(grp, x + H * 0.42, shY + H * 0.1, A.r[0], A.r[1], H * 0.85, H * 0.8, s.top, armW);
  el("ellipse", { cx: fh[0], cy: fh[1], rx: H * 0.15, ry: H * 0.17, fill: skin, stroke: INK, "stroke-width": 5 }, grp);
  if (s.extra) s.extra(grp, { x, H, headCY, neckY, shY, hipY, f, hand: fh, backHand: bh });
  return { g: grp, mouth: [fx + f * H * 0.12, ey + H * 0.24], headCY, H, hand: fh, backHand: bh };
}
function breathPuff(g, x, y, t, scale = 1) { // t in 0..1 over 0.7 s
  if (t < 0 || t > 1) return;
  const r = (30 + 60 * t) * scale, o = Math.min(1, (1 - t) * 1.15);
  el("ellipse", { cx: x + 30 * t * scale, cy: y - 40 * t * scale, rx: r, ry: r * 0.72, fill: "url(#puff)", opacity: o }, g);
  el("ellipse", { cx: x + 52 * t * scale, cy: y - 18 * t * scale, rx: r * 0.6, ry: r * 0.45, fill: "url(#puff)", opacity: o * 0.8 }, g);
}
// hair/costume helpers
const KIT = {
  kaiHair: { hairBack: (g, c) => { el("path", { d: `M ${c.x - c.H * 0.62} ${c.cy + c.H * 0.55} q ${-c.H * 0.1} ${-c.H * 0.9} ${c.H * 0.62} ${-c.H * 0.95} q ${c.H * 0.72} ${0} ${c.H * 0.62} ${c.H * 0.95} z`, fill: "#E3B32A", stroke: INK, "stroke-width": 6 }, g); },
             hairFront: (g, c) => { [[-0.3, -0.48], [-0.08, -0.56], [0.16, -0.52], [0.34, -0.42], [-0.42, -0.34]].forEach(([dx, dy]) => el("circle", { cx: c.x + dx * c.H, cy: c.cy + dy * c.H, r: c.H * 0.17, fill: "#1b1b1f", stroke: INK, "stroke-width": 4 }, g)); } },
  headphones: (g, c) => { el("path", { d: `M ${c.x - c.H * 0.38} ${c.neckY + c.H * 0.18} q ${c.H * 0.38} ${c.H * 0.32} ${c.H * 0.76} 0`, stroke: "#22262e", "stroke-width": c.H * 0.1, fill: "none" }, g);
    [-1, 1].forEach(k => el("ellipse", { cx: c.x + k * c.H * 0.4, cy: c.neckY + c.H * 0.16, rx: c.H * 0.1, ry: c.H * 0.13, fill: "#22262e", stroke: INK, "stroke-width": 4 }, g)); },
  helmet: (fog) => (g, c) => { el("circle", { cx: c.x, cy: c.cy, r: c.H * 0.78, fill: "#dfe9ef", "fill-opacity": 0.18, stroke: "#e9f2f6", "stroke-width": 8 }, g);
    el("path", { d: `M ${c.x - c.H * 0.5} ${c.cy - c.H * 0.45} q ${c.H * 0.25} ${-c.H * 0.25} ${c.H * 0.55} ${-c.H * 0.22}`, stroke: "#ffffff", "stroke-width": 8, "stroke-linecap": "round", fill: "none", opacity: 0.8 }, g);
    if (fog > 0) el("ellipse", { cx: c.x + c.f * c.H * 0.12, cy: c.cy + c.H * 0.3, rx: c.H * 0.5 * (0.6 + fog * 0.4), ry: c.H * 0.32, fill: "url(#fog)", opacity: 0.9 * fog }, g);
    [-1, 1].forEach(k => el("path", { d: starPath(c.x + k * c.H * 0.28, c.cy - c.H * 0.42, c.H * 0.08), fill: "#FFD84A", stroke: INK, "stroke-width": 2 }, g)); },
  hat: (col) => (g, c) => { el("path", { d: `M ${c.x - c.H * 0.7} ${c.cy - c.H * 0.36} h ${c.H * 1.4} l ${-c.H * 0.45} ${-c.H * 0.12} l ${-c.H * 0.1} ${-c.H * 0.85} l ${-c.H * 0.32} ${c.H * 0.85} z`, fill: col, stroke: INK, "stroke-width": 5 }, g); },
  veil: (g, c) => { el("path", { d: `M ${c.x - c.H * 0.5} ${c.cy - c.H * 0.3} q ${c.H * 0.5} ${-c.H * 0.5} ${c.H} 0 l ${c.H * 0.25} ${c.H * 1.4} h ${-c.H * 1.5} z`, fill: "#f4f1ea", opacity: 0.55, stroke: INK, "stroke-width": 3 }, g); },
  beanie: (col) => (g, c) => { el("path", { d: `M ${c.x - c.H * 0.46} ${c.cy - c.H * 0.18} q ${c.H * 0.46} ${-c.H * 0.75} ${c.H * 0.92} 0 z`, fill: col, stroke: INK, "stroke-width": 5 }, g); },
  ponytail: (g, c) => { el("path", { d: `M ${c.x - c.f * c.H * 0.35} ${c.cy - c.H * 0.25} q ${-c.f * c.H * 0.55} ${c.H * 0.15} ${-c.f * c.H * 0.35} ${c.H * 0.85}`, stroke: "#7a3b22", "stroke-width": c.H * 0.2, "stroke-linecap": "round", fill: "none" }, g); },
  cap: (g, c) => { el("path", { d: `M ${c.x - c.H * 0.44} ${c.cy - c.H * 0.2} q ${c.H * 0.44} ${-c.H * 0.65} ${c.H * 0.88} 0 h ${c.f * c.H * 0.3} z`, fill: "#4b5a68", stroke: INK, "stroke-width": 5 }, g); },
  greyHair: (g, c) => { el("path", { d: `M ${c.x - c.H * 0.44} ${c.cy - c.H * 0.12} q ${c.H * 0.1} ${-c.H * 0.5} ${c.H * 0.44} ${-c.H * 0.42} q ${c.H * 0.36} ${-c.H * 0.06} ${c.H * 0.44} ${c.H * 0.42}`, fill: "#c9c9c4", stroke: INK, "stroke-width": 4 }, g); },
};
function starPath(cx, cy, r) { let d = ""; for (let i = 0; i < 10; i++) { const a = Math.PI / 5 * i - Math.PI / 2, rr = i % 2 ? r * 0.45 : r; d += (i ? "L" : "M") + (cx + Math.cos(a) * rr).toFixed(1) + " " + (cy + Math.sin(a) * rr).toFixed(1) + " "; } return d + "Z"; }
