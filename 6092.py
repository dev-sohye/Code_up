n = int(input())
a = list(map(int,input().split()))
d = []

for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print (d[i], end=' ')

a = int(input())
n = list(map(int, input().split()))

for i in range(1, 24):
    b = n.count(i)
    print (b, end=' ')