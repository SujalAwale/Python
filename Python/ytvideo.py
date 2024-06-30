from pytube import YouTube

link = YouTube('https://youtu.be/L1VGmTwW23I?si=51HSlaDMbR5I_4jt')

# Get the stream that includes both video and audio
video = link.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

video.download()
