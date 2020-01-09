import urllib.request as req
import pyodbc

import requests
from bs4 import BeautifulSoup as bs
import time
import random
import json

# conn = pyodbc.connect('DRIVER={SQL Server};SERVER={localServer};DATABASE={localDB}')
# cursor = conn.cursor()
# for record in response:
#     print(json.dumps(record))
#     cursor.execute("Insert Into Ticket_Info values ?", json.dumps(record))
#     cursor.commit()
# cursor.close()
# conn.close()

def sqlquote( value ):
    """Naive SQL quoting
    All values except NULL are returned as SQL strings in single quotes,
    with any embedded quotes doubled.
    """
    if value is None or value=="":
        return 'NULL'
    return "'{}'".format(str(value).replace( "'", "''" ))


conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=LAPTOP-AIQB4OTH;'
                     'Database=naver;'
                     'Trusted_Connection=yes;')
cursor = conn.cursor()


complex_columns = [
    'complexNo', 'complexName', 'cortarNo', 'realEstateTypeCode', 'realEstateTypeName', 'detailAddress', 'roadAddress',
    'latitude', 'longitude', 'totalHouseholdCount', 'totalLeaseHouseholdCount', 'highFloor', 'lowFloor', 'completionYearMonth', 
    'totalDongCount', 'maxSupplyArea', 'minSupplyArea', 'dealCount', 'rentCount', 'leaseCount', 'shortTermRentCount', 'isBookmarked',
    'batlRatio', 'btlRatio', 'plumbReplace', 'parkingCountByHousehold', 'constructionCompanyName', 'heatMethodTypeCode', 'heatFuelTypeCode',
    'pyoengNames', 'managementOfficeTelNo', 'buildingRegister', 'address', 'roadAddressPrefix'
]

photo_columns = [
    'imageKey', 'imageSrc', 'imageId', 'etcItem1', 'newOldGbn', 'smallCategoryName', 'explaination', 'registYmdt', 'imageOrder'
]

complexPyeongDetail_columns = [    
    'complexNo', 'pyeongNo', 'supplyAreaDouble', 'supplyArea', 'pyeongName', 'supplyPyeong', 'pyeongName2', 'exclusiveArea',
    'exclusivePyeong', 'householdCountByPyeong', 'realEstateTypeCode', 'exclusiveRate', 'grandPlanList', 'maintenanceCostList', 'averageMaintenanceCost',
    'articleStatistics', 'entranceType', 'landPriceMaxByPtp', 'roomCnt', 'bathroomCnt'
]

complexRebuilding_columns = [
    'complexNo', 'businessStep', 'selectedBuilder', 'householdCount', 'assignedArea', 'floorAreaRatio', 'builderTelNo'
]

grandPlan_columns = [
    'grandPlanNo', 'complexPyeongNo', 'imageId', 'imageOrder', 'imageSrc', 'imageType'
]

maintenanceCost_columns = [
    'complexPyeongNo', 'basisYearMonth', 'totalPrice'
]

averageMaintenanceCost_columns = [
    'complexPyeongNo', 'averageTotalPrice', 'summerTotalPrice', 'winterTotalPrice'
]

landPriceMaxByPtp_columns = [
    'complexPyeongNo', 'ptpNo', 'supplyArea', 'totalArea', 'maxPrice', 'stdYear', 'stdYmd', 'landPriceTax'
]

landPriceTax_columns = [
    'complexPyeongNo', 'propertyTotalTax', 'propertyTax', 'localEduTax', 'cityAreaTax', 'realEstateTotalTax', 'decisionTax', 'ruralSpecialTax'
]

articleStatistics_columns = [
    'complexPyeongNo', 'pyeongNo', 'dealCount', 'leaseCount', 'rentCount', 'shortTermRentCount',
    'dealPriceMin', 'dealPriceMax', 'leasePriceMin', 'leasePriceMax', 'dealPricePerSpaceMin', 'dealPricePerSpaceMax',
    'leasePricePerSpaceMin', 'leasePricePerSpaceMax', 'leasePriceRateMin', 'leasePriceRateMax', 'dealPriceString', 'dealPricePerSpaceString',
    'leasePriceString', 'leasePricePerSpaceString', 'leasePriceRateString', 'rentPriceString', 'rentDepositPriceMin', 'rentPriceMin',
    'rentDepositPriceMax', 'rentPriceMax'
]




with requests.Session() as s:
    first_page = s.get('https://naver.com')
   
