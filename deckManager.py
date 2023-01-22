def txtToTuple(filepath):
    with open(filepath, 'r') as file:
        cardLines = filter(None, file.read().splitlines()) 
        deckTuple = []
        for card in cardLines:
            frequency = int(card.split()[0])
            card_name = " ".join(card.split()[1:])
            deckTuple.extend([card_name]*frequency)
    return deckTuple