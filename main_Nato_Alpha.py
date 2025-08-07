##I ran the below version I made through AI with some request, building off that
import pandas

# Read the CSV file correctly
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create the dictionary: {"A": "Alfa", "B": "Bravo"}
Alpha_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print("Phonetic Alphabet Dictionary:", Alpha_dict)

# Function to get user input and convert to phonetic code
def call_word():
    # Get user input and convert to uppercase
    word = input("What's the code word? ").upper()

    # Create a list of phonetic code words
    list_of_code_words = [Alpha_dict.get(letter, "?") for letter in word]
    print("Phonetic Code List:", list_of_code_words)

    # Optional: Join into a single string if needed
    final_answer = ' '.join(list_of_code_words)
    print("Final Answer:", final_answer)

# Loop to allow restarting based on yes/no input
while True:
    call_word()
    again = input("Do you want to try another word? (yes/no): ").strip().lower()
    if again.startswith("y"):
        continue
    elif again.startswith("n"):
        print("Goodbye!")
        break
    else:
        print("Didn't catch that, but let's stop here. 👋")
        break








# #________________________________
# #Original Version Below
# #take csv of nato phonetic alpha and create a formatted dictionary key actual letter, value is coresponding code word.
# #create a list of the phonetic code words from a word that the user inputs
# #add a run again option
# import pandas
#
# def call_word():
#     the_data = pandas.read_csv("nato_phonetic_alphabet.csv")
#     nato_data_frame = pandas.DataFrame(the_data)
#     # TODO 1. Create a dictionary in this format:
#     # {"A": "Alfa", "B": "Bravo"}
#     Alpha_dict = dict(zip(nato_data_frame.letter, nato_data_frame.code))
#     # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#     word = input("Whats the code word?").upper()
#     # #create a list of phonetic code words
#     list_of_code_words = [Alpha_dict.get(letter, "") for letter in word]
#     print("Phonetic Code List:", list_of_code_words)
#     game_is_on = False
#
#
#
# game_is_on = True
#call_word()
# while game_is_on:
#     restart = input("Would You like to go again? Enter yes or no:").title()
#     if restart.lower() in ["yes", "y"]:
#         call_word()
#     else:
#       game_is_on = False
#
# # list_of_code_letters = [letter for letter in word]
#Below would be the same result
# list_of_code_letters = []
# for letter in word:
#     list_of_code_letters.append(letter)

# # print(list_of_code_letters)
# # final_answer = ''.join([Alpha_dict.get(c, word) for c in word])
# # print(final_answer)