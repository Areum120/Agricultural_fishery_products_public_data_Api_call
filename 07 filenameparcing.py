def filename_parcing(filename):
    f1 = filename.split('/')
    print(f1)
    f2 = f1[5].split('_')#CallAPI\res_js02.json_1202.json
    print(f2)
    f3 = f2[1]#js20210104파싱
    print(f3)
    f4 = f3[2:10]
    print(f4)
    return f4

filename = 'C:/Users/tjfsu/PycharmProjects/pythonProject/CallAPI\res_js20210104_1202.json'
filename_parcing(filename)