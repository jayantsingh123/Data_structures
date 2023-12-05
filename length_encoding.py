def encoding(s):
    """ for a given string s, compute the length
    encoding, e.g s='aaab' output shd be 'a3b1' """
    res = ''
    ctr = 1
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return ctr
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ctr += 1
        else:
            res = res + (s[i] + str(ctr))
            ctr = 1
    res = res + (s[i + 1] + str(ctr))
    return res
