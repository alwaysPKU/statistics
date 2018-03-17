import sys
def fun(n, m):
    r=0
    if n == 1:
        r == m
    elif n == 2:
        r = m * (m - 1)
    elif n == 3:
        r = m * (m - 1) * (m - 2)
    else:
        r = fun(n - 1, m) * (m - 2) + fun(n - 2, m) * (m - 1)
    return r

if __name__ == '__main__':
    line = input().split(' ')
    n = int(line[0])
    m = int(line[1])
    # n = int(input())
    # m = int(input())
    # print(fun(n, m))
    sys.stdout.write(str(fun(n, m)))
