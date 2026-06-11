from lib import BoardInit
from lib import Board
import random
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
WINNING = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
li = []
for i in WINNING:
    a=0
    a+=pow(2,i[0])
    a+=pow(2,i[1])
    a+=pow(2,i[2])
    li.append(a)
def main():
    print(li)
        
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    print(perf_counter()-t1)