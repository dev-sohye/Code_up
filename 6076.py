a = int(input())

for i in range(101):
    print (i)
    i += 1
    if i > a:
        break

a = int(input())
b = 0
while True:
    print (b)
    b += 1
    if a < b:
        break