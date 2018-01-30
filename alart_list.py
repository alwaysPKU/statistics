import datetime

# 获得单一分区的建表语句
def get_create():
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


# 获得双分区的建表语句
def get_doublePartitions_create():
    with open('./files/list_filtered') as f:
        lines = f.readlines()
        for line in lines:
            item = line.split()[-1]
            # print(item)
            items = item.split('/')
            table = items[4]
            # print(table)
            dt = items[5].split('=')[1]
            # print(dt)
            dt2_name = items[-1].split('=')[0]
            dt2 = items[-1].split('=')[1]
            # print(dt2)
            with open('./files/alart_doublepartition_list', 'a') as w:
                text1 = 'ALTER TABLE '
                text2 = ' ADD PARTITION (dt='
                text3 = ") location '/user_ext/wbdata_hot/warehouse/"
                w.write(text1 + table + text2 + "'" + dt + "'," +
                        dt2_name+"='"+dt2+"'"+text3 + table + '/dt=' +
                        dt + '/'+dt2_name+'='+dt2 + "'" + '\n')

# 去掉Found开头行
def filter():
    with open('./files/list') as f:
        line = f.readline()
        while line:
            if line.startswith('Found'):
                line = f.readline()
                continue
            else:
                with open('./files/list_filtered', 'a') as w:
                    w.write(line)
            line = f.readline()


if __name__ == '__main__':
    # filter()
    get_doublePartitions_create()