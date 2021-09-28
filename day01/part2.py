import sys

numbers = set()

while line := sys.stdin.readline():
    if line:
        numbers.add(int(line.strip()))

sums = dict()
for num1 in numbers:
    for num2 in numbers:
        if num1+num2 > 2020:
            continue
        else:
            sums[num1+num2] = (num1,num2)

flag = False
for num1 in numbers:
    if 2020-num1 in sums:
        nums = sums[2020-num1]
        print(num1 * nums[0] * nums[1])
        break
