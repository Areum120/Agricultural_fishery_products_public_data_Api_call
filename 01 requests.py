import bs4
import requests
key='CTFUEzKcx7CIIBqAvwD%2BJ9MObIpZoglK5TtrmnaBqeaiaFS%2FDlPS2Bt%2Fq52xl%2B33kK8hAHvCMK1b7Mu77hN17w%3D%3D'
date = '20210311'
prd_cd="1202"
url=f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows=10&delngDe={date}&prdlstCd={prd_cd}'
#parameter 서버로 넘겨주는 정보
print(url)

# 데이터불러오기
res = requests.get(url)#Xml파일에 접근
with open(f'{date}_{prd_cd}.xml', 'w+') as f:
    f.write(str(res.content))
