##################### Normal Starting Project #####################
import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "Your email"
password = "Your pw"


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
now = dt.datetime.now()
date_tuple = (now.month, now.day)
Letter_paths =["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

df_bday = pd.read_csv("birthdays.csv") #This is now a dataframe
print(df_bday)
#Use dictionary comprehension to create a dictionary
birthday_dic = {
    (row["month"], row["day"]): row
    for anything, row in df_bday.iterrows()
}
print(birthday_dic)
#compare and see if today's month/day tuple matches
if (date_tuple) in birthday_dic:
    birthday_person= birthday_dic[date_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]
    print(f"Made it here {name}, {email}")
    #if match, pick a random letter(letter_1.txt / letter_2.txt / letter_3.txt)
    LetterChoice = random.choice(Letter_paths)
    print(LetterChoice)
    # from letter_templates and replace the[NAME] with the person's actual name
    with open(LetterChoice, "r") as file:
        letter_contents = file.read()
        #Replace the actual name
        PersonalizedLetter = letter_contents.replace("[NAME]", name)
        print(PersonalizedLetter)
    # from birthdays.csv Think about the relative file path to open each letter.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Happy birthday!\n\n{PersonalizedLetter}"
        )






    # with open("quotes.txt", "r", encoding="utf-8") as qoute_file:
    #     all_qoutes = qoute_file.readlines()
        # qoute = random.choice(all_qoutes)
        # #Qoute needed to be sanitized before sending, it removes non ascii chars
        # qoute = qoute.encode("ascii", "ignore").decode("ascii")
# HINT 2: Use pandas to read the birthdays.csv


#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



