import dis
def caseSort(s, n):
    lower_list, upper_list = [], []
    lower, upper = 0, 0
    for i in s:
        if i.islower():
            lower_list.append(i)
        else:
            upper_list.append(i)
    lower_list.sort()
    upper_list.sort()
    s2 = list(s)
    for i in range(n):
        if s2[i].islower():
            s2[i] = lower_list[lower]
            lower += 1
        else:
            s2[i] = upper_list[upper]
            upper += 1
    return ''.join(s2)

bytecode = dis.Bytecode(caseSort('defRTSersUXI', 12 ))
for instr in bytecode:
    print(instr.opname)
#if __name__ == '__main__':
 #   print(caseSort('defRTSersUXI', 12))
