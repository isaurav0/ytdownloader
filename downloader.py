import sys
from pytube import YouTube as youtube

url = sys.argv[1]

if sys.argv[-1]==url:
    media_type = "video"
else:
    media_type = sys.argv[-1]

#print("url= ", url)
#print("format = ", media_type)

print("Parsing video ...")
yt = youtube(url)
if media_type == 'video':
    stream = yt.streams.get_highest_resolution()
else:
    stream = yt.streams.get_audio_only()


