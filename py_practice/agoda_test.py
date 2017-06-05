import requests
import time

from selenium import webdriver
from bs4 import BeautifulSoup

# url
url = 'https://www.agoda.com/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?asq=u2qcKLxwzRU5NDuxJ0kOF3T91go8JoYYMxAgy8FkBH1BN0lGAtYH25sdXoy34qb9ggMjKvvLEVbYKbVh%2Fv3g6039PP9sVcqHVwW%2FShBWryCaIppML0jZW9Cx%2FY%2B4QVLP%2BEb154g2%2BAvy%2BAt%2BHc%2FRX%2BqiQzGLvfye6Kdb%2BBkhdjbZF6Y4SVFz3NQNyVWv7etVxfkFVjQ6pq54JTx%2BnutqKw%3D%3D&city=4951&tick=636319452061&isdym=true&searchterm=%E5%8F%B0%E5%8C%97&txtuuid=f9e47cbb-13ee-4ddd-afce-7b55bda172e2&pagetypeid=5&origin=TW&cid=-1&tag=&gclid=&aid=81837&userId=1c6ec5af-f8cc-4454-bce4-cd49246dc0c2&languageId=20&sessionId=baohaizoxwoask0ooutjzmsh&storefrontId=3&currencyCode=TWD&htmlLanguage=zh-tw&trafficType=User&cultureInfoName=zh-TW&textToSearch=%E5%8F%B0%E5%8C%97&guid=f9e47cbb-13ee-4ddd-afce-7b55bda172e2&isHotelLandSearch=true&checkIn=2017-06-10&checkOut=2017-06-17&los=7&rooms=1&adults=1&children=0&childages=&ckuid=1c6ec5af-f8cc-4454-bce4-cd49246dc0c2'

# use PhantomJS
driver = webdriver.PhantomJS()
driver.get(url)

# total pages of query results
page_count  = 0

while page_count < 3:
    soup = BeautifulSoup(driver.page_source)
    for hotel in soup.select('.hotel-item-box'):
        # get hotel's name, currency and price.
        print(hotel.select('.hotel-name')[0].text, hotel.select('.currency')[0].text, hotel.select('.price')[0].text)

    # click button "Next Page"
    driver.find_element_by_id('paginationNext').click()
    page_count += 1
    # sleep to avoid error while the page not loading completly.
    time.sleep(2)

driver.close()
