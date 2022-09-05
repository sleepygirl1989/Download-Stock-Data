import requests
from datetime import datetime as dt
import time

ticker = input("Enter your ticker symbol : ")
from_date =input("Enter start date in yyyy/mm/dd format : ")
to_date =input("Enter end date in yyyy/mm/dd format : ")

d= dt.strptime(from_date, '%Y/%m/%d')
t= dt.strptime(to_date, '%Y/%m/%d')
d_epoch=int(time.mktime(d.timetuple()))
t_epoch=int(time.mktime(t.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={d_epoch}&period2={t_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url , headers=headers).content
#print(content)

with open("data.csv","wb") as file:
  file.write(content)
