
program = open('input').readlines()


PC = 0
ACC = 0
alreadyRan = set()

changed = set()

jumpBack = tuple()

while PC < len(program) and PC >= 0:
   if PC in alreadyRan:
      PC, ACC, alreadyRan = jumpBack
      jumpBack = tuple()
      
   alreadyRan.add(PC)
   instr, val = program[PC].split()

   if instr == 'nop':
      if PC not in changed and not jumpBack:
         changed.add(PC)
         jumpBack = (PC, ACC, alreadyRan.copy())
         PC += int(val)
      else:
         PC += 1

         
      
   elif instr=='jmp':
      if PC not in changed and not jumpBack:
         changed.add(PC)
         jumpBack = (PC, ACC, alreadyRan.copy())
         PC += 1
      else:
         PC += int(val)

   elif instr=='acc':
      ACC += int(val)
      PC += 1

print(ACC)
   
