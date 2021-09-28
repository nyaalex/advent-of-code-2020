





sub = {'F': '0',
       'B': '1',
       'R': '1',
       'L': '0',
       }



lines = open('input').readlines()
maxID = 0

for line in lines:
   line = line.strip()
   for k in sub:
      line = line.replace(k,sub[k])
   if int(line,base=2) > maxID:
      maxID = int(line,base=2)

print(maxID)
