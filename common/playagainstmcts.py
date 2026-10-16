import tkinter as tk
import math
from lib import BoardInit, Board
from MCTS import mcts_search
import utils

# Global board state
board = BoardInit()

# Maps player numbers to symbols and colors
PLAYER_SYMBOLS = {
    1: ("X", "#2980b9", "#ffffff"),  # (Symbol, Text Color, Background Color)
    2: ("O", "#e74c3c" , "#ffffff")
}

def update_button_ui(button_index, player):
    """Updates the target button's text, color, and disables it."""
    if button_index in buttons:
        btn = buttons[button_index]
        symbol, fg_color, bg_color = PLAYER_SYMBOLS.get(player, ("sym", "fg", "bg"))
        btn.config(
            text=symbol,
            fg=fg_color,
            bg=bg_color,
            state="disabled",
            disabledforeground=fg_color,
            font=("Arial", 11, "bold")
        )

def process_turn(human_move=None):
    global board

    if board.GameFinished():
        status_label.config(text=f"Game Over! Result: {board.GameFinished()}")
        return

    # 1. Handle Human Move
    if human_move is not None and board.player != 1:
        current_player = board.player
        
        board.MakeMove(1<<human_move)
        update_button_ui(human_move, current_player)
        board.PrintBoard()
        
        if board.GameFinished():
            status_label.config(text=f"Game Over! Result: {board.GameFinished()}")
            return

    # 2. Handle MCTS Turn
    if board.player == 1:
        status_label.config(text="MCTS is thinking...")
        root.update()  # Force GUI refresh before computation
        
        current_player = board.player
        mcts_move_bit = mcts_search(board, 1.024)
        
        # Convert bitmask move (1 << index) back to index (0-80)
        mcts_move_index = utils.bitmask_to_index(mcts_move_bit)
        
        board.MakeMove(mcts_move_bit)
        if mcts_move_index != -1:
            update_button_ui(mcts_move_index, current_player)
            
        board.PrintBoard()
        
        if board.GameFinished():
            status_label.config(text=f"Game Over! Result: {board.GameFinished()}")
            return
        
        status_label.config(text="Your turn! Click an available square.")

def handle_click(button_num):
    # Ignore click if it's MCTS turn or button is already used
    if board.player == 1 or buttons[button_num]["state"] == "disabled":
        return
    
    status_label.config(text=f"You played position #{button_num}")
    process_turn(human_move=button_num)


# --- GUI Setup ---
root = tk.Tk()
root.title("Ultimate Tic-Tac-Toe vs MCTS")

status_label = tk.Label(root, text="Game started. Make your move!", font=("Arial", 12, "bold"))
status_label.pack(pady=10)

grid_frame = tk.Frame(root)
grid_frame.pack(expand=True, padx=10, pady=10)

buttons = {}

for num in range(81):
    block_index = num // 9
    block_row, block_col = block_index // 3, block_index % 3
    
    within_block = num % 9
    inside_row, inside_col = within_block // 3, within_block % 3
    
    row = (block_row * 3) + inside_row
    col = (block_col * 3) + inside_col
    
    pad_y = (4, 10) if inside_row == 2 else 2
    pad_x = (4, 10) if inside_col == 2 else 2

    btn = tk.Button(
        grid_frame, 
        text="",  # Empty at start
        width=4, 
        height=2,
        relief="groove",
        command=lambda n=num: handle_click(n)
    )
    btn.grid(row=row, column=col, padx=pad_x, pady=pad_y)
    buttons[num] = btn

def main():
    if board.player == 1:
        process_turn()
    root.mainloop()

if __name__ == '__main__':
    main()