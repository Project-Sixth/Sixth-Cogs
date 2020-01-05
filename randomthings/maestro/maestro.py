from re import sub as resub
from time import strftime
from random import choice
from os import listdir
from yaml import safe_load as yamlload

def maestro_replace(msg):
    library = yamlload(open('maestrolist.yaml', 'r'))

    def GetSpecificRandomItem(regexMatch):
        if regexMatch[1] in library:
            return choice(library[regexMatch[1]])
        return regexMatch[0]

    msg = resub('\[\[day\]\]', strftime("%d"), msg)
    msg = resub('\[\[month\]\]', strftime("%b"), msg)
    msg = resub('\[\[year\]\]', strftime("%Y"), msg)
    msg = resub('\[\[(\S+?)\]\]', GetSpecificRandomItem, msg)
    return msg