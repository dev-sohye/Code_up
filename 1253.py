a, b = map(int, input().split())
if a < b:
    for i in range(a, b+1):
        print (i, end=' ')
if a > b:
    for i in range(b, a+1):
        print (i, end=' ')
if a == b:
    print (a)