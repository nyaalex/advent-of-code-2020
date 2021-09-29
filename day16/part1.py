import re


def verify_data(bounds, number):
    for bound in bounds:
        if min(bound) <= number <= max(bound):
            return True

    return False


input_data = open("input").read()
bounds = []
for i in re.findall("[0-9]+-[0-9]+", input_data):
    bounds.append(tuple(map(int, i.split('-'))))

ticket_data = re.findall("(?:[0-9]+,)+[0-9]+", input_data)
our_ticket = ticket_data.pop(0)

result = 0
for ticket in ticket_data:
    for value in ticket.split(','):
        value = int(value)
        if not verify_data(bounds, value):
            result += value

print(result)
