d = [[0] * 20 for i in range(20)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print (d[i][j], end=' ')
    print ()

d=[]
d=[[0]*19 for i in range(19)]

n = int(input())

for i in range(n):
    x,y = list(map(int, input().split()))
    d[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')

    print ()