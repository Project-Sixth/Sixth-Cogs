from random import choice
# Vowel and Consonant
def generate_sylphname_english(name=""):
    FemaleStart = ["c", "ch", "l", "m", "n", "ph", "s", "th", "v", "w", "y"]
    SingingVowel = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ae", "ea", "ei", "ia", "ie", "ue", "ua", "aei", "aea", "eae"]
    FemaleConsonant = ["bh", "c", "ch", "h", "y", "hl", "hm", "hy", "l", "lm", "ln", "ls", "lt", "lth", "lv", "ll", "m", "mm", "mn", "mh", "ms", "mth", "n", "nh", "nn", "nl", "nt", "ns", "nth", "nv", "nf", "nm", "nh", "nhr", "ph", "phr", "r", "rd", "rph", "rs", "rth", "rh", "rn", "rm", "rv", "ss", "sn", "sh", "st", "t", "th", "thr", "v", "w"]
    FemaleEnd = ["f", "l", "m", "n", "s", "th", "f", "ff", "h", "l", "m", "n", "ph", "s", "sh", "th", "y"]
    MaleStart = ["", "", "", "", "dh", "f", "h", "l", "m", "n", "ph", "s", "sh", "th", "w", "y"]
    MaleConsonant = ["c", "h", "y", "hl", "hn", "hm", "hsh", "hph", "hy", "hth", "ht", "l", "ll", "lsh", "lf", "ln", "lph", "ls", "lth", "m", "mn", "mh", "ms", "n", "nh", "nl", "nsh", "nt", "ns", "nth", "nph", "nf", "nm", "nh", "nhr", "ph", "phn", "phl", "r", "rd", "rph", "rsh", "rs", "rth", "rh", "rn", "rm", "ss", "sn", "shn", "sh", "st", "sht", "t", "th", "thr", "v", "w"]
    MaleEnd = ["", "", "", "", "f", "ff", "h", "l", "m", "n", "ph", "s", "sh", "y", "f", "ff", "h", "ph", "s", "sh", "y"]
    NeutralStart = ["", "", "", "", "", "c", "dh", "f", "h", "l", "m", "n", "ph", "s", "sh", "th", "v", "w", "y"]
    NeutralConsonant = ["ch", "h", "hl", "hn", "hm", "hsh", "hph", "ht", "hth", "l", "lsh", "lf", "lm", "ln", "lph", "ls", "lt", "lth", "lv", "m", "mm", "mn", "mh", "ms", "msh", "mth", "mf", "n", "nh", "nl", "nsh", "nt", "ns", "nth", "nph", "nv", "nf", "nm", "nh", "nhr", "ph", "phr", "phn", "phl", "r", "rd", "rph", "rsh", "rs", "rth", "rh", "rn", "rm", "ss", "sn", "shn", "sh", "st", "sht", "t", "th", "thr", "v", "w", "y"]
    NeutralEnd = ["f", "ff", "h", "l", "m", "n", "ph", "s", "sh", "th", "y"]
    
    if not name:
        name = choice(["Male", "Neutral", "Female"])

    if name == "Male":
        C = choice([1,2,3])
        if C == 1:
            R = choice(MaleStart) + choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + choice(MaleEnd)
        elif C == 2:
            A = choice(MaleEnd)
            while A == "":
                A = choice(MaleEnd)
            R = choice(MaleStart) + choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + A + choice(SingingVowel)
        elif C == 3:
            R = choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + choice(MaleEnd) + choice(SingingVowel)
    elif name == "Neutral":
        C = choice([1,2])
        if C == 1:
            R = choice(NeutralStart) + choice(SingingVowel) + choice(NeutralConsonant) + choice(SingingVowel) + choice(NeutralEnd)
        elif C == 2:
            R = choice(NeutralStart) + choice(SingingVowel) + choice(NeutralConsonant) + choice(SingingVowel) + choice(NeutralConsonant) + choice(SingingVowel) + choice(NeutralEnd)
    elif name == "Female":
        C = choice([1,2])
        if C == 1:
            R = choice(FemaleStart) + choice(SingingVowel) + choice(FemaleConsonant) + choice(SingingVowel) + choice(FemaleEnd)
        elif C == 2:
            R = choice(FemaleStart) + choice(SingingVowel) + choice(FemaleConsonant) + choice(SingingVowel) + choice(FemaleConsonant) + choice(FemaleEnd)
    return R.capitalize()

