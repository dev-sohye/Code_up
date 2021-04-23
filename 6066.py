num = map(int,input().split())

for test in num:
    i = test % 2
    if i == 0:
        print ("even")

    else:
        print ("odd")