from lib import BoardInit
from lib import Board
import random
import statistics
import math
from MCTS import mcts_search
from time import perf_counter
from eval import Eval
import bots
def RandomVSRandom():
    board = BoardInit()
    curreval = 0
    while not board.GameFinished():
        print("Info:")
        board.Info()
        print("Eval:")
        curreval = Eval(board)
        moves = board.GetMoves()
        indices = [i for i in range(moves.bit_length()) if (moves >> i) & 1]
        index = random.choice(indices)
        board.MakeMove((1<<index))
        print('Made Move '+str(index))
    print(board.GameFinished())
    print(f'{curreval:.2f}')
    return [board.GameFinished(),curreval]

def main():
    print("Hello World!")
    pass
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)
