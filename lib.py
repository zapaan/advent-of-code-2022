def readlines():
    try:
        while True:
            yield input()
    except EOFError:
        return
