from bs4 import BeautifulSoup as bs
import requests

url = 'https://news.v.daum.net/v/20190728165812603'

resp = requests.get( url )
soup = bs( resp.text )
print( soup.find('h3', class_='tit_view').get_text() )

print( soup.find_all( 'span', class_='txt_info' )[0].get_text() )

containers = soup.find( 'div', id='harmonyContainer').find_all('p')
# print( containers )

for container in containers:
    print( container.get_text().strip() )




