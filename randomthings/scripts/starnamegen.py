"""
Generator from https://www.fantasynamegenerators.com/star-names.php
"""

from random import choice
# Vowel and Consonant
def generate_starname_russian():
    """Generates star name
    
    Returns
    -------
    String
        Completely random-generated Star Name (using Russian letters)
    """
    single_vowel_25_chance = ["а", "е", "и", "о", "у",
                              "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    all_consonants_rlh = ["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н",
                          "п", "р", "с", "т", "ф", "ц", "ч", "ш",
                          "бр", "вр", "др", "гр", "кр", "пр", "ср", "тр", "стр", "цр", "жр",
                          "бл", "цл", "фл", "гл", "кл", "пл", "сл", "вл", "зл",
                          "ч", "ш", "пх", "тх"]
    all_vowels_and_double_vowels = ["а", "е", "и", "о", "у",
                                    "а", "е", "и", "о", "у",
                                    "а", "е", "и", "о", "у",
                                    "ае", "аи", "ао", "ау", "аа",
                                    "еа", "еи", "ео", "еу", "ее",
                                    "иа", "ио", "иу",
                                    "оа", "ои", "оо",
                                    "уа", "уе"]
    all_consonants_rlhdsto = ["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п",
                              "р", "с", "т", "ф", "ц", "ч", "ш",
                              "бр", "вр", "др", "гр", "кр", "пр", "ср", "тр", "стр", "цр", "жр",
                              "бл", "цл", "фл", "хл", "гл", "кл", "мл",
                              "нл", "пл", "сл", "тл", "вл", "зл",
                              "ч", "ш", "пх", "тх",
                              "бд", "цд", "гд", "кд", "лд", "мд", "нд", "пд", "рд", "сд", "жд",
                              "бс", "цс", "дс", "гс", "кс", "лс", "мс", "нс", "пс", "рс", "тс",
                              "цт", "гт", "лт", "нт", "ст", "рт", "жт",
                              "бб", "цц", "дд", "гг", "кк", "лл", "мм", "нн",
                              "рр", "пп", "сс", "тт", "жж"]
    all_consonants_sth_with_chance_of_nothing = ["", "", "", "", "", "", "", "", "", "", "", "", "",
                                                 "б", "в", "г", "д", "ж", "з", "к", "л", "м", "н",
                                                 "п", "р", "с", "т", "ф", "ц", "ч", "ш",
                                                 "б", "в", "г", "д", "ж", "з", "к", "л", "м", "н",
                                                 "п", "р", "с", "т", "ф", "ц", "ч", "ш",
                                                 "цс", "кс", "лс", "мс", "нс", "пс",
                                                 "рс", "тс", "ус",
                                                 "цт", "фт", "кт", "лт", "нт",
                                                 "пх", "ш", "тх"]

    single_vowel = ["а", "е", "и", "о", "у"]
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

def generate_starname_english():
    """Generates star name
    
    Returns
    -------
    String
        Completely random-generated Star Name (using English letters)
    """
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
