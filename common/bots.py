from eval import Eval
import lib
from lib import Board
from lib import BoardInit
import utils
import random
INF = 1000000
def RandomMover(board:Board,time:int):
    moves = board.GetMoves()
    total = moves.bit_count()
    target = random.randint(1,total)
    for i in range(target-1):
        moves&=moves-1
    return moves&-moves

def main():
    pass
if __name__=='__main__':
    main()
