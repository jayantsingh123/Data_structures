def pairwise_swap(arr):
    """ Pairwise swap elements in array"""
    n = len(arr)
    i = 0
    while i <= n - 2:
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
        i += 2
    return arr