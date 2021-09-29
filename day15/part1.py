starting_numbers = list(map(int, open("input").read().strip().split(',')))

turn = 1
last_spoken = 0
last_seen = dict()
for v in starting_numbers:
    last_seen[v] = turn
    last_spoken = v
    turn += 1

while turn <= 2020:
    if last_spoken in last_seen:
        turn_seen = last_seen[last_spoken]
        last_seen[last_spoken] = turn - 1
        last_spoken = turn - (1 + turn_seen)
    else:
        last_seen[last_spoken] = turn - 1
        last_spoken = 0

    turn += 1

print(turn, last_spoken)
