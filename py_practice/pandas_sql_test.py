import pandas
import sqlite3
from datetime import datetime

# get data
dfs = pandas.read_html("http://rate.bot.com.tw/xrt?Lang=zh-TW")

currency = dfs[0]
# read columns we need
currency = currency.ix[:, 0:5]

# change column tags.
currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出',
                    u'即期匯率-本行買入', u'即期匯率-本行賣出']
# change 幣別
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
# add a column "Date" to record time.
currency['Date'] = datetime.now().strftime('%Y-%m-%d')
currency['Date'] = pandas.to_datetime(currency['Date'])

# the code below will save data to .xlsx
# currency.to_excel('currency.xlsx')

# save data to sql by using sqlite3
with sqlite3.connect('currency.sqlite') as db:
    # table, connect='db_file'
    currency.to_sql('currency', con=db, if_exists='append')

""" read currency.sqlite file
with sqlite3.connect('currency.sqlite') as db:
    dfs = pandas.read_sql_query('select * from currency', con=db)

print(dfs)
"""
