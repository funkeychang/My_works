import requests
from bs4 import BeautifulSoup

payload = {
    'from': '/bbs/sex/index.html',
    'yes': 'yes'
}

rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18?from=%2Fbbs%2Fsex%2Findex.html', verify=False, data=payload)
res = rs.get('https://www.ptt.cc/bbs/sex/index.html', verify=False)
soup = BeautifulSoup(res.text)

for entry in soup.select('.r-ent'):
    print(entry.select('.title')[0].text, entry.select('.author')[0].text)
w
