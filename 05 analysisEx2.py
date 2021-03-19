
# 해당 경로 폴더에 있는 .json 파일명 리스트 모두 가져오기

import os
import json
import pandas as pd

path = './경로/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .json인 경우

## json 파일들을 DataFrame으로 불러오기

dict_list = []
for i in file_list_py:
    for line in open((path+i),"r"):
        dict_list.append(json.loads(line))
df = pd.DataFrame(dict_list.head(10))



#데이터 전부 하나에 합치기

#csv파일로 저장하기

#분석 시작
