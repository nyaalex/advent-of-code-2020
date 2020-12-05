





sub = {'F': '0',
       'B': '1',
       'R': '1',
       'L': '0',
       }



lines = open('input').readlines()
maxID = 0
seatIDs = []

for line in lines:
   line = line.strip()
   for k in sub:
      line = line.replace(k,sub[k])
   seatIDs.append(int(line,base=2))

seatIDs.sort()

last = seatIDs[0] - 1

for ID in seatIDs:
   if ID - last != 1:
      print(ID - 1)
   last = ID
