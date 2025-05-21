##make a question class that has text and answer as attributes. Needs to initalize each time. Then
##constructor code will take those pieces of data and add them. use init method to initalize two attributs
from quiz_brain import QuizBrain
from data import question_data
from question_model import Question
import random

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer) #call to question function in question_model
    question_bank.append(new_question)

#random.shuffle(question_bank)  #This makes it random!
Quizbrain_constructor = QuizBrain(question_bank)


while Quizbrain_constructor.is_still_question():
    Quizbrain_constructor.next_question()

print(f"You've completed the game! Witha score of: {Quizbrain_constructor.score}")

#bring up a question and ask user to answer it.
# For all quiz functionality add in quiz brain