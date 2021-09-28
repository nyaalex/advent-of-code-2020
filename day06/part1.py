
lines = open('input').readlines()


letters = ''
count = 0

for form in lines:
   form = form.strip()
   
   if not form:
      count += len(set(letters))
      letters = ''

   else:
      letters += form

count += len(set(letters))
print(count)
   
