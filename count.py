import pandas as pd


df = pd.read_csv('outfile_new.csv', header=None, sep=',')
df.columns = list('1234567')
print(df)
# data = df["1"].groupby(df["1"]).count()
data = df.groupby(['1', '3'])[['3']].count()
print(data)

data3 = df.groupby(['1', '3', '7'])[['7']].count()
print(data3)
# print(data)
# print(type(data))
data2 = df['7'].groupby([df['1'], df['7']]).count()
print(data2)
data.to_csv('res.csv', header=False, index=False, encoding='utf-8')
data2.to_csv('res_new.csv', header=False, index=False, encoding='utf-8')
