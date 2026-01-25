
## Video Info

### Typical bitrate recommendations by resolution:
- 1080p: 4-8 Mbps
- 720p: 2-4 Mbps
- 480p: 0.5-1.5 Mbps
- 360p: 0.3-0.7 Mbps

### Example for significant size reduction:
```py
ffmpeg.input(ts_name).output(
    video_name,
    s='1280x720', # resolution
    crf=28,
    preset='slow', # slow, medium, fast (slower = better compression)
    audio_bitrate='96k' # Compress audio
).run()
```

### CRF scale reference:
- CRF 18: ~8-12 Mbps (1080p) - very high quality
- CRF 23: ~3-6 Mbps (1080p) - default, good quality
- CRF 26: ~2.5-4 Mbps (1080p) - good balance - noticeable compression but still good quality
- CRF 28: ~1.5-4 Mbps (1080p) - noticeable compression, but acceptable
- CRF 32: ~1-2 Mbps (1080p) - lower quality

### At 3 Mbps (megabits per second), a 1-minute video is:
3 Mbps × 60 seconds = 180 megabits = 22.5 MB

### Quick conversion formula:

Mbps × 60 seconds ÷ 8 bits/byte = MB per minute

#### Reference table:
- 1 Mbps = 7.5 MB per minute
- 2 Mbps = 15 MB per minute
- 3 Mbps = 22.5 MB per minute
- 4 Mbps = 30 MB per minute
- 5 Mbps = 37.5 MB per minute

### If you only specify resolution without bitrate or CRF, ffmpeg will automatically adjust the bitrate to match the new resolution.
```py 
ffmpeg.input(ts_name).output(video_name, s='1280x720').run()
```
Ffmpeg will:  
- Use its default encoding mode (CRF 23 for libx264)
- Automatically use less bitrate for 720p than it would for 1080p
- The bitrate will scale roughly with pixel count

Example:  
- If 1080p uses ~3.3 Mbps with CRF 23
- Then 720p would use roughly ~1.5-2 Mbps with CRF 23
- (720p has about 44% the pixels of 1080p)

#### Just reducing resolution alone will reduce file size significantly!
```py
# 1080p → 720p: expect ~50-60% file size reduction
ffmpeg.input(ts_name).output(video_name, s='1280x720').run()

# 1080p → 480p: expect ~70-80% file size reduction  
ffmpeg.input(ts_name).output(video_name, s='854x480').run()
```
