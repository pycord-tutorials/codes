import discord

client = discord.Bot(debug_guilds=[...]) # Replace the three dots with your test server ID.
                                         # If you want to have commands on multiple servers, separate the IDs with commas.

@client.event
async def on_ready():
    print(f"{client.user} is online | Watching {len(client.guilds)} servers")

@client.slash_command(description="Say hello")
async def hi(ctx):
    await ctx.respond(f"Hello {ctx.author.name}!", ephemeral=True)

client.run("...") # Replace the three dots with your bot's token.