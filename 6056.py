a, b = list(map(int,input().split()))

a = bool(a)
b = bool(b)

print ((a and (not b)) or b and (not a))