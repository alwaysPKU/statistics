list1 = [0,1,2,3]
list2 = [0,11,2,3]

def judge():
    count = 0
    for (m,n) in zip(pd_merge_p['should_date_x'],pd_merge_p['should_date_y']):
        if m==n:
            count+=0
            continue
        else:
            print(m,n)
    print (count)

judge()

