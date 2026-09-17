from lib import BoardInit
from lib import Board
import random
import math
from time import perf_counter
from eval import Eval
def NumsToBB():
    string = input("gimme")
    out = 0
    print("[",end='')
    for i in string:
        if i.isdigit():
            out+=(1<<int(i))
        else:
            print(out,end=",")
            out = 0
    print(str(out)+"]")
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
def PlayWithSelf():
    board = BoardInit()
    while not board.GameFinished():
        board.PrintBoard()
        move = input("enter the boardsquare combo")
        #tmp = math.floor(float(move)/10)*9
        tmp+=int(move)%10
        print(tmp)
        board.MakeMove((1<<tmp))
    print(board.GameFinished)
def RandomPlay():
    board = BoardInit()
    while not board.GameFinished():
        print("Info:")
        board.Info()
        print("Eval:")
        Eval(board)
        moves = board.GetMoves()
        indices = [i for i in range(moves.bit_length()) if (moves >> i) & 1]
        index = random.choice(indices)
        board.MakeMove((1<<index))
        #print('Made Move'+str(index))
    print(board.GameFinished())
def main():
    for i in range(1):
        RandomPlay()
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)
