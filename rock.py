import tkinter as tk
from tkinter import messagebox
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
score_player = 0
score_computer = 0

def play(choice):
    global score_player, score_computer

    computer_choice = random.choice(choices)

    if choice == computer_choice:
        result = "It's a Draw!"
        color = "#00F9FF"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! {choice} beats {computer_choice}"
        score_player += 1
        color = "#39FF14"
    else:
        result = f"You Lose! {computer_choice} beats {choice}"
        score_computer += 1
        color = "#FF3131"

    result_label.config(text=result, fg=color)
    update_scoreboard()

    # Check for match win (best of 5 → first to 3)
    if score_player == 3 or score_computer == 3:
        winner = "YOU" if score_player == 3 else "COMPUTER"
        show_congratulations(winner)

def update_scoreboard():
    score_label.config(text=f"Score - You: {score_player}   Computer: {score_computer}")

def reset_game():
    global score_player, score_computer
    score_player = 0
    score_computer = 0
    update_scoreboard()
    result_label.config(text="Make your move!", fg="#FF10F0")

def show_congratulations(winner):
    congrats_label = tk.Label(root, text=f"🏆 {winner} Wins the Match! 🏆",
                              font=("Consolas", 22, "bold"), bg="black", fg="#FF10F0")
    congrats_label.place(relx=0.5, rely=0.4, anchor="center")

    emojis = ["🎉", "✨", "🔥", "🎊"]
    confetti_labels = []
    for i in range(15):
        lbl = tk.Label(root, text=random.choice(emojis), font=("Arial", 20), bg="black")
        lbl.place(x=random.randint(50, 400), y=-30)
        confetti_labels.append(lbl)

    def animate(count=0):
        colors = ["#FF10F0", "#39FF14", "#00F9FF", "#FFD300"]
        congrats_label.config(fg=colors[count % len(colors)])
        root.configure(bg=colors[(count + 1) % len(colors)])

        for lbl in confetti_labels:
            x, y = lbl.winfo_x(), lbl.winfo_y()
            if y < 300:
                lbl.place(x=x, y=y+15)
            else:
                lbl.place_forget()

        if count < 20:
            root.after(200, animate, count+1)
        else:
            root.configure(bg="black")
            congrats_label.destroy()
            for lbl in confetti_labels:
                lbl.destroy()
            messagebox.showinfo("🏆 Match Over!", f"🎉 {winner} wins the MATCH! 🎉")
            reset_game()

    animate()

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="black")

# Title
title_label = tk.Label(root, text="ROCK PAPER SCISSORS", font=("Consolas", 20, "bold"),
                       bg="black", fg="#FFD300")
title_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Make your move!", font=("Consolas", 16, "bold"),
                        bg="black", fg="#FF10F0")
result_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

for choice in choices:
    btn = tk.Button(button_frame, text=choice, font=("Consolas", 16, "bold"),
                    width=10, bg="black", fg="#00FFEF", activeforeground="#39FF14",
                    highlightbackground="#FF10F0", highlightthickness=2,
                    command=lambda c=choice: play(c))
    btn.pack(side="left", padx=10)

# Scoreboard
score_label = tk.Label(root, text=f"Score - You: {score_player}   Computer: {score_computer}",
                       font=("Consolas", 16, "bold"), bg="black", fg="#FFD300")
score_label.pack(pady=10)

# Reset button
reset_btn = tk.Button(root, text="RESET GAME", font=("Consolas", 14, "bold"),
                      bg="black", fg="#FFD300", activeforeground="#39FF14",
                      highlightbackground="#00FFEF", highlightthickness=2,
                      command=reset_game)
reset_btn.pack(pady=15)

root.mainloop()