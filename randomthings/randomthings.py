from random import randint,choice
from redbot.core import commands

class RandomThings(commands.Cog):
    """
    DnD game-like functions just for you!
    """

    @commands.group()
    async def randomthings(self, ctx):
        """All random generators from RandomThings is here!"""
        pass

    @randomthings.command()
    async def dayplopyname(self, ctx):
        """
        Create a random Day Plopy name. Using RUssian language.
        """
        S = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
        G = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
        if choice([2, 3]) == 2:
            if choice([1, 2]) == 1:
                R = choice(S).upper() + choice(G)
            else:
                R = choice(G).upper() + choice(S)
        else:
            R = choice(S).upper + choice(G) + choice(S)
        await ctx.send("Случайное имя Дневного Плопи: {}.".format(R+"-"+R))
    
    @randomthings.command()
    async def dayplopynameen(self, ctx):
        """
        Create a random Day Plopy name. Using ENglish language.
        """
        S = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        G = ['a', 'e', 'i', 'o', 'u']
        if choice([2, 3]) == 2:
            if choice([1, 2]) == 1:
                R = choice(S).upper() + choice(G)
            else:
                R = choice(G).upper() + choice(S)
        else:
            R = choice(S).upper + choice(G) + choice(S)
        await ctx.send("Random name of Day Plopy: {}.".format(R+"-"+R))
