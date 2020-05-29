import re
import random
import yaml

config = {}

### ORDER OF YAML FILE - first comes pool, then all subgens
# pool:
#   - Something reads that {{ generator }} is very rare, found only in {{ random_gen }} people
#   - Another {{ random_gen }} is coming
# vars (optional):
#   sesso: "{{ generator }}"
# generator:
#   - white flower
#   - black dye
#   - "{{ random_gen }} witch"
# random_gen:
#   - drunken
#   - erect
#   - holding {{ sesso }}

def check_and_define_vars():
    global config
    if 'vars' in config:
        for var in config['vars']:
            config['vars'][var] = mutate([config['vars'][var]])

def getMutationFromConfig(match):
    global config
    
    if match.group(1) in config['vars']:
        return config['vars'][match.group(1)]
    elif match.group(1) in config:
        return random.choice(config[match.group(1)])
    else:
        raise Exception(f'No dictionary of variable "{match.group(1)}" found.')

def getMutationFromFile(match):
    try:
        with open(f'{str(__file__)[:-11]}/libs/{match.group(1)}.yml', 'r', encoding='utf-8') as f:
            lib = yaml.safe_load(f)
            return random.choice(lib)
    except:
        raise Exception(f'No file "./libs/{match.group(1)}.yml" found.')

def mutate(mutationTrail=[]):
    if len(mutationTrail) > 1:
        if mutationTrail[-2] == mutationTrail[-1]:
            return mutationTrail[-1]
    
    newMutation = re.sub('{{ (.*?) }}', getMutationFromConfig, mutationTrail[-1], count=1)
    newMutation = re.sub('\[\[ (.*?) \]\]', getMutationFromFile, newMutation, count=1)
    
    return mutate(mutationTrail + [newMutation])

def load(gen_name):
    global config

    try:
        with open(f'{str(__file__)[:-11]}/gens/{gen_name}.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except Exception as E:
        return f'**Маэстро:** Ох! Кажется, произошла какая-то серьезная ошибка!\n```\nError of Reading-State:\n{E}\n```'
       
    try:
        check_and_define_vars()
    except Exception as E:
        return f'**Маэстро:** Ох! Кажется, произошла какая-то серьезная ошибка!\n```\nError of Var-Defining-State:\n{E}\n```'
    
    return mutate([random.choice(config['pool'])])

def say(message):
    return mutate([message])