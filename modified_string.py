def modified(s):
    """ A string needs to modify, as per the following rules to make it valid:

       The string should not have three consecutive same characters (Refer example for explanation).
       He can add any number of characters anywhere in the string.
       Find the minimum number of characters which Ishaan must insert in the string to make it valid.
       """
    ctr=0
    prev=''
    idx=[]
    for i in range(len(s)):
        curr=s[i]
        if curr==prev:
            ctr+=1
            if ctr==2:
                idx.append(i)
                ctr=0
        else:
            ctr=0
        prev=curr
    return len(idx)

if __name__ == '__main__':
    print(modified('aabbbcc'))