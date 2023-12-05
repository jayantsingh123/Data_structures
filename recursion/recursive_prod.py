#def rec_sequence(n):
 #   curr, total = 0, 0

def recursive_prod(j, idx, curr):
    if idx == j:
        return 1
    curr += 1
    return (curr * recursive_prod(j, idx + 1, curr), curr)
    #for i in range(n):
     #   j = i+1
      #  idx = 0
       # total += recursive_prod(j, idx, curr)
    #return total




# if __name__ == '__main__':
#    print (recursive_prod(2, 0, 1))
