from random import randint

def main(*args):
    if len(args) == 0:
        return randint(0, 100)
    elif len(args) == 1:
        try:
            return randint(0, int(args(0)))
        except:
            return randint(0, 100)
    else:
        try:
            return randint(int(args(0)), int(args(1)))
        except:
            return randint(0, 100)
