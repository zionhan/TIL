# import requests
# import urllib.request as req
# 
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# 
# from bs4 import BeautifulSoup as bs
# import time
# 
# chrome_driver = '../chromedriver.exe'
# driver = webdriver.Chrome( chrome_driver )
# 
# 
# 
# 
# url = 'secretUrl'
# for i in range( 2000743000, 2002000000 ):    
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

with requests.Session() as s:
    first_page = s.get('https://naver.com')

for page in range(1900000001,9999999999):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'secretUrl' + str(page)
    html = requests.get(url, headers = headers).text
    time.sleep(random.uniform(1,4))  
    
    
    
        
    soup = bs(html,'html.parser')
    print(html)
    print()