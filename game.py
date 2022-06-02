import requests
import numpy as np


class Game:
    def __init__(self, amount: int, category="", difficulty="", ty=""):
        self.amount = amount
        self.category = category
        self.difficulty = difficulty
        self.ty = ty

    def set_parameters(self):
        """This function returns a dictionary with the query parameters required by the triviaApi"""
        return {
            "amount": self.amount,
            "category": self.category,
            "difficulty": self.difficulty,
            "type": self.ty
        }

    def display(self):
        """Display the list of questions"""
        for e in enumerate(self.questions.options):
            print(f"{e[0]}){e[1]}")


class Question:
    def __init__(self, question_num, api):
        self.answer = api.json()["results"][question_num]["correct_answer"]
        self.options = api.json()["results"][question_num]["incorrect_answers"]
        self.question = api.json()["results"][question_num]["question"]

    def shuffle(self):
        """shuffle the answer and the options list"""
        self.options.append(self.answer)
        np.random.shuffle(self.options)
        return self.options

    def check(self, player):
        """check whether the player input is correct or not"""
        while True:
            if -len(self.options) <= int(player) < len(self.options):
                if self.options[int(player)] == self.answer:
                    return True
                break
            else:
                player = input("value out of range please insert a value inside the range: ")


# to-do: print the instructions of the game and ask for some configurations
# Welcome to this trivia game!

# It's pretty straight-forward, so I will just ask you a few questions.

# Do you want to play a random subject, yes (y) or not (n)?

# if not(display list of subjects)

# Do you want a determinate number of questions to answer yes (y) or no (n)?

# if(how many questions do you want to be ask?)
# categories = {"9": "General Knowledge",
#              "10": "Entertainment: Books",
#              "11": "Entertainment: Film",
#              "12": "Entertainment: Music",
#              "13": "Entertainment: Musicals & Theatres",
#              "14": ""}

# def instructions():
#    "code to give some instructions to the user, not going to use it in this version..."
#    category = ""
#    print("Welcome to this trivia game!\nIt's pretty straight-forward, so I will ask you a few questions.")
#    player = input("Do you want to play a random subject, yes (y) or not (n)?")
#    if player == "not" or "n":
#        print("Choose a category:\n ")
#        category = input()

if __name__ == '__main__':
    pass
