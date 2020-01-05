from random import randint,choice
from redbot.core import commands

from .minlai import *

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
        await ctx.send("Случайное имя Дневного Плопи: {}.".format(generate_dayplopyname()))

    @randomthings.command()
    async def dayplopynameen(self, ctx):
        """
        Create a random Day Plopy name. Using ENglish language.
        """
        await ctx.send("Random name of Day Plopy: {}.".format(generate_dayplopyname_english()))
