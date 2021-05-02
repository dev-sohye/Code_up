a, b = map(int,input().split())

for i in range(a, b+1):
    for j in range(1, 10):
        s = i * j
        print (i, "*", j, "=", s, sep='')