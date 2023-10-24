import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question_index = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Paris", "Madrid", "Rome"],
                "correct_answer": "Paris",
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_answer": "Mars",
            },
            # Add more questions here
        ]

        self.label_question = tk.Label(root, text="", font=("Helvetica", 16))
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_btn = tk.Radiobutton(root, text="", variable=self.radio_var, value="", command=self.submit_answer)
            radio_btn.pack(anchor=tk.W)
            self.radio_buttons.append(radio_btn)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option, value=option)

            self.radio_var.set(None)
        else:
            self.show_final_results()

    def submit_answer(self):
        user_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question_index]["correct_answer"]

        if user_answer == correct_answer:
            self.score += 1

        feedback = "Correct!" if user_answer == correct_answer else f"Incorrect. The correct answer is {correct_answer}."
        messagebox.showinfo("Feedback", feedback)

    def next_question(self):
        self.current_question_index += 1
        self.load_question()

    def show_final_results(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(self.questions)}")
        self.root.destroy()  # Close the window after the quiz is completed

if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
