def arr_permutations(arr, low, high):
    """ find count of permutations of  array
        cnt variable accumulates count of permutations"""
    cnt = 0
    if low == high:
        cnt += 1
        return cnt
    for i in range(low, high+1):
        arr[i], arr[low] = arr[low], arr[i]
        cnt += arr_permutations(arr, low+1, high)
        arr[i], arr[low] = arr[low], arr[i]
    return cnt

if __name__ == '__main__':
    print(arr_permutations(['a', 'b', 'c'], 0, 2))

