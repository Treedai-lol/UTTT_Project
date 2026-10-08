import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

import pandas as pd
from lib import Board
from lib import BoardInit
from time import perf_counter
from MCTS import mcts_search as A
from MCTScopy import mcts_search as B
#from minimax import RandomMover as B

def Compare(func1:callable,func2:callable,games:int,t1,t2)->list:
    result = [0,0,0]#func1 win, func2 win, draw
    for i in range(games):
        #print(i+1)
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
        #print(games+i+1)
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
def MakeData(func1:callable,func2:callable,games,t1,t2):
    res = Compare(func1,func2,games,t1,t2)
    header = ["bot1","bot2","wins","draws","losses","win.perc"]
    df = pd.read_csv(r'common\results.csv')
    df.loc[(df["bot1"]==t1)&(df["bot2"]==t2),"wins"]+=res[0]
    df.loc[(df["bot1"]==t1)&(df["bot2"]==t2),"draws"]+=res[2]
    df.loc[(df["bot1"]==t1)&(df["bot2"]==t2),"losses"]+=res[1]
    w = df.loc[(df["bot1"]==t1)&(df["bot2"]==t2),"wins"]
    d = df.loc[(df["bot1"]==t1)&(df["bot2"]==t2),"draws"]
    l = df.loc[(df["bot1"]==t1)&(df["bot2"]==t2),"losses"]
    df.loc[(df["bot1"]==t1)&(df["bot2"]==t2),"win.perc"] = (w+d/2)/(w+d+l)
    df.to_csv(r'common\results.csv', index=False)
def CsvInit():
    alltimes = [0.001,0.002,0.004,0.008,0.016,0.032,0.064,0.128,0.256,0.512,1.024]
    bot1 = []
    bot2 = []
    zeroes = []
    for i in alltimes:
        for j in alltimes:
            if(i>=j):
                bot1.append(i)
                bot2.append(j)
                zeroes.append(0)
    data = {
    "bot1": bot1,
    "bot2": bot2,
    "wins": zeroes,
    "draws":zeroes,
    "losses":zeroes,
    "win.perc":zeroes
    }
    df = pd.DataFrame(data)
    df.to_csv(r'common\results.csv', index=False)
def main():
    while True:
        MakeData(A,B,1,0.001,0.001)
        MakeData(A,B,1,0.002,0.002)
        MakeData(A,B,1,0.004,0.004)
        MakeData(A,B,1,0.008,0.008)
        MakeData(A,B,1,0.016,0.016)
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(t2 - t1)