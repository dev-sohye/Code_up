n = input()

for i in n:
    j = ord(i)
    if j == 32:
        print (' ', end='')
    elif j == 120:
        print ("a", end='')
    elif j == 121:
        print ("b", end='')
    elif j == 122:
        print ("c", end='')
    else:
        print (chr(j-3), end='')