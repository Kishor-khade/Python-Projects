from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg='#375362')

        self.score = Label(
            text='score : 0',
            font=('Monospace', 15, 'normal'),
            fg='white',
            bg='#375362'
        )
        self.score.grid(row=0, column=1, pady=10)

        self.canvas = Canvas(width=400, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            200, 100,
            width=300,
            text='What are you doing and how are you',
            font=('Arial', 17, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.right_img = PhotoImage(file='right.png')
        self.right = Button(image=self.right_img,
                            bg='#375362',
                            highlightthickness=0,
                            command=self.true)
        self.right.grid(row=2, column=1, pady=20, padx=20)

        self.wrong_png = PhotoImage(file='wrong.png')
        self.wrong = Button(image=self.wrong_png,
                            bg='#375362',
                            highlightthickness=0,
                            command=self.false)
        self.wrong.grid(row=2, column=0, pady=20, padx=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You have reached the end of the game.")
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
