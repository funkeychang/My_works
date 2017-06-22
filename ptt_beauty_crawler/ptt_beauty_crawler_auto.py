import requests
import shutil
import os
import time

from bs4 import BeautifulSoup

PTT_BEAUTY_URL = 'https://www.ptt.cc/bbs/Beauty/index.html'
PTT_URL = 'https://www.ptt.cc'
BASE_DIR = os.getcwd()
articles = []

# get PTT_BEAUTY page info
def get_page_info(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    article_data = soup.select('.r-ent')

    for data in article_data:
        if data.find('a'):
            title = data.a.text
            link = data.a['href']
            date = data.select('.date')[0].text
            push = data.select('.nrec')[0].text

        articles.append({
            'title': title,
            'link': PTT_URL + link,
            'date': date,
            'push': push if push else 0
        })

# get image links from article link
def get_img_links(article_link):
    res = requests.get(article_link)
    soup = BeautifulSoup(res.text, 'lxml')
    img_links = []

    for link in soup.select('a')[5:]:
        img_links.append(link.text)

    img_links = list(filter(None, img_links))
    return img_links

# Check if link is //imgur.com/xxxxx without .jpg
def check_links(links):
    for index, link in enumerate(links):
        img_name = link.split('/')[-1]
        if 'imgur' in link and '.jpg' not in link:
            links[index] = 'http://i.imgur.com/{}.jpg'.format(img_name)
        elif 'imgur' not in link:
            links.remove(link)

    return links

# check image's type
def is_jpg(link):
    if link.split('.')[-1] == 'jpg':
        return True

# ckeck if dir exists and create dir
def is_dir_exists(dir_name):
    if not os.path.exists(dir_name):
        print('{} folder does not exist!'.format(dir_name))
        print('Creating folder {} ...'.format(dir_name))
        os.mkdir(dir_name)
        print('Done.')
    else:
        print('{} folder exists!'.format(dir_name))

# download images
def download_images(img_links):
    print('Start downloading images ...')
    for img in img_links:
        img_name = img.split('/')[-1]

        if is_jpg(img):
            res = requests.get(img, stream=True)
            f = open(img_name, 'wb')
            shutil.copyfileobj(res.raw, f)
            f.close()
            del res

    print('finished.')

def main():

    get_page_info('https://www.ptt.cc/bbs/Beauty/index2196.html')

    for article in articles:
        if article['push'] == '爆' or int(article['push']) >= 20:
            img_links = get_img_links(article['link'])

            check_links(img_links)
            is_dir_exists(article['title'])
            os.chdir(article['title'])
            download_images(img_links)
            os.chdir(BASE_DIR)

if __name__ == '__main__':
    main()
