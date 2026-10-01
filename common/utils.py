from lib import BoardInit
from lib import Board
import random
import statistics
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
    curreval = 0
    while not board.GameFinished():
        #print("Info:")
        #board.Info()
        #print("Eval:")
        #Eval(board)
        curreval = Eval(board)
        moves = board.GetMoves()
        indices = [i for i in range(moves.bit_length()) if (moves >> i) & 1]
        index = random.choice(indices)
        board.MakeMove((1<<index))
        #print(curreval)
        #print('Made Move'+str(index))
    #print(board.GameFinished())
    #print(f'{curreval:.2f}')
    return [board.GameFinished(),curreval]
def PlayEvalMove():
    board = BoardInit( )
    while not board.GameFinished():
        moves = board.GetMoves()
        board.PrintBoard()
        if board.player==1:
            move_eval = [-1,-1000]
        if board.player==2:
            move_eval = [-1,1000]
        while moves!=0:
            move = moves&-moves
            moves&=moves-1
            nb = board.copy()
            #print(move.bit_length())
            ev = Eval(nb.MakeMove(move))
            if(board.player==1):
                if ev>move_eval[1]:
                    move_eval = [move,ev]
            if(board.player==2):
                if ev<move_eval[1]:
                    move_eval = [move,ev]
        board.MakeMove(move_eval[0])
        print(Eval(board))
def RandomAnalysis(n:int):
    oeval = []
    xeval = []
    deval = []
    for i in range(n):
        l = RandomPlay()
        if(l[0]==1):
            oeval.append(l[1])
        if(l[0]==2):
            xeval.append(l[1])
        if(l[0]==3):
            deval.append(l[1])
    print("average evaluation when o wins:")
    print(statistics.fmean(oeval))
    print("average evaluation when x wins:")
    print(statistics.fmean(xeval))
    print("average evaluation when d wins:")
    print(statistics.fmean(deval))
def main():
    #RandomAnalysis(1000)
    PlayEvalMove()
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)
