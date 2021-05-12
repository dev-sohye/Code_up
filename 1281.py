n, m = map(int, input().split())
a = ""
b = 0
for i in range(n, m+1):
    if i % 2 == 1:
        if i == n:
            a += str(i)
        else:
            a += "+" + str(i)
        b += i
    else:
        a += "-" + str(i)
        b -= i

print (a,"=",b, sep='')