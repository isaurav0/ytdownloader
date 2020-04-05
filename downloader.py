#!/usr/bin/python
import sys
from pytube import YouTube as youtube
import subprocess

# python downloader.py url audio/video
# python downloader.py -f file.txt audio/video

try:
    location = sys.argv[1]
except:
    print("Syntax Error. ")
    print("Usage: python downloader.py url audio/video")
    print("Usage: python downloader.py -f file.txt audio/video")
    exit()

if location=='-file':
    file = open(sys.argv[2], "r")
    urls = []
    for url in file:
        urls.append(url)
else:
    urls = [location]

if sys.argv[-1]=="audio":
    media_type = "audio"
else:
    media_type = "video"

for url in urls:
    print("********* Parsing video ***********")
    # print("Parsing video ;)  ...")
    yt = youtube(url)
    print(yt.title)
    if media_type == 'video':        
        stream = yt.streams.first()
    else:
        stream = yt.streams.get_audio_only()

    print("Downloading ...")
    stream.download('youtube')

    if media_type != 'video':
        print("Converting ...")
        filename = stream.default_filename.split(".mp")[0]+'.mp3'
        subprocess.call(['ffmpeg','-i','youtube/'+stream.default_filename,'youtube/'+filename])
        subprocess.call(['rm','youtube/'+stream.default_filename])
    print("*********Completed***********")
