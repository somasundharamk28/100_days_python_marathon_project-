

import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
user_input = input("Enter a word").upper()

final_output = [new_dict[letter] for letter in user_input]
print(final_output)


