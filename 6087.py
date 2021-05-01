n = int(input())
a = 0

for i in range(1, n+1):
    a += 1
    if i % 3 != 0:
        print(i, end=' ')