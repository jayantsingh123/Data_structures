def concatenatestring(s1, s2):
    from collections import defaultdict
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in range(len(s1)):
        d1[s1[i]] += 1
    for j in range(len(s2)):
        d2[s2[j]] += 1
    for k in d1.keys():
        if d2.get(k):
            d1[k] = 0
            d2[k] = 0
    strnew = ''.join([i for i in d1.keys() if d1[i] > 0]) + ''.join([j for j in d2.keys() if d2[j] > 0])
    if strnew == '':
        return -1
    else:
        return strnew


if __name__ == '__main__':
    print(concatenatestring('abcs', 'ccasb'))
