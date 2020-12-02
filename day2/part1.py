import sys

lines = []



while line := sys.stdin.readline():
   if line:
      lines.append(line.strip())


for line in lines:
   count, letter, password = line.split(" ")
   smallest, longest = map(int, count.split('-'))
   letter = letter[0]
   
   count = password.count(letter)
    
   if count >= smallest and count <= longest:
      print(password)


