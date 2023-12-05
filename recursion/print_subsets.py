def print_subsets(arr, curr, idx):
    """ find all subsets of arr """
    lnew2 = []
    # print(idx,curr)
    if idx == len(arr):
        # L+curr
        if len(curr) != 0:
            curr.sort()
            #return [curr.sort()]
        return [curr]
    lnew = print_subsets(arr, curr, idx + 1) + print_subsets(arr, curr + [arr[idx - 1]], idx + 1)
    [lnew2.append(x) for x in lnew if x not in lnew2]
    # add only unique elements to avoid duplicacy of subsets

    return lnew2
