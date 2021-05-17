n = input()
Num = list()
Calculations = list()
temp = 0
dest = ''

for i in n:

    if i == '+':
        Num.append(int(dest))
        Calculations.append('+')
        dest = ''
    elif i == '-':
        Num.append(int(dest))
        Calculations.append('-')
        dest = ''
    elif i == '*':
        Num.append(int(dest))
        Calculations.append('*')
        dest = ''
    elif i == '/':
        Num.append(int(dest))
        Calculations.append('/')
        dest = ''
    elif i == '=':
        Num.append(int(dest))
        dest = ''
    else:
        dest += i

a = 0
temp = int(Num[0])
for i in range(0, len(Calculations)):
    # temp = int(Num[0])
     
    if Calculations[i] == '+':
        temp += int(Num[i + 1]) 
    elif Calculations[i] == '-':
        temp -= int(Num[i + 1])        
    elif Calculations[i] == '*':
        temp *= int(Num[i + 1])         
    elif Calculations[i] == '/':
        temp //= int(Num[i + 1])  
        
print (int(temp))