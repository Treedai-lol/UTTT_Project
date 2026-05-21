from lib import Board
from lib import BoardInit
from math import floor
from eval import RandomEval
from time import perf_counter
from MCTS import mcts_search
def Compare(func1:callable,func2:callable,games:int)->list:
    result = [0,0,0]#func1 win, func2 win, draw
    for _ in range(games):
        board = BoardInit()
        while True:
            o = board.player
            if o==1:
                move = func1(board)
            if o==2:
                move = func2(board)
            board.MakeMove(move)
            print("------------------------")
            board.PrintBoard()
            #print(str(floor(move/9))+str(move%9))
            if board.GameFinished()==1:
                result[0]+=1
                break
            if board.GameFinished()==2:
                result[1]+=1
                break
            if board.GameFinished()==3:
                result[2]+=1
                break
    for _ in range(games):
        board = BoardInit()
        while True:
            o = board.player
            if o==1:
                move = func2(board)
            if o==2:
                move = func1(board)
            board.MakeMove(move)
            if board.GameFinished()==1:
                result[1]+=1
                break
            if board.GameFinished()==2:
                result[0]+=1
                break
            if board.GameFinished()==3:
                result[2]+=1
                break
    return result
def main():
    print(Compare(mcts_search,RandomEval,10))
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(t2 - t1)