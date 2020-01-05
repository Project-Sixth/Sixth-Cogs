from random import choice

def generate_starname_russian():
    return generate_starname_english() #Placeholder...
    
def generate_starname_english():
    Part1 = ["a","e","i","o","u","","","","","","","","","","","","","",""]
    Part2 = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","br","cr","dr","gr","kr","pr","sr","tr","str","vr","zr","bl","cl","fl","gl","kl","pl","sl","vl","zl","ch","sh","ph","th"]
    Part3 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ae","ai","ao","au","aa","ea","ei","eo","eu","ee","ia","io","iu","oa","oi","oo","ua","ue"]
    Part4 = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","br","cr","dr","gr","kr","pr","sr","tr","str","vr","zr","bl","cl","fl","hl","gl","kl","ml","nl","pl","sl","tl","vl","zl","ch","sh","ph","th","bd","cd","gd","kd","ld","md","nd","pd","rd","sd","zd","bs","cs","ds","gs","ks","ls","ms","ns","ps","rs","ts","ct","gt","lt","nt","st","rt","zt","bb","cc","dd","gg","kk","ll","mm","nn","pp","rr","ss","tt","zz"]
    Part5 = ["","","","","","","","","","","","","","b","c","d","f","g","h","k","l","m","n","p","r","s","t","x","y","b","c","d","f","g","h","k","l","m","n","p","r","s","t","x","y","cs","ks","ls","ms","ns","ps","rs","ts","ys","ct","ft","kt","lt","nt","ph","sh","th"]
    if choice([1, 2] == 1):
        R = choice(Part1).upper() + choice(Part2) + choice(Part3) + choice(Part5)
    else:
        R = choice(Part1).upper() + choice(Part2) + choice(Part3) + choice(Part4) + choice(Part3) + choice(Part5)
    return R