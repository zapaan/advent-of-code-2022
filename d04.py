from lib import *

pat = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)$')

def rooms(start1, end1, start2, end2):
    return set(range(start1, end1 + 1)), set(range(start2, end2 + 1))

def intuple(tup):
    # damn, there must be a way in the standard lib
    yield from (int(s) for s in tup)

def fully_overlap(elf1, elf2):
    return bool(elf1 <= elf2 or elf2 <= elf1)

def overlap(elf1, elf2):
    return bool(elf1 & elf2)

if __name__ == "__main__":
    if sys.argv[1] == "1":
        funk = fully_overlap
    elif sys.argv[1] == "2":
        funk = overlap
    print(sum(starmap(funk, (starmap(rooms, map(intuple, map(methodcaller('groups'), map(pat.match, readlines()))))))))