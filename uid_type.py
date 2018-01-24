import pandas as pd

if __name__ == '__main__':
    # df = pd.read_csv('rcmd.list.txt', header=None, sep='\t')
    # df.columns = list('1234')
    # type_dict = {}
    # with open('20180117.txt', encoding='utf-8') as f:
    #     for line in f.readlines():
    #         item_list = line.split()
    #         if len(item_list) == 3:
    #             oid = item_list[0]
    #             types = item_list[2]
    #             type_dict[oid] = types
    #     print(len(type_dict))
    df1 = pd.read_csv('rcmd.list.txt', header=None, sep='\t')
    df1.columns = list('1234')
    df2 = pd.read_csv('20180117.txt', header=None, sep='\t')
    df2.columns = list('123')
    outfile = pd.merge(df1, df2, how='left', left_on='4', right_on='2')
    outfile.to_csv('outfile_new.csv', header=None, index=False, encoding='utf-8')




