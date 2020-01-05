"""
selenium 
 - 웹 페이지 테스트 자동화용 모듈
 - 개발/테스트용 드라이버를 사용하여 실제 사용자가 사용하는 것처럼 동작
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

chrome_driver = 'chromedriver.exe'
driver = webdriver.Chrome( chrome_driver )

# driver.get( 'https://www.python.org' )
# search = driver.find_element_by_id('id-search-field')
# search.clear()
# time.sleep(3)
# search.send_keys('lambda')
# time.sleep(3)
# search.send_keys(Keys.RETURN)
# time.sleep(3)
# driver.close()


url = 'https://sports.news.naver.com/news.nhn?oid=032&aid=0002984411'
driver.get(url)
WebDriverWait( driver, 10 ).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.u_cbox_count')))

src = driver.page_source
soup = BeautifulSoup( src, 'html.parser' )
driver.close()

comment = soup.select_one('span.u_cbox_count')
print( comment.get_text() )
