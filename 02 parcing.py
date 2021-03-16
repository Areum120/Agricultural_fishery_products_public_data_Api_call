import bs4
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import pandas as pd
from time import sleep
import xml.etree.ElementTree as ET
import sys
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# url로 xml 읽어오기
url= "http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey=CTFUEzKcx7CIIBqAvwD%2BJ9MObIpZoglK5TtrmnaBqeaiaFS%2FDlPS2Bt%2Fq52xl%2B33kK8hAHvCMK1b7Mu77hN17w%3D%3D&pageNo=1&numOfRows=10&delngDe=20210311&prdlstCd=1202"
response = urlopen(url).read()
xtree = ET.fromstring(response)

print(xtree)

# 파일로 xml 읽어오기
# tree = parse('20210311_1202.xml')

# root 노드 가져오기
# root = tree.getroot()
# 일치하는 모든 노드 가져오기
# item = root.findall("item")
# 일치하는 첫번째 노드 가져오기
# item.find("delngDe")
# 첫번째 노드 값 가져오기
# item.find("delngDe").text


# rows = []
#
# for i in xtree:
#     i_aucSeCode =i.find("aucSeCode").text
#     i_Date = i.find("delngDe").text
#     i_Price = i.find("sbidPric").text
#     i_LocalCode= i.find("stdMtcNewCode").text
#     i_Local = i.find("stdMtcNewNm").text
#     i_ItemCode = i.find("stdPrdlstCode").text
#     i_Item = i.find("stdPrdlstNewNm").text
#     i_Qlity = i.find("stdQlityNewNm").text
#     i_SpeciesCode = i.find("stdSpciesCode").text
#     i_SpeciesName = i.find("stdSpciesNm").text
#     i_MarketCode = i.find("whsalMrktNewCode").text
#     i_Market = i.find("whsalMrktNewNm").text
#     i_QY = i.find("delngQy").text
#     i_Transaction= i.find("delngPrut").text #거래단량(매매단위명+포장상태명 조합)
#     i_unit = i.find("stdUnitNewNm").text
#     i_Packing = i.find("stdFrmlcNewNm").text
#     i_Size = i.find("stdMgNewNm").text
#
# # XML text를 데이터 프레임 변환
#     rows.append({
#                 "aucSeCode": i_aucSeCode,
#                  "Date": i_Date,
#                  "Price": i_Price,
#                  "LocalCode": i_LocalCode,
#                  "Local": i_Local,
#                  "ItemCode": i_ItemCode,
#                  "Item": i_Item,
#                  "Qlity": i_Qlity,
#                  "SpeciesCode": i_SpeciesCode,
#                  "SpeciesName": i_SpeciesName,
#                  "MarketCode": i_MarketCode,
#                  "Market": i_Market,
#                  "QY": i_QY,
#                  "Transaction": i_Transaction,
#                  "unit": i_unit,
#                  "Packing": i_Packing,
#                  "Size": i_Size,
#                  })
#
# columns = ["Date","Price","LocalCode","Local","ItemCode","Item","Qlity","SpeciesCode","SpeciesName","MarketCode","Market","QY","Transaction","unit","Packing","Size"]
# df = pd.DataFrame(rows, columns = columns)
# df.head(10)



#기간별 데이터 조회
# dt_index = pd.date_range(start='20210101',end='20210312')
# print(dt_index)
# dt_list = dt_index.strftime("%Y%m%d").tolist()
# print(dt_list)



