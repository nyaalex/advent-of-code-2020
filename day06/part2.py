
lines = open('input').readlines()


letters = set()
first = True
count = 0

for form in lines:
   form = form.strip()
   
   if not form:
      print(letters)
      count += len(letters )
      letters = set()
      first = True

   else:
      print(form)
      if first:
         letters = set(form)
         first = False
      else:
         letters = letters.intersection(set(form))         

count += len(letters)
print(count)
   
