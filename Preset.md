# Preset

The **preset** is quite important, but it's a **time vs compression tradeoff**, not a quality vs compression tradeoff.

**What preset does:**
- Controls **encoding speed** and **compression efficiency**
- Does NOT significantly affect quality at the same CRF
- Slower = better compression (smaller file), takes longer to encode
- Faster = worse compression (larger file), encodes quickly

**Preset options (from slowest to fastest):**
- `veryslow` - best compression, very slow
- `slower` - excellent compression
- `slow` - great compression ← good choice for archiving
- `medium` - **default**, balanced
- `fast` - quick encoding
- `faster`, `veryfast`, `superfast`, `ultrafast` - progressively faster but larger files

**Real-world impact:**

At the same CRF 23:
- `ultrafast`: 100 MB file, encodes in 10 seconds
- `medium`: 80 MB file, encodes in 30 seconds (default)
- `slow`: 75 MB file, encodes in 60 seconds
- `veryslow`: 73 MB file, encodes in 120 seconds

**When to use what:**

```python
# One-time conversions, archiving - use slow
ffmpeg.input(ts_name).output(video_name, preset='slow', crf=23).run()

# Batch processing many videos - use medium (default)
ffmpeg.input(ts_name).output(video_name, crf=23).run()

# Quick preview/test - use fast
ffmpeg.input(ts_name).output(video_name, preset='fast', crf=23).run()
```

**Recommendation:**
- If you're converting a few videos and file size matters: use `slow`
- If you're converting many videos in batch: stick with `medium` (default)
- The file size difference between medium and slow is usually only **5-10%**
