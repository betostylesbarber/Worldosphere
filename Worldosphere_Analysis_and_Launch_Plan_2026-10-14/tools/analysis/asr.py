import sys, json, wave, numpy as np, sherpa_onnx
M = sys.argv[1]; wav = sys.argv[2]; out = sys.argv[3]
def load(p):
    with wave.open(p) as w:
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)/32768
        return a, w.getframerate()
a, sr = load(wav)
pk = M + "/sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8"
rec = sherpa_onnx.OfflineRecognizer.from_transducer(encoder=pk+"/encoder.int8.onnx", decoder=pk+"/decoder.int8.onnx", joiner=pk+"/joiner.int8.onnx", tokens=pk+"/tokens.txt", model_type="nemo_transducer", num_threads=4)
wh = M + "/sherpa-onnx-whisper-small.en"
recw = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=wh+"/small.en-encoder.int8.onnx", decoder=wh+"/small.en-decoder.int8.onnx", tokens=wh+"/small.en-tokens.txt", language="en", task="transcribe", num_threads=4)
cfg = sherpa_onnx.VadModelConfig(); cfg.silero_vad.model = M+"/silero_vad.onnx"; cfg.silero_vad.min_silence_duration = 0.25; cfg.silero_vad.min_speech_duration=0.15; cfg.silero_vad.threshold=0.4; cfg.sample_rate = sr
vad = sherpa_onnx.VoiceActivityDetector(cfg, buffer_size_in_seconds=120)
segs=[]; i=0; ws=cfg.silero_vad.window_size
while i < len(a):
    vad.accept_waveform(a[i:i+ws]); i+=ws
    while not vad.empty():
        segs.append((vad.front.start, np.array(vad.front.samples))); vad.pop()
vad.flush()
while not vad.empty():
    segs.append((vad.front.start, np.array(vad.front.samples))); vad.pop()
res=[]
for st, s in segs:
    t0 = st/sr
    s1 = rec.create_stream(); s1.accept_waveform(sr, s); rec.decode_stream(s1); r=s1.result
    s2 = recw.create_stream(); s2.accept_waveform(sr, s); recw.decode_stream(s2)
    toks = [{"t": tk, "s": round(t0+ts,2)} for tk, ts in zip(r.tokens, r.timestamps)]
    res.append({"start": round(t0,2), "end": round(t0+len(s)/sr,2), "parakeet": r.text.strip(), "whisper": s2.result.text.strip(), "tokens": toks})
    print(f"[{t0:6.2f}-{t0+len(s)/sr:6.2f}] P: {r.text.strip()}\n                 W: {s2.result.text.strip()}")
json.dump(res, open(out,"w"), indent=1)
