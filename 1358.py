n = int(input())
temp = []
for i in range(1, n+1):
    if i % 2 == 1:
        temp.append(i)
var = len(temp)

a = 0
for i in temp:
    a += 1
    print (" "*(var-a), end='')
    print ("*"*i)