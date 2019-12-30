from random import randint
from redbot.core import commands

class Dnd(commands.Cog):
    """
    DnD game-like functions just for you!
    """

    async def dndrolld(self, ctx, roll):
        """
        Roll an DX dice
        The result will be between 1 and X.
        """
        await ctx.send("{author.mention} бросил :game_die: D{d}. Результат: {n}".format(author=ctx.author, n=randint(1, roll), d=roll))

    @commands.command()
    async def dndrolld4(self, ctx):
        """
        Roll an D4 dice
        The result will be between 1 and 4.
        """
        await self.dndrolld(ctx, 4)

    @commands.command()
    async def dndrolld6(self, ctx):
        """
        Roll an D6 dice
        The result will be between 1 and 6.
        """
        await self.dndrolld(ctx, 6)

    @commands.command()
    async def dndrolld8(self, ctx):
        """
        Roll an D8 dice
        The result will be between 1 and 8.
        """
        await self.dndrolld(ctx, 8)
    
    @commands.command()
    async def dndrolld10(self, ctx):
        """
        Roll an D8 dice
        The result will be between 1 and 10.
        """
        await self.dndrolld(ctx, 10)
    
    @commands.command()
    async def dndrolld12(self, ctx):
        """
        Roll an D12 dice
        The result will be between 1 and 12.
        """
        await self.dndrolld(ctx, 12)
    
    @commands.command()
    async def dndrolld20(self, ctx):
        """
        Roll an D20 dice
        The result will be between 1 and 20.
        """
        await self.dndrolld(ctx, 20)
    
    @commands.command()
    async def dndrolld100(self, ctx):
        """
        Roll an D100 dice
        The result will be between 1 and 100.
        """
        await self.dndrolld(ctx, 100)
    
    @commands.command()
    async def dndroll3d6(self, ctx):
        """
        Roll an 3D6 dice
        The result will be between 3 and 18.
        """
        num1, num2, num3 = randint(1, 6), randint(1, 6), randint(1, 6)
        await ctx.send("{author.mention} бросил :game_die::game_die::game_die: 3D6. Результат: {n1}, {n2}, {n3} += **{r1}**".format(author=ctx.author, n1=num1, n2=num2, n3=num3, r1=num1+num2+num3))