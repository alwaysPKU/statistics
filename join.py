import pandas as pd
# import xlrd

file1 = pd.read_csv('./files/学校产品.csv', sep=',', low_memory=False)
file1.to_csv('res.csv', encoding='gbk')
