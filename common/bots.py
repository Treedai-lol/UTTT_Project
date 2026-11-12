from eval import Eval
import lib
from lib import Board
from lib import BoardInit
import utils
from time import perf_counter
import random
INF = 1000000

def RandomMover(board:Board,depth:int):
    moves = board.GetMoves()
    total = moves.bit_count()
    target = random.randint(1,total)
    for i in range(target-1):
        moves&=moves-1
    return moves&-moves


def _next_move_bitmask(moves:int):
    if moves == 0:
        return 0
    return moves & -moves


def minimax(board:Board, depth:int, alpha:int=-INF, beta:int=INF, color:int=1) -> int:
    """Negamax minimax with the current board evaluated from the side-to-move perspective.
    color = 1 for player 1 (O) and -1 for player 2 (X).
    """
    result = board.GameFinished()
    if result == 1:
        return 100000 + depth if color == 1 else -100000 - depth
    if result == 2:
        return -100000 - depth if color == 1 else 100000 + depth
    if result == 3:
        return 0
    if depth == 0:
        return color * Eval(board)

    best_score = -INF
    moves = board.GetMoves()
    while moves:
        move = _next_move_bitmask(moves)
        child = board.copy()
        child.MakeMove(move)
        score = -minimax(child, depth-1, -beta, -alpha, -color)
        if score > best_score:
            best_score = score
        if best_score > alpha:
            alpha = best_score
        if alpha >= beta:
            break
        moves ^= move
    return best_score


def minimax_move(board:Board, depth:int, alpha:int=-INF, beta:int=INF):
    """Return the best legal move bitmask for the current player using minimax."""
    moves = board.GetMoves()
    if moves == 0:
        return 0

    best_move = 0
    best_score = -INF
    color = 1 if board.player == 1 else -1

    while moves:
        move = _next_move_bitmask(moves)
        child = board.copy()
        child.MakeMove(move)
        score = -minimax(child, depth-1, -beta, -alpha, -color)
        if score > best_score:
            best_score = score
            best_move = move
        if best_score > alpha:
            alpha = best_score
        moves ^= move

    return best_move


def main():
    b = BoardInit(3)

    print(minimax_move(b, 3))


if __name__=='__main__':
    main()
