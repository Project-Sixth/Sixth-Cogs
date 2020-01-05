from random import randint,choice
from redbot.core import commands

from .minlai import *
from .starnamegen import *
from .planetnamegen import *

class RandomThings(commands.Cog):
    """
    DnD game-like functions just for you!
    """

    @commands.group()
    async def randomthings(self, ctx):
        """All random generators from RandomThings is here!"""
        pass

    @randomthings.command()
    async def starname(self, ctx):
        """
        Создать название случайной звезды на русском языке.
        """
        await ctx.send("Случайная звезда: {}.".format(generate_starname_russian()))
    
    @randomthings.command()
    async def starnameen(self, ctx):
        """
        Create a random star name on English Language
        """
        await ctx.send("Random star name: {}.".format(generate_starname_english()))

    @randomthings.command()
    async def planetname(self, ctx):
        """
        Создать название случайной планеты на русском языке.
        """
        await ctx.send("Случайная планета: {}.".format(generate_planetname_russian()))
    
    @randomthings.command()
    async def planetnameen(self, ctx):
        """
        Create a random planet name on English Language
        """
        await ctx.send("Random planet name: {}.".format(generate_planetname_english()))

    @randomthings.command()
    async def dayplopyname(self, ctx):
        """
        Создать имя случайного Дневного Плопи на русском языке.
        Имена Дневных Плопи состоят из 2-3 букв, формирующих слог, который повторяется сам с собой через дефис.
        """
        await ctx.send("Случайное имя Дневного Плопи: {}.".format(generate_dayplopyname_russian()))

    @randomthings.command()
    async def dayplopynameen(self, ctx):
        """
        Create a random Day Plopy name. Using ENglish language.
        Day Plopies have name consisting of 2-3 letters, forming a syllable, that is repeated 2 times, divided by dash.
        """
        await ctx.send("Random name of Day Plopy: {}.".format(generate_dayplopyname_english()))

    @randomthings.command()
    async def nightplopyname(self, ctx):
        """
        Создать имя случайного Ночного Плопи на русском языке.
        Ночные Плопи имеют имена, которые связаны с названиями небесных тел, событий и космосом впринципе.
        """
        r = choice([generate_planetname_russian, generate_starname_russian])
        await ctx.send("Случайное имя Ночного Плопи: {}.".format(r()))

    @randomthings.command()
    async def nightplopynameen(self, ctx):
        """
        Create a random Night Plopy name. Using ENglish language.
        Night Plopies usually have names that somehow connected to stars or cosmos.
        """
        r = choice([generate_planetname_english, generate_starname_english])
        await ctx.send("Random name of Night Plopy: {}.".format(r()))
