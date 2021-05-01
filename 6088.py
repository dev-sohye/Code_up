a, d, n = map(int,input().split())
for i in range(1, n+1):
    a += d
    if i == n - 1:
        print (a)

a, d, n = map(int,input().split())
s = 0
while True:
    a += d
    s += 1
    if s == n - 1:
        break
print (a)

a, d, n = map(int,input().split())

for i in range(1, n):
    a+=d
print(a)