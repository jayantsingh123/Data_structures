def balance_check(exp):
    """ Check if parentheses are balanced"""

    input_new = {'(', '{', '['}
    output_new = {')', '}', ']'}
    dnew = {'}': '{', ')': '(', ']': '['}
    print(dnew)
    S = []
    for i in range(len(exp)):
        # print(exp[i])
        if exp[i] in input_new:
            S.append(exp[i])
        elif exp[i] in output_new:
            if len(S) > 0 and dnew[exp[i]] == S[-1]:
                S.pop()
                # print(S)
            else:
                S.append(exp[i])
        print(S)
    if len(S) == 0:
        return 'Balanced'
    else:
        return 'Unbalanced'
