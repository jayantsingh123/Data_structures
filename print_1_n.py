def print_1_n(n):
    res=0
    if n==0:
        return 0
    res = 1+print_1_n(n-1)
    print(res)
    return res

if __name__ == '__main__':
    print_1_n(4)