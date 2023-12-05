class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack

    def insert(self, s, elem):
        if len(s) == 0 or s[-1] < elem:
            s.append(elem)
            return s
        temp = s.pop()
        self.insert(s, elem)
        s.append(temp)
        return s

    def sorted(self, s):
        if len(s) == 0:
            return s
        elem = s.pop()
        s = self.sorted(s)
        s = self.insert(s, elem)
        # print(s)
        return s


# def insert(S, elem):
#     print(S, elem)
#     if len(S) == 0 or S[-1] < elem:
#         S.append(elem)
#         return S
#     temp = S.pop()
#     insert(S, elem)
#     S.append(temp)
#     return S
#
#
# def sort(S):
#     if len(S) == 0:
#         return S
#     elem = S.pop()
#     S = sort(S)
#     S = insert(S, elem)
#     return S


if __name__ == '__main__':
    obj = Solution()
    print(obj.sorted([3, 2, 1]))
    # print(sort([3, 2, 1]))
