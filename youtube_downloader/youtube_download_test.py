import requests
import re
import time
import urllib
import shutil

from bs4 import BeautifulSoup

url = input("Give me a youtube video url : ")
video_id = url.split('=')[-1]
video_info = requests.get('https://www.youtube.com/get_video_info?video_id=' + video_id)

m = re.search('url_encoded_fmt_stream_map=(.*)', video_info.text)
a = urllib.parse.parse_qs(m.group(0))
time.sleep(2)
b = urllib.parse.parse_qs(a['url_encoded_fmt_stream_map'][0])

"""
for q, u in zip(b['quality'], b['url']):
    print(q, u)
"""

print("Downloading ...")
res = requests.get(b['url'][0], stream=True)
f = open('test1.mp4', 'wb')
shutil.copyfileobj(res.raw, f)
f.close()
print("Finished.")
