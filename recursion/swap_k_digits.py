def swap_kdigits(s, k):
    # define current max
    maximum = int(s)

    for i in range(0, len(s) - 1):
        maxc = s[i]
        if k == 0:
            break
        for j in range(i + 1, len(s)):

            if int(s[j]) > int(maxc):
                maxc = s[j]
        # print(maxc, i)

        if maxc != s[i]:
            k -= 1
            idx = s[i + 1:].rfind(maxc) + i + 1  # find last occurrence
            ll = list(s)
            # do the swap
            ll[i], ll[idx] = ll[idx], ll[i]
            s = ''.join(ll)
            # find the new max
            maximum = max(int(s), maximum)
            print(maximum, k, s)
            # print(res)
            # backtrack
            # ll[i], ll[idx] = ll[idx], ll[i]

            # s = ''.join(ll)
            # print(s)
    return maximum