def generate_sylphname_russian(name=""):
    FemaleStart = ["ц", "ч", "л", "м", "н", "ф", "с", "тх", "в", "ви"]
    SingingVowel = ["а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "ае", "еа", "еи", "иа", "ие", "уе", "уа", "аеи", "аеа", "еае"]
    FemaleConsonant = ["бх", "ц", "ч", "х", "y", "хл", "хм", "хи", "л", "лм", "лн", "лс", "лт", "лв", "лл", "м", "мм", "мн", "мх", "мс", "н", "нх", "нн", "нл", "нт", "нс", "нв", "нф", "нм", "нх", "ф", "фр", "р", "рд", "рф", "рс", "рх", "рн", "рм", "рв", "сс", "сн", "ш", "ст", "т", "тх", "в", "ви"]
    FemaleEnd = ["ф", "л", "м", "н", "с", "тх", "ф", "фф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "y"]
    MaleStart = ["", "", "", "", "дх", "ф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "ви", "y"]
    MaleConsonant = ["ц", "х", "y", "хл", "хн", "хм", "хш", "хф", "хи", "хт", "л", "лл", "лш", "лф", "лн", "лс", "м", "мн", "мх", "мс", "н", "нх", "нл", "нш", "нт", "нс", "нф", "нм", "нх", "ф", "фн", "фл", "р", "рд", "рф", "рш", "рс", "рх", "рн", "рм", "сс", "сн", "шн", "ш", "ст", "шт", "т", "тх", "в", "ви"]
    MaleEnd = ["", "", "", "", "ф", "фф", "х", "л", "м", "н", "ф", "с", "ш", "y", "ф", "фф", "х", "ф", "с", "ш", "y"]
    NeutralStart = ["", "", "", "", "", "ц", "дх", "ф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "в", "ви"]
    NeutralConsonant = ["ч", "х", "хл", "хн", "хм", "хш", "хф", "хт", "л", "лш", "лф", "лм", "лн", "лс", "лт", "лв", "м", "мм", "мн", "мх", "мс", "мш", "мф", "н", "нх", "нл", "нш", "нт", "нс", "нф", "нв", "нм", "нх", "ф", "фр", "фн", "фл", "р", "рд", "рф", "рш", "рс", "рх", "рн", "рм", "сс", "цн", "шн", "ш", "ст", "шт", "т", "тх", "в", "ви", "y"]
    NeutralEnd = ["ф", "фф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "y"]
    
    if not name:
        name = choice(["Male", "Neutral", "Female"])

    if name == "Male":
        C = choice([1,2,3])
        if C == 1:
            R = choice(MaleStart) + choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + choice(MaleEnd)
        elif C == 2:
            A = choice(MaleEnd)
            while A == "":
                A = choice(MaleEnd)
            R = choice(MaleStart) + choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + A + choice(SingingVowel)
        elif C == 3:
            R = choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + choice(MaleConsonant) + choice(SingingVowel) + choice(MaleEnd) + choice(SingingVowel)
    elif name == "Neutral":
        C = choice([1,2])
        if C == 1:
            R = choice(NeutralStart) + choice(SingingVowel) + choice(NeutralConsonant) + choice(SingingVowel) + choice(NeutralEnd)
        elif C == 2:
            R = choice(NeutralStart) + choice(SingingVowel) + choice(NeutralConsonant) + choice(SingingVowel) + choice(NeutralConsonant) + choice(SingingVowel) + choice(NeutralEnd)
    elif name == "Female":
        C = choice([1,2])
        if C == 1:
            R = choice(FemaleStart) + choice(SingingVowel) + choice(FemaleConsonant) + choice(SingingVowel) + choice(FemaleEnd)
        elif C == 2:
            R = choice(FemaleStart) + choice(SingingVowel) + choice(FemaleConsonant) + choice(SingingVowel) + choice(FemaleConsonant) + choice(FemaleEnd)
    return R.capitalize()