for page in range(1, 300):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'secretApi' + str(page)
    html = requests.get(url, headers = headers).text
    time.sleep(random.uniform(1,4))
    json_data = json.loads( html )
       
    if 'error' not in json_data:        
        ''' complexDetail Table '''
        complexDetail = json_data['complexDetail']
           
        for column in complex_columns:
            if( column not in complexDetail ):
                complexDetail[column] = None
        print( complexDetail )        
           
        execute_command = """
            INSERT INTO dbo.complexDetail
            VALUES( {complexNo}, {complexName}, {cortarNo}, {realEstateTypeCode}, {realEstateTypeName}, {detailAddress},
            {roadAddress}, {latitude}, {longitude}, {totalHouseholdCount}, {totalLeaseHouseholdCount},
            {highFloor}, {lowFloor}, {completionYearMonth}, {totalDongCount}, {maxSupplyArea}, {minSupplyArea},
            {dealCount}, {rentCount}, {leaseCount}, {shortTermRentCount}, {isBookmarked},
            {batlRatio}, {btlRatio}, {plumbReplace}, {parkingCountByHousehold}, {constructionCompanyName}, {heatMethodTypeCode}, {heatFuelTypeCode},
            {pyoengNames}, {managementOfficeTelNo}, {buildingRegister}, {address}, {roadAddressPrefix} );
        """        
        cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in complexDetail.items()} ) )
        cursor.commit()        
        
        ''' photos Table '''
        photos = json_data['photos']
        if len(photos) > 0:
            for photo in photos:
                for column in photo_columns:
                    if( column not in photo ):
                        photo[column] = None
                print( photo )
                execute_command = """
                    INSERT INTO dbo.photos
                    VALUES( {imageKey}, {imageSrc}, {imageId}, {etcItem1}, {newOldGbn}, {smallCategoryName}, {explaination}, {registYmdt}, {imageOrder} );
                """
                cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in photo.items() } ) )
                cursor.commit()        

