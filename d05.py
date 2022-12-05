from lib import *


def move_one_by_one(n, src, dst):
    for _ in range(n):
        dst.append(src.pop())

def move_pack(n, src, dst):
    dst.extend(src[-n:])
    del src[-n:]

cmd_pat = re.compile(r"move (\d+) from (\d+) to (\d+)$")

def parse_cmd(s):
    return tuple(map(int, cmd_pat.match(s).groups()))

if __name__ == "__main__":
    inp = readlines()
    storelines = []
    while s := next(inp):
        # stops at first empty line
        storelines.append(s)
    num = storelines.pop().strip()[-1]
    store = [[] for n in range(int(num))]
    for line in storelines[::-1]:
        for i, c, in enumerate(line[1::4]):
            if c.strip():
                store[i].append(c)
    
    if sys.argv[1] == "1":
        funk = move_one_by_one
    elif sys.argv[1] == "2":
        funk = move_pack
    
    for cmd in map(parse_cmd, inp):
        funk(cmd[0], store[cmd[1] - 1], store[cmd[2] - 1])
    
    print("".join(map(itemgetter(-1), store)))
