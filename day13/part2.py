import re

input_data = open("input").read()
all_nums = re.findall("([0-9]+|x)", input_data)

jump, result = 1, 0

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
for slot, bus_id in enumerate(all_nums[1:]):
    if bus_id != 'x':
        bus_id = int(bus_id)
        slot = (bus_id - slot) % bus_id
        while result % bus_id != slot:
            result += jump

        jump *= bus_id

print(result)