#         ''' complexRebuilding Table '''
#         if 'complexRebuilding' in json_data:
#             complexRebuilding = json_data['complexRebuilding']
#             complexRebuilding['complexNo'] = page
#             for column in complexRebuilding_columns:
#                 if column not in complexRebuilding:
#                     complexRebuilding[column] = None
#             print( complexRebuilding )
#             execute_command = """
#                 INSERT INTO dbo.complexRebuilding
#                 VALUES( {complexNo}, {businessStep}, {selectedBuilder}, {householdCount}, {assignedArea}, {floorAreaRatio}, {builderTelNo} );
#             """
#             cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in complexRebuilding.items() } ) )
#             cursor.commit()
# 
#         ''' complexPyeongDetailList Table '''
#         complexPyeongDetailList = json_data['complexPyeongDetailList']        
#          
#         for complexPyeongDetail in complexPyeongDetailList:        
#             complexPyeongDetail['complexNo'] = page
#             for column in complexPyeongDetail_columns:
#                 if column not in complexPyeongDetail:
#                     complexPyeongDetail[column] = None
#             print( complexPyeongDetail )
#               
#             execute_command = """
#                 INSERT INTO dbo.complexPyeongDetail
#                 VALUES ( {complexNo}, {pyeongNo}, {supplyAreaDouble}, {supplyArea}, {pyeongName}, {supplyPyeong}, {pyeongName2}, 
#                 {exclusiveArea}, {exclusivePyeong}, {householdCountByPyeong}, {realEstateTypeCode}, {exclusiveRate}, {grandPlanList},
#                 {maintenanceCostList}, {averageMaintenanceCost}, {articleStatistics}, {entranceType}, {landPriceMaxByPtp}, {roomCnt}, {bathroomCnt} );
#             """
#             cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in complexPyeongDetail.items() } ) )
#             cursor.commit()
#             
#             cursor.execute( "SELECT complexPyeongNo FROM complexPyeongDetail WHERE complexNo={} and pyeongNo={}".format( page, complexPyeongDetail['pyeongNo'] ) )
#             
#             row = cursor.fetchone()
#             complexPyeongNo = [x for x in row][0]            
#              
#             if complexPyeongDetail['grandPlanList'] is not None and len(complexPyeongDetail['grandPlanList'])>0:
#                 grandPlanList = complexPyeongDetail['grandPlanList']                
#                 for grandPlan in grandPlanList:                
#                     print( grandPlan )
#                     grandPlan['complexPyeongNo'] = complexPyeongNo
#                     for column in grandPlan_columns:
#                         if column not in grandPlan:
#                             grandPlan[column] = None
#                             print( grandPlan )
#                   
#                     execute_command = """
#                         INSERT INTO dbo.grandPlanList
#                         VALUES ( {complexPyeongNo}, {imageId}, {imageOrder}, {imageSrc}, {imageType} );
#                     """
#                     cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in grandPlan.items() } ) )
#                     cursor.commit() 
#                 
#                 
#             if complexPyeongDetail['maintenanceCostList'] is not None and len( complexPyeongDetail['maintenanceCostList'] ) >0:
#                 maintenanceCostList = complexPyeongDetail['maintenanceCostList']
#                 for maintenanceCost in maintenanceCostList:
#                     maintenanceCost['complexPyeongNo'] = complexPyeongNo
#                     for column in maintenanceCost_columns:
#                         if column not in maintenanceCost:
#                             maintenanceCost[column] = None
#                             print( maintenanceCost )
#                   
#                     execute_command = """
#                         INSERT INTO dbo.maintenanceCostList
#                         VALUES ( {complexPyeongNo}, {basisYearMonth}, {totalPrice} );
#                     """
#                     cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in maintenanceCost.items() } ) )
#                     cursor.commit()
#        
#             
#             if complexPyeongDetail['averageMaintenanceCost'] is not None:
#                 averageMaintenanceCost = complexPyeongDetail['averageMaintenanceCost']
#                 averageMaintenanceCost['complexPyeongNo'] = complexPyeongNo
#                 for column in averageMaintenanceCost_columns:
#                     if column not in averageMaintenanceCost:
#                         averageMaintenanceCost[column] = None
#                         print( averageMaintenanceCost )
#               
#                 execute_command = """
#                     INSERT INTO dbo.averageMaintenanceCost
#                     VALUES ( {complexPyeongNo}, {averageTotalPrice}, {summerTotalPrice}, {winterTotalPrice} );
#                 """
#                 cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in averageMaintenanceCost.items() } ) )
#                 cursor.commit()
#           
#             
#             if complexPyeongDetail['articleStatistics'] is not None:
#                 articleStatistics = complexPyeongDetail['articleStatistics']
#                 articleStatistics['complexPyeongNo'] = complexPyeongNo
#                 for column in articleStatistics_columns:
#                     if column not in articleStatistics:
#                         articleStatistics[column] = None
#                         print( articleStatistics )
#               
#                 execute_command = """
#                     INSERT INTO dbo.articleStatistics
#                     VALUES ( {complexPyeongNo}, {pyeongNo}, {dealCount}, {leaseCount}, {rentCount}, {shortTermRentCount}, {dealPriceMin},
#                     {dealPriceMax}, {leasePriceMin}, {leasePriceMax}, {dealPricePerSpaceMin}, {dealPricePerSpaceMax}, {leasePricePerSpaceMin}, {leasePricePerSpaceMax},
#                     {leasePriceRateMin}, {leasePriceRateMax}, {dealPriceString}, {dealPricePerSpaceString}, {leasePriceString}, {leasePricePerSpaceString},
#                     {leasePriceRateString}, {rentPriceString}, {rentDepositPriceMin}, {rentPriceMin}, {rentDepositPriceMax}, {rentPriceMax} );
#                 """
#                 cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in articleStatistics.items() } ) )
#                 cursor.commit()
#             
#             
#             if complexPyeongDetail['landPriceMaxByPtp'] is not None:
#                 landPriceMaxByPtp = complexPyeongDetail['landPriceMaxByPtp']
#                 landPriceMaxByPtp['complexPyeongNo'] = complexPyeongNo
#                 for column in landPriceMaxByPtp_columns:
#                     if column not in landPriceMaxByPtp:
#                         landPriceMaxByPtp[column] = None
#                         print( landPriceMaxByPtp )
#               
#                 execute_command = """
#                     INSERT INTO dbo.landPriceMaxByPtp
#                     VALUES ( {complexPyeongNo}, {ptpNo}, {supplyArea}, {totalArea}, {maxPrice}, {stdYear}, {stdYmd}, {landPriceTax} );
#                 """
#                 cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in landPriceMaxByPtp.items() } ) )
#                 cursor.commit()
#                 
#                 if complexPyeongDetail['landPriceMaxByPtp']['landPriceTax'] is not None:                 
#                     landPriceTax = complexPyeongDetail['landPriceMaxByPtp']['landPriceTax']
#                     landPriceTax['complexPyeongNo'] = complexPyeongNo
#                     for column in landPriceTax_columns:
#                         if column not in landPriceTax:
#                             landPriceTax[column] = None
#                             print( landPriceTax )
#                   
#                     execute_command = """
#                         INSERT INTO dbo.landPriceTax
#                         VALUES ( {complexPyeongNo}, {propertyTotalTax}, {propertyTax}, {localEduTax}, {cityAreaTax}, {realEstateTotalTax}, {decisionTax}, {ruralSpecialTax} );
#                     """
#                     cursor.execute( execute_command.format( **{k: sqlquote(v) for k, v in landPriceTax.items() } ) )
#                     cursor.commit()
                 
    else:
        print( '단지 정보가 없습니다.' )

cursor.close()
conn.close()
