n, m = map(int, input().split())
a = 0
for i in range(n, m+1):
    if i % 2 != 0:
        a += i
    else:
        a -= i


print (a)