
rules = open('input').readlines()


bagTree = dict()

for rule in rules:
   rule = rule.strip()
   rule = rule.replace('.','')
   rule = rule.replace('bags','bag')
   parent, children = rule.split(' contain ')

   for child in children.split(','):
      if child == 'no other bag':
         continue
      
      child = child.strip()

      count = int(child[0])
      name = child[2:]

      if parent in bagTree:
         bagTree[parent].append((count,name))
      else:
         bagTree[parent] = [(count,name)]

     
total = 0
   
stack = [(0, 'END')]

node = 'shiny gold bag'
count = 1

explored = set()

while node != 'END':

   if node in bagTree:
      children = bagTree[node]
   else:
      explored.add(tuple(stack + [(count, node)]))
      count, node = stack.pop()

      continue

   number, child = children[0]
   identifier = tuple(stack + [(count,node),(count*number,child)])
   
   i = 0

   while identifier in explored and i < len(children) - 1:
      i += 1
      number, child = children[i]
      identifier = tuple(stack + [(count,node),(count*number,child)])

   if identifier in explored:
      explored.add(tuple(stack + [(count, node)]))
      count, node = stack.pop()


   else:
      stack.append((count, node))
      node = child
      print('+ %s (%s * %s %ss)'%(count * number,count,number,child))
      count *= number
      total += count 

print(total)
      





   

