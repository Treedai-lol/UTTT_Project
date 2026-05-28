from lib import BoardInit
from lib import Board
import random
from time import perf_counter

def maim():
    result = [0,0]
    for i in range(100000):
        board = BoardInit()
        board.MakeMove(40)
        while board.GameFinished()==0:
            move = random.choice(board.GetMoves())
            board.MakeMove(move)
        if board.GameFinished()==1:
            result[0]+=1
    for i in range(100000):
        board = BoardInit()
        board.MakeMove(39)
        while board.GameFinished()==0:
            move = random.choice(board.GetMoves())
            board.MakeMove(move)
        if board.GameFinished()==1:
            result[1]+=1   
    print(result)
def main():
    maim()
        
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)