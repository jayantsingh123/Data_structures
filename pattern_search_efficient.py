def naive_pattern(S, P):
    n = len(S)
    m = len(P)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            # loop over the pattern P for each value of i
            if P[j] != S[i + j]:
                break
            j += 1
            if j == m:
                return True
        if j > 0:
            i += j
        else:
            i += 1
    return False


if __name__ == '__main__':
    print(naive_pattern('abceabcdabceabcd', 'gfhij'))
