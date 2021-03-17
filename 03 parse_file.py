import json, glob
import pandas as pd
import openpyxl

# json으로 requests한 data json으로 저장
filenames = glob.glob('res_json/*.json')
print(filenames)

for filename in filenames:
    with open('res_js20210311_1202.json') as f:
        jo = json.loads(f.read())
        print(len(jo), jo)
        print(filename, len(jo))

        # save to excel

# dataframe에 저장
for filename in filenames:
    # df = pd.read_json(filename)
    # print(df)

#excel에 저장
    df = pd.read_json(filename)
    spl = filename.split('.')
    df.to_excel(f'{spl[0]}.xlsx')