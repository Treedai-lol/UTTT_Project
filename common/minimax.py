from eval import Eval
import lib
from lib import Board
from lib import BoardInit
from bitboard import GetIndex
import random
INF = 1000000
def alphaBetaMax(board: Board,alpha,beta,depthleft):
    if depthleft==0:
        return Eval(board)
    bestValue = -INF
    moves = board.GetMoves()
    while moves!=0:
        move = moves&-moves
        moves&=moves-1
        score = alphaBetaMin(board.copy().MakeMove(move),alpha,beta,depthleft-1)
        if score>bestValue:
            bestValue = score
            if score>alpha:
                alpha = score #alpha acts like max in MiniMax
        if score>=beta:
            return score   #fail soft beta-cutoff
    return bestValue
def alphaBetaMin(board: Board,alpha,beta,depthleft):
    if depthleft==0:
        return -Eval(board)
    bestValue = INF
    moves = board.GetMoves()
    while moves!=0:
        move = moves&-moves
        moves&=moves-1
        score = alphaBetaMax(board.copy().MakeMove(move),alpha,beta,depthleft-1)
        if score<bestValue:
            bestValue = score
            if score<beta:
                alpha = score #beta acts like min in MiniMax
        if score<=alpha:
            return score   #fail soft alpha-cutoff
    return bestValue

def RandomMover(board:Board,time:int):
    moves = board.GetMoves()
    total = moves.bit_count()
    target = random.randint(1,total)
    for i in range(target-1):
        moves&=moves-1
    return moves&-moves
def main():
    board = BoardInit()
    while not board.GameFinished():
        moves = board.GetMoves()
        board.PrintBoard()
        if board.player==1:
            move_eval = [-1,-1000]
        if board.player==2:
            move_eval = [-1,1000]
        while moves!=0:
            move = moves&-moves
            moves&=moves-1
            nb = board.copy()
            if(board.player==1):
                ev = alphaBetaMax(nb.MakeMove(move),-INF,INF,5)
                if ev>move_eval[1]:
                    move_eval = [move,ev]
            if(board.player==2):
                ev = alphaBetaMin(nb.MakeMove(move),-INF,INF,5)
                if ev<move_eval[1]:
                    move_eval = [move,ev]
        board.MakeMove(move_eval[0])
        print(Eval(board))
if __name__=='__main__':
    main()
