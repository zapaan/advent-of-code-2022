from lib import readlines


elves = [0]
for l in readlines():
    if not l:
        elves.append(0)
    else:
        elves[-1] += int(l)

elves.sort()
print(elves[-1])
print(sum(elves[-3:]))