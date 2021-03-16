from idlelib.multicall import r

import item as item
import requests
import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from pandas import DataFrame
from pandas import Series
# 시간 얼마나 걸리는지 확인
from datetime import datetime
import pandas


def call_api(prd_cd, date):

    # 공공데이터 API Call (농수산물 도매시장 경락가격 data)
    key='CTFUEzKcx7CIIBqAvwD%2BJ9MObIpZoglK5TtrmnaBqeaiaFS%2FDlPS2Bt%2Fq52xl%2B33kK8hAHvCMK1b7Mu77hN17w%3D%3D'

    # 제한갯수
    limit = '10000'
    url=f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
    #parameter 서버로 넘겨주는 정보

    res = requests.get(url)
    jo = json.loads(res.content)
    body = jo['response']['body']
    item = body['items']#items 안에 item

    # print(f'date:{date} len:{len(item)} body: {body["totalCount"]}')

    if item != "":  # item이 널이 아닐때(공휴일, 휴일 등 data가 없음)
        # json으로 저장
        file_name = f'res_js{date}_{prd_cd}.json'

        # 파일 저장
        with open(file_name, 'w+') as f:
            f.write(json.dumps(item))
            # print(file_name, 'save success')#로그 기록 찍기`


# dates 일정 기간의 날짜 출력 방법(2021 1월~2021 3월)
rct3 = pandas.date_range(start='20210227', end='20210315')
dt_list = rct3.strftime("%Y%m%d").to_list()

dates = []
for i in dt_list:
    # print(i)
    dates.append(i) #리스트에 일정 기간 날짜 데이터 값 넣기
    # dates = ['20210130']
for date in dates:
    # prd_cd = '1202'  # 품목코드
    print(date, 'start:', datetime.now())
    call_api('1202', date) #데이터 API call
    print(date, 'end:', datetime.now()) #1일 데 소요 기간 12달, 12분 소요
    print('------------------------')







