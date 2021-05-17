n = int(input())
p = ' '
a = 0
for i in reversed(range(1, n+1)):
    print (p*int(a), end='')
    for j in range(1, i+1):
        print ("*", end='')
    print ()
    a += 1

n = int(input())
for i in range(n, 0, -1):
    print (" "*(n-i), end='')
    print ("*"*i)