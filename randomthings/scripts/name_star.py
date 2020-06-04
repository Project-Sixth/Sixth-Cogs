from random import choice
def generate_starname_english():
    single_vowel_25_chance = ["a", "e", "i", "o", "u",
                              "", "", "", "", "",
                              "", "", "", "", "",
                              "", "", "", "", ""]
    all_consonants_rlh = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r",
                          "s", "t", "v", "w", "x", "y", "z",
                          "br", "cr", "dr", "gr", "kr", "pr", "sr", "tr", "str", "vr", "zr",
                          "bl", "cl", "fl", "gl", "kl", "pl", "sl", "vl", "zl",
                          "ch", "sh", "ph", "th"]
    all_vowels_and_double_vowels = ["a", "e", "i", "o", "u",
                                    "a", "e", "i", "o", "u",
                                    "a", "e", "i", "o", "u",
                                    "ae", "ai", "ao", "au", "aa",
                                    "ea", "ei", "eo", "eu", "ee",
                                    "ia", "io", "iu",
                                    "oa", "oi", "oo",
                                    "ua", "ue"]
    all_consonants_rlhdsto = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r",
                              "s", "t", "v", "w", "x", "y", "z",
                              "br", "cr", "dr", "gr", "kr", "pr", "sr", "tr", "str", "vr", "zr",
                              "bl", "cl", "fl", "hl", "gl", "kl", "ml",
                              "nl", "pl", "sl", "tl", "vl", "zl",
                              "ch", "sh", "ph", "th",
                              "bd", "cd", "gd", "kd", "ld", "md", "nd", "pd", "rd", "sd", "zd",
                              "bs", "cs", "ds", "gs", "ks", "ls", "ms", "ns", "ps", "rs", "ts",
                              "ct", "gt", "lt", "nt", "st", "rt", "zt",
                              "bb", "cc", "dd", "gg", "kk", "ll", "mm", "nn", "pp",
                              "rr", "ss", "tt", "zz"]
    all_consonants_sth_with_chance_of_nothing = ["", "", "", "", "", "", "", "", "", "", "", "",
                                                 "b", "c", "d", "f", "g", "h", "k", "l", "m", "n",
                                                 "p", "r", "s", "t", "x", "y",
                                                 "b", "c", "d", "f", "g", "h", "k", "l", "m", "n",
                                                 "p", "r", "s", "t", "x", "y",
                                                 "cs", "ks", "ls", "ms", "ns", "ps", "rs",
                                                 "ts", "ys",
                                                 "ct", "ft", "kt", "lt", "nt",
                                                 "ph", "sh", "th"]

    single_vowel = ["a", "e", "i", "o", "u"]
    if choice([1, 2]) == 1:
        R = choice(single_vowel_25_chance) + \
            choice(all_consonants_rlh) + \
            choice(all_vowels_and_double_vowels) + \
            choice(all_consonants_sth_with_chance_of_nothing)
    else:
        A = choice(all_vowels_and_double_vowels)
        B = choice(single_vowel) if A not in single_vowel else choice(all_vowels_and_double_vowels)
        R = choice(single_vowel_25_chance) +\
            choice(all_consonants_rlh) + \
            A + \
            choice(all_consonants_rlhdsto) + \
            B + \
            choice(all_consonants_sth_with_chance_of_nothing)
    return R.capitalize()

def main(*args):
    return generate_starname_english()