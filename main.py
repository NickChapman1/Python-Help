import os

names_path = "../__MACOSX/Mail Merge Project Start/Input/Names/._invited_names.txt"
letter_template_path = "Input/Letters/starting_letter.txt"
output_dir = "Output/ReadyToSend"

#make sure directory exists
os.makedirs(output_dir, exist_ok=True)

#load in names
with open(names_path, "r") as names_file:
    names = [name.strip() for name in names_file.readlines()]

#load letter template
with open(letter_template_path, "r") as letter_file:
    letter_template = letter_file.read()

#create personalized Letters
for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    output_path = os.path.join(output_dir, f"{name}_letter.txt")
    with open(output_path, "w") as output_file:
        output_file.write(personalized_letter)




# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# def load_content():
#     #path = os.p ath.join(BASE_DIR, HIGH_SCORE_FILE)
#     path = ""
#     if os.path.exists(path):
#         with open(path, "r") as file:
#             content = file.read()
#             return content
#
# names = load_content()
# print(load_content())
# #Yeah load letter or the names, put it into a variable. Then do a write to
# #letter and input it into the other letter.
#
# def merge_letter_content():
#     path = os.path.join()
#     with open(f"{path}", "w") as file: #"a" wouldve been for append.
#         for name in names:
#             file.write(str())

#C:\Users\nchapman\PycharmProjects\day_24\Mail+Merge+Project+Start\__MACOSX\Mail Merge Project Start\Input\Names
#f = open("../__MACOSX/Mail Merge Project Start/Input/Names/._invited_names.txt")
#print(f.readlines())