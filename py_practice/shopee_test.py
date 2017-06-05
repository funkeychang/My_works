import requests
import json
import pandas

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://shopee.tw')
c = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in driver.get_cookies()])
token = [item.get('value') for item in driver.get_cookies() if item.get('name') == 'csrftoken'][0]
driver.close()

jd = json.loads('{"item_shop_ids":[{"itemid":131449,"adsid":0,"shopid":12290,"campaignid":0},{"itemid":2330735,"adsid":0,"shopid":196610,"campaignid":0},{"itemid":10457386,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":21807228,"adsid":0,"shopid":5435363,"campaignid":0},{"itemid":5644382,"adsid":0,"shopid":1982863,"campaignid":0},{"itemid":16710024,"adsid":0,"shopid":4932757,"campaignid":0},{"itemid":7903371,"adsid":0,"shopid":1975307,"campaignid":0},{"itemid":10454400,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10452173,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":7422660,"adsid":0,"shopid":2722176,"campaignid":0},{"itemid":5595311,"adsid":0,"shopid":118045,"campaignid":0},{"itemid":19785078,"adsid":0,"shopid":5435363,"campaignid":0},{"itemid":13738028,"adsid":0,"shopid":3544877,"campaignid":0},{"itemid":10468022,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":6021332,"adsid":0,"shopid":196610,"campaignid":0},{"itemid":5398424,"adsid":0,"shopid":118223,"campaignid":0},{"itemid":13540440,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":830634,"adsid":0,"shopid":67000,"campaignid":0},{"itemid":10463413,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":13837697,"adsid":0,"shopid":3625341,"campaignid":0},{"itemid":16968304,"adsid":0,"shopid":2015250,"campaignid":0},{"itemid":10454564,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10453533,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":15839282,"adsid":0,"shopid":482619,"campaignid":0},{"itemid":21573462,"adsid":0,"shopid":482725,"campaignid":0},{"itemid":10465863,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":30161458,"adsid":0,"shopid":2559226,"campaignid":0},{"itemid":10463269,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":18793542,"adsid":0,"shopid":2517316,"campaignid":0},{"itemid":25174874,"adsid":0,"shopid":482725,"campaignid":0},{"itemid":10463527,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":10039169,"adsid":0,"shopid":2618568,"campaignid":0},{"itemid":13542992,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":5731732,"adsid":0,"shopid":2559226,"campaignid":0},{"itemid":16966133,"adsid":0,"shopid":3448884,"campaignid":0},{"itemid":15227066,"adsid":0,"shopid":3918821,"campaignid":0},{"itemid":5528797,"adsid":0,"shopid":1249908,"campaignid":0},{"itemid":19279156,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":28327136,"adsid":0,"shopid":3905134,"campaignid":0},{"itemid":14638986,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":11614283,"adsid":0,"shopid":3942297,"campaignid":0},{"itemid":3372002,"adsid":0,"shopid":1587437,"campaignid":0},{"itemid":22007754,"adsid":0,"shopid":2395242,"campaignid":0},{"itemid":10029639,"adsid":0,"shopid":2559226,"campaignid":0},{"itemid":10460052,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":2329695,"adsid":0,"shopid":196610,"campaignid":0},{"itemid":14483747,"adsid":0,"shopid":118223,"campaignid":0},{"itemid":23963890,"adsid":0,"shopid":3905134,"campaignid":0},{"itemid":10453346,"adsid":0,"shopid":2698155,"campaignid":0},{"itemid":3326952,"adsid":0,"shopid":196610,"campaignid":0}]}')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://shopee.tw/%E6%89%8B%E6%A9%9F%E5%B9%B3%E6%9D%BF%E8%88%87%E5%91%A8%E9%82%8A-cat.70',
    'x-csrftoken': token,
    'Cookie': c
}

res = requests.post('https://shopee.tw/api/v1/items/', json=jd, headers=headers)
df = pandas.DataFrame(res.json())
print(df)
