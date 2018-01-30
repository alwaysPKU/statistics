# 找到failed的dt在alart_list的位置，从而确定是哪个表的哪个分区
def find_log():
    n = 0
    with open('./files/log') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                n += 1
            if line.startswith('FAILED: SemanticException'):
                with open('./files/find_th', 'a') as w:
                    w.write(str(n)+'\n'+line)


# log2是从23831开始的
def find_log2():
    n = 21830
    with open('./files/log2') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n':
                n += 1
            if line.startswith('FAILED: SemanticException'):
                with open('./files/find_th', 'a') as w:
                    w.write(str(n)+'\n'+line)


def find_table():
    with open('./files/alart_list') as ff:
        full_alart = ff.readlines()
        with open('./files/find_th') as f:
            lines = f.readlines()
            n = 0
            for line in lines:
                if n % 2 == 0:
                    with open('./files/failed_dt', 'a') as w:
                        w.write(line+full_alart[int(line)-1])
                    # print(line)
                    # print(full_alart[int(line)-1])
                n += 1


# 从failed_dt里提取地址（用这些地址遍历双分区地址）
def find_adress_for_hdfs():
    n = 0
    with open('./files/failed_dt') as f:
        lines = f.readlines()
        for line in lines:
            if n % 2 == 1:
                with open('./files/address2', 'a') as w:
                    data = line.split()[7]
                    w.write(line.split()[7].lstrip("'").rstrip("'")+'\n')
            n += 1

if __name__ == '__main__':
    find_adress_for_hdfs()
