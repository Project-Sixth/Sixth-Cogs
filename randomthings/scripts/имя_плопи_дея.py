from random import choice
def generate_dayplopynamepart_russian():
    """
    :returns String: Random Day Plopy name part in Russian
    """
    all_consontants =      ['б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р',
                            'б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р',
                            'б', 'в', 'г', 'д', 'ж', 'з', 'л', 'м', 'н', 'р',
                            'й', 'к', 'п', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш']
    all_vowels =           ['а', 'и', 'о', 'у', 'е',
                            'а', 'и', 'о', 'у', 'е',
                            'а', 'и', 'о', 'у', 'е',
                            'а', 'и', 'о', 'у', 'е',
                            'э', 'ы', 'ё', 'ю', 'я']
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
        'VCь',
        'VCь',
        'VCь',
        'VCь',
        'VCь',
        'VCь',
        'VCь',
        'VCь',
        'VCь',
        'VCь',
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
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
        'CVCь',
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

def generate_dayplopyname_russian():
    """
    :returns String: Random Shadow-Day Plopy name in Russian
    """
    R = generate_dayplopynamepart_russian().capitalize()
    return R+"-"+R

def main(*args):
    return generate_dayplopyname_russian()
