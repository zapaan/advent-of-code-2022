from lib import *

def halves(inp):
    return islice(inp, 0, len(inp) // 2), islice(inp, len(inp) // 2, len(inp))

def chunk(it, n=3):
    yield from zip(*[it] * n)

def find_same(*iterz):
    return reduce(and_, map(set, iterz))


def priority(c):
    return ord(c.upper()) - ord('A') + 1 + 26 * c.isupper()


if __name__ == "__main__":
    if sys.argv[1] == "1":
        print(sum(starmap(priority, starmap(find_same, map(halves, readlines())))))
    elif sys.argv[1] == "2":
        print(sum(starmap(priority, starmap(find_same, chunk(readlines())))))