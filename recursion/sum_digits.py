def computesum(n):
    total = 0
    if n == 0:
        return 0
    q, r = divmod(n, 10)
    total = r + computesum(q)
    return total

if __name__ == '__main__':
    print(computesum(9999))
