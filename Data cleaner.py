import pandas as pd

file_name = "all_mtg_cards.csv"

data = pd.read_csv(file_name)
data.drop_duplicates(subset ="name", inplace = True) 
data.to_csv('data.csv')