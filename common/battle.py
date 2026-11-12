import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

import pandas as pd
from lib import BoardInit,Board
import utils
from time import perf_counter
from MCTS import mcts_search as MCTS
from bots import RandomMover as C
from bots import minimax_move as M

def CMiniMini(func1:callable,func2:callable,games:int,dep1:int,dep2:int)->list:
    result = [0,0,0]#func1 win, func2 win, draw
    for i in range(games):
        #print(i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func1(board,depth=dep1)
            if o==2:
                move = func2(board,depth=dep2)
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
        #print(games+i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func2(board,depth=dep2)
            if o==2:
                move = func1(board,depth=dep1)
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
def CMonteMini(func1:callable,func2:callable,games:int,time1:int,dep2:int)->list:
    result = [0,0,0]#func1 win, func2 win, draw
    for i in range(games):
        #print(i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func1(board,time=time1)
            if o==2:
                move = func2(board,depth=dep2)
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
        #print(games+i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func2(board,depth=dep2)
            if o==2:
                move = func1(board,time=time1)
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
def CMonteMonte(func1:callable,func2:callable,games:int,time1:int,time2:int,exp1:int,exp2:int)->list:
    result = [0,0,0]#func1 win, func2 win, draw
    for i in range(games):
        #print(i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func1(board,time=time1,exp=exp1)
            if o==2:
                move = func2(board,time=time2,exp=exp2)
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
        #print(games+i+1)
        board = BoardInit()
        while True:
            #board.PrintBoard()
            o = board.player
            if o==1:
                move = func2(board,time=time2,exp=exp2)
            if o==2:
                move = func1(board,time=time1,exp=exp1)
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
    #print(CMiniMini(M,M,1,4,4))
    #print(CMonteMonte(MCTS,MCTS,15,1.024,1.024,1,1.4))
    print(CMonteMini(MCTS,M,5,1.024,5))
        
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(t2 - t1)