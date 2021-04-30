h, b, c, s = map(int, input().split())
n = (h * b * c * s) / 8 / 1024 / 1024
print (format(n, ".1f"), "MB")