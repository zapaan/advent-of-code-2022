from lib import *

def marker_pat(n):
    s = r'(\w)'
    for i in range(1, n):
        s += r"(?!(?:"
        s += "|".join(rf"\{j}" for j in range(1, i+1))
        s += r"))(\w)"
    return s

data = input()
m = re.search(marker_pat(int(sys.argv[1])), data)
print(m.end())
