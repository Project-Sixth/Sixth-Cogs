from random import choice
def generate_dayplopynamepart_english():
    """
    :returns String: Random Day Plopy name part in English
    """
    all_consontants =   ['b', 'd', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 'v', 'w',
                         'b', 'd', 'g', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 'v', 'w',
                         'c', 'f', 'h', 'p', 's', 't', 'x', 'y', 'z']
    all_vowels =        ['a', 'e', 'i', 'o', 'u']
    possible_names_templates = [
        'CV',
        'VC',
        'CCV',
        'VCC',
        'CVC',
        'CCVC',
        'CVCC',
        'CCVCC'
    ]
    
    selected_template = choice(possible_names_templates)
    R = ''
    for letter in selected_template:
        if letter == 'C':
            R += choice(all_consontants)
        elif letter == 'V':
            R += choice(all_vowels)
        else:
            R += letter

    return R

def generate_shadowdayplopyname_english():
    """
    :returns String: Random Shadow-Day Plopy name in English
    """
    A = generate_dayplopynamepart_english()
    A += A[::-1]
    R = A.capitalize() + "-" + generate_dayplopynamepart_english().capitalize()
    return R

def main():
    return f'**Маэстро** улыбается, создавая новое имя: {generate_shadowdayplopyname_english()}'
