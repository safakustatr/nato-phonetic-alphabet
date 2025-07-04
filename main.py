import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

program_on = True

while program_on:
    try:
        word = input("Enter a word: ").upper()
        output = [alphabet_dict[letter] for letter in word]
        print(output)
        choice = input("Do you wish to continue? (y/n): ").lower()
        if choice == "n":
            program_on = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
