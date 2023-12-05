def longest_k_substring(str1, k):
    """ find the longest substring in the string str1 with
    k unique characters """
    from collections import defaultdict
    dnew = defaultdict(int)
    n = len(str1)
    if k > len(set(str1)):
        return -1
    i, start = 0, 0
    res = -9999
    while i < n:
        dnew[str1[i]] += 1
        while len(dnew.keys()) > k:
            dnew[str1[start]] -= 1
            if dnew[str1[start]] == 0:
                del dnew[str1[start]]
            start += 1
        if len(dnew.keys()) == k:
            res = max(res, (i - start) + 1)
        i += 1
    return res
