ck = [[0] * 10 for _ in range(10)]

for i in range(10):
    a = list(map(int, input().split()))
    for j in range(10):
        ck[i][j] = a[j]

x, y = 1, 1
while True:
    if ck[x][y] == 2:
        ck[x][y] = 9
        break

    ck[x][y] = 9

    if ck[x+1][y] == 1 and ck[x][y+1] == 1:
        break

    if ck[x][y+1] == 1:
        x += 1
    elif ck[x+1][y] == 1:
        y += 1
    elif ck[x][y+1] == 0:
        y += 1
    elif ck[x+1][y] == 0:
        x += 1

for i in range(10):
    for j in range(10):
        print (ck[i][j], end=' ')
    print ()