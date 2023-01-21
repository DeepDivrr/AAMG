import lightbulb
import scrython
import hikari
import nest_asyncio

nest_asyncio.apply()

TOKEN='MTA2NjIwNjc5NjIxNTIyNjM2OQ.GwywTN.X2OPyB4C2yhlHWQcbp1fXxPCSCav9f-LOrfFm8'

bot = lightbulb.BotApp(
    token=TOKEN
)

def getCard(name):
    return scrython.cards.Named(fuzzy=name)

@bot.command()
@lightbulb.option('name', 'Name of card')
@lightbulb.command('lookup', 'Looks up card details')
@lightbulb.implements(lightbulb.SlashCommand)
async def lookup(ctx):
    name = str(ctx.options.name)

    try:
        card = getCard(name)
    except scrython.foundation.ScryfallError:
        await ctx.respond("Your query wasn't good enough.  You might need to refine your search.")

    image = card.image_uris().get('png')
    await ctx.respond(image)

bot.run()