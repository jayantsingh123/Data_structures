def minpalindrome(str1):
    s2 = str1
    n = len(str1)
    # print(n)
    L = []
    for k in range(n - 1, -1, -1):
        m = len(s2)
        flag = True
        print(m)
        for i in range(m // 2):
            if s2[i] != s2[m - 1 - i]:
                flag = False
                break

        if flag == True:
            # print(L)
            # print(L)
            return len(L)
        else:
            # print(L)
            L.append(str1[k])
            s3 = ''.join(i for i in L)
            s2 = s3 + str1
            print(L, s2)
