from bs4 import BeautifulSoup as bs
import requests

'''
CSS를 이용하여  tag 찾기
    - select, select_one 함수 사용
    - css selector 사용법
             태그명 찾기 tag
             자손 태그 찾기 - 자손 관계(tag tag)
             자식 태그 찾기 - 다이렉트 자식 관계 ( tag > tag )
             아이디 찾기 - #id
             클래스 찾기 - .class
             속성값 찾기 [속성name='test] ( prefix [name^='test'], suffix [name $='test'], substring [name *='test']
      n번째 자식 tag 찾기 - nth-child(n)
'''


url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get( url )
soup = bs( resp.text )

print( soup.select('h3.tit_view') )
# > 바로 하위 자손, " " 자손들 모두, # id, . class 
for p in soup.select('#harmonyContainer p'):
    print( p.get_text() )
    
    
print( soup.select('h3[class="tit_view"]') )
print( soup.select('h3[class^="tx"]') )
print( soup.select('h3[class$="ew"]') )


print( soup.select( 'span.txt_info:nth-child(1)' ) )
print( soup.select( 'span.txt_info:nth-child(2)' ) )