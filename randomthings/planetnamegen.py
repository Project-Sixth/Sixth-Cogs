from random import choice
# Vowel and Consonant

def generate_planetname_russian():
    AllConsontantsWithChanceOfNothing = ["б", "ц", "ч", "д", "г", "х", "к", "л", "м", "н", "п", "р", "с", "т", "тх", "в", "з", "", "", "", "", ""]
    AllVowels = ["а", "о", "и", "у", "е"]
    AllConsontantsPlusRKLZ = ["б", "бб", "бр", "ц", "цц", "ч", "цр", "д", "др", "г", "гн", "гр", "л", "лл", "лр", "лм", "лн", "лв", "м", "н", "нд", "нг", "нк", "нн", "нр", "нв", "нз", "ф", "с", "стр", "тх", "тр", "в", "з"]
    AllConsontantsAndBasicSyllables = ["б", "бр", "ц", "ч", "цр", "д", "др", "г", "гн", "гр", "л", "лл", "м", "н", "ф", "с", "стр", "тх", "тр", "в", "з"]
    AllVowelsAndCombos = ["а", "о", "и", "у", "е"
    "а", "о", "и", "у", "е",
    "а", "о", "и", "у", "е",
    "ае", "аи", "ао", "ау", "а",
    "еа", "еи", "ео", "еу", "е",
    "уа", "уе", "уи", "у",
    "иа", "ие", "иу", "ио",
    "оа", "оу", "ои", "о"]
    PlanetEndings = ["турн", "тер", "нус", "рус", "тани", "хири", "хинес", "гава", "нидес", "карро", "рилия", "стеа", "лиа", "леа", "риа", "нов", "фус", "миа", "нерт", "вей", "рута", "тов", "зуно", "вис", "лара", "ниа", "лив", "тера", "ганту", "яма", "туне", "тер", "нус", "кури", "бос", "пра", "фея", "ноп", "тис", "клит"]
    PlanedEndingsToo = ["уна", "ион", "иеа", "ири", "иллес", "идес", "агва", "олла", "инда", "эшан", "ория", "иллия", "ерт", "арт", "орт", "отх", "иллион", "ичи", "ов", "арвис", "ара", "арс", "ук", "урия", "оной", "иппе", "оси", "он", "ор", "ад", "адус", "урн", "упсо", "ора", "юк", "орикс", "апус", "ион", "еон", "ерон", "ао", "омия"]

    C = choice([1,2,3,4])
    if C == 1:
        A = choice(AllConsontantsWithChanceOfNothing)
        B = choice(AllConsontantsPlusRKLZ)
        while A == B:
            B = choice(AllConsontantsPlusRKLZ)
        R = A + choice(AllVowels) + B + choice(AllVowelsAndCombos) + choice(PlanetEndings)
    elif C == 2:
        A = choice(AllConsontantsWithChanceOfNothing)
        B = choice(AllConsontantsPlusRKLZ)
        while A == B:
            B = choice(AllConsontantsPlusRKLZ)
        R = A + choice(AllVowels) + B + choice(PlanedEndingsToo)
    elif C == 3:
        R = choice(AllConsontantsWithChanceOfNothing) + choice(AllVowelsAndCombos) + choice(PlanetEndings)
    elif C == 4:
        A = choice(AllConsontantsWithChanceOfNothing)
        B = choice(AllConsontantsAndBasicSyllables)
        while A == B:
            B = choice(AllConsontantsAndBasicSyllables)
        R = A + choice(AllVowels) + B + choice(AllVowels) + choice(PlanetEndings)
    return R.capitalize()

def generate_planetname_english():
    AllConsontantsWithChanceOfNothing = ["b", "c", "ch", "d", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "th", "v", "x", "y", "z", "", "", "", "", ""]
    AllVowels = ["a", "e", "i", "o", "u"]
    AllConsontantsPlusRKLZ = ["b", "bb", "br", "c", "cc", "ch", "cr", "d", "dr", "g", "gn", "gr", "l", "ll", "lr", "lm", "ln", "lv", "m", "n", "nd", "ng", "nk", "nn", "nr", "nv", "nz", "ph", "s", "str", "th", "tr", "v", "z"]
    AllConsontantsAndBasicSyllables = ["b", "br", "c", "ch", "cr", "d", "dr", "g", "gn", "gr", "l", "ll", "m", "n", "ph", "s", "str", "th", "tr", "v", "z"]
    AllVowelsAndCombos = ["a", "e", "i", "o", "u",
    "a", "e", "i", "o", "u",
    "a", "e", "i", "o", "u",
    "ae", "ai", "ao", "au", "a",
    "ea", "ei", "eo", "eu", "e",
    "ua", "ue", "ui", "u",
    "ia", "ie", "iu", "io",
    "oa", "ou", "oi", "o"]
    PlanetEndings = ["turn", "ter", "nus", "rus", "tania", "hiri", "hines", "gawa", "nides", "carro", "rilia", "stea", "lia", "lea", "ria", "nov", "phus", "mia", "nerth", "wei", "ruta", "tov", "zuno", "vis", "lara", "nia", "liv", "tera", "gantu", "yama", "tune", "ter", "nus", "cury", "bos", "pra", "thea", "nope", "tis", "clite"]
    PlanedEndingsToo = ["una", "ion", "iea", "iri", "illes", "ides", "agua", "olla", "inda", "eshan", "oria", "ilia", "erth", "arth", "orth", "oth", "illon", "ichi", "ov", "arvis", "ara", "ars", "yke", "yria", "onoe", "ippe", "osie", "one", "ore", "ade", "adus", "urn", "ypso", "ora", "iuq", "orix", "apus", "ion", "eon", "eron", "ao", "omia"]


    C = choice([1,2,3,4])
    if C == 1:
        A = choice(AllConsontantsWithChanceOfNothing)
        B = choice(AllConsontantsPlusRKLZ)
        while A == B:
            B = choice(AllConsontantsPlusRKLZ)
        R = A + choice(AllVowels) + B + choice(AllVowelsAndCombos) + choice(PlanetEndings)
    elif C == 2:
        A = choice(AllConsontantsWithChanceOfNothing)
        B = choice(AllConsontantsPlusRKLZ)
        while A == B:
            B = choice(AllConsontantsPlusRKLZ)
        R = A + choice(AllVowels) + B + choice(PlanedEndingsToo)
    elif C == 3:
        R = choice(AllConsontantsWithChanceOfNothing) + choice(AllVowelsAndCombos) + choice(PlanetEndings)
    elif C == 4:
        A = choice(AllConsontantsWithChanceOfNothing)
        B = choice(AllConsontantsAndBasicSyllables)
        while A == B:
            B = choice(AllConsontantsAndBasicSyllables)
        R = A + choice(AllVowels) + B + choice(AllVowels) + choice(PlanetEndings)
    return R.capitalize()