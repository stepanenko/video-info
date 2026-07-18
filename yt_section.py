from yt_dlp import YoutubeDL

def to_seconds(timestamp: str) -> int:
    """Convert MM:SS or HH:MM:SS to seconds."""
    parts = list(map(int, timestamp.split(":")))

    if len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds
    elif len(parts) == 3:
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds

    raise ValueError("Timestamp must be MM:SS or HH:MM:SS")


video_id = "Q8ft4FyQPhA"
url = f"https://www.youtube.com/watch?v={video_id}"

start = "16:03"
end = "16:56"

ydl_opts = {
    # "format": "bv*+ba/b",  # Download the best video + audio
    "format": "bestvideo[vcodec^=avc1][height<=720]+bestaudio[acodec^=mp4a]/best[vcodec^=avc1][height<=720]", # if video doesn't open
    # "format": "bestvideo[height<=720]+bestaudio[abr<=128]/best[height<=720]", # 720p video with medium/low-quality audio
    "merge_output_format": "mp4",  # merge into MP4
    "outtmpl": "clip.%(ext)s",
    # "download_ranges": lambda *_: [{
    #     "start_time": to_seconds(start),
    #     "end_time": to_seconds(end),
    # }],
    "force_keyframes_at_cuts": True,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# use: ffprobe clip.mp4 to log the codec info
