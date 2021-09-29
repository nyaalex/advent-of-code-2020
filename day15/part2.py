import time

starting_numbers = list(map(int, open("input").read().strip().split(',')))

turn = 1
last_spoken = 0
last_seen = dict()
for v in starting_numbers:
    last_seen[v] = turn
    last_spoken = v
    turn += 1

start_time = time.time()

while turn <= 30000000:
    if turn % 10000 == 0:
        total_time = time.time() - start_time
        print(f"Completed {turn} turns after {int(total_time)}s Left: {int((total_time/turn) * (30000000-turn))}",
              end="\r")
    if last_spoken in last_seen:
        turn_seen = last_seen[last_spoken]
        last_seen[last_spoken] = turn - 1
        last_spoken = turn - (1 + turn_seen)
    else:
        last_seen[last_spoken] = turn - 1
        last_spoken = 0

    turn += 1

print("\n", turn, last_spoken)
