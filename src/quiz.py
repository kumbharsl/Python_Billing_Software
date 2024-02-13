import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Quiz App")
        self.geometry("300x600")
        
        self.current_question = 0
        self.score = 0
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Jupiter"
            },
            {
                "question": "Which language used in flutter frameWork",
                "options": ["Dart", "Go", "Roby", "c"],
                "correct_answer": "Dart"
            },
            # Add more questions here
        ],
        
        self.label_question = tk.Label(self, text="")
        self.label_question.pack()
        
        self.radio_var = tk.StringVar()
        self.radio_var.set(None)
        
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.radio_var, value=i)
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)
        
        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack()
        
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.label_question.config(text=q["question"])
            for i, rb in enumerate(self.radio_buttons):
                rb.config(text=q["options"][i])
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
            self.destroy()
    
    def next_question(self):
        if self.radio_var.get() is not None:
            q = self.questions[self.current_question]
            if q["options"][int(self.radio_var.get())] == q["correct_answer"]:
                self.score += 1
            self.current_question += 1
            self.radio_var.set(None)
            self.show_question()
        else:
            messagebox.showwarning("Select an Option", "Please select an option before proceeding.")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
