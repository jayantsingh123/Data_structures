def getMaxOccurringChar(s):
    from collections import defaultdict
    dnew = defaultdict(int)
    maximum = 0
    least = 'z'
    if len(s) == 1:
        return s
    for i in range(len(s)):
        dnew[s[i]] += 1

    for j in dnew.keys():
        maximum = max(dnew[j], maximum)
        if maximum == dnew[j]:
            least = min(j, least)
    return least

if __name__ == '__main__':
    print(getMaxOccurringChar('fdsalkjhfh'))