from tkinter import *

THEME_COLOR = "#375362"
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"


class QuizInterface:

    def __init__(self, quiz_brain):
    #Make all buttons and layouts of the UI
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20)
        #Set up a smaller box on the rectangle. You do self. canvas to add a canvas.
        self.canvas = Canvas(width=400, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Draw a smaller square
        self.canvas.create_rectangle(50, 50, 300, 225, fill="white", outline="black")
        #Add text
        self.question_text = self.canvas.create_text(175, 140, width=250, text="", font=(FONT_NAME, 12, "italic"), fill="black")

    # buttons: All these need to be created outside of the functions so they don't die with them.
        know_it_pic = PhotoImage(file="images/true.png")
        dont_know_pic = PhotoImage(file="images/false.png")
        check_but = Button(image=know_it_pic, highlightthickness=0, command=self.true_pressed)
        check_but.grid(column=0, row=1)
        x_but = Button(image=dont_know_pic, highlightthickness=0, command=self.false_pressed)
        x_but.grid(column=1, row=1)

        #Keeps program running. Never ending while loop for the GUI, will get confused if another while loop is near it.
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")


    def true_pressed(self):
        self.quiz.check_answer("True")
        self.get_next_question()


    def false_pressed(self):
        self.quiz.check_answer("False")
        self.get_next_question()
