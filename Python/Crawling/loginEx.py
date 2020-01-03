'''
XHR( XML Http Request )
HTTP 상태코드
 - 1XX (정보 ) : 요청을 받았으며 프로세스를 계속한다.
 - 2XX (성공) : 요청을 성공적으로 받았으며 인식했고 수용하였다. 
 - 3XX (리다이렉션) : 요청 완료를 위해 추가 작업 조치가 필요하다.
 - 4XX (클라이언트 오류) : 요청의 문법이 잘못되었거나 요청을 처리할 수 없다.
 - 5XX (서버 오류) : 서버가 명백히 유효한 요청에 대해 충족을 실패했다.
'''
from bs4 import BeautifulSoup as bs
import requests
headers = {
    'Accept' : '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwiZ3JhbnRfdHlwZSI6ImFsZXhfY3JlZGVudGlhbHMiLCJzY29wZSI6W10sImV4cCI6MTU3ODA3NTI5OCwiYXV0aG9yaXRpZXMiOlsiUk9MRV9DTElFTlQiXSwianRpIjoiZTQ4Yzc1NTgtNjgxZS00NTVlLTlhNjctODc1MjhjYWQwYjRiIiwiZm9ydW1faWQiOi05OSwiY2xpZW50X2lkIjoiMjZCWEF2S255NVdGNVowOWxyNWs3N1k4In0.OAv5-PFjc97gAEJXHx2NCfx7JZ8IsNmBRAlAFgWZ7Q8',
    'Connection': 'keep-alive',
    'Cookie': 'webid=1abe29c8ef854a0eb1d67fba198438f7; SLEVEL=0; AGEN=RxUM8UwSSSpwS7sM9KqRyeggHiqHFnLkM2R3RaHRrCQ; TIARA=g.gWdp4oAWBiWkoZhI_tF_51nLl8IXYfUjomVExso4XSPEBqVF91hMMt-.t1TPLjp5FQsmDOgQqL2V2Nf9Ekvkm3z_xVRync; webid_sync=1578032323476',
    'Host': 'comment.daum.net',
    'Origin': 'https://news.v.daum.net',
    'Referer': 'https://news.v.daum.net/v/20190728165812603',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url = 'https://comment.daum.net/apis/v1/posts/@20190728165812603'
resp = requests.get( url, headers=headers )
print( resp )
print( resp.json()['commentCount'] )

# login endpoint
endpoint = 'https://www.kangcom.com/member/member_check.asp'
info = {
    'id': '***********',
    'pwd': '*********'
}

s = requests.Session()
resp = s.post( endpoint, data=info )
print( resp )

url = 'https://www.kangcom.com/basket/cart.asp?tC=1'
resp = s.get(url)
soup = bs( resp.text )
print( soup.select( 'span.cart_member_point' )[0].text )

# .cart_member_point1