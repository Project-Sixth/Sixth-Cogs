from random import randint,choice
from redbot.core import commands

from .minlai import *
from .starnamegen import *

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
        await ctx.send("Случайное имя Ночного Плопи: {}.".format(generate_starname_english()))

    @randomthings.command()
    async def nightplopynameen(self, ctx):
        """
        Create a random Night Plopy name. Using ENglish language.
        Night Plopies usually have names that somehow connected to stars or cosmos.
        """
        await ctx.send("Random name of Night Plopy: {}.".format(generate_starname_english()))
