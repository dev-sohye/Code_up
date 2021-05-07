d = [[0] * 20 for _ in range(20)]

for i in range(1, 20):
    n = list(map(int, input().split()))
    for j in range(1, 20):
        d[i][j] = n[j - 1]

a = int(input())
for i in range(a):
    x, y = map(int,input().split())
    for j in range(1, 20):
        if d[x][j] == 1:
            d[x][j] = 0
        else:
            d[x][j] = 1

        if d[j][y] == 1:
            d[j][y] = 0
        else:
            d[j][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print (d[i][j], end=' ')
    print ()