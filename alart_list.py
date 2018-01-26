import datetime

with open('/Users/zhangwei/PycharmProjects/statistics/files/res_dt') as f:
    line = f.readline()
    n = 1
    while line:
        item = line.split()
        name = item[0]
        start = datetime.datetime.strptime(item[1], '%Y%m%d')
        end = datetime.datetime.strptime(item[2],'%Y%m%d')
        while start<=end:
            # print(start.strftime("%Y%m%d"))
            dt = start.strftime("%Y%m%d")
            with open('./files/alart_list', 'a') as w:
                text1 = 'ALTER TABLE '
                text2 = ' ADD PARTITION (dt='
                text3 = ") location '/user_ext/wbdata_hot/warehouse/"
                w.write(text1+name+text2+"'"+dt+"'"+text3+name+'/dt='+dt+"'"+'\n')
            start += datetime.timedelta(days=1)
        line = f.readline()



    #     end = int(item[2])
    #     for i in range(start, end+1):
    #         n += 1
    #         with open('./files/alart_list', 'a') as w:
    #             text1 = 'ALTER TABLE '
    #             text2 = ' ADD PARTITION (dt='
    #             text3 = ") location '/user_ext/wbdata_hot/warehouse/"
    #             w.write(text1+name+text2+str(i)+text3+name+'/dt='+str(i)+"'"+'\n')
    #     line = f.readline()
    # print(n)
