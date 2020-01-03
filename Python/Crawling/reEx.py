# Regular Expression 정규표현식
# 정규표현식 공부좀 해볼까나
import re
from bs4 import BeautifulSoup as bs
import requests
url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get( url )
soup = bs( resp.text )
print( soup.find_all( re.compile('h\d') ) )
print()
print( soup.find_all('img', attrs={'src': re.compile('.+\.jpg')}) )
print()
print( soup.find_all('h3', class_=re.compile('.+view$')) )
