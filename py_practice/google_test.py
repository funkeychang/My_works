from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.google.com.tw/search?q=python&oq=python&aqs=chrome..69i57j69i61l2j69i65l3.3371j0j9&sourceid=chrome&ie=UTF-8'

driver = webdriver.PhantomJS()
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source)

for title in soup.select('.r'):
    print(title.text)
