import sys

numbers = []

while line := sys.stdin.readline():
    if line:
        numbers.append(int(line.strip()))

flag = False
for num1 in numbers:
    if flag:
        break
    
    for num2 in numbers:
        if flag:
            break
        
        for num3 in numbers:
            if num1 == num2 or num1 == num2 or num3 == num2:
                continue
            elif num1+num2+num3 == 2020:
                print(num1*num2*num3)
                flag = True
                break
            
