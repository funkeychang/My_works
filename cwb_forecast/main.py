import pandas as pd
from datetime import datetime
from sqlalchemy import engine

# get tables from cwb.gov.tw
df = pd.read_html('http://www.cwb.gov.tw/V7/forecast/f_index.htm?_=1496715762494')

# arrange the table
for i in range(len(df)):
    df[i] = df[i].ix[1:]

# concat the tables
df2 = pd.concat(df)

# add datetime to the table df2
df2[3] = datetime.now().strftime('%Y%m%d-%H:%M')

# rename the labels
df2.columns = [u'城市', u'溫度', u'溼度', u'時間']

# save table to .csv
#df2.to_csv('cwb.csv')

# create mysql connection by using sqlalchemy..
# syntax: engine.create_engine("sql_name://uesr:password@host/db_name")
mysql_con = engine.create_engine("mysql://user:pwd@localhost/cwb_test")

print("Save data to database 'cwb_test' ...")
df2.to_sql(con=mysql_con, name='cwb_data', if_exists='append')
print("Done, now closing databse.")
