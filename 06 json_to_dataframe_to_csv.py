# 1개씩 json 데이터 불러와서 csv 파일로 담기

import os
import glob
import json
import csv
import requests

import pandas
import pandas as pd
import gc # 메모리 대비
from pandas import json_normalize#json 데이터프레임 변환

'''
params
file_location : './separated/*.json'
'''
#파라미터 path 입력하여 get_file_list 호출
def get_file_list(file_location):
    file_names = glob.glob(file_location)
    #glob 특정 파일만 출력하는 기능
    print(len(file_names))#파일 갯수
    return file_names

# 출력한 파일을 한줄씩 열어서 읽는 기능
def json_from_json_file_nm(filename):
    # print(filename)
    with open(filename, encoding='utf-8-sig') as f:
        return json.loads(f.read())

# csv저장 일자 모음 리스트 기능
# def date_csv(date):
#     print()
#     rct3 = pd.date_range(start='20210101', end='20210315')
#     dt_list = rct3.strftime("%Y%m%d").to_list()
#     month = []
#     for i in dt_list:
#         print(i)
#         month.append(i)  # 리스트에 일정 기간 날짜 데이터 값 넣기
#     if date in month:
#         return date

# filename split()기능
# def filename_parcing(filename):
#     f1 = filename.split('/')
#     # print(f1)
#     f2 = f1[5].split('_')#CallAPI\res_js02.json_1202.json
#     # print(f2)
#     f3 = f2[1]#js20210104파싱
#     # print(f3)
#     f4 = f3[2:10]
#     # print(f4)
#     return f4
#
# #데이터프레임 일자별 csv파일 이름 저장 기능
# # fn은 filename
# def filename_date_to_csv_nm(fn):
#     if fn in fl:
#         print(fn)
#         fn2 = str(fn)
#         date = filename_parcing(fn2)
#         print(date)
#         return date

#데이터프레임을 CSV로 저장하는 기능의 함수
# def df_to_csv(dffile):
#     return df2

path = 'C:/Users/tjfsu/PycharmProjects/pythonProject/CallAPI/*.json'
fl = get_file_list(path)
print(fl)#65개의 json 파일 [] 한눈에 출력

#json파일들을 모두 호출하여 fl에 넣고
# fl에서 필요한 갯수만 호출하여 filename에 저장

json_list = []#리스트자료형
#filename에 fl을 넣으면 전체가 하나로 합쳐져서 마지막것만 출력, 그래서 덮어씌운 1개파일만 만들어짐
for filename in fl:
    print(filename)
    jo = json_from_json_file_nm(filename)
    print(jo)
    if len(jo) != 0:#빈데이터는 건너띄기
         data = jo['item']
         json_list.append(data)
print(json_list)
print(json_list[0])#0102파일
print(json_list[1])#0104파일


for i in range(len(json_list)):
    df = pd.DataFrame(json_list[i])#데이터프레임 변환
    df2 = df.to_csv(f'{i}.csv', encoding='utf-8-sig')# csv파일로 저장
    print(df)





