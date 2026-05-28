import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from lib import Board
from lib import BoardInit
from eval import RandomEval
from time import perf_counter
from MCTS import mcts_search
from MCTScopy import mcts_search as fancy
from historical.MCTS_26_5_21_1 import mcts_search as baseline

def Compare(func1:callable,func2:callable,games:int)->list:
    result = [0,0,0]#func1 win, func2 win, draw
    for i in range(games):
        print(i+1)
        board = BoardInit()
        while True:
            o = board.player
            if o==1:
                move = func1(board)
            if o==2:
                move = func2(board)
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
            o = board.player
            if o==1:
                move = func2(board)
            if o==2:
                move = func1(board)
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
    print(Compare(mcts_search,fancy,10))
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(t2 - t1)