import json

class flashcaards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display(self):
        print(self.question, self.answer)

t_or_s = input("teacher mode or student mode (enter t or s): ")
if t_or_s == "t":
    print("u are now in teacher mode")
    input_ques = input("enter question: ")
    input_ans = input("enter answer to the question: ")
    