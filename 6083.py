r, g, b = map(int,input().split())
n = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            n += 1
            print (i, j, k)
print (n)