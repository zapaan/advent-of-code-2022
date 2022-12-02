from dataclasses import dataclass
from lib import readlines

@dataclass
class Score:
    res: tuple[str, str, str]
    bonus: int

    def solve(self, elf):
        return self.res.index(elf) * 3 + self.bonus

RPS = {
    "X": Score(("B", "A", "C"), 1),
    "Y": Score(("C", "B", "A"), 2),
    "Z": Score(("A", "C", "B"), 3),
}

def fight(inp):
    if not inp:
        return 0
    elf, self = inp.split()
    return RPS[self].solve(elf)

print(sum(map(fight, readlines())))