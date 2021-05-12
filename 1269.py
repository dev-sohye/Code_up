a, b, c, n = map(int, input().split())
Result = 0

if n <= 1:
    Result = a
else:
    for i in range (n - 1):
        Result = a * b + c
        a = Result

print (Result)

a, b, c, n = map(int, input().split())

for i in range(1, n):
    a = a * b + c
print (a)