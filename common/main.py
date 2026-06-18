from lib import BoardInit
from lib import Board
import random
import math
from time import perf_counter
e = 0
nld = 0
def edge(board:Board,depth):
    global e
    e += len(board.GetMoves())
    if(depth==0):
        return
    moves = board.GetMoves()
    while(moves!=[]):
        nb = board.copy()
        nb.MakeMove(moves.pop())
        edge(nb,depth-1)
    return
def getnld(board:Board,depth):
    global nld
    nld+=1
    if(depth==0):
        return
    moves = board.GetMoves()
    while(moves!=[]):
        nb = board.copy()
        nb.MakeMove(moves.pop())
        getnld(nb,depth-1)
def getbf(k):
    global e,nld
    e = 0
    nld = 0
    edge(BoardInit(),k)
    getnld(BoardInit(),k)
    print(k)
    print(e)
    print(nld)
    return e/nld
def movecomp():
    result = [0,0]
    for i in range(10000):
        board = BoardInit()
        board.MakeMove(40)
        while board.GameFinished()==0:
            move = random.choice(board.GetMoves())
            board.MakeMove(move)
        if board.GameFinished()==1:
            result[0]+=1
    for i in range(10000):
        board = BoardInit()
        board.MakeMove(39)
        while board.GameFinished()==0:
            move = random.choice(board.GetMoves())
            board.MakeMove(move)
        if board.GameFinished()==1:
            result[1]+=1   
    print(result)
def main():
       print(math.floor(0/9))
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)