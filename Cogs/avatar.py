import discord
import asyncio
from discord.ext import commands


class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def avatar(self, ctx, member : discord.Member = None):

        if member is None:
            embed=discord.Embed(title="<:error:909515248833294336> CHYBA!", color=0xff1c21)
            embed.add_field(name="CHYBÍ ARGUMENT!", value="Chybějící argument: **user.Mention**")
            embed.set_footer(text="© WooxBot 2021")
            await ctx.send(embed=embed)
            return

        else:
            embed2 = discord.Embed(title=f"Avatar uživatele {member} !", colour=0x0000ff, timestamp=ctx.message.created_at)
            embed2.add_field(name="Animovaný?", value=member.is_avatar_animated())
            embed2.set_image(url=member.avatar_url)
            await ctx.send(embed=embed2)



def setup(bot):
    bot.add_cog(avatar(bot))