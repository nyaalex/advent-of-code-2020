import re


def verify_data(types, bounds, number):
    valid_types = set()
    for i, bound in enumerate(bounds):
        if min(bound) <= number <= max(bound):
            valid_types.add(types[i//2])
    return valid_types


input_data = open("input").read()
bounds = []
types = []

for i in re.findall(".*: ", input_data):
    types.append(i.split(':')[0])

for i in re.findall("[0-9]+-[0-9]+", input_data):
    bounds.append(tuple(map(int, i.split('-'))))

ticket_data = re.findall("(?:[0-9]+,)+[0-9]+", input_data)
our_ticket = ticket_data.pop(0)

result = 0
possibilities = [set(types) for i in types]

for ticket in ticket_data:
    is_valid = True
    valid_types = []
    for value in ticket.split(','):
        value = int(value)
        result = verify_data(types, bounds, value)
        valid_types.append(result)
        is_valid = is_valid and result

    if is_valid:
        for i, v in enumerate(valid_types):
            possibilities[i] = possibilities[i].intersection(v)

for _ in range(len(possibilities)):
    for i, v in enumerate(possibilities):
        if len(v) == 1:
            to_remove = v.pop()

            for ii in possibilities:
                if to_remove in ii:
                    ii.remove(to_remove)

            possibilities[i] = to_remove
            print(possibilities[i])

result = 1
for field, value in zip(possibilities, our_ticket.split(',')):
    if field[:3] == 'dep':
        result *= int(value)

print(result)
