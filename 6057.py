a = list(map(int, input().split()))
b = bool(a[0])
c = bool(a[1])

print (b and c or (not b) and (not c))