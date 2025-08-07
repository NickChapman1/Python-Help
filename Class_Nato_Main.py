import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()

word_list = [phonetic_dict[letter] for letter in word]
print(word_list)
