with open('res') as f:
    line = f.readline()
    while line:
        item = line.split()
        name = item[0].split('/')[1]
        time1 = item[0].split('=')[1]
        time2 = item[1].split('=')[1]
        with open('res_dt','a') as w:
            w.write(name+'\t'+time1+'\t'+time2+'\n')
        line = f.readline()