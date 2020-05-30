import re
import random
import importlib
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

def executeScript(script_name):
    try:
        script = importlib.import_module(f'randomthings.scripts.{script_name}')
        return script.main()
    except Exception as E:
        return f'**Маэстро:** Ох! Кажется, произошла какая-то серьезная ошибка!\n```\nError of Script-Execution-State:\n{E}\n```'

def check_and_define_vars():
    global config
    if 'vars' in config:
        for var in config['vars']:
            config['vars'][var] = mutate([config['vars'][var]])

def getMutationFromConfig(match):
    global config
    
    if ('vars' in config) and (match.group(1) in config['vars']):
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

def getMutationFromScript(match):
    try:
        return executeScript(match.group(1))
    except:
        raise Exception(f'No file "./scripts/{match.group(1)}.py" found.')

def mutate(mutationTrail=[]):
    if len(mutationTrail) > 1:
        if mutationTrail[-2] == mutationTrail[-1]:
            return mutationTrail[-1]
    
    newMutation = re.sub('{{ (.*?) }}', getMutationFromConfig, mutationTrail[-1], count=1)
    newMutation = re.sub('\[\[ (.*?) \]\]', getMutationFromFile, newMutation, count=1)
    newMutation = re.sub('\(\( (.*?) \)\)', getMutationFromScript, newMutation, count=1)
    
    return mutate(mutationTrail + [newMutation])

def getExecution(match):
    actions = match.group(1)
    affectedwords = match.group(2)
    
    if 'C' in actions:
        affectedwords = affectedwords.capitalize()
    if 'U' in actions:
        affectedwords = affectedwords.upper()
    if 'L' in actions:
        affectedwords = affectedwords.lower()
    return affectedwords

def execute(mutationTrail=[]):
    if len(mutationTrail) > 1:
        if mutationTrail[-2] == mutationTrail[-1]:
            return mutationTrail[-1]
    
    newMutation = re.sub('\$\$(\w+) (.*?) \$\$', getExecution, mutationTrail[-1], count=1)
    
    return execute(mutationTrail + [newMutation])

def loadGenerator(gen_name):
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
    
    try:
        return execute([mutate([random.choice(config['pool'])])])
    except Exception as E:
        return f'**Маэстро:** Ох! Кажется, произошла какая-то серьезная ошибка!\n```\nError of Mutation-State:\n{E}\n```'

def say(message):
    try:
        return execute([mutate([message])])
    except Exception as E:
        return f'**Маэстро:** Ох! Кажется, произошла какая-то серьезная ошибка!\n```\nError of Mutation-State:\n{E}\n```'