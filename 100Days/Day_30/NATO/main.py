import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
CSV_data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_data = {row.letter: row.code for (index, row) in CSV_data.iterrows()}
# print(NATO_data)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [NATO_data[letter] for letter in word]
    except:
        print("Sorry, only letters in the Alphabets please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()