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
        'CV',
        'CV',
        'CV',
        'CV',
        'CV',
        'CV',
        'CV',
        'CV',
        'CV',
        'VC',
        'VC',
        'VC',
        'VC',
        'VC',
        'VC',
        'VC',
        'VC',
        'VC',
        'VC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVC',
        'CVCC',
        'CVCC',
        'CVCC',
        'CCVC',
        'CCV',
        'VCC',
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

def generate_dayplopyname_english():
    """
    :returns String: Random Shadow-Day Plopy name in English
    """
    R = generate_dayplopynamepart_english().capitalize()
    return R+"-"+R

def main(*args):
    return generate_dayplopyname_english()
