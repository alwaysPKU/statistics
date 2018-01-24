import re

# 统计分区
# with open('test.out.tbs.bak') as f:
#     line = f.readline()
#     while line:
#         m = re.findall(r'/[^/]{1,50}/dt=\d{8}', line)
#         if m:
#             with open('res', 'a') as w:
#                 w.write(m[0]+'\t'+m[-1]+'\n')
#         line = f.readline()

# 统计未分区的
with open('test.out.tbs.bak') as f:
    line = f.readline()
    while line:
        m = re.findall(r'/[^/]{1,50}/dt=\d{8}', line)
        if not m:
            m2 = re.findall(r'hdfs://ns1/user/wbdata_hot/warehouse/[^/]{1,50}', line)
            if m2:
                mark = m2[0].split('/')[-1]
                with open('res_without_dt', 'a') as w:
                    w.write(mark+'\n')
        line = f.readline()
