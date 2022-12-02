from lib import readlines
import sys
from functools import partial

bonus = ["A", "B", "C"]
res = ["X", "Y", "Z"]

def fight(inp, mode):
    if not inp:
        return 0
    elf, r = inp.split()
    if mode == "2":
        self = bonus[(bonus.index(elf) - (1 - res.index(r))) % 3]
        return bonus.index(self) + 1 + res.index(r) * 3
    elif mode == "1":
        return res.index(res[(((res.index(r) - bonus.index(elf)) % -3) + 1)]) * 3 + res.index(r) + 1

print(sum(map(partial(fight, mode=sys.argv[1]), readlines())))
