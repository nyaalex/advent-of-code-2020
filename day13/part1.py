import re

# Easy peasy hehehe
input_data = open("input").read()
all_nums = re.findall("[0-9]+", input_data)

time_now = int(all_nums[0])
buses = map(int, all_nums[1:])

time_to_wait = [(i, -time_now % i) for i in buses]
next_bus = min(time_to_wait, key=lambda x: x[1])

print(next_bus[0] * next_bus[1])
