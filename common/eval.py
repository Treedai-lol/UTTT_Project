from lib import Board
from lib import BoardInit
import random
#Eval functions return a value from -1 to 1, with -100 and 100 meaning game over. positive is good for O
def RandomEval(board:Board) -> float:
    return random.choice(board.GetMoves())
def NaiveEval(board:Board,o:bool) ->int:
    r = board.GameFinished()
    if r==1:
        return 100
    if r==2:
        return -100
    if r==3:
        return 0
    

def main():
    b = BoardInit()
    
if __name__== '__main__':
    main()