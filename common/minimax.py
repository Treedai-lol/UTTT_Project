from eval import Eval
import lib
from lib import Board
from lib import BoardInit
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
def main():
    board = BoardInit(3)
    print(alphaBetaMax(board,-INF,INF,8))
if __name__=='__main__':
    main()
