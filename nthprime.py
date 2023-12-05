def nthprimedigitsnumber(n):
    L = [2, 3, 5, 7]
    if n <= 4:
        return L[n - 1]
    p = 22
    ctr = 0
    while ctr < n - 4 and p >= 22:
        prime = True
        for c in str(p):
            #print(c)
            if c not in ['2', '3', '5', '7']:
                prime = False
                break
        if prime != False:
            L.append(p)
            ctr += 1
        p += 1
    return L[n - 1]

if __name__ == '__main__':
    print(nthprimedigitsnumber(3))