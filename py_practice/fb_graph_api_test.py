import requests
import jieba
import operator
from bs4 import BeautifulSoup

# FB token by graph api
# go to FB graph api and get token
TOKEN = ''

# GET info from graph.facebook.com/
res = requests.get('https://graph.facebook.com/v2.9/me/posts?limit=100&access_token=' + TOKEN)

# info we get is json type, so we use .json()
jd = res.json()

# store cutted words into corpus
corpus = []
# count words
dic = {}

# load all my post until 'paging' to the end
while 'paging' in jd:
    for post in jd['data']:
        # avoid message error
        if 'message' in post:
            # cut words in message
            corpus += jieba.cut(post['message'])

    res = requests.get(jd['paging']['next'])
    jd = res.json()

# count words
for ele in corpus:
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] = dic[ele] + 1

# sort words which appear most times
sorted_word = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

# store result of sorted_word into count.csv
f = open("count.csv", "w")
f.write("word, count\n")
for word in sorted_word:
    if len(word[0]) >= 2:
        f.write("%s, %d\n" % (word[0], word[1]))

f.close()
