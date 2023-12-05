def subset_sum(arr,curr,idx):
    """ find sum of all subsets """
    L=[]
    #print(idx,curr)
    if idx == len(arr):
        #print(curr, len(curr))
        if curr == []:
            L.append(0)
        else:
            #print(curr, type(curr))
            L.append(sum(curr))
            print(L)
        return L
    return subset_sum(arr, curr, idx+1) + subset_sum(arr, curr + [arr[idx-1]], idx+1)
    #return L

if __name__=='__main__':
    print(subset_sum([3,34,4], [], 0))