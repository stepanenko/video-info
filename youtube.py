import yt_dlp # pip3 install yt-dlp

def download_audio_for_ipod(url, output_path='.'):
    """Download audio compatible with iPod/iTunes"""

    ydl_opts = {
        # 'format': 'bestaudio/best', # COMMENT OUT for subtitles only
        'skip_download': True, # don't download video/audio
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'writesubtitles': True,
        'writeautomaticsub': True,  # include auto-generated French subs if manual ones aren't available
        'subtitleslangs': ['fr'],
        'subtitlesformat': 'srt',  # Format: srt, vtt, or best
        # 'postprocessors': [{ # COMMENT OUT - not needed for subtitles only
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'm4a',  # AAC format, native iPod support
        #     'preferredquality': '256',  # High quality
        # }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio for iPod...")
            info = ydl.extract_info(url, download=True)
            print(f"✓ Downloaded: {info['title']}.m4a")
    except Exception as e:
        print(f"Error: {e}")

# Usage
url = "https://www.youtube.com/watch?v=RgzmMwcpZzQ"
download_audio_for_ipod(url)
