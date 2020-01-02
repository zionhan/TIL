import requests
# 크롤링이 안될 때 header이용, 보통 User-agent 값 이용.
url = 'https://news.v.daum.net/v/20190728165812603'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36' 
}
resp = requests.get( url, headers=header )

print( resp )
print( resp.encoding )
# 2로 시작하면 요청-응답 성공.
if resp.status_code == 200 :
    print( resp.text )
else :
    print( 'error' )

print('===================================================')


data = {
    'id': 'macmath22',
    'pwd': 'Test1357!'
}


url2 = 'https://www.kangcom.com/member/member_check.asp'
resp2 = requests.post( url, data=data )
print( resp2.text )