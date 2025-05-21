##make this ask the questions
#Check if the answer was correct
#chcek if were at the end of the quiz.
#class will have two attributes question number default 0 and question list. will pass over the bank into the list
#Question number should keep track of which question the user is on to go through the list
#Method as well called next_question() ,in final veriosn it does display the question number.
#from main import question_bank
from tabnanny import check
import random

#question_list = question_bank

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.random_number = random.choice(self.number_list)
        self.random_question = ""
        self.question_list = q_list
        self.score = 0

    def is_still_question(self):
       ## test = self.question_number < len(self.question_list)
        ##print(f"{test}")
        return self.question_number < len(self.question_list)

    def next_question(self):
        #set current question equal to the question list indexed to the question num all self
        current_question = self.question_list[self.question_number]
        #increment question num
        self.question_number += 1
    # self.random_question = random.choice(self.question_list[self.random_number])
       # print(f"{self.random_question}")
        #set user answer to input
        user_answer = input(f"Current score {self.score} out of {len(self.question_list)}...you're on question #{self.question_number}.."
                            f" {current_question.question} Is this true or false??").lower()
        #call to the self check answer funtion and pass the user answer and current question.answer]
        self.check_answer(current_question.answer, user_answer)
        return

    def check_answer(self, answer, user_answer):
        if answer.lower() != user_answer.lower():
            print(f"\nYou we're incorrect fool. You've now lost. You had a score of {self.score}\n")
            print("\n" * 6)
            #exit()

        else:
            self.score += 1
            print(f"\nBravo yous right! Well done, that puts your score at {self.score}")
            print("\n" * 6)
            #self.next_question()
