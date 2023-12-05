def recursive_sequence(n):

    """
    for a given n,(say n=2) find the value given by following expression,
    f(2) = 1+(2*3)

    :param n:
    :return:
    """
    curr, prod, total = 0, 1, 0
    for i in range(n):
        prod = 1
        for k in range(i+1):
            curr += 1
            prod = prod*curr
        total += prod
    return total

if __name__ == '__main__':
    print(recursive_sequence(5))