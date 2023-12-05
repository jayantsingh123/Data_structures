def anagram_groups(arr):
    """ given list of strings, find the groups of anagrams
    e.g if arr= ['act','god','cat','dog','tac']
    the output will be [['act','cat','tac'],['god','dog']]"""

    from collections import defaultdict
    dnew = defaultdict(list)
    # n = len(arr)
    for k, v in enumerate(arr):
        # print(k, v)
        v = ''.join(sorted(v))
        # print(k, v)
        dnew[v].append(arr[k])

    res = []
    for k in dnew.keys():
        res.append(dnew[k])
    return res
