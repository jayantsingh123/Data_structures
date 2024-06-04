from collections import defaultdict
def reverse(str):
    if len(str)==1:
        return str
    return str[-1]+reverse(str[0:len(str)-1])
def main_fn(text):
    L=text.split(' ')
    print(L)
    rev_txt=[]
    dnew=defaultdict(int)
    for i in L:
        if dnew[i]!=0:
            rev_txt.append(dnew[i])
        else:
            rev = reverse(i)
            dnew[i] = rev
            rev_txt.append(rev)
    return ' '.join(rev_txt)

res = main_fn('the cat in the hat')