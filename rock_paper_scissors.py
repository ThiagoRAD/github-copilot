"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random
import sys

def play_round():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Enter a choice (r for rock, p for paper, s for scissors) or 'quit' to exit: ").lower()
    if player_choice == 'r':
        player_choice = 'rock'
    elif player_choice == 'p':
        player_choice = 'paper'
    elif player_choice == 's':
        player_choice = 'scissors'

    if player_choice == "quit":
        sys.exit("Thanks for playing!")

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")


# --- Simple Tkinter GUI for Rock Paper Scissors ---
import tkinter as tk
from tkinter import messagebox

class RPSGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0

        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors:")
        self.label.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.score_label = tk.Label(master, text=self.get_score_text())
        self.score_label.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()
        for choice in self.choices:
            btn = tk.Button(self.button_frame, text=choice.capitalize(), width=10,
                            command=lambda c=choice: self.play_round(c))
            btn.pack(side=tk.LEFT, padx=5, pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def get_score_text(self):
        return f"Player: {self.player_score}  Computer: {self.computer_score}  Ties: {self.tie_score}"

    def play_round(self, player_choice):
        computer_choice = random.choice(self.choices)
        if player_choice == computer_choice:
            result = "It's a tie!"
            self.tie_score += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.player_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1
        self.result_label.config(text=f"Computer chose: {computer_choice}. {result}")
        self.score_label.config(text=self.get_score_text())


if __name__ == "__main__":
    try:
        root = tk.Tk()
        game = RPSGame(root)
        root.mainloop()
    except Exception as e:
        print("Error starting GUI:", e)

# --- Original CLI version below ---
# while True:
#     play_round()
