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
date = '20210130'
prd_cd="1202"
limit = '10000'
url=f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
#parameter 서버로 넘겨주는 정보
print(url)

# 데이터불러오기
r= requests.get(url).content#json파일에 접근

jo = json.loads(r)
item = jo['response']['body']['items']['item']

# 당일 경매 데이터 건수
print(len(item))


# 데이터프레임으로 변환
df = pd.DataFrame.from_dict(item, orient='columns')
print(df.head(10))
