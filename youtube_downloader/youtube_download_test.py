import requests
import re
import time
import urllib
import shutil

from bs4 import BeautifulSoup

# Get youtube video url
youtube_url = input("Give me a youtube video url : ")
# parse url to get video_info
video_id = youtube_url.split('=')[-1]
video_info = requests.get('https://www.youtube.com/get_video_info?video_id=' + video_id)

# first parse to get title and url_encoded_fmt_stream_map
first_parse = urllib.parse.parse_qs(video_info.text)
video_title = first_parse['title'][0]
url_encoded_fmt_stream_map = first_parse['url_encoded_fmt_stream_map'][0]

# parse again to get video_source like url and quality ... etc
video_source = urllib.parse.parse_qs(url_encoded_fmt_stream_map)
video_url = video_source['url']
video_quality = video_source['quality']

# start to download video
print("Downloading video : " + video_title)

# Always get video_url[0] cuz I am lazy :D
res = requests.get(video_url[0], stream=True)
f = open(video_title + '.mp4', 'wb')
shutil.copyfileobj(res.raw, f)
f.close()
print("Finished.")
