def nonrepeating(s):
    """ find first non-repeating character in s"""
    from collections import defaultdict
    dnew = defaultdict(list)
    minimum = 9999
    for i in range(len(s)):
        dnew[s[i]].append(i)

    for j in dnew.keys():
        if len(dnew[j]) == 1:
            minimum = min(dnew[j][0], minimum)
    if minimum == 9999:
        return '$'
    else:
        return s[minimum]

if __name__ == '__main__':
    print(nonrepeating('zxvczbtxyzvy'))

