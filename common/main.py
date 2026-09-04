from lib import BoardInit
from lib import Board
import random
import math
from time import perf_counter
def NumsToBB():
    string = input("gimme")
    out = 0
    for i in string:
        if i.isdigit():
            out+=(1<<int(i))
        else:
            print(out)
            out = 0
def movecomp(k=10000): #compares two moves
    result = [0,0]
    for i in range(k):
        board = BoardInit()
        board.MakeMove(40) #move 1
        while board.GameFinished()==0:
            move = random.choice(board.GetMoves())
            board.MakeMove(move)
        if board.GameFinished()==1:
            result[0]+=1
    for i in range(k):
        board = BoardInit()
        board.MakeMove(39) #move 2
        while board.GameFinished()==0:
            move = random.choice(board.GetMoves())
            board.MakeMove(move)
        if board.GameFinished()==1:
            result[1]+=1   
    print(result)
def main():
       NumsToBB()
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)
