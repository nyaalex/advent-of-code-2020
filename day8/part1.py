
program = open('input').readlines()


PC = 0
ACC = 0
alreadyRan = set()

while PC not in alreadyRan:
   alreadyRan.add(PC)
   instr, val = program[PC].split()

   if instr == 'nop':
      PC += 1
      
   elif instr=='jmp':
      PC += int(val)

   elif instr=='acc':
      ACC += int(val)
      PC += 1

print(ACC)
   
