def count_rev(s):
    # find number of reversals in string 's' so as to make
    #   it balanced. e.g s='{{}{', if we flip last opening curly brace it
    #   will be a balanced string
    #   Note that for balancing we shd have equal number of right
    #   and left curly braces

    L1 = []
    res = 0
    for i in range(len(s)):
        if len(L1) == 0 and s[i] == '}':
            L1.append('{')
            res += 1
        elif s[i] == '{':
            L1.append(s[i])
        elif s[i] == '}' and L1[-1] == '{':
            L1.pop()
    print(L1)
    if len(L1) == 0:
        return res
    # if odd number of open curly braces are left in the stack, we cannot balance it.
    if len(L1) % 2 != 0:
        return -1
    else:
        return res + (len(L1) // 2)
