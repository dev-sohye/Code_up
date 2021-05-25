h, r = map(int, input(). split())

for j in range(r):
    for i in range(h):
        print (" "*i, end='')
        print ("*")
    for i in range(h-2, -1, -1):
        print (" "*i, end='')
        print ("*")