"""
Module, that generates things from Min-Lai planet.
"""

from random import choice
# Vowel and Consonant
def generate_dayplopynamepart_russian():
    """
    :returns String: Random Day Plopy name part in Russian
    """
    all_consontants = ['б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р',
                       'б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р',
                       'б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р',
                       'й', 'к', 'п', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш']
    all_vowels = ['а', 'и', 'о', 'у', 'е',
                  'а', 'и', 'о', 'у', 'е',
                  'а', 'и', 'о', 'у', 'е',
                  'а', 'и', 'о', 'у', 'е',
                  'э', 'ы', 'ё', 'ю', 'я']
    if choice([2, 3]) == 2:
        if choice([1, 2]) == 1:
            R = choice(all_consontants) + choice(all_vowels)
        else:
            R = choice(all_vowels) + choice(all_consontants)
    else:
        R = choice(all_consontants) + choice(all_vowels) + choice(all_consontants)
    return R

def generate_dayplopynamepart_english():
    """
    :returns String: Random Day Plopy name part in English
    """
    all_consontants = ['b', 'd', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 'v', 'w',
                       'b', 'd', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 'v', 'w',
                       'c', 'f', 'h', 'p', 's', 't', 'x', 'y', 'z']
    all_vowels = ['a', 'e', 'i', 'o', 'u']
    if choice([2, 3]) == 2:
        if choice([1, 2]) == 1:
            R = choice(all_consontants) + choice(all_vowels)
        else:
            R = choice(all_vowels) + choice(all_consontants)
    else:
        R = choice(all_consontants) + choice(all_vowels) + choice(all_consontants)
    return R

def generate_dayplopyname_russian():
    """
    :returns String: Random Day Plopy name in Russian
    """
    R = generate_dayplopynamepart_russian().capitalize()
    return R+"-"+R

def generate_dayplopyname_english():
    """
    :returns String: Random Day Plopy name in English
    """
    R = generate_dayplopynamepart_english().capitalize()
    return R+"-"+R

def generate_shadowdayplopyname_russian():
    """
    :returns String: Random Shadow-Day Plopy name in Russian
    """
    A = generate_dayplopynamepart_russian()
    A += A[::-1]
    R = A.capitalize() + "-" + generate_dayplopynamepart_russian().capitalize()
    return R

def generate_shadowdayplopyname_english():
    """
    :returns String: Random Shadow-Day Plopy name in English
    """
    A = generate_dayplopynamepart_english()
    A += A[::-1]
    R = A.capitalize() + "-" + generate_dayplopynamepart_english().capitalize()
    return R
