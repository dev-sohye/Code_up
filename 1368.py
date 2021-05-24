h, k, d = input().split()
h, k = int(h), int(k)
num = 0
for i in range(h):
    if d == "L":
        print (" "*num, end='')
        print ("*"*k)
        num += 1

    else:
        num += 1
        print (" "*(h-num), end='')
        print ("*"*k)