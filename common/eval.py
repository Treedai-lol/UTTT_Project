from lib import Board
from lib import BoardInit
import random
def RandomEval(board:Board) ->list:
    return random.choice(board.GetMoves())
def NaiveEval(board:Board,o:bool) ->int:
    temp = 0
    wb = board.wonboards
    if o:
        for i in wb:
            if i == 1:
                temp = temp+1
            if i == 2:
                temp = temp-1
    else:
        for i in wb:
            if i == 1:
                temp = temp-1
            if i == 2:
                temp = temp+1
    return temp