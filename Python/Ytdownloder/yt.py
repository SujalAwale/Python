from pytube import YouTube

link = YouTube('https://youtu.be/i2N3sQpPCBA?si=qyL3qfznrIt73u-F')

video = link.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

video.download()