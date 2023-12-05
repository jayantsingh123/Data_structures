def smallest_distinct_substring(str1):
    """ find length of smallest substring containing
    all distinct characters of str1"""

    from collections import defaultdict
    dnew = defaultdict(int)
    # d1 = set(str1)
    i, start, res = 0, 0, 9999
    found = False
    while i < len(str1):
        dnew[str1[i]] += 1
        if set(str1).issubset(set(dnew.keys())):

            while dnew[str1[start]] > 1:
                dnew[str1[start]] -= 1
                if dnew[str1[start]] == 0:
                    del dnew[str1[start]]
                start += 1
            res = min(res, (i - start) + 1)

            # found = True
        ##   while set(str1).issubset(set(dnew.keys())):
        #     dnew[str1[start]] -= 1
        #    if dnew[str1[start]] == 0:
        #       del dnew[str1[start]]
        #  start += 1
        # while found:
        # res = min(res, i - (start - 1) + 1)
        #    dnew[str1[start]] -= 1
        #   if dnew[str1[start]] == 0:
        #      del dnew[str1[start]]
        # start += 1
        # if not set(str1).issubset(set(dnew.keys())):
        #   res = min(res, i - (start - 1) + 1)
        # found = False
        i += 1
    return res
