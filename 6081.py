num = int(input(), 16)

for i in range(1, 16):
    a = i * num
    print('%X'%num, '*%X'%i, '=%X'%a, sep='')