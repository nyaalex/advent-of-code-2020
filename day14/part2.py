import re


def apply_mask(mask, c):
    a = int(mask.replace("X", "0"), 2)
    b = int(mask.replace("X", "1"), 2)
    return (a & b) | (a & c) | (b & c)


def conv_mask(mask):
    if mask == '':
        yield ''
    else:
        for comb in conv_mask(mask[1:]):
            if mask[0] == '1':
                yield '1' + comb
            elif mask[0] == '0':
                yield 'X' + comb
            else:
                yield '1' + comb
                yield '0' + comb


mem = dict()
mask = ""
for line in open("input"):
    line = line.strip()
    if line[:4] == "mask":
        mask = line[7:]
    else:
        address, val = re.findall("[0-9]+", line)
        for new_mask in conv_mask(mask):
            address = apply_mask(new_mask, int(address))
            mem[address] = int(val)

result = 0
for i in mem:
    result += mem[i]

print(result)
