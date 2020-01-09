import pyodbc
import requests
import time
import random
import json

conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=LAPTOP-AIQB4OTH;'
                     'Database=naver_article;'
                     'Trusted_Connection=yes;')
cursor = conn.cursor()


def sqlquote( value ):
    """Naive SQL quoting
    All values except NULL are returned as SQL strings in single quotes,
    with any embedded quotes doubled.
    """
    if value is None or value=="":
        return 'NULL'
    return "'{}'".format(str(value).replace( "'", "''" ))


def sqlquery( tableName, columns, page ):    
    if 'articleNo' not in columns:      # 참조 변수 변경시 수정해줘야 한다.
        columns['articleNo'] = page 
    
    if 'lineNo' in columns:
        columns['tempNo'] = columns.pop('lineNo')    
    print( columns )
            
    query_command = "INSERT INTO {} (".format(tableName)
    for column in columns:       
        query_command += column + ","
    query_command = query_command[0:-1] + ") VALUES ("
     
    for column in columns:
        query_command += "{" + column + "},"
    query_command = query_command[0:-1] + ");"
    
#     print( query_command.format( ** {k: sqlquote(v) for k, v in columns.items()} ) )
        
    # 예외처리를 여기서 해야한다!
    cursor.execute( query_command.format( ** {k: sqlquote(v) for k, v in columns.items()} ) )
    cursor.commit()



def autoCrawling_naverlandApi( json_data, page ):
    """autoCrawling
        네이버 api DB 적재 자동화
    """
    del( json_data['articleExistTabs'] ) # 의미 없는 데이터.
#     del( json_data['landPrice'] ) # 'lineNo' 칼럼에서 알 수 없는 오류.   
    
    for tableName in json_data:                
        columns = json_data[tableName]                       
        
        if( len(columns) > 0 ): # 테이블 안에 값이 없는 경우도 있다.
            print( columns )
            # 조건 조정을 일반화 할 수 없을까...?    
            if isinstance( columns, list ): # 리스트인 경우 한번더 벗겨야 한다.                
                for i in range( 0, len(columns) ):
                    change_columns = columns[i] 
                    sqlquery( tableName, change_columns, page )            
            
            else:
                sqlquery( tableName, columns, page )
                                
                for column in columns:  # 서브 테이블 관련 코드                    
                    change_columns = columns[column]
                    tableName = column     
                                              
                    if isinstance( change_columns, list ) and len(change_columns)>0 and isinstance( change_columns[0], dict ):                                                
                        for i in range( 0, len(change_columns) ):                            
                            sqlquery( tableName, change_columns[i], page )
                            
                    elif isinstance ( change_columns, dict ):
                        sqlquery( tableName, change_columns, page )                        
                        print( change_columns )
                        
                        for column in change_columns:    # 테이블 안의 테이블 안의 테이블.
                            if isinstance( change_columns[column], list ):
                                tableName = column
                                for i in range( 0, len(change_columns[column]) ):
                                    sqlquery( tableName, change_columns[column][i], page )                
                
# 2000700300,2000701155 ,2000701532
with requests.Session() as s:
    first_page = s.get('https://naver.com')
   
for page in range(2000701533, 2000703783 ):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'secretApi' + str(page)
    html = requests.get(url, headers = headers).text
    time.sleep(random.uniform(1,4))
    json_data = json.loads( html )    
    
    print( "page : " + str(page) )
       
    if 'error' not in json_data:     
        autoCrawling_naverlandApi(json_data, page)           
    else:
        print( '단지 정보가 없습니다.' )
        print()

cursor.close()
conn.close()
