# 웹 스크래핑 
from bs4 import BeautifulSoup
from numpy import e
import requests
import re
import pandas as pd

# 위키피디아 미국 ETF 웹 페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')   
rows = soup.select('div > ul > li') #  html의 li 를 가져옴 

etfs = {}
# try except 구문 
for row in rows :
    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
        
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]] # 리스트를 원소로 갖는 딕셔너리를 정의하는법 

    except AttributeError as err:
        pass    

print(etfs)
print('\n')

# etfs 딕셔너리를 df로 변환
df = pd.DataFrame(etfs)
print(df)