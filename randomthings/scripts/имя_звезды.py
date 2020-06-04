from random import choice
def generate_starname_russian():
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


def main(*args):
    return generate_starname_russian()