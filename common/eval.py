import math
import random
from time import perf_counter
from lib import Board
from lib import BoardInit


class MCTSNode():
    def __init__(self, board:Board, parent=None, move=None, player=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.player = player
        self.children = []
        self.visits = 0
        self.wins = 0.0
        self.untried_moves = board.GetMoves()
    def terminal_state(self):
        ret = 0
        if(self.board.GetMoves()==[]):
            ret = 3
        if(self.board.GameFinished!=0):
            ret = self.board.GameFinished()
        return ret
    def is_fully_expanded(self):
        return len(self.untried_moves) == 0
    
    def expand(self):
        move = self.untried_moves.pop()
        new_board = self.board.copy()
        new_board.MakeMove(new_board.o,move[0],move[1])
        new_board.o = not new_board.o

        child = MCTSNode(new_board, parent=self, move=move, player=self.board.o)
        self.children.append(child)
        return child
    
    def best_child(self, c=1.4):
        for child in self.children:
            if child.visits == 0:
                return child

        def ucb(child):
            exploit = child.wins / child.visits
            explore = c * math.sqrt(math.log(self.visits) / child.visits)
            return exploit + explore

        return max(self.children, key=ucb)
    
    def rollout(self): #uses random moves to finish the game, True or False for a win, None for a draw
        board = self.board.copy()
        while True:
            o = board.o
            moves = board.GetMoves()
            if not moves:
                return None
            move = random.choice(moves)
            board.MakeMove(o,move[0],move[1])
            if board.GameFinished(o) is True:
                return o
            board.o = not board.o
    def backpropagate(self, winner):
        self.visits += 1
        if self.player is not None:
            if winner is None:
                self.wins += 0.5
            elif winner == self.player:
                self.wins += 1.0
        if self.parent:
            self.parent.backpropagate(winner)
def mcts_search(root_board, iterations=500):
    root = MCTSNode(root_board, player=False)
    for _ in range(iterations):
        node = root
        while not node.board.GameFinished(not node.board.o) and node.is_fully_expanded() and not node.terminal:
            node = node.best_child()

        if not node.board.GameFinished(not node.board.o) and not node.is_fully_expanded() and not node.terminal:
            node = node.expand()
        
        if node.board.GameFinished(not node.board.o):
            winner = node.board.o
        elif node.terminal:
            winner = None
        else:    
            winner = node.rollout()

        node.backpropagate(winner)
    best = max(root.children, key=lambda c: c.visits)
    return best.move
    
def RandomEval(board:Board) ->list:
    return random.choice(board.GetMoves())
def NaiveEval(board:Board,o:bool) ->int:
    temp = 0
    wb = board.wonboards
    if o:
        for i in wb:
            if i == 1:
                temp = temp+1
            if i == 2:
                temp = temp-1
    else:
        for i in wb:
            if i == 1:
                temp = temp-1
            if i == 2:
                temp = temp+1
    return temp
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

def IntegrityCheck():
    checks = 2
    fails = 0
    try:
        mcts_search(BoardInit())
    except Exception as e:
        print("MCTS_Search is comprimised, throwing error: "+str(e))
        fails+=1
    else:
        print("MCTS_Search OK")  
    print(f'{checks} check(s) in total.')
    print(f'{fails} fail(s) in total.')
def main():
    t1 = perf_counter()
    
    t2 = perf_counter()
    print(t2 - t1)
if __name__ == '__main__':
    main()