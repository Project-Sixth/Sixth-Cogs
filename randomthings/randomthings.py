"""
Project: Sixth module for doing random stuff
"""

import os
from redbot.core import commands

# from .generators.minlaigen import generate_dayplopyname_russian, generate_dayplopyname_english, generate_shadowdayplopyname_russian, generate_shadowdayplopyname_english
# from .generators.starnamegen import generate_starname_russian, generate_starname_english
# from .generators.planetnamegen import generate_planetname_russian, generate_planetname_english
# from .generators.sylphnamegen import generate_sylphname_russian, generate_sylphname_english
from .maestro import load as MAEload
from .maestro import say as MAEsay

class RandomThings(commands.Cog):
    """
    A random things... a lot of them - just for you.
    """

    @commands.group()
    async def maestro(self, ctx):
        """
        The Great One. The Mad One. The Best One.
        """
        pass

    @maestro.command()
    async def say(self, ctx, text):
        """
        Make an improvised text, still, random. / Перечислить все доступные YML-файлы сценариев.
        """
        await ctx.send(MAEsay(text))

    @maestro.command()
    async def load(self, ctx, scenario_name):
        """
        Load a YML-file of scenario. / Загрузить YML-файл сценария.
        """
        await ctx.send(MAEload(scenario_name))
    
    @maestro.command()
    async def list_scenarios(self, ctx):
        """
        List all available YML-scenarios. / Перечислить все доступные YML-файлы сценариев.
        """
        grep = os.listdir(f'{str(__file__)[:-16]}/gens')
        scenarios = []
        for g in grep:
            if g.endswith('.yml'):
                scenarios.append(f'`{g[:-4]}`')
        await ctx.send(f'**Маэстро: Я имею следующий список загруженных сценариев:\n{', '.join(scenarios)}')
    
    @maestro.command()
    async def list_libraries(self, ctx):
        """
        List all available YML-libraries. / Перечислить все доступные YML-файлы библиотек.
        """
        grep = os.listdir(f'{str(__file__)[:-16]}/libs')
        libs = []
        for g in grep:
            if g.endswith('.yml'):
                libs.append(f'`{g[:-4]}`')
        await ctx.send(f'**Маэстро: Я имею следующий список загруженных библиотек:\n{', '.join(libs)}')

#     @randomthings.command()
#     async def starname(self, ctx):
#         """
#         Создать название случайной звезды на русском языке.
#         """
#         await ctx.send("Случайная звезда: {}.".format(generate_starname_russian()))

#     @randomthings.command()
#     async def starnameen(self, ctx):
#         """
#         Create a random star name on English Language
#         """
#         await ctx.send("Random star name: {}.".format(generate_starname_english()))

#     @randomthings.command()
#     async def planetname(self, ctx):
#         """
#         Создать название случайной планеты на русском языке.
#         """
#         await ctx.send("Случайная планета: {}.".format(generate_planetname_russian()))

#     @randomthings.command()
#     async def planetnameen(self, ctx):
#         """
#         Create a random planet name on English Language
#         """
#         await ctx.send("Random planet name: {}.".format(generate_planetname_english()))

#     @randomthings.command()
#     async def sylphname(self, ctx):
#         """
#         Создать название случайного сильфа на русском языке.
#         """
#         await ctx.send("Случайный сильф: {}.".format(generate_sylphname_russian()))

#     @randomthings.command()
#     async def sylphnameen(self, ctx):
#         """
#         Create a random sylph name on English Language
#         """
#         await ctx.send("Random sylph name: {}.".format(generate_sylphname_english()))

#     @randomthings.command()
#     async def dayplopyname(self, ctx):
#         """
#         Создать имя случайного Дневного Плопи на русском языке.
#         Имена Дневных Плопи состоят из 2-3 букв, формирующих слог,
#         который повторяется сам с собой через дефис.
#         """
#         await ctx.send("Случайное имя Дневного Плопи: {}.".format(generate_dayplopyname_russian()))

#     @randomthings.command()
#     async def dayplopynameen(self, ctx):
#         """
#         Create a random Day Plopy name. Using ENglish language.
#         Day Plopies have name consisting of 2-3 letters,
#         forming a syllable, that is repeated 2 times, divided by dash.
#         """
#         await ctx.send("Random name of Day Plopy: {}.".format(generate_dayplopyname_english()))

#     @randomthings.command()
#     async def shadowdayplopyname(self, ctx):
#         """
#         Создать имя случайного Тень-Дневного Плопи на русском языке.
#         Имена Дневных Плопи состоят из 2-3 букв, формирующих слог,
#         который повторяется сам с собой через дефис.
#         """
#         await ctx.send("Случайное имя Тень-Дневного Плопи: {}.".format(generate_shadowdayplopyname_russian()))

#     @randomthings.command()
#     async def shadowdayplopynameen(self, ctx):
#         """
#         Create a random Shadow-Day Plopy name. Using ENglish language.
#         Day Plopies have name consisting of 2-3 letters, forming a syllable,
#         that is repeated 2 times, divided by dash.
#         """
#         await ctx.send("Random name of Shadow-Day Plopy: {}.".format(generate_shadowdayplopyname_english()))

#     @randomthings.command()
#     async def nightplopyname(self, ctx):
#         """
#         Создать имя случайного Ночного Плопи на русском языке.
#         Ночные Плопи имеют имена, которые связаны с названиями небесных тел,
#         событий и космосом впринципе.
#         """
#         r = choice([generate_planetname_russian, generate_starname_russian, generate_sylphname_russian])
#         await ctx.send("Случайное имя Ночного Плопи: {}.".format(r()))

#     @randomthings.command()
#     async def nightplopynameen(self, ctx):
#         """
#         Create a random Night Plopy name. Using ENglish language.
#         Night Plopies usually have names that somehow connected to stars or cosmos.
#         """
#         r = choice([generate_planetname_english, generate_starname_english, generate_sylphname_english])
#         await ctx.send("Random name of Night Plopy: {}.".format(r()))

# # ====== MAESTRO ======
#     @randomthings.command()
#     async def maestro(self, ctx, *, msg: str):
#         """
#         Пробудить безумного Маэстро!
#         """
#         await ctx.send("**Маэстро**: {}".format(maestro_replace(msg)))
