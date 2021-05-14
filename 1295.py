n = input()
for i in n:
    if i.isupper():
        print (i.lower(), end='')
    else:
        print (i.upper(), end='')

n = input()
print (n.swapcase())