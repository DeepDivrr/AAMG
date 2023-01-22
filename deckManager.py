import os

def txtToTuple(filepath):
    _, ext = os.path.splitext(filepath)
    if ext != '.txt':
        raise ValueError("File should be .txt format")
    with open(filepath, 'r') as file:
        cardLines = filter(None, file.read().splitlines()) 
        deckTuple = [line[2:] for line in cardLines for _ in range(int(line[0]))]
    return deckTuple




            


print(txtToTuple('Decks/Grixis Midrange.txt'))