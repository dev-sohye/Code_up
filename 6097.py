h, w = map(int, input().split())
sh = [[0] * (w+1) for _ in range(h+1)]
a = int(input())
for i in range(a):
    l, d, x, y = map(int, input().split())  
    for j in range(l):
        if d == 0:
            sh[x][y + j] = 1
        elif d == 1:
            sh[x + j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print (sh[i][j], end=' ')
    print ()