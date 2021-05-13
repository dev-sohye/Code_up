n = int(input())
for i in range(1, n+1):
    if i*i > n:
        break
    a = i

j = a * a
k = n - j
print (k, a)