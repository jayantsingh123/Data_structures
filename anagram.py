def remanagram(str1, str2):
    """ given two strings, str1 and str2
    find number of total deletions from either string
    so that one string becomes  an anagram of other."""
    from collections import defaultdict

    d1 = defaultdict(int)
    d2 = defaultdict(int)
    n = len(str1)
    m = len(str2)
    cnt = 0
    for i in range(n):
        d1[str1[i]] += 1
    for j in range(m):
        d2[str2[j]] += 1
    for i in d1.keys():
        if d1[i] > d2[i]:
            cnt += (d1[i] - d2[i])

    for j in d2.keys():
        if d2[j] > d1[j]:
            cnt += (d2[j] - d1[j])
    return cnt
