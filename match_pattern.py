def match_pattern(arr, pat):
    from collections import defaultdict, OrderedDict
    dnew, dnew2 = defaultdict(int), defaultdict(int)
    dnew3, dnew4 = OrderedDict(), OrderedDict()
    L, res = [], []
    for i in arr:
        if len(set(i)) == len(set(pat)):
            L.append(i)
    for i in range(len(pat)):
        dnew[pat[i]] += 1
        dnew3[pat[i]] = dnew[pat[i]]
    for k in L:
        for i in range(len(k)):
            dnew2[k[i]] += 1
            dnew4[k[i]] = dnew2[k[i]]
        if list(dnew4.values()) == list(dnew3.values()):
            res.append(k)
        dnew2 = defaultdict(int)
        dnew4 = OrderedDict()

    return res
