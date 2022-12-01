from lib import readlines


elves = []
cur_elf = 0
elves.append(0)
for l in readlines():
    if not l:
        elves.append(0)
        cur_elf += 1
    else:
        elves[cur_elf] += int(l)

elves.sort()
print(elves[-1])
print(sum(elves[-3:]))