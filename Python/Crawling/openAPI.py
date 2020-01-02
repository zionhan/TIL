import requests
from bs4 import BeautifulSoup

serviceKey = '9b1iU7GyA5eJvn%2BqsZ4n3%2B33JFFk%2BLePFzeg0g1NTszXMyCQCP7INi77Bw0oNrpJi3%2BDAYGtcFag0u69aMzcQA%3D%3D'
endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/areaCode?serviceKey={}&numOfRows=10&pageSize=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&_type=json'.format( serviceKey )
print( endpoint )

resp = requests.get(endpoint)
print( resp.text )
print( resp.status_code )

data = resp.json()
print( data['response']['body']['items']['item'][0] )
