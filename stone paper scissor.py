import tkinter as tk
import random
player_score = 0
computer_score = 0
choices = ["Stone", "Paper", "Scissors"]
def play_game(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)
    player_label.config(text=f"You: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    if player_choice == computer_choice:
        result_label.config(text="😐 DRAW!")
    elif (
        (player_choice == "Stone" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Stone")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="🎉 YOU WIN!")
        player_score += 1
    else:
        result_label.config(text="😂 COMPUTER WINS!")
        computer_score += 1
    score_label.config(
        text=f"🏆 You: {player_score}     Computer: {computer_score}"
    )
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_label.config(text="You: -")
    computer_label.config(text="Computer: -")
    result_label.config(text="🤔 Choose your weapon!")
    score_label.config(text="🏆 You: 0     Computer: 0")
window = tk.Tk()
window.title("😈 Stone Paper Scissors")
window.geometry("500x550")
window.resizable(False, False)
title = tk.Label(
    window,
    text="😈 STONE PAPER SCISSORS 😈",
    font=("Arial", 22, "bold")
)
title.pack(pady=25)
instruction = tk.Label(
    window,
    text="Choose your weapon!",
    font=("Arial", 14)
)
instruction.pack(pady=5)
button_frame = tk.Frame(window)
button_frame.pack(pady=25)
stone_button = tk.Button(
    button_frame,
    text="🪨 STONE",
    font=("Arial", 14, "bold"),
    width=12,
    command=lambda: play_game("Stone")
)
stone_button.grid(row=0, column=0, padx=8)
paper_button = tk.Button(
    button_frame,
    text="📄 PAPER",
    font=("Arial", 14, "bold"),
    width=12,
    command=lambda: play_game("Paper")
)
paper_button.grid(row=0, column=1, padx=8)
scissors_button = tk.Button(
    button_frame,
    text="✂️ SCISSORS",
    font=("Arial", 14, "bold"),
    width=12,
    command=lambda: play_game("Scissors")
)
scissors_button.grid(row=0, column=2, padx=8)
player_label = tk.Label(
    window,
    text="You: -",
    font=("Arial", 16, "bold")
)
player_label.pack(pady=10)
computer_label = tk.Label(
    window,
    text="Computer: -",
    font=("Arial", 16, "bold")
)
computer_label.pack(pady=10)
result_label = tk.Label(
    window,
    text="🤔 Choose your weapon!",
    font=("Arial", 20, "bold")
)
result_label.pack(pady=25)
score_label = tk.Label(
    window,
    text="🏆 You: 0     Computer: 0",
    font=("Arial", 15, "bold")
)
score_label.pack(pady=10)
reset_button = tk.Button(
    window,
    text="🔄 RESET GAME",
    font=("Arial", 13, "bold"),
    width=18,
    command=reset_game
)
reset_button.pack(pady=20)
window.mainloop()