from typing import List, Union, Tuple, Any


def reduced_string(s, k):
    """ Given a string s and an integer k, the task is to reduce the string by applying the
    following operation:
Choose a group of k consecutive identical characters and remove them.

The operation can be performed any number of times until it is no longer possible."""

    n = len(s)
    L = []
    ctr = 0
    res = ''
    if k == 1:
        return res
    if k == 0:
        return s
    for i in range(n):
        if len(L) == 0 or L[-1][0] != s[i]:
            L.append((s[i], 1))
        elif s[i] == L[-1][0]:
            x = L.pop()
            ctr = x[1] + 1
            if ctr < k:
                L.append((s[i], ctr))
            elif ctr == k:
                continue

    while len(L) > 0:
        x = L.pop(0)
        res += (x[0] * x[1])
    return res
