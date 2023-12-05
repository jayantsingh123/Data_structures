# given strings S, and P which is a pattern. Check whether P exists in S or not. Naive search
# does search in quadratic time complexity.

def naive_pattern(S, P):
    n = len(S)
    m = len(P)
    for i in range(n-m+1):
        j = 0
        while j<m:
            #loop over the pattern P for each value of i
            if P[j]!=S[i+j]:
                break
            j+=1
            if j==m:
                return True
    return False

if __name__ == '__main__':
    print(naive_pattern('aabaacaadaabaaabaa', 'ccda'))