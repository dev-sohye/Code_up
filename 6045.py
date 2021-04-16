# num = list(map(int, input().split()))

# print (sum(num), format(sum(num) / len(num), ".2f"))

a,b = input().split()

cnt = 1
Temp = 1
while True:
    Temp *= 2   

    if cnt == int(b):
        break

    cnt += 1


Result = int(a) * Temp

print(Result)