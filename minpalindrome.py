class Solution:

    def __init__(self):
        pass

    def palindromic(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True

    def minpalindrome(self, str1):
        s2 = str1
        n = len(str1)
        # print(n)
        L = []
        for k in range(n - 1, -1, -1):
            if self.palindromic(s2) == True:
                # print(L)
                # print(L)
                return len(L)
            else:
                L.append(str1[k])

                s3 = ''.join(i for i in L)
                s2 = s3 + str1
                print(s2)


if __name__ == '__main__':
    solobj = Solution()
    ans = solobj.minpalindrome('geeks')
    print(ans)
