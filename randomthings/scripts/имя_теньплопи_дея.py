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

def generate_shadowdayplopyname_russian():
    """
    :returns String: Random Shadow-Day Plopy name in Russian
    """
    A = generate_dayplopynamepart_russian()
    A += A[::-1]
    R = A.capitalize() + "-" + generate_dayplopynamepart_russian().capitalize()
    return R

def main():
    return f'**Маэстро** улыбается, создавая новое имя: {generate_shadowdayplopyname_russian()}'
