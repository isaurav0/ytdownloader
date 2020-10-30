#!/usr/bin/python
import re
import sys
from pytube import YouTube, Playlist
import subprocess
import traceback

help_message = '''
        Usage: Downloads video from youtube

        Syntax:

        $ python downloader.py -url url [audio/video]
        $ python downloader.py -file filename.txt [audio/video]
        $ python downloader.py -playlist -url url [audio/video]
        $ python downloader.py -playlist -file filename.txt [audio/video]
'''


class Downloader():

    def __init__(self, url='', file_name='', is_playlist=False, output_type='video', out_folder='youtube'):                
        self.url = url
        self.pattern = re.compile(r'https[^\s]+')
        self.file_name = file_name
        self.is_playlist = is_playlist
        self.output_type =  output_type
        self.out_folder =  out_folder

    def __download__(self, url):
        print('--------- Parsing video ----------')
        try:
            yt = YouTube(url)
            stream = yt.streams.get_audio_only() if self.output_type == 'audio' else yt.streams.first()
            print(f'Downloading {yt.title} ....')
            stream.download(self.out_folder)        
            if self.output_type == 'audio':
                self.__convert_to_audio__(stream.default_filename)
            print("*********Completed***********")
        except:
            print('------ Aborted --------')

    def __download__playlist(self, playlist_url):
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        for url in playlist.video_urls:
            self.__download__(url)


    def __convert_to_audio__(self, filename):
        out_filename = filename.split(".mp")[0]+'.mp3'
        print('-------converting---------')
        subprocess.call(['ffmpeg','-i','youtube/'+filename,'youtube/'+out_filename])
        subprocess.call(['rm','youtube/'+filename])

    def download(self):
        urls = []     
        if self.file_name:            
            with open(self.file_name) as fp:
                for line in fp:
                    url = self.pattern.findall(line)
                    if url:
                        urls.append(url[0])
        if self.url:
            urls.append(self.pattern.findall(self.url)[0])

        if self.is_playlist:
            for url in urls:
                self.__download__playlist(url)
        else:
            for url in urls:
                self.__download__(url)


def get_flag_value(flag):
    try:
        return sys.argv[sys.argv.index('-' + flag) + 1]
    except:
        print("Error: Value of {} not found".format(flag))


if __name__ == '__main__':
    config = {
        'url': '',
        'has_file': False,
        'file_name': '',
        'is_playlist': False,
        'output_type': 'audio',
    }
    try:
        if 'help' in sys.argv:
            print(help_message)
            exit()
        config['url'] = '' if not '-url' in sys.argv else get_flag_value('url')
        config['has_file'] = '-file' in sys.argv
        config['file_name'] = '' if not config['has_file'] else get_flag_value('file')
        config['output_type'] = 'audio' if 'audio' in sys.argv else 'video'
        config['is_playlist'] = '-playlist' in sys.argv
        config['out_folder'] = 'youtube' if not '-out' in sys.argv else get_flag_value('file')

        downloader = Downloader(config['url'],
                              config['file_name'],
                              config['is_playlist'],
                              config['output_type'])

        downloader.download()
    except Exception:
        traceback.print_exc()        
        print(help_message)
        exit()

