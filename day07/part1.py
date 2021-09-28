
rules = open('input').readlines()


inverseTree = dict()

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

      if name in inverseTree:
         inverseTree[name].append(parent)
      else:
         inverseTree[name] = [parent]
      

count = 0
   
stack = ['END']
node = 'shiny gold bag'
explored = set()

while node != 'END':

   if node in inverseTree:
      children = inverseTree[node]
   else:
      explored.add(node)
      node = stack.pop()
      continue

   child = children[0]
   i = 0
   
   while child in explored and i < len(children) - 1:
      i += 1
      child = children[i]

   if child in explored:
      explored.add(node)
      node = stack.pop()

   else:
      stack.append(node)
      node = child
      count += 1

print(count)
      





   

