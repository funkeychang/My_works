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
    else:
        print("The folder %s exists! Start downloading ..." % name)

def is_jpg(file_name):
    if file_name.split('.')[-1] == 'jpg':
        return True

def start_crawl():
    beauty_url = get_url()
    res = requests.get(beauty_url)
    soup = BeautifulSoup(res.text, "html.parser")
    pbar = ProgressBar()
    dir_name = soup.select('.article-meta-value')[2].text
    check_dir(dir_name)
    os.chdir(dir_name)
    #print("now in : " + os.getcwd())

    print("Now start to download pictures ...")

    for a in pbar(soup.select('a')[5::]):
        pic_link = a.text
        file_name = pic_link.split('/')[-1]

        if is_jpg(file_name):
        	res2 = requests.get(pic_link, stream=True)
        	f = open(file_name, 'wb')
        	shutil.copyfileobj(res2.raw, f)
        	f.close()
        	del res2

    print("Pictures download finished!")

if __name__ == '__main__':
    while True:
        start_crawl()
