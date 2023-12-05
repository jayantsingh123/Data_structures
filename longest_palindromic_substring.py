def longest_palindrome(s1):
    import numpy as np
    n = len(s1)
    res = 0
    result = ''
    # i, j = 0, 0
    C = np.zeros((n, n))
    for diff in range(0, n):
        i = 0
        j = i + diff
        while i < n and j < n:
            if diff == 0:  # single characters
                C[i][j] = 1
            elif diff == 1:  # two characters
                if s1[i] == s1[j]:
                    C[i][j] = 2
            else:
                # if s1[i] == s1[j] and s1[i + 1] == s1[j - 1]:
                if s1[i] == s1[j] and C[i + 1][j - 1] > 0:
                    # use the fact that previous smaller string is a palindrome
                    C[i][j] = (j - i) + 1
            res = max(res, C[i, j])
            if res == C[i, j]:
                result = s1[i:j + 1]
            i += 1
            j += 1
    return result
