from random import choice
def generate_planetname_english():
    all_consontants_with_chance_of_nothing = ["b", "c", "ch", "d", "g", "h", "k", "l", "m", "n",
                                              "p", "r", "s", "t", "th", "v", "x", "y", "z",
                                              "", "", "", "", ""]
    all_vowels = ["a", "e", "i", "o", "u"]
    all_consontants_rklz = ["b", "bb", "br", "c", "cc", "ch", "cr", "d", "dr", "g", "gn", "gr",
                            "l", "ll", "lr", "lm", "ln", "lv", "m", "n", "nd", "ng", "nk", "nn",
                            "nr", "nv", "nz", "ph", "s", "str", "th", "tr", "v", "z"]
    all_consontants_and_basic_syllables = ["b", "br", "c", "ch", "cr", "d", "dr", "g", "gn", "gr",
                                           "l", "ll", "m", "n", "ph", "s", "str", "th", "tr", "v",
                                           "z"]
    all_vowels_and_combos = ["a", "e", "i", "o", "u",
                             "a", "e", "i", "o", "u",
                             "a", "e", "i", "o", "u",
                             "ae", "ai", "ao", "au", "a",
                             "ea", "ei", "eo", "eu", "e",
                             "ua", "ue", "ui", "u",
                             "ia", "ie", "iu", "io",
                             "oa", "ou", "oi", "o"]
    planet_endings = ["turn", "ter", "nus", "rus", "tania", "hiri", "hines", "gawa", "nides",
                      "carro", "rilia", "stea", "lia", "lea", "ria", "nov", "phus", "mia",
                      "nerth", "wei", "ruta", "tov", "zuno", "vis", "lara", "nia", "liv",
                      "tera", "gantu", "yama", "tune", "ter", "nus", "cury", "bos", "pra",
                      "thea", "nope", "tis", "clite"]
    planet_endings_too = ["una", "ion", "iea", "iri", "illes", "ides", "agua", "olla", "inda",
                          "eshan", "oria", "ilia", "erth", "arth", "orth", "oth", "illon", "ichi",
                          "ov", "arvis", "ara", "ars", "yke", "yria", "onoe", "ippe", "osie", "one",
                          "ore", "ade", "adus", "urn", "ypso", "ora", "iuq", "orix", "apus", "ion",
                          "eon", "eron", "ao", "omia"]


    C = choice([1, 2, 3, 4])
    if C == 1:
        A = choice(all_consontants_with_chance_of_nothing)
        B = choice(all_consontants_rklz)
        while A == B:
            B = choice(all_consontants_rklz)
        R = A + choice(all_vowels) + B + choice(all_vowels_and_combos) + choice(planet_endings)
    elif C == 2:
        A = choice(all_consontants_with_chance_of_nothing)
        B = choice(all_consontants_rklz)
        while A == B:
            B = choice(all_consontants_rklz)
        R = A + choice(all_vowels) + B + choice(planet_endings_too)
    elif C == 3:
        R = choice(all_consontants_with_chance_of_nothing) + \
            choice(all_vowels_and_combos) + \
            choice(planet_endings)
    elif C == 4:
        A = choice(all_consontants_with_chance_of_nothing)
        B = choice(all_consontants_and_basic_syllables)
        while A == B:
            B = choice(all_consontants_and_basic_syllables)
        R = A + choice(all_vowels) + B + choice(all_vowels) + choice(planet_endings)
    return R.capitalize()

def main(*args):
    return generate_planetname_english()