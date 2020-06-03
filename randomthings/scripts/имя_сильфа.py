from random import choice
def generate_sylphname_russian(gender=""):
    availableGenders = ["Male", "Neutral", "Female"]
    if gender not in availableGenders:
        gender = choice(availableGenders)
    
    # --- COMMON
    SingingVowel = ["а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "а", "е", "и", "о", "у", "ае", "еа", "еи", "иа", "ие", "уе", "уа", "аеи", "аеа", "еае"]
    # --- MALES
    MaleStart = ["", "", "", "", "дх", "ф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "ви", "y"]
    MaleConsonant = ["ц", "х", "y", "хл", "хн", "хм", "хш", "хф", "хи", "хт", "л", "лл", "лш", "лф", "лн", "лс", "м", "мн", "мх", "мс", "н", "нх", "нл", "нш", "нт", "нс", "нф", "нм", "нх", "ф", "фн", "фл", "р", "рд", "рф", "рш", "рс", "рх", "рн", "рм", "сс", "сн", "шн", "ш", "ст", "шт", "т", "тх", "в", "ви"]
    MaleEnd = ["", "", "", "", "ф", "фф", "х", "л", "м", "н", "ф", "с", "ш", "y", "ф", "фф", "х", "ф", "с", "ш", "y"]
    MaleEndNonEmpty = ["ф", "фф", "х", "л", "м", "н", "ф", "с", "ш", "y", "ф", "фф", "х", "ф", "с", "ш", "y"]
    # --- NEUTRALS
    NeutralStart = ["", "", "", "", "", "ц", "дх", "ф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "в", "ви"]
    NeutralConsonant = ["ч", "х", "хл", "хн", "хм", "хш", "хф", "хт", "л", "лш", "лф", "лм", "лн", "лс", "лт", "лв", "м", "мм", "мн", "мх", "мс", "мш", "мф", "н", "нх", "нл", "нш", "нт", "нс", "нф", "нв", "нм", "нх", "ф", "фр", "фн", "фл", "р", "рд", "рф", "рш", "рс", "рх", "рн", "рм", "сс", "цн", "шн", "ш", "ст", "шт", "т", "тх", "в", "ви", "y"]
    NeutralEnd = ["ф", "фф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "y"]
    # --- FEMALES
    FemaleStart = ["ц", "ч", "л", "м", "н", "ф", "с", "тх", "в", "ви"]
    FemaleConsonant = ["бх", "ц", "ч", "х", "y", "хл", "хм", "хи", "л", "лм", "лн", "лс", "лт", "лв", "лл", "м", "мм", "мн", "мх", "мс", "н", "нх", "нн", "нл", "нт", "нс", "нв", "нф", "нм", "нх", "ф", "фр", "р", "рд", "рф", "рс", "рх", "рн", "рм", "рв", "сс", "сн", "ш", "ст", "т", "тх", "в", "ви"]
    FemaleEnd = ["ф", "л", "м", "н", "с", "тх", "ф", "фф", "х", "л", "м", "н", "ф", "с", "ш", "тх", "y"]
    
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
        return generate_sylphname_russian(choice(["Male", "Neutral", "Female"]))
    else:
        return generate_sylphname_russian(args[0])