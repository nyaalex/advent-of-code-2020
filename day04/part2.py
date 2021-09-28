import re

verification = {
   'byr': lambda x: int(x) >= 1920 and int(x) <=2002,
   'iyr': lambda x: int(x) >= 2010 and int(x) <=2020,
   'eyr': lambda x: int(x) >= 2020 and int(x) <=2030,
   'hgt': lambda x: (x[-2:] == 'cm' and
                     int(x[:-2]) >= 150 and int(x[:-2]) <= 193
                     ) or (x[-2:] == 'in' and
                     int(x[:-2]) >= 59 and int(x[:-2]) <= 76
                     ),
   'hcl': lambda x: re.match("^#[0-9a-f]{6}$",x),
   'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
   'pid': lambda x: re.match("^[0-9]{9}$",x)
}


def verify(toVerify):
   if set(verification).difference(set(toVerify)):
      return False
   
   flag = True
   for key in toVerify:
      if key == 'cid':
         continue
      value = verification[key](toVerify[key])
      if not value:
         flag = False
      

   return flag
   

challengeInput = open('input').readlines()

count = 0
toVerify = dict()

for line in challengeInput:
   line = line.strip()

   if not line:

      if verify(toVerify):
         count += 1
      toVerify = dict()
      
   for entry in line.split():
      field, value = entry.split(':')
      toVerify[field] = value

if verify(toVerify):
   count+=1
   
print(count)
