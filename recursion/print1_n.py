def print1_n(n):
    if n==1:
        print(n)
        return
    print1_n(n-1)
    print(n)
