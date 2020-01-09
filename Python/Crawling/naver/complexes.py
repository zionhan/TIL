'''
숫자만 받는다.
'''
import requests
import urllib.request as req

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs
import time



# 
# resp = requests.get( url.format('1') )
# print( resp )
# print( resp.text )

# data = req.urlopen( url.format('1') ).read().decode( "utf-8" )
# xmlsoup = bs( data, 'lxml-xml' )
# 
# print( xmlsoup )

# chrome_driver = '../chromedriver.exe'
# driver = webdriver.Chrome( chrome_driver )

# driver.get( 'https://www.python.org' )
# search = driver.find_element_by_id('id-search-field')
# search.clear()
# time.sleep(3)
# search.send_keys('lambda')
# time.sleep(3)
# search.send_keys(Keys.RETURN)
# time.sleep(3)
# driver.close()



# for i in range( 1, 19790 ):    
#     driver.get(url.format(i))
# #     time.sleep(1)
# #     print( driver )
# #     print( type(driver) )
#      
#     # WebDriverWait( driver, 10 ).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.u_cbox_count')))
#     src = driver.page_source
#     soup = bs( src, 'html.parser' )
#     comment = soup.select_one('pre')
#     print( comment.get_text() )


import requests
from bs4 import BeautifulSoup as bs
import time
import random
import json

with requests.Session() as s:
    first_page = s.get('https://naver.com')

for page in range(1035,99999):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'secretApi' + str(page)
    html = requests.get(url, headers = headers).text
    time.sleep(random.uniform(1,3))
    json_data = json.loads( html )
    
    
#     photo_cnt = []
#     complexDetail_cnt = []    
#     complexPyeongDetailList_cnt = []    
#     photo_cnt.append( len( photos[0] ) )
#     complexDetail_cnt.append( len(complexDetail) )
#     complexPyeongDetailList_cnt.append( len(complexPyeongDetailList[0]) )

    if 'error' in json_data:
        print( '단지 정보가 없습니다.' )
        print()

    if 'error' not in json_data :
        photos = json_data['photos']
        complexDetail = json_data['complexDetail']
        complexPyeongDetailList = json_data['complexPyeongDetailList']
        
        print( '단지번호 : ' + str(page) )
        if(len( json_data ) > 4 ):
            print( 'wowowowowwowowowowowowow!!!!!' )
        print( "table 갯수 : " + str(len(json_data)) )
            
        if( len(photos) > 0 ):
            print( '사진칼럼수 : ' + str(len(photos[0])) )
            if( len(photos[0]) > 9 ):
                print( 'wowowowowwowowowowowowow!!!!!' )
                print( '사진칼럼수 : ' + str(len(photos[0])) )
        else:
            print( '사진이 없습니다.' )
            
        
        if( len(complexDetail) > 33 ):
            print( 'wowowowowwowowowowowowow!!!!!' )
        print( '단지상세정보 칼럼수 : ' + str(len(complexDetail)) ) 
            
        if len(complexPyeongDetailList) > 0 :
            print( '평당 상세정보 칼럼수 : ' + str(len(complexPyeongDetailList[0])) )
            if len(complexPyeongDetailList[0]) > 19 :
                print( 'wowowowowwowowowowowowow!!!!!' )            
                print( '평당 상세정보 칼럼수 : ' + str(len(complexPyeongDetailList[0])) )            
        else:
            print( '평당 상세정보가 없습니다.' )            
        print()
#     soup = bs(html,'html.parser')
# #     print(soup)
#     print(html)
#     print()


# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# html = requests.get(url, headers=headers).text
# json_data = json.loads( html )
# photos = json_data['photos']
# complexDetail = json_data['complexDetail']
# complexPyeongDetailList = json_data['complexPyeongDetailList']
# photo_cnt = []
# complexDetail_cnt = []
# complexPyeongDetailList_cnt = []
# print( len( photos[0] ) )
# print( len(complexDetail) )
# print( len(complexPyeongDetailList[0]) )
# soup = bs(html, 'html.parser')
# print( soup )
# json_soup = 
# photos = soup['photos']