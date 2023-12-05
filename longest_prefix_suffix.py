def longest_prefix_suffix(s):
    """ for the given string s find the longest
    proper prefix which is also a proper suffux.
    e.g. s=abab has answer as ab"""
    n = len(s)
    lps = [0] * n
    length, idx = 0, 1
    ## here lps[idx] gives length of longest prefix which
    ## is also a suffix in the string upto index i
    while idx < n:
        if s[length] == s[idx]:
            lps[idx] = length + 1
            idx += 1
            length += 1
        else:
            if length == 0:
                lps[idx] = 0
                idx += 1
            else:
                length = lps[length - 1]
    return lps[n - 1]
