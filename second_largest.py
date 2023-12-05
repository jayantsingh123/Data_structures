def second_largest(L):
    """ Find second largest element in L using single traversal """

    n = len(L)
    maximum = L[0]
    second = -999
    for i in range(1, n):
        print(L[i], maximum, second)
        if L[i] > maximum:
            second = maximum
            maximum = L[i]

        elif (second < L[i]) and (L[i] < maximum):
            second = L[i]
            print(second)
    return second

if __name__ == '__main__':
    print(second_largest([4,2,3,8,1]))