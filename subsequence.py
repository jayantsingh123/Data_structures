def subsequence(a,b):
    i,j = len(a)-1, len(b)-1
    while i>=0 and j>=0:
        if a[i]==b[j]:
            i-=1
            j-=1
        else:
            j-=1
    return i==-1

if __name__=='__main__':
    print(subsequence('AXY','YADXCP'))
