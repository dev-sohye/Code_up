n = map(int, input().split())
b = 0
for i in n:
    if i % 5 == 0:
        b += 1
        print (i)
        break
if b == 0:
    print (0)