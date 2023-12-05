def longest_prefix(arr, N):
    """ find longest common prefix in list of strings
    if arr=['gee', 'geek'] answer shd be 'gee'
    """
    if N == 1:
        return -1
    res = ''
    result = arr[0]
    # common = False
    for i in range(1, N):
        s = arr[i]
        k = 0
        while k < min(len(s), len(result)):
            if result[k] == s[k]:
                res += s[k]
                k += 1
            else:
                break
        if res != '':
            # common = True
            result = res
            res = ''
        else:
            return -1

    return result


