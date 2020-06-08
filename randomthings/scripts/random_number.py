from random import randint

def main(*args):
    return str(args)
    # if len(args) == 0:
    #     return str(randint(0, 100))
    # elif len(args) == 1:
    #     try:
    #         return str(randint(0, int(args[0])))
    #     except:
    #         return str(randint(0, 100))
    # else:
    #     try:
    #         return str(randint(int(args[0]), int(args[1])))
    #     except:
    #         return str(randint(0, 100))
