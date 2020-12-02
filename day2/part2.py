import sys

lines = []



while line := sys.stdin.readline():
   if line:
      lines.append(line.strip())


for line in lines:
   count, letter, password = line.split(" ")
   smallest, longest = map(int, count.split('-'))
   letter = letter[0]

   if (password[smallest-1] == letter) != (password[longest-1] == letter):
      print(password)


