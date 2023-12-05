def valid_ip_test(str1):
    str_list = str1.split('.')
    # flag = False
    for i in str_list:
        flag = False
        if i.isdigit() and (0 <= int(i) <= 255):
            if len(i) == 1:
                flag = True
            elif len(i.lstrip('0')) == len(i):
                # print(i, len(i), len(i.lstrip('0')))
                flag = True
        if not flag:
            return 0
    return 1
