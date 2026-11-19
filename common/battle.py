import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

#import pandas as pd
from lib import BoardInit,Board
import utils
from time import perf_counter
from MCTS import mcts_search as MCTS
from bots import RandomMover as C
from bots import minimax_move as M
from MCTSEPT import mcts_search as MCTSEPT

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
    for t1 in [0.4,0.45,0.5]:
        for t2 in [0.2,0.25,0.3,0.35,0.4,0.45,0.5]:
            if t1>=t2:
                print(t1)
                print(t2)
                print(CMonteMonte(MCTS,MCTS,100,0.256,0.256,t1,t2))
    #print(CMonteMonte(MCTS,MCTS,50,0.256,0.256,1.4,0.5))#[11, 64, 25]
    #print(CMonteMonte(MCTS,MCTS,50,0.256,0.256,1.4,0.8))#[20, 62, 18]
    #print(CMonteMonte(MCTS,MCTS,50,0.256,0.256,1.4,1.0))#[30, 48, 22]
    #print(CMonteMonte(MCTS,MCTS,50,0.256,0.256,1.4,1.4))#[44, 32, 24]
    #print(CMonteMonte(MCTS,MCTS,50,0.256,0.256,1.4,2.0))#[39, 38, 23]
    #print(CMonteMini(MCTS,M,5,1.024,5))
    pass
"""0.2
0.2
[31, 42, 27]
0.3
0.2
[50, 13, 37]
0.3
0.3
[34, 29, 37]
0.4
0.2
[50, 11, 39]
0.4
0.3
[38, 22, 40]
0.4
0.4
[32, 37, 31]
0.5
0.2
[54, 15, 31]
0.5
0.3
[30, 37, 33]
0.5
0.4
[28, 31, 41]
0.5
0.5
[36, 36, 28]
0.8
0.2
[45, 24, 31]
0.8
0.3
[29, 36, 35]
0.8
0.4
[29, 43, 28]
0.8
0.5
[24, 52, 24]
0.8
0.8
[37, 35, 28]
1.0
0.2
[41, 26, 33]
1.0
0.3
[25, 42, 33]
1.0
0.4
[14, 62, 24]
1.0
0.5
[16, 53, 31]
1.0
0.8
[35, 42, 23]
1.0
1.0
[37, 40, 23]
1.4
0.2
[41, 27, 32]
1.4
0.3
[17, 57, 26]
1.4
0.4
[19, 60, 21]
1.4
0.5
[19, 59, 22]
1.4
0.8
[18, 60, 22]
1.4
1.0
[25, 48, 27]
1.4
1.4
[31, 40, 29]
2.0
0.2
[26, 44, 30]
2.0
0.3
[14, 65, 21]
2.0
0.4
[7, 70, 23]
2.0
0.5
[11, 70, 19]
2.0
0.8
[20, 61, 19]
2.0
1.0
[34, 50, 16]
2.0
1.4
[31, 44, 25]
2.0
2.0
[37, 44, 19]
"""
"""0.2
0.2
[67, 61, 72]
0.25
0.2
[88, 43, 69]
0.25
0.25
[49, 76, 75]
0.3
0.2
[106, 23, 71]
0.3
0.25
[77, 56, 67]
0.3
0.3
[64, 67, 69]
0.35
0.2
[121, 36, 43]
0.35
0.25
[87, 45, 68]
0.35
0.3
[79, 54, 67]
0.35
0.35
[63, 57, 80]
0.4
0.2
[112, 25, 63]
0.4
0.25
[98, 40, 62]
0.4
0.3
[65, 61, 74]
0.4
0.35
[88, 58, 54]
0.4
0.4
[57, 75, 68]
0.45
0.2
[114, 26, 60]
0.45
0.25
[95, 47, 58]
0.45
0.3
[76, 50, 74]
0.45
0.35
[86, 60, 54]
0.45
0.4
[63, 68, 69]
0.45
0.45
[65, 74, 61]
0.5
0.2
[106, 26, 68]
0.5
0.25
[82, 51, 67]
0.5
0.3
[66, 62, 72]"""
        
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(t2 - t1)