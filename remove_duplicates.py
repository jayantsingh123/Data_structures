class AdjacentDups:

    def __init__(self, s):
        self.data = s

    def remove(self):
        temp = self.data
        print(temp)
        result = ''
        while len(temp) > 0 and len(temp) != len(result):
            result = temp
            temp = self.remove_dups(result)
        if len(temp) == 0:
            return temp
        else:
            return temp

    def remove_dups(self, s1):
        """ remove all adjacent duplicates in string
        for example if s1='caab' then output is 'cb' """
        n = len(s1)
        res = ''
        j = 0

        while j < n:
            if j < n - 1 and s1[j] == s1[j + 1]:
                while j < n - 1 and s1[j] == s1[j + 1]:
                    j += 1
            else:
                res += s1[j]
            j += 1

        return res
