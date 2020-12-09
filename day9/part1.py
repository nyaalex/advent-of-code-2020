lines = list(map(int, open('input').readlines()))

for i in range(len(lines) - 25):

   toFindSum = lines[i:i+25]
   num = lines[i+25]

   canSum = False

   for toCheck in toFindSum:
      if (num - toCheck) in toFindSum:
         canSum = True
         break

   if not canSum:
      print(num)
      break
      
