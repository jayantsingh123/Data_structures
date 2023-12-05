def findSum(s):
    total = 0
    temp = "0"
    for i in range(len(s)):
        if s[i].isdigit():

            temp += s[i]
            #print(temp)
        else:
            #print(temp)
            if temp != '0':
                total += int(temp.lstrip('0'))
               # print(total)
                temp = "0"
    return total+int(temp.lstrip('0'))

if __name__ == '__main__':
    print(findSum('1abc23'))