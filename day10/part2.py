lines = list(map(int, open('input').readlines()))
lines.sort()
#lines.append(max(lines) + 3)



stairs = [0]*(lines[-1]+1)
stairs[0] = 1
for n in lines:
       stairs[n] = stairs[n-3] + stairs[n-2] + stairs[n-1]


print(stairs[-1])
   
