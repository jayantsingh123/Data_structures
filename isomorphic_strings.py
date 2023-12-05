def areIsomorphic(str1, str2):
    # check if string2 is one to one image of str1.

    from collections import defaultdict

    if len(str1) != len(str2):
        return False
    dnew = defaultdict(list)
    dnew2 = defaultdict(list)

    for i in range(len(str1)):
        if len(dnew[str1[i]]) > 0:
            if dnew[str1[i]][0] != str2[i]:
                return False

        else:
            dnew[str1[i]].append(str2[i])

    for j in range(len(str2)):
        if len(dnew2[str2[j]]) > 0:
            if dnew2[str2[j]][0] != str1[j]:
                print(dnew2)
                return False

        else:
            dnew2[str2[j]].append(str1[j])

    return True


if __name__ == '__main__':
    print(areIsomorphic('pijthbsfy', 'fvladzpbf'))
