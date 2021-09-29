import re


def apply_mask(mask, c):
    a = int(mask.replace("X", "0"), 2)
    b = int(mask.replace("X", "1"), 2)
    return (a & b) | (a & c) | (b & c)


mem = dict()
mask = ""
for line in open("input"):
    line = line.strip()
    if line[:4] == "mask":
        mask = line[7:]
    else:
        address, val = re.findall("[0-9]+", line)
        val = apply_mask(mask, int(val))
        mem[address] = val

result = 0
for i in mem:
    result += mem[i]

print(result)