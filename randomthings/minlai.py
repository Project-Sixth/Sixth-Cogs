from random import choice
# Vowel and Consonant
def generate_dayplopynamepart_russian():
    AllConsontants = ['б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р', 'б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р', 'б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р', 'й', 'к', 'п', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш']
    AllVowels = ['а', 'и', 'о', 'у', 'е', 'а','и', 'о', 'у', 'е', 'а', 'и', 'о', 'у', 'е', 'а', 'и', 'о', 'у', 'е', 'э', 'ы', 'ё', 'ю', 'я']
    if choice([2, 3]) == 2:
        if choice([1, 2]) == 1:
            R = choice(AllConsontants) + choice(AllVowels)
        else:
            R = choice(AllVowels) + choice(AllConsontants)
    else:
        R = choice(AllConsontants) + choice(AllVowels) + choice(AllConsontants)
    return R

def generate_dayplopynamepart_english():
    AllConsontants = ['b', 'd', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 'v', 'w', 'b', 'd', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 'v', 'w', 'c', 'f', 'h', 'p', 's', 't', 'x', 'y', 'z']
    AllVowels = ['a', 'e', 'i', 'o', 'u']
    if choice([2, 3]) == 2:
        if choice([1, 2]) == 1:
            R = choice(AllConsontants) + choice(AllVowels)
        else:
            R = choice(AllVowels) + choice(AllConsontants)
    else:
        R = choice(AllConsontants) + choice(AllVowels) + choice(AllConsontants)
    return R

def generate_dayplopyname_russian():
    R = generate_dayplopynamepart_russian().capitalize()
    return R+"-"+R
    
def generate_dayplopyname_english():
    R = generate_dayplopynamepart_english().capitalize()
    return R+"-"+R

def generate_shadowdayplopyname_russian():
    A = generate_dayplopynamepart_russian()
    A += A[::-1]
    R = A.capitalize() + "-" + generate_dayplopynamepart_russian().capitalize()
    return R

def generate_shadowdayplopyname_english():
    A = generate_dayplopynamepart_english()
    A += A[::-1]
    R = A.capitalize() + "-" + generate_dayplopynamepart_english().capitalize()
    return R