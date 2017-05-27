import os
import requests
import shutil

from progressbar import ProgressBar
from bs4 import BeautifulSoup

def get_url():
    url = input("Input an URL: ")

    if not url:
        print("You must input an URL! Try again!")
        get_url()

    return url

def check_dir(name):
    if not os.path.exists(name):
        print("Creating folder %s ..." % name)
        os.mkdir(name)
        print("Done.")

def start_crawl(ptt_url):
    res = requests.get(ptt_url)
    soup = BeautifulSoup(res.text, "html.parser")
    pbar = ProgressBar()
    dir_name = soup.select('.article-meta-value')[2].text
    check_dir(dir_name)
    #print("now in : " + os.getcwd())
    os.chdir(dir_name)
    #print("now in : " + os.getcwd())

    print("Now start to download pictures ...")

    for link in pbar(soup.select('a')[5::2]):
    	file_name = link['href'].split('/')[-1]
    	res2 = requests.get(link['href'], stream=True)
    	f = open(file_name, 'wb')
    	shutil.copyfileobj(res2.raw, f)
    	f.close()
    	del res2

    print("Pictures download finished!")

if __name__ == '__main__':
    while True:
        beauty_url = get_url()
        start_crawl(beauty_url)
