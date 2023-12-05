def smallest_string(s, p):
    # global result
    from collections import defaultdict
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    result = ''
    # res = 999
    prev = 9999
    if len(p) > len(s):
        return -1
    i, start = 0, 0
    flag = False
    for j in range(len(p)):
        d2[p[j]] += 1
    while i < len(s):
        d1[s[i]] += 1
        if set(d2.keys()).issubset(set(d1.keys())):
            flag = True
        while set(d2.keys()).issubset(set(d1.keys())):
            d1[s[start]] -= 1
            if d1[s[start]] == 0:
                del d1[s[start]]
            start += 1
        if flag:
            res = min(len(s[start - 1:i + 1]), prev)
            if res == len(s[start - 1:i + 1]) and res < prev:
                result = s[start - 1:i + 1]
                res = len(result)
                prev = res
            flag = False
        i += 1
    if result == '':
        return -1
    return result


if __name__ == '__main__':
    print(smallest_string('zoomlazapzo', 'oza'))
