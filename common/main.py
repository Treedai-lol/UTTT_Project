import lib
import MCTS

def main():
    board = lib.BoardInit()
    while True:
        move = MCTS.mcts_search(board,5)
        board.MakeMove(move)
        board.GameFinished()
        move = int(input("move is"))
if __name__ == '__main__':
    main()