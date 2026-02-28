import ffmpeg

def cut_audio(input_file, output_file, start_time, end_time=None, reencode=True):
    """
    Cut audio file between time points

    Args:
        input_file: Input audio file path
        output_file: Output audio file path
        start_time: Start time (seconds or 'HH:MM:SS')
        end_time: End time (seconds or 'HH:MM:SS'), None for end of file
        reencode: False for fast copy, True for precise cut
    """
    try:
        if end_time:
            if reencode:
                ffmpeg.input(input_file, ss=start_time, to=end_time).output(output_file).run()
            else:
                ffmpeg.input(input_file).output(output_file, ss=start_time, to=end_time, c='copy').run()
        else:
            if reencode:
                ffmpeg.input(input_file, ss=start_time).output(output_file).run()
            else:
                ffmpeg.input(input_file).output(output_file, ss=start_time, c='copy').run()

        print(f"✓ Audio cut successfully: {output_file}")
    except Exception as e:
        print(f"Error cutting audio: {e}")

# Examples:
# cut_audio('audio.m4a', 'cut1.m4a', 30, 90)  # 30s to 90s, re-encode (precise)
# cut_audio('audio.m4a', 'cut2.m4a', '00:01:00', '00:02:30')  # 1min to 2:30min
# cut_audio('audio.m4a', 'cut3.m4a', 60, reencode=False)  # From 1min to end, fast copy

# Which to use:
  # Precise cuts, quality matters: Use re-encoding (default)
  # Speed matters, rough cuts OK: Use c='copy'
  # Very large files: Use c='copy' first, can always re-encode later

cut_audio(
  'my_video.m4a',
  'my_video_part_1.m4a',
  '00:00:00',
  '00:19:45'
)
