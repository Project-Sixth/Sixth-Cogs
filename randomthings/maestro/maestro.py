"""
Module, that exists just for getting the Maestro functions
and imports away from everything.
"""

from re import sub as resub
from time import strftime
from random import choice
from pathlib import Path
from yaml import safe_load as yamlload

def maestro_replace(msg):
    """Main function, that replaces [[tags]] inside message.

    Parameters
    ----------
    msg : String
        Input message, containing [[tags]]

    Returns
    -------
    String
        Output message, with all [[tags]] replaced, if possible
    """

    library = yamlload(open(Path(__file__).parent.resolve() / "maestrolist.yaml", 'r'))

    def tag_replacer(regex):
        if regex[1] in library:
            return choice(library[regex[1]])
        return regex[0]

    msg = resub('\[\[day\]\]', strftime("%d"), msg)
    msg = resub('\[\[month\]\]', strftime("%b"), msg)
    msg = resub('\[\[year\]\]', strftime("%Y"), msg)
    msg = resub('\[\[(\S+?)\]\]', tag_replacer, msg)
    return msg
