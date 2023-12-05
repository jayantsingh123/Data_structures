def reverse_stack(s):
    """ Reverse string S using stack"""
    L = list(s)
    n = len(L)
    res = ''
    for i in range(n - 1, -1, -1):
        res += L[i]
    return res
