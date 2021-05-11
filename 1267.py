n = int(input())
var = list(map(int, input().split()))
s = 0
for i in var:
    if i % 5 == 0:
        s += i
print (s)