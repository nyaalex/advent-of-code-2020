import sys

numbers = set()

while line := sys.stdin.readline():
    if line:
        numbers.add(int(line.strip()))

flag = False
while flag:
    
    if 2020 - num1 in numbers:
        print((2020 - num1) * num1)
        flag = True
