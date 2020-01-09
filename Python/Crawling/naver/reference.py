import pandas as pd
from bs4 import BeautifulSoup
import csv
import urllib.request as req

# 
# ads = pd.read_excel( "address.xlsx" )
# df = pd.DataFrame( ads )
# df = df.iloc[:,0:1]
# df.columns = [ "code" ]
# df.code = df.code//100000
# df = df.drop_duplicates("code", keep='first')
# print( df.loc[df['code']>=41570], ["code"] )
# print( df )
# df2 = df.loc[df['code']>41570], ["code"]
# print( df2 )

# for i in df.code :    
#     url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=" + str(i) + "&DEAL_YMD=201812&numOfRows=999&serviceKey=OUwSlot%2BeCADq1M9zzdj8Sh1Ni9C4Iiaj9VqSEnyvikodjynkoS1hrbUsP6mSENccvTJH%2FDe3s3y7i836Lk7ew%3D%3D"
#     data = req.urlopen(url).read().decode("utf-8")
#     xmlsoup = BeautifulSoup(data, 'lxml-xml')
#     te=xmlsoup.find_all("item")
#     sil=pd.DataFrame()    
#     for t in te :
#         price = t.find("거래금액").text.strip()
#         dong=t.find("법정동").text.strip()
#         year=t.find("년").text.strip()
#         month=t.find("월").text.strip()
#         day=t.find("일").text.strip()
#         jimock=t.find("지번").text.strip()
#         lawd_cd=t.find("지역코드").text.strip()
#          
#         temp = pd.DataFrame([[price,year,dong,month,day,jimock,lawd_cd]],
#                             columns=["가격","년","동","월","일","지목","번지"])
#         sil=pd.concat([sil,temp]) 
#     sil.to_csv( "cost.csv", mode='a')    
#     print( str(i) + "입력 완료" )
#      
#  
# print( "csv 파일생성 완료" )

# url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=" + '41590' + "&DEAL_YMD=201812&numOfRows=999&serviceKey=OUwSlot%2BeCADq1M9zzdj8Sh1Ni9C4Iiaj9VqSEnyvikodjynkoS1hrbUsP6mSENccvTJH%2FDe3s3y7i836Lk7ew%3D%3D"
# data = req.urlopen(url).read().decode("utf-8")
# xmlsoup = BeautifulSoup(data, 'lxml-xml')
# te=xmlsoup.find_all("item")
# sil=pd.DataFrame()    

# print( sil )
# for t in te :
#     price = t.find("거래금액").text.strip()
#     dong=t.find("법정동").text.strip()
#     year=t.find("년").text.strip()
#     month=t.find("월").text.strip()
#     day=t.find("일").text.strip()
#     jimock=t.find("지번").text
#     print( jimock )
#     lawd_cd=t.find("지역코드").text.strip()
#       
#     temp = pd.DataFrame([[price,year,dong,month,day,jimock,lawd_cd]],
#                         columns=["가격","년","동","월","일","지목","번지"])
#     sil=pd.concat([sil,temp]) 
#     print( sil )
#     
#     
# print( sil )    
# sil.to_csv( "cost.csv", mode='a')   


serviceKey = "%2BccCMVzlmloga4mYfWGCfSYuyTkP7LeBwSxw9DVFi4MM6djOYH66lnYCkM%2BQugxEAasvX%2FoVv%2FmwcEsEWdNJzA%3D%3D" 
url = "http://apis.data.go.kr/1611000/BldRgstService/getBrExposPubuseAreaInfo?serviceKey=" + serviceKey + "&numOfRows=999&sigunguCd=11680&bjdongCd=10300"
data = req.urlopen( url ).read().decode( "utf-8" )
xmlsoup = BeautifulSoup( data, 'lxml-xml' )
te = xmlsoup.find_all( "item" )
sil = pd.DataFrame()

print( te )
for t in te :
    print('요기')
    print( t )


# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('sigunguCd') : '11680', quote_plus('bjdongCd') : '10300', quote_plus('platGbCd') : '0', quote_plus('bun') : '0012', quote_plus('ji') : '0000', quote_plus('dongNm') : '', quote_plus('hoNm') : '', quote_plus('startDate') : '', quote_plus('endDate') : '' })