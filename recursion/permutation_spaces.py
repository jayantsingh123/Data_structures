class solution:
    """
    This function gives different permutations of  string obtained by adding spaces at different positions
     in the string
    """
    def permutation(self, s):
        n = len(s)
        buff = [' ']*(2*n)
        op = []
        i, j = 0, 0
        buff[j] = s[i]
        output = self.solve(s, buff, 1, 1, n, op)
        output.sort()
        return output

    def solve(self, s, buff, i, j, n, op):
        if i == n:
            op.append((''.join(buff)).rstrip())
            return
        buff[j] = s[i]
        #print(buff)
        self.solve(s, buff, i+1, j+1, n, op)
        #print(buff)
        buff[j] =" "
        buff[j+1] = s[i]
        self.solve(s, buff, i+1, j+2, n, op)
        return op
if __name__ == '__main__':
    x = solution()
    print(x.permutation('abc'))