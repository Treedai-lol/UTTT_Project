from lib import Board
from lib import BoardInit
def Compare(func1:callable,func2:callable,games:int)->list:
    a = True
    result = [0,0,0]#func1 win, func2 win, draw
    for _ in range(games):
        board = BoardInit()
        while True:
            o = board.o
            if not board.GetMoves():
                result[2]+=1
                break
            if o:
                move = func1(board)
            if not o:
                move = func2(board)
            board.MakeMove(o,move[0],move[1])
            if o and board.GameFinished(o):
                result[0]+=1
                break
            elif board.GameFinished(o):
                result[1]+=1
                break
            board.o = not board.o
    for _ in range(games):
        board = BoardInit()
        while True:
            o = board.o
            if not board.GetMoves():
                result[2]+=1
                break
            if not o:
                move = func1(board)
            if o:
                move = func2(board)
            board.MakeMove(o,move[0],move[1])
            if o and board.GameFinished(o):
                result[1]+=1
                break
            elif board.GameFinished(o):
                result[0]+=1
                break
            board.o = not board.o
    return result