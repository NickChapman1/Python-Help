import html
class QuizBrain:

    # use the output arrow to notify output and after colon for type hint.
    def __init__(self, q_list: str) -> str:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text}"
        else:
            return None

    # def next_question(self): #Need to change this from manual input.
    #     self.current_question = self.question_list[self.question_number]
    #     self.question_number += 1
    #     user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
    #     self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

