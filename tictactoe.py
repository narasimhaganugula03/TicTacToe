import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = [""] * 9

def check_winner():
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

def is_draw():
    return "" not in board

def on_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")

        winner = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s Turn")

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    label.config(text="Player X's Turn")

    for btn in buttons:
        btn.config(text="", state="normal")

# UI Label
label = tk.Label(root, text="Player X's Turn", font=("Arial", 16))
label.pack()

# Buttons (Grid)
frame = tk.Frame(root)
frame.pack()

buttons = []

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(root, text="Restart Game", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()