from idlelib.multicall import r

import requests
import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from pandas import DataFrame
from pandas import Series


# 공공데이터 API Call (농수산물 도매시장 경락가격 data)
key='CTFUEzKcx7CIIBqAvwD%2BJ9MObIpZoglK5TtrmnaBqeaiaFS%2FDlPS2Bt%2Fq52xl%2B33kK8hAHvCMK1b7Mu77hN17w%3D%3D'
date = '20210311'
prd_cd='1202'
limit = '10000'
url=f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
#parameter 서버로 넘겨주는 정보
print(url)

# 데이터불러오기
r= requests.get(url).content

jo = json.loads(r)
item = jo['response']['body']['items']['item']

# 당일 경매 데이터 건수
# print(len(item))


# 데이터프레임으로 변환
df = pd.DataFrame.from_dict(item, orient='columns')
# print(df.head(10))
df2 = df[['delngDe','sbidPric','stdMtcNewCode','stdMtcNewNm','stdPrdlstCode','stdPrdlstNewNm','stdQlityNewNm','stdSpciesCode','stdSpciesNm','whsalMrktNewCode','whsalMrktNewNm','delngQy','delngPrut','stdUnitNewNm','stdFrmlcNewNm','stdMgNewNm']]

# 컬럼명 변경
df3 = df2.rename({'delngDe':'Date','sbidPric':'Price','stdMtcNewCode':'LocalCode','stdMtcNewNm':'Local','stdPrdlstCode':'ItemCode','stdPrdlstNewNm':'Item','stdQlityNewNm':'Qlity','stdSpciesCode':'SpeciesCode','stdSpciesNm':'SpeciesName','whsalMrktNewCode':'MarketCode','whsalMrktNewNm':'Market','delngQy':'QY','delngPrut':'Transaction','stdUnitNewNm':'unit','stdFrmlcNewNm':'Packing','stdMgNewNm':'Size'}, axis='columns')
# print(df3.head(10))

# 널값
# print(np.sum(pd.isnull(df3)))# Local 76개

# print(df3.describe())

# 산지 지역별 데이터 합계
# grouped = df3.groupby(df3['Local']).sum()
# print(grouped)

# 총합계
Price_sum = df3[['Price','Transaction']].sum()

# 대파 키로당 가격
Price_divide = Price_sum['Price']/Price_sum['Transaction']

# print(Price_sum)

# 3월 11일 대파 한단(2kg내외) 평균 가격
print(round(Price_divide)*2)


# 1)Price, unit 전체 합계는?
df3['합계'] = df3.groupby(['Price'])['unit'].transform('sum')

# print(df3['합계'])
# xml 파일로 만들기
# with open(f'{date}_{prd_cd}.xml', 'w+') as f:
#     f.write(str(res.content))
