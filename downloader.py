import sys
from pytube import YouTube as youtube
import subprocess

url = sys.argv[1]

if sys.argv[-1]==url:
    media_type = "video"
else:
    media_type = sys.argv[-1]

#print("url= ", url)
#print("format = ", media_type)

print("Parsing video ;)  ...")
yt = youtube(url)
print(yt.title)
if media_type == 'video':
#    stream = yt.streams.filter(res='1080p')[-1]
#    if not stream:
#        stream = yt.streams.filter(res='720p')[-1]
#        if not stream:
#            stream = yt.streams.first()

    
    stream = yt.streams.first()
else:
    stream = yt.streams.get_audio_only()

print("Downloading ...")
stream.download()

if media_type != 'video':
    print("Converting ...")
    filename = stream.default_filename.split(".mp")[0]+'.mp3'
    subprocess.call(['ffmpeg','-i',stream.default_filename,filename])
    subprocess.call(['rm',stream.default_filename])

print("*********Completed***********")
