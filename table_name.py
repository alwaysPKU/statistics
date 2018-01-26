with open('./files/res_dt') as f:
    line = f.readline()
    while line:
        item = line.split()
        name = item[0]
        with open('./files/table_name', 'a') as w:
            w.write(name+'\n')
        line = f.readline()

with open('./files/res_without_dt') as f2:
    line = f2.readline()
    while line:
        with open('./files/table_name','a') as w2:
            w2.write(line)
        line = f2.readline()
