from lib import readlines


bonus = ["A", "B", "C"]
res = ["X", "Y", "Z"]

def fight(inp):
    elf, r = inp.split()
    self = bonus[(bonus.index(elf) - (1 - res.index(r))) % 3]
    return bonus.index(self) + 1 + res.index(r) * 3

print(sum(map(fight, readlines())))
