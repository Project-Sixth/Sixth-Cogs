from random import choice
def generate_planetname_russian():
    all_consontants_with_chance_of_nothing = ["б", "ц", "ч", "д", "г", "х", "к", "л", "м", "н",
                                              "п", "р", "с", "т", "тх", "в", "з",
                                              "", "", "", "", ""]
    all_vowels = ["а", "о", "и", "у", "е"]
    all_consontants_rklz = ["б", "бб", "бр", "ц", "цц", "ч", "цр", "д", "др", "г", "гн", "гр", "л",
                            "лл", "лр", "лм", "лн", "лв", "м", "н", "нд", "нг", "нк", "нн", "нр",
                            "нв", "нз", "ф", "с", "стр", "тх", "тр", "в", "з"]
    all_consontants_and_basic_syllables = ["б", "бр", "ц", "ч", "цр", "д", "др", "г", "гн",
                                           "гр", "л", "лл", "м", "н", "ф", "с", "стр", "тх",
                                           "тр", "в", "з"]
    all_vowels_and_combos = ["а", "о", "и", "у", "е"
                             "а", "о", "и", "у", "е",
                             "а", "о", "и", "у", "е",
                             "ае", "аи", "ао", "ау", "а",
                             "еа", "еи", "ео", "еу", "е",
                             "уа", "уе", "уи", "у",
                             "иа", "ие", "иу", "ио",
                             "оа", "оу", "ои", "о"]
    planet_endings = ["турн", "тер", "нус", "рус", "тани", "хири", "хинес", "гава", "нидес",
                      "карро", "рилия", "стеа", "лиа", "леа", "риа", "нов", "фус", "миа", "нерт",
                      "вей", "рута", "тов", "зуно", "вис", "лара", "ниа", "лив", "тера", "ганту",
                      "яма", "туне", "тер", "нус", "кури", "бос", "пра", "фея", "ноп", "тис",
                      "клит"]
    planet_endings_too = ["уна", "ион", "иеа", "ири", "иллес", "идес", "агва", "олла",
                          "инда", "эшан", "ория", "иллия", "ерт", "арт", "орт", "отх",
                          "иллион", "ичи", "ов", "арвис", "ара", "арс", "ук", "урия", "оной",
                          "иппе", "оси", "он", "ор", "ад", "адус", "урн", "упсо", "ора", "юк",
                          "орикс", "апус", "ион", "еон", "ерон", "ао", "омия"]

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
    return generate_planetname_russian()