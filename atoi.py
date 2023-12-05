def atoi_chk(s):
    """ convert string into integer without using
    in-built functions. if non digit character
    is encountered then return -1"""

    total = 0
    j = 0
    neg_sign = False
    if s[0] == '-':
        neg_sign = True
    n = len(s)
    if n == 1 and neg_sign:
        return -1
    for i in range(n - 1, -1, -1):
        if i == 0 and neg_sign:
            return -1 * total
        elif s[i].isdigit():
            total += int(s[i]) * pow(10, j)
            j += 1
        else:
            return -1
    return total
