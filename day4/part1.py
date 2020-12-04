

verification  = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}
verification1 = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

challengeInput = open('input').readlines()

count = 0
toVerify = set()

for line in challengeInput:
   line = line.strip()
   if not line:
      if not verification1.difference(toVerify):
         count += 1
      toVerify = set()
   for entry in line.split():
      field, value = entry.split(':')
      toVerify.add(field)

if not verification1.difference(toVerify):
   count += 1

      
print(count)
