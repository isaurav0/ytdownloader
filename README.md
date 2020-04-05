# ytdownloader
Script to download videos, audios from youtube 

How to use? 

1. Clone this repository 
``` 
git clone https://github.com/isaurav0/ytdownloader
```

2. Install pytube3 from pip
``` 
pip install pytube3 --upgrade
```

3. Install ffmpeg module compatible to your platform. Download from [here](http://ffmpeg.org/download.html). If you're on windows don't forget to add its $PATH to environment variable. 

4. Navigate to ytdownloader file. 
``` 
cd ytdownloader
```

5. Use following syntax to download. 
``` 
python downloader.py https://urlhere [audio/video]
```

Example: 
To download video: 

``` 
python downloader.py https://www.youtube.com/watch?v=fJ9rUzIMcZQ 
```  

To download audio: 

``` 
python downloader.py https://www.youtube.com/watch?v=fJ9rUzIMcZQ audio
```

To download from a file containing url lists:
``` 
python downloader.py -f file.txt audio/video
```
  
