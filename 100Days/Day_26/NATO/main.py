import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
CSV_data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_data = {row.letter: row.code for (index, row) in CSV_data.iterrows()}
# print(NATO_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [NATO_data[letter] for letter in word]
print(output_list)