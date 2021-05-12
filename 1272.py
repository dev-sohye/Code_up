n, m = map(int, input().split())
a, b = 0, 0
c, d = 0, 0
if n % 2 == 0:
    a = n * 5
    b += a
else:
    a = n // 2 + 1
    b += a

if m % 2 == 0:
    c = m * 5
    d += c
else:
    c = m // 2 + 1
    d += c

print (b + d)