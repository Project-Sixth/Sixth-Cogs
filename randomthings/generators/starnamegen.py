from random import choice
# Vowel and Consonant
def generate_starname_russian():
    SingleVowel25Chance = ["а","е","и","о","у","","","","","","","","","","","","","","",""]
    AllConsonantsAndRLH = ["б","в","г","д","ж","з","к","л","м","н","п","р","с","т","ф","ц","ч","ш",
    "бр","вр","др","гр","кр","пр","ср","тр","стр","цр","жр",
    "бл","цл","фл","гл","кл","пл","сл","вл","зл",
    "ч","ш","пх","тх"]
    AllVowelsAndDoubleVowels = ["а","е","и","о","у","а","е","и","о","у","а","е","и","о","у",
    "ае","аи","ао","ау","аа","еа","еи","ео","еу","ее","иа","ио","иу","оа","ои","оо","уа","уе"]
    AllConsonantsAndRLHDSTO = ["б","в","г","д","ж","з","к","л","м","н","п","р","с","т","ф","ц","ч","ш",
    "бр","вр","др","гр","кр","пр","ср","тр","стр","цр","жр",
    "бл","цл","фл","хл","гл","кл","мл","нл","пл","сл","тл","вл","зл",
    "ч","ш","пх","тх",
    "бд","цд","гд","кд","лд","мд","нд","пд","рд","сд","жд",
    "бс","цс","дс","гс","кс","лс","мс","нс","пс","рс","тс",
    "цт","гт","лт","нт","ст","рт","жт",
    "бб","цц","дд","гг","кк","лл","мм","нн","рр","пп","сс","тт","жж"]
    AllConsonantsAndSTHWithChanceOfNothing = ["","","","","","","","","","","","","",
    "б","в","г","д","ж","з","к","л","м","н","п","р","с","т","ф","ц","ч","ш",
    "б","в","г","д","ж","з","к","л","м","н","п","р","с","т","ф","ц","ч","ш",
    "цс","кс","лс","мс","нс","пс","рс","тс","ус",
    "цт","фт","кт","лт","нт",
    "пх","ш","тх"]

    SingleVowel = ["а","е","и","о","у"]
    if choice([1, 2]) == 1:
        R = choice(SingleVowel25Chance) + choice(AllConsonantsAndRLH) + choice(AllVowelsAndDoubleVowels) + choice(AllConsonantsAndSTHWithChanceOfNothing)
    else:
        A = choice(AllVowelsAndDoubleVowels)
        B = choice(SingleVowel) if A not in SingleVowel else choice(AllVowelsAndDoubleVowels)
        R = choice(SingleVowel25Chance) + choice(AllConsonantsAndRLH) + A + choice(AllConsonantsAndRLHDSTO) + B + choice(AllConsonantsAndSTHWithChanceOfNothing)
    return R.capitalize()

def generate_starname_english():
    SingleVowel25Chance = ["a","e","i","o","u","","","","","","","","","","","","","","",""]
    AllConsonantsAndRLH = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z",
    "br","cr","dr","gr","kr","pr","sr","tr","str","vr","zr",
    "bl","cl","fl","gl","kl","pl","sl","vl","zl",
    "ch","sh","ph","th"]
    AllVowelsAndDoubleVowels = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u",
    "ae","ai","ao","au","aa","ea","ei","eo","eu","ee","ia","io","iu","oa","oi","oo","ua","ue"]
    AllConsonantsAndRLHDSTO = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z",
    "br","cr","dr","gr","kr","pr","sr","tr","str","vr","zr",
    "bl","cl","fl","hl","gl","kl","ml","nl","pl","sl","tl","vl","zl",
    "ch","sh","ph","th",
    "bd","cd","gd","kd","ld","md","nd","pd","rd","sd","zd",
    "bs","cs","ds","gs","ks","ls","ms","ns","ps","rs","ts",
    "ct","gt","lt","nt","st","rt","zt",
    "bb","cc","dd","gg","kk","ll","mm","nn","pp","rr","ss","tt","zz"]
    AllConsonantsAndSTHWithChanceOfNothing = ["","","","","","","","","","","","","",
    "b","c","d","f","g","h","k","l","m","n","p","r","s","t","x","y",
    "b","c","d","f","g","h","k","l","m","n","p","r","s","t","x","y",
    "cs","ks","ls","ms","ns","ps","rs","ts","ys",
    "ct","ft","kt","lt","nt",
    "ph","sh","th"]

    SingleVowel = ["a","e","i","o","u"]
    if choice([1, 2]) == 1:
        R = choice(SingleVowel25Chance) + choice(AllConsonantsAndRLH) + choice(AllVowelsAndDoubleVowels) + choice(AllConsonantsAndSTHWithChanceOfNothing)
    else:
        A = choice(AllVowelsAndDoubleVowels)
        B = choice(SingleVowel) if A not in SingleVowel else choice(AllVowelsAndDoubleVowels)
        R = choice(SingleVowel25Chance) + choice(AllConsonantsAndRLH) + A + choice(AllConsonantsAndRLHDSTO) + B + choice(AllConsonantsAndSTHWithChanceOfNothing)
    return R.capitalize()