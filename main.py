import lightbulb
import scrython
import hikari
import nest_asyncio
import private
import deckManager
import os

nest_asyncio.apply()

bot = lightbulb.BotApp(
    token=private.token()
)

# Help
@bot.command()
@lightbulb.command('help', 'List all commands and a description of each')
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    pass

# lookup
@bot.command()
@lightbulb.option('name', 'Name of card')
@lightbulb.command('lookup', 'Looks up card details')
@lightbulb.implements(lightbulb.SlashCommand)
async def lookup(ctx):
    name = str(ctx.options.name)
    try:
        card = scrython.cards.Named(fuzzy=name)
        image = card.image_uris().get('png')
        await ctx.respond(image)
    except scrython.foundation.ScryfallError:
        await ctx.respond("Your query wasn't good enough for me. Try harder.")

# Deck management
@bot.command()
@lightbulb.command('deck', 'For deck management')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def deck(ctx):
    pass

@deck.child
@lightbulb.option('file', '.txt attachment file', type=hikari.Attachment)
@lightbulb.command('add', 'Add a new deck to your list')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def deckAdd(ctx):
    # Create user directory
    userid = ctx.author.id
    filename = ctx.options.file.filename

    user_dir = f"Decks/{userid}"
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    
    await ctx.options.file.save(f"Decks/{userid}", force=True)

    # Check that the file is .txt
    _, ext = os.path.splitext(filename)
    if ext != '.txt':
        await ctx.respond("File should be .txt format")
    
    await ctx.respond("Success! Here is your decklist:")

    deckTuple = deckManager.txtToTuple(f"Decks/{userid}/{filename}")
    embed = hikari.Embed(
            title=f"{filename}",
            color=ctx.author.accent_color
        )

    embed.set_author(
        name=ctx.author.username,
        icon =ctx.author.avatar_url
    )
    
    for i in range(0, len(deckTuple), 10):
        chunk=tuple(deckTuple[i:i+10])
        embed.add_field(
            name=f'{i}',
            value="\n".join(chunk), 
            inline=True
        )

    await ctx.respond(embed=embed)
     

@deck.child
@lightbulb.command('list', 'List all of your decks')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def deckList(ctx):
    userid = ctx.author.id
    user_dir = f'Decks/{userid}'
    decklist = []
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    
    for entry in os.listdir(user_dir):
        _, ext = os.path.splitext(entry)
        if os.path.isfile(os.path.join(user_dir, entry)) and ext==".txt":
            decklist.append(entry)
    
    embed = hikari.Embed(
        title="Decklist"
    )
    embed.set_author(
        name=ctx.author.username,
        icon =ctx.author.avatar_url
    )

    for i in range(0, len(decklist), 10):
        chunk=tuple(decklist[i:i+10])
        embed.add_field(
            name=f'Chunk {i/10 +1}',
            value="\n".join(chunk), 
            inline=True
        )
    await ctx.respond(embed=embed)



@deck.child
@lightbulb.option('name', 'exact name of deck')
@lightbulb.command('remove', 'Remove a deck from your list')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def deckRemove(ctx):
    userid = ctx.author.id
    filename = ctx.options.name
    path = f"Decks/{userid}/{filename}"
    if os.path.isfile(path):
        os.remove(path)
        await ctx.respond(f"File {filename} removed from user {ctx.author.username}'s directory.")
    else:
        await ctx.respond(f"File {filename} not found in user {ctx.author.username}'s directory.")

@bot.command()
@lightbulb.command('game', 'For running a game')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def game():
    pass

@game.child
@lightbulb.option('deckname', 'Just the exact name')
@lightbulb.command('start', 'Choose a deck to play with')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def gameStart():
    pass
    

@game.child
@lightbulb.option('number', 'Number of cards to draw')
@lightbulb.command('draw', 'Draw a number of cards')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def gameDraw():
    pass


bot.run()