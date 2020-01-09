import urllib.request as req
import pyodbc

import requests
from bs4 import BeautifulSoup as bs
import time
import random
import json

def sqlquote( value ):
    """Naive SQL quoting
    All values except NULL are returned as SQL strings in single quotes,
    with any embedded quotes doubled.
    """
    if value is None or value=="":
        return 'NULL'
    return "'{}'".format(str(value).replace( "'", "''" ))


# for page in range(1900000001,9999999999):
for page in range(2000700783, 2000728783):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    url = 'secretUrl'.format(page)
    html = requests.get(url, headers = headers).text
    time.sleep(random.uniform(1,4))  
    json_data = json.loads( html )
    
    print( 'articleNo : ' + str(page) )
    if 'error' not in json_data:
        print( 'table : ' + str(len(json_data)) )
        print()
        for table in json_data:            
            if table == "landPrice":
                print( '응 landPrice는 있어' )
                for column in json_data[table]:
                    if column == 'landPriceTax':
                        print("와우우우우웅웅우우우우우웅우!!!!!!")
                        print('=========================')
                    
#             print( table + " : " + str( len(json_data[table]) ) )            
#             for column in table:
#                 print( "column : " + column )
#                 print( type( column ) )
#                 if len(column) > 0:                
#                     print( type(column[0]) )           
        print()
        print('==========================================')
        print()
    else:
        print()
        print( '단지정보가 없습니다.' )
        print( '=========================================' )