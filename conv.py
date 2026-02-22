import os
import ffmpeg

# FOR SINGLE VIDEO FILE:
file_name = 'Input File.mov'
video_name = 'Output file.mp4'

# for 2880 x 1800
ffmpeg.input(file_name).output(video_name, s='1440x900').run()

# ffmpeg.input(file_name).output(video_name, s='1280x720').run()

# for mobile videos:
# ffmpeg.input(file_name).output(video_name, s='360x640').run()

# Convert to 40s (specify end time)
# ffmpeg.input(file_name, to=497).output(video_name, s='1440x900').run()

# Convert from 10s to 40s (specify start end time)
# ffmpeg.input(file_name, ss=10, to=40).output(video_name, s='1440x900').run()

# extract AUDIO
# audio_name = 'my_audio_output.m4a'
# ffmpeg.input(file_name).output(audio_name, vn=None).run()
# vn=None - "no video" - extracts only audio
# acodec='copy' - keep original audio quality - no re-encoding, no quality loss

print("==== Conversion completed! Video is ready! =====")
os.system('say "Conversion completed!"')


# ===== FOR LIST OF VIDEOS: =====
# for index in range(1, 6): # to convert only videos #7 and #8 use range(7, 9)
#     # ts_name = f'RAW_{index}.ts'
#     ts_name = f'RAW_{index}.ts'
#     video_name = f'VIDEO_{"0" if index < 10 else ""}{index}.mp4' # original = default settings

#     print(f"==== START CONVERTING VIDEO {index} ====")
#     # os.system(f'say "Start converting video {index}"')

#     try:
#         ffmpeg.input(ts_name).output(
#             video_name,
#             # s='1280x720', # resolution
#             # video_bitrate='1M', # 1 Mbps (megabits per second)
#             # crf=28, # ~2.5-4 Mbps (1080p) - noticeable compression, but acceptable
#             preset='slow', # compression speed
#         ).run('/opt/homebrew/bin/ffmpeg')
#     except ffmpeg.Error as e:
#         print(f"FFmpeg ERROR: {e}")
#     except Exception as e:
#         print(f"Failed to convert video {index}: {e}")
#         os.system(f'say "Failed to convert video {index}."')
#     else:
#         print(f"==== CONVERTION OF VIDEO {index} COMPLETED ====")
#         os.system(f'say "Video {index} is ready"')

# print("++++++ All videos are ready! ++++++")
# os.system('say "Conversion completed!"')

# The following maintain the 16:10 aspect ratio if your original is 2880x1800:
# 1920 × 1200  (2/3 scale)
# 1440 × 900   (1/2 scale)
# 1280 × 800   (slightly less)
# 960 × 600    (1/3 scale)
# 720 × 450    (1/4 scale)
