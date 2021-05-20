n = int(input())
sum = 0
temp = 0
for i in range(1, n+1):
    sum += i
    temp += sum
print (temp)