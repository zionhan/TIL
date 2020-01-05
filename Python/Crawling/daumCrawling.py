from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import requests

def get_daum_news_title(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tag = soup.select_one('h3.tit_view')
    if title_tag:
        return title_tag.get_text()
    return ''

def get_daum_news_content(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    content = ''
    for p in soup.select('div#harmonyContainer p'):
        content += p.get_text() + '\n'
    
    return content


print( get_daum_news_title('20200105213021253') )
print( get_daum_news_content('20200105213021253'))
print()
print()
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwidXNlcl92aWV3Ijp7ImlkIjoyMjc5OTkyMiwiaWNvbiI6Imh0dHBzOi8vdDEuZGF1bWNkbi5uZXQvcHJvZmlsZS9DQ0JTQTFvSXpLUTAiLCJwcm92aWRlcklkIjoiREFVTSIsImRpc3BsYXlOYW1lIjoi7ZWc64-EIn0sImdyYW50X3R5cGUiOiJhbGV4X2NyZWRlbnRpYWxzIiwic2NvcGUiOltdLCJleHAiOjE1NzgyNzc1MjEsImF1dGhvcml0aWVzIjpbIlJPTEVfREFVTSIsIlJPTEVfSURFTlRJRklFRCIsIlJPTEVfVVNFUiJdLCJqdGkiOiI4ZGEwNzM2My04OWRlLTRiZDAtOTliZi0yNTQzZmZlNDBjNWUiLCJmb3J1bV9pZCI6LTk5LCJjbGllbnRfaWQiOiIyNkJYQXZLbnk1V0Y1WjA5bHI1azc3WTgifQ.3BqcOxnXjqL5YSBCid2SA3r9FmlYgalJthHFmopL7t8',
    'Connection': 'keep-alive',
    'Cookie': 'webid=1abe29c8ef854a0eb1d67fba198438f7; SLEVEL=0; HM_CU=5CyID0CuD79; PROF=0603012032024076024140UiQPJk7X-6w0mlxoempuua-X8T9SYaoHRiH_UXIqrSdJKuZP3z7wEl2bxriNh5SdkQ00LYYSA9A1_cGNLCyhCzrwOkP8vT4.SomZE8SzF8R5U6hNJuTinJs6upShqUiqe6jrGQxWoed2CVY0fIauQlo8OTLLnHHY.bHDTw005.D3F1Q7ttKHZZwwRPDWZskvueiTnsl5ty2xKV.z9E8p8KEY8qjVdkhOFke8Idmp2_jHhhQq2q.QFLx92AjMPRZizKu7EweEYh4ZS3pV8w1Vf_732JGeBzeyes5.51L5jzgRyoUfLxQ0; TS=1578234315; HTS=cJ1JXe.8wi6Ha_.o-CPDHw00; ALID=luaRwQb94aR39blund9BtUV8GdoClbNdiEczUHuU4EuHrO5AjEnIN5oszMeiixP2w999UI; ALCT=KsLAFvjGDXvfJvS488LXb9cndebdPs54YXyNM37H_GU; LSID=99b7bd02-710a-4b42-afb4-2277adeb00691578234315888; AGEN=JbuDNXrLwilSlqYhl81loTO5mD3fLKW1Dedu9H7kbiQ; webid_sync=1578234857517; TIARA=YWLCGP4HVK6nIsjIAxHtUkUlpZLNAFSw66.e4FV4yKVsvTYLphFNkzW7GkIwmQVdDl5rU-gf3Uj9rT1gsyUIcSZVnHNql7dJ',
    'Host': 'comment.daum.net',
    'Origin': 'https://news.v.daum.net',
    'Referer': 'https://news.v.daum.net/v/20200105213021253',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url = 'https://comment.daum.net/apis/v1/posts/@20200105213021253/comments?parentId=0&offset=543&limit=10&sort=RECOMMEND&isInitial=false'
resp = requests.get(url, headers=headers)
print( resp.json() )

def get_daum_news_comments(news_id):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwidXNlcl92aWV3Ijp7ImlkIjoyMjc5OTkyMiwiaWNvbiI6Imh0dHBzOi8vdDEuZGF1bWNkbi5uZXQvcHJvZmlsZS9DQ0JTQTFvSXpLUTAiLCJwcm92aWRlcklkIjoiREFVTSIsImRpc3BsYXlOYW1lIjoi7ZWc64-EIn0sImdyYW50X3R5cGUiOiJhbGV4X2NyZWRlbnRpYWxzIiwic2NvcGUiOltdLCJleHAiOjE1NzgyNzc1MjEsImF1dGhvcml0aWVzIjpbIlJPTEVfREFVTSIsIlJPTEVfSURFTlRJRklFRCIsIlJPTEVfVVNFUiJdLCJqdGkiOiI4ZGEwNzM2My04OWRlLTRiZDAtOTliZi0yNTQzZmZlNDBjNWUiLCJmb3J1bV9pZCI6LTk5LCJjbGllbnRfaWQiOiIyNkJYQXZLbnk1V0Y1WjA5bHI1azc3WTgifQ.3BqcOxnXjqL5YSBCid2SA3r9FmlYgalJthHFmopL7t8',
        'Connection': 'keep-alive',
        'Cookie': 'webid=1abe29c8ef854a0eb1d67fba198438f7; SLEVEL=0; HM_CU=5CyID0CuD79; PROF=0603012032024076024140UiQPJk7X-6w0mlxoempuua-X8T9SYaoHRiH_UXIqrSdJKuZP3z7wEl2bxriNh5SdkQ00LYYSA9A1_cGNLCyhCzrwOkP8vT4.SomZE8SzF8R5U6hNJuTinJs6upShqUiqe6jrGQxWoed2CVY0fIauQlo8OTLLnHHY.bHDTw005.D3F1Q7ttKHZZwwRPDWZskvueiTnsl5ty2xKV.z9E8p8KEY8qjVdkhOFke8Idmp2_jHhhQq2q.QFLx92AjMPRZizKu7EweEYh4ZS3pV8w1Vf_732JGeBzeyes5.51L5jzgRyoUfLxQ0; TS=1578234315; HTS=cJ1JXe.8wi6Ha_.o-CPDHw00; ALID=luaRwQb94aR39blund9BtUV8GdoClbNdiEczUHuU4EuHrO5AjEnIN5oszMeiixP2w999UI; ALCT=KsLAFvjGDXvfJvS488LXb9cndebdPs54YXyNM37H_GU; LSID=99b7bd02-710a-4b42-afb4-2277adeb00691578234315888; AGEN=JbuDNXrLwilSlqYhl81loTO5mD3fLKW1Dedu9H7kbiQ; webid_sync=1578234857517; TIARA=YWLCGP4HVK6nIsjIAxHtUkUlpZLNAFSw66.e4FV4yKVsvTYLphFNkzW7GkIwmQVdDl5rU-gf3Uj9rT1gsyUIcSZVnHNql7dJ',
        'Host': 'comment.daum.net',
        'Origin': 'https://news.v.daum.net',
        'Referer': 'https://news.v.daum.net/v/20200105213021253',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    offset = 0
    url_template = 'https://comment.daum.net/apis/v1/posts/@{}/comments?parentId=0&offset={}&limit=10&sort=RECOMMEND&isInitial=false'
    comments = []
    while True:
        url = url_template.format( news_id, offset )
        resp = requests.get( url, headers=headers )
        data = resp.json()
        if not data :
            break
        
        comments.extend(data)
        offset += 10
    return comments
    
print( len( get_daum_news_comments('20200105213021253') ) )
    