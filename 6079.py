num = int(input())
b = 0
sum = 0
while True:
    b += 1
    sum += b
    if num <= sum:
        break
print (b)

num = int(input())
var = 0
sum = 0

while num > sum:
    var += 1
    sum += var
print (var)