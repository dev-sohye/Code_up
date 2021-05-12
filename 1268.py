n = int(input())
var = list(map(int, input().split()))
s = 0
for i in var:
    if i % 2 == 0:
        s += 1
print (s)