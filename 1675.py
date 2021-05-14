n = input()

for i in n:
    j = ord(i)
    if j == 32:
        print (' ', end='')
    elif j == 97:
        print ("x", end='')
    elif j == 98:
        print ("y", end='')
    elif j == 99:
        print ("z", end='')
    else:
        print (chr(j-3), end='')