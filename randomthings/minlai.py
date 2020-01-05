from random import choice

def generate_dayplopyname():
    S = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
    G = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    if choice([2, 3]) == 2:
        if choice([1, 2]) == 1:
            R = choice(S).upper() + choice(G)
        else:
            R = choice(G).upper() + choice(S)
    else:
        R = choice(S).upper() + choice(G) + choice(S)
    return R+"-"+R
    
async def generate_dayplopyname_english():
    S = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    G = ['a', 'e', 'i', 'o', 'u']
    if choice([2, 3]) == 2:
        if choice([1, 2]) == 1:
            R = choice(S).upper() + choice(G)
        else:
            R = choice(G).upper() + choice(S)
    else:
        R = choice(S).upper() + choice(G) + choice(S)
    return R+"-"+R
