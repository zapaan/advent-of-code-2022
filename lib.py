def readlines():
    try:
        while True:
            yield input()
    except EOFError:
        return

from itertools import *
from functools import *
from operator import *
import sys