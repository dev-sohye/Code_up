a = int(input())
b = 0
for i in range(1, a+1):
    if i % 2 == 0:
        b += i
print (b)


a = int(input())
b = 0
c = 0
while True:
    b += 1
    if b % 2 == 0:
        c += b
    if a == b:
        break
print (c)


a = int(input())
b = 0
c = 0
while a > b:
    b += 1
    if b % 2 == 0:
        c += b
print (c)