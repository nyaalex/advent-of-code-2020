import sys

count = 0
x = 0

file = open('input')

for line in file:
   if line[x] == '#':
      count += 1
   x += 3
   x %= 31

print(count)
