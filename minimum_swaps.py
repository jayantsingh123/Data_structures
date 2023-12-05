def minimum_swaps(S):
    """ find minimum swaps to make the string balanced,
    e.g S='[]][][' needs two swaps with adjacent characters to make it
    '[][][]'
    The idea is to maintain imbalance the difference between right brackets and
    left brackets. And as a left bracket is encountered use that to
     decrease the imbalance by 1 """

    imbalance, left, right, swap = 0, 0, 0, 0
    for i in range(len(S)):
        if S[i] == '[':
            left += 1
            if imbalance > 0:
                swap += imbalance
                imbalance -= 1
        else:
            right += 1
            imbalance = right - left
        return swap
