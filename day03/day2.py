import sys


file = open('input')
lines = list(map(str.strip,file.readlines()))

def doTheThing(xStep,yStep,lines):
   count = 0
   x= 0
   for y in range(0,len(lines),yStep):
      if lines[y][x] == '#':
         count += 1
      x += xStep
      x %= 31
   return count

total = 1

for xStep,yStep in [
      (1,1),
      (3,1),
      (5,1),
      (7,1),
      (1,2),
      ]:
   total *= doTheThing(xStep, yStep, lines)
   
print(total)
