from lib import *

def split(inp):
    return islice(inp, 0, len(inp) // 2), islice(inp, len(inp) // 2, len(inp))


def find_same(first, second):
    return set(first) & set(second)


def priority(c):
    return ord(c.upper()) - ord('A') + 1 + 26 * c.isupper()


if __name__ == "__main__":
    print(sum(starmap(priority, starmap(find_same, map(split, readlines())))))