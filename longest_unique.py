def longest_unique(str1):
    """ find the longest window containing all unique characters"""
    from collections import defaultdict
    dnew = defaultdict(int)
    n = len(str1)
    res = -9999
    i, start = 0, 0

    while n > i >= start:
        if dnew[str1[i]] > 0:
            res = max(res, i - start)
        while dnew[str1[i]] > 0:
            dnew[str1[start]] -= 1
            if dnew[str1[start]] == 0:
                del dnew[str1[start]]
            start += 1
        dnew[str1[i]] += 1
        i += 1
    return max(res, i - start)
