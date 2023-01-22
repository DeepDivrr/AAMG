import lightbulb
import scrython
import hikari
import nest_asyncio
import secrets
import deckManager

nest_asyncio.apply()

bot = lightbulb.BotApp(
    token=secrets.token()
)

@bot.command()
@lightbulb.option('name', 'Name of card')
@lightbulb.command('lookup', 'Looks up card details')
@lightbulb.implements(lightbulb.SlashCommand)
async def lookup(ctx):
    name = str(ctx.options.name)

    try:
        card = getCard(name)
    except scrython.foundation.ScryfallError:
        await ctx.respond("Your query wasn't good enough for me. Try harder.")

    image = card.image_uris().get('png')
    await ctx.respond(image)


@bot.command()
@lightbulb.option('name', 'Name of card')
@lightbulb.command('lookup', 'Looks up card details')
@lightbulb.implements(lightbulb.SlashCommand)
async def lookup(ctx):
    name = str(ctx.options.name)

    try:
        card = scrython.cards.Named(fuzzy=name)
    except scrython.foundation.ScryfallError:
        await ctx.respond("Your query wasn't good enough for me. Try harder.")

    image = card.image_uris().get('png')
    await ctx.respond(image)

@bot.command()
@lightbulb.command('Deck', 'For deck management')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def deck():
    pass

@deck.child
@lightbulb.command('Add', 'Add a new deck to your list')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def deckAdd():
    pass

@deck.child
@lightbulb.command('List', 'List all of your decks')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def deckAdd():
    pass

@deck.child
@lightbulb.command('Remove', 'Remove a deck from your list')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def deckAdd():
    pass


bot.run()