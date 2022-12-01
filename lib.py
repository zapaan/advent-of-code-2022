def readlines():
    try:
        while (inp := input()) is not None:
            yield inp
    except EOFError:
        return