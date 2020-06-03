from random import choice
def generate_sylphname_english(gender=""):
    availableGenders = ["Male", "Neutral", "Female"]
    if gender not in availableGenders:
        gender = choice(availableGenders)
    
    # --- COMMON
    SingingVowel = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ae", "ea", "ei", "ia", "ie", "ue", "ua", "aei", "aea", "eae"]
    # --- MALES
    MaleStart = ["", "", "", "", "dh", "f", "h", "l", "m", "n", "ph", "s", "sh", "th", "w", "y"]
    MaleConsonant = ["c", "h", "y", "hl", "hn", "hm", "hsh", "hph", "hy", "hth", "ht", "l", "ll", "lsh", "lf", "ln", "lph", "ls", "lth", "m", "mn", "mh", "ms", "n", "nh", "nl", "nsh", "nt", "ns", "nth", "nph", "nf", "nm", "nh", "nhr", "ph", "phn", "phl", "r", "rd", "rph", "rsh", "rs", "rth", "rh", "rn", "rm", "ss", "sn", "shn", "sh", "st", "sht", "t", "th", "thr", "v", "w"]
    MaleEnd = ["", "", "", "", "f", "ff", "h", "l", "m", "n", "ph", "s", "sh", "y", "f", "ff", "h", "ph", "s", "sh", "y"]
    MaleEndNonEmpty = ["f", "ff", "h", "l", "m", "n", "ph", "s", "sh", "y", "f", "ff", "h", "ph", "s", "sh", "y"]
    # --- NEUTRALS
    NeutralStart = ["", "", "", "", "", "c", "dh", "f", "h", "l", "m", "n", "ph", "s", "sh", "th", "v", "w", "y"]
    NeutralConsonant = ["ch", "h", "hl", "hn", "hm", "hsh", "hph", "ht", "hth", "l", "lsh", "lf", "lm", "ln", "lph", "ls", "lt", "lth", "lv", "m", "mm", "mn", "mh", "ms", "msh", "mth", "mf", "n", "nh", "nl", "nsh", "nt", "ns", "nth", "nph", "nv", "nf", "nm", "nh", "nhr", "ph", "phr", "phn", "phl", "r", "rd", "rph", "rsh", "rs", "rth", "rh", "rn", "rm", "ss", "sn", "shn", "sh", "st", "sht", "t", "th", "thr", "v", "w", "y"]
    NeutralEnd = ["f", "ff", "h", "l", "m", "n", "ph", "s", "sh", "th", "y"]
    # --- FEMALES
    FemaleStart = ["c", "ch", "l", "m", "n", "ph", "s", "th", "v", "w", "y"]
    FemaleConsonant = ["bh", "c", "ch", "h", "y", "hl", "hm", "hy", "l", "lm", "ln", "ls", "lt", "lth", "lv", "ll", "m", "mm", "mn", "mh", "ms", "mth", "n", "nh", "nn", "nl", "nt", "ns", "nth", "nv", "nf", "nm", "nh", "nhr", "ph", "phr", "r", "rd", "rph", "rs", "rth", "rh", "rn", "rm", "rv", "ss", "sn", "sh", "st", "t", "th", "thr", "v", "w"]
    FemaleEnd = ["f", "l", "m", "n", "s", "th", "f", "ff", "h", "l", "m", "n", "ph", "s", "sh", "th", "y"]
    
    # S = starts
    # V = vowel
    # C = consonant
    # E = end
    # N = end not empty
    R = ''
    if gender == "Male":
        name_templates = [
            "SVCVE",
            "SVCVNV",
            "VCVCVEV",
        ]
        name_template = choice(name_templates)
        for letter in name_template:
            if letter == 'S':
                R += choice(MaleStart)
            elif letter == 'V':
                R += choice(SingingVowel)
            elif letter == 'C':
                R += choice(MaleConsonant)
            elif letter == 'E':
                R += choice(MaleEnd)
            elif letter == 'N':
                R += choice(MaleEndNonEmpty)
            else:
                R += letter
    elif name == "Neutral":
        name_templates = [
            "SVCVE",
            "SVCVCVE",
        ]
        name_template = choice(name_templates)
        for letter in name_template:
            if letter == 'S':
                R += choice(NeutralStart)
            elif letter == 'V':
                R += choice(SingingVowel)
            elif letter == 'C':
                R += choice(NeutralConsonant)
            elif letter == 'E':
                R += choice(NeutralEnd)
            else:
                R += letter
    elif name == "Female":
        name_templates = [
            "SVCVE",
            "SVCVCE",
        ]
        name_template = choice(name_templates)
        for letter in name_template:
            if letter == 'S':
                R += choice(FemaleStart)
            elif letter == 'V':
                R += choice(SingingVowel)
            elif letter == 'C':
                R += choice(FemaleConsonant)
            elif letter == 'E':
                R += choice(FemaleEnd)
            else:
                R += letter

    return R.capitalize()

def main(*args):
    if len(args) == 0:
        return generate_sylphname_english(choice(["Male", "Neutral", "Female"]))
    else:
        return generate_sylphname_english(args[0])