import requests as req
from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# 시스템 환경변수 : 새로 만들기 PYTHONIOENCODING // utf-8

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
resp = req.get( "https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20191104", headers=headers )
soup = BeautifulSoup( resp.text, 'html.parser' )


charts = soup.select( "#body-content > div.newest-list > div > table > tbody > tr" )


for i in range( 50 ) :
    rank = i+1
    title = charts[i].select_one("td.info > a.title.ellipsis").text.strip()
    singer = charts[i].select_one("td.info > a.artist.ellipsis").text.strip()
    print( rank," : ", title, singer )
