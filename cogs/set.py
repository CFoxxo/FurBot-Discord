import discord
from discord.ext import commands
from configparser import SafeConfigParser

parser = SafeConfigParser()

class set:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def set(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid setting command!')

    @set.command(name="osu")
    async def _osu(self, ctx, *arg):
        args = ' '.join(arg)
        username = str(args)
        userid = ctx.message.author.id
        parser.add_section(str(userid))
        parser.set(str(userid), "osu_username", username)
        with open('user.ini', 'w') as configfile:
            parser.write(configfile)
        await ctx.send("Set osu! username to: {}".format(username))

def setup(bot):
    bot.add_cog(set(bot))