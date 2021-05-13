a = int(input())
n = int(a)
b = int(input())
c = map(int, input().split())

for i in c:
    n = n * i /100 + n
s = format(n - a, ".0f")
print (s)
if int(s) >= 1:
    print ("good")
elif int(s) < 0:
    print ("bad")
else:
    print ("same")