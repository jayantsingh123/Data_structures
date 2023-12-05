def palindrome(strnew):
    n = len(strnew)
    for j in range(n // 2):
        if strnew[j] != strnew[n - 1 - j]:
            flag = False
            return flag
    flag = True
    return flag


def longest(s):
    from collections import defaultdict
    dnew = defaultdict(list)
    m = len(s)
    i, j = 0, 0
    while i <= j <= m - 1:
        strnew = s[i:j + 1]
        if i == j:
            dnew[len(strnew)].append(strnew)
        else:
            res = palindrome(strnew)
            print(res, strnew)
            if res:
                if len(strnew) > max(dnew.keys()):
                    dnew[len(strnew)].append(strnew)
                elif len(strnew) == max(dnew.keys()):
                    dnew[len(strnew)].append(strnew)
        if j == m - 1 and i < j:
            i += 1
            j = i
        else:
            j += 1
    return dnew[max(dnew.keys())]
