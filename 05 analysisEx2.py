
import os
import glob
import json
import csv
import pandas as pd
import gc # 메모리 대비
from pandas import json_normalize#json 데이터프레임 변환
# json 파일 3개월 데이터 모두 불러와서 데이터 프레임으로 변환하고 parsing 하기

# 1개 데이터 불러오기(dic type)
# with open('res_js20210102_1202.json','r') as f:#r은 읽기모드를 뜻함
#     data = json.load(f)
#
# # 전체 json data 출력하기
# print(json.dumps(data, indent='\t'))
#
# all_data = json.dumps(data, indent='\t')
# info = json.loads(all_data)
# print(info)
#
# df = json_normalize(info['item'])
# print(df)
# df.to_csv('res_js20210102_1202.csv', encoding='utf-8-sig')# 한글깨짐 유의

# 특정 속성값 접근, 바로 aucSeCode에 접근하면 keyerror, iem에 먼저 접근
# print(data['item']['aucSeNm'])
#검색했을 때 TypeError: list indices must be integers or slices, not str error 발생
# print(data['item'])
# print(data['item'][0]['delngDe'])
# print(type(data['item'][0]['aucSeCode']))

# 아래 방법 문제 : 파일 모두 가져와서 리스트안의 딕셔너리 형태로 담았으나 index 0 item 0으로 형태가 나와서 값에 어떻게 접근하는지 모르겠다.
# 해당 경로 폴더에 있는 .json 파일명 리스트 모두 가져오기 1

# print(type(json_text))

# 리스트 형태로 데이터 프레임으로 변환하기 -> but index 0 item 0으로 나온다
#         df = pd.DataFrame(list(json_text))
#         # columns=['delngDe','sbidPric','stdMtcNewCode','stdMtcNewNm','stdPrdlstCode','stdPrdlstNewNm','stdQlityNewNm','stdSpciesCode','stdSpciesNm','whsalMrktNewCode','whsalMrktNewNm','delngQy','delngPrut','stdUnitNewNm','stdFrmlcNewNm','stdMgNewNm'])
#         print(df)


        #타입 확인 -> dict 이므로 파싱이 어려움(타입에러 발생), 리스트 안의 딕셔너리 파싱 알아보기 (str 타입 변환과는 상관없음)
        # print(type(json_text))


        #여기서부터 오류 TypeError: string indices must be integers
        # detail_data = json_text[item]['aucSeNm']['sbidPric']['stdMtcNewCode']['stdMtcNewNm']['stdPrdlstCode']['stdPrdlstNewNm']['stdQlityNewNm']['stdSpciesCode']['stdSpciesNm']['whsalMrktNewCode']['whsalMrktNewNm']['delngQy']['delngPrut']['stdUnitNewNm']['stdFrmlcNewNm']['stdMgNewNm']
        # print(detail_data)
        # file_list.loc[index] = [detail_data]
        #
        # print(file_list)


# dict_list = []
# for i in file_list_py:
#     for line in open((path+i),"r"):
#         dict_list+=line #item만 json파일로 저장 or line
#
# print(dict_list)

#오류남
# jo = json.loads(dict_list)#한줄씩 읽어오기
# item = jo['response']['body']['items']['item']
# print(item)

