import yt_dlp
import os

def download_youtube_resolution(url, resolution=720, output_path='.'):
  """Download YouTube video at specific resolution"""

    # Resolution format options
    # format_options = {
    #     '2160p': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',  # 4K
    #     '1440p': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',  # 2K
    #     '1080p': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    #     '720p': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    #     '480p': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
    #     '360p': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
    #     'best': 'bestvideo+bestaudio/best',  # Highest available
    # }

  ydl_opts = {
    'cookiefile': 'youtube_cookies.txt',
    # Re-export the cookies if you see WARNING: [youtube] The provided YouTube account cookies are no longer valid.
    # 'listformats': True, # Lists available formats but doesn't download
    'format': "136+140", # "VIDEO_ID+AUDIO_ID" - get these IDs from the 'listformats'
    # 'format': 'bestvideo+bestaudio/best',
    # 'format': f'bestvideo[height<={resolution}][vcodec^=avc1]+bestaudio[ext=m4a]/bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/best[height<={resolution}]',
    'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      print(f"Downloading YouTube video at {resolution}...")
      info = ydl.extract_info(url, download=True)
      print(f"✓ Downloaded: {info['title']}")
      os.system('say "Download completed!"')
  except Exception as e:
    print(f"Error: {e}")

# Usage:
download_youtube_resolution("https://www.youtube.com/watch?v=qUtX3y1KLa4", resolution=1080)


# If getting WARNING: [youtube] MyeKFWYwTKI: Signature solving failed: Some formats may be missing.
# Ensure you have a supported JavaScript runtime and challenge solver script distribution installed.
# Install deno with: brew install deno

# If the above fails (as it does for Members only content) and you're getting:
# WARNING: [youtube] [jsc] Remote components challenge solver script (deno) and NPM package (deno) were skipped.
# These may be required to solve JS challenges. You can enable these downloads with --remote-components ejs:github.
# >>>> Run this command in the terminal first:
# yt-dlp --remote-components ejs:github --cookies youtube_cookies.txt --update "https://www.youtube.com/watch?v=MyeKFWYwTKI"
# This forces downloading the solver files. Now you can use it in your Python script normally - the solver files are downloaded and cached.

# TIPS:
# 1 - using 'listformats': True - is great to just get the list of all videos and make sure of no errors (if used, download will not happen)
