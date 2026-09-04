from lib import BoardInit
from lib import Board
import random
import math
from time import perf_counter
e = 0
nld = 0
def edge(board:Board,depth):
    global e
    if(depth==0):
        return
    moves = board.GetMoves()
    while(moves!=0):
        e+=1
        nb = board.copy()
        move = (moves^(moves-1))&(moves)
        moves&=(moves-1)
        nb.MakeMove(move)
        edge(nb,depth-1)
    return
def getnld(board:Board,depth):
    global nld
    nld+=1
    if(depth==1):
        return
    moves = board.GetMoves()
    while(moves!=0):
        nb = board.copy()
        move = (moves^(moves-1))&(moves)
        moves&=(moves-1)
        nb.MakeMove(move)
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
    print(e/nld)
def main():
    getbf(10)
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)