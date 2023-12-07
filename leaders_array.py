def leaders_array(arr):
    """ an element is called leader, if there is no element
    on its right which is greater than the given element"""

    n = len(arr)
    L = []
    dnew = {k: float('inf') for k in arr}

    for i in range(n):
        while len(L) > 0 and L[-1] < arr[i]:
            dnew[L[-1]] = arr[i]
            L.pop()
        L.append(arr[i])

    leaders = [k for k in dnew.keys() if dnew[k] == float('inf')]
    return leaders


if __name__ == "__main__":
    res = leaders_array([63, 70, 80, 33, 33, 47, 20])
