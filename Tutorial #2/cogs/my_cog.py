import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Get the ID of a user")
    async def id(self, ctx, user: Option(discord.User, "User", required=False)):
        user = user or ctx.author
        await ctx.respond(f"The ID of {user} is {user.id}")

def setup(client):
    client.add_cog(Cog(client))