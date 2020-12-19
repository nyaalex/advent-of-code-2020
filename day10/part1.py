lines = list(map(int, open('input').readlines()))
lines.sort()
lines.append(max(lines) + 3)

last = 0

step3 = 0
step1 = 0

for i in lines:
   diff = i - last
   last = i
   
   if diff == 3:
      step3 += 1
      
   elif diff == 1:
      step1 += 1


print(step1 * step3)
   
