def lucky(num, ctr):
    """ say n=7, then we have sequence like 1,2,3,4,5,6,7,8,9,.....
    delete every second number to get 1,3,5,7,9,.....
    delete every third element to get 1,3,7,9,,,, and so on
    whatever numbers are left are called lucky number. here 7 is lucky
     Here ctr begins from 2, every second number"""
    if ctr > num:
        # means that number is missed hence is lucky
        return 1
    elif num % ctr == 0:
        # means number will be deleted
        return 0
    else:
        pos = num
        pos = pos - (pos // ctr)
        # new position of the number
        return lucky(pos, ctr + 1)
