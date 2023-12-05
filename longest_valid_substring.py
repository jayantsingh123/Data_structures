def longest_valid(s):
    """ given string of left and right parentheses, find the length of the
        longest valid substring, e.g. s='(()' has length as 2 for the substring () """
    L = [-1]
    maxlen = 0
    length = 0
    if len(s) == 1 or len(s) == 0:
        return maxlen
    for i in range(len(s)):
        if s[i] == '(':
            L.append(i)
        else:
            if L[-1] != -1:
                # -1 helps in the case if all left parentheses have popped
                L.pop()
                length = i - L[-1]
                # gives length of valid substring upto index i
                maxlen = max(length, maxlen)
    return maxlen


# other approach: use the position of unbalanced parentheses to find length of valid substring

def valid_longest(s):
    S = []
    res = 0
    for i in range(len(S)):
        if s[i] == '(':
            S.append(i)
        else:
            if len(S) > 0 & s[S[-1]] == '(':
                # right parentheses balance left parentheses
                S.pop()
            else:
                S.append(i)

    length = len(s)
    while len(S) > 0:
        top = S.pop()
        res = max(res, length - top - 1)  # find the distance between two unbalanced parentheses
        # this will be the length of the valid substring
        length = top  # update length
    return max(length, res)
