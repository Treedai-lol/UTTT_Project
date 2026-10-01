import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from lib import Board
from lib import BoardInit
from time import perf_counter
from MCTS import mcts_search as A
from MCTScopy import mcts_search as B
#from minimax import RandomMover as B

def Compare(func1:callable,func2:callable,games:int,t1,t2)->list:
    result = [0,0,0]#func1 win, func2 win, draw
    for i in range(games):
        print(i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func1(board,time=t1)
            if o==2:
                move = func2(board,time=t2)
            board.MakeMove(move)
            g = board.GameFinished()
            if g==1:
                result[0]+=1
                break
            if g==2:
                result[1]+=1
                break
            if g==3:
                result[2]+=1
                break
    for i in range(games):
        print(games+i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func2(board,time=t2)
            if o==2:
                move = func1(board,time=t1)
            board.MakeMove(move)
            g = board.GameFinished()
            if g==1:
                result[1]+=1
                break
            if g==2:
                result[0]+=1
                break
            if g==3:
                result[2]+=1
                break
    return result
def main():
    """lis = [0.001,0.002,0.004,0.008,0.016,0.032,0.064,0.128,0.256]
    for i in range(9):
        for j in range(i+1):
            print(lis[i])
            print(lis[j])
            print(Compare(A,B,50,lis[i],lis[j]))"""
    print(Compare(A,B,50,0.512,0.256))
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(t2 - t1)