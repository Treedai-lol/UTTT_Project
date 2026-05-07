import math
import random
from time import perf_counter
from lib import Board
from lib import BoardInit
# For MCTS: 0 stands for not yet determined, 1 is o win, 2 is x win, 3 is draw
# For the backpropogation, o.5 is a draw and 1 is o win, 0 is x win

class MCTSNode():
    def __init__(self, board, parent=None, move=None, player=0):
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
    
    def rollout(self)->int: #uses random moves to finish the game, 1,2,3
        board = self.board.copy()
        while True:
            o = board.player
            moves = board.GetMoves()
            if not moves:
                return 0.5
            move = ChooseRolloutMove(moves)
            board.MakeMove(o,move)
            if board.GameFinished()==1:
                return 1.0
            if board.GameFinished()==2:
                return 0.0
            board.o = not board.o
    def backpropagate(self, winner):
        self.visits += 1
        self.wins+=winner
        if self.parent:
            self.parent.backpropagate(winner)
def mcts_search(root_board, iterations=500):
    root = MCTSNode(root_board, player=False)
    for _ in range(iterations):
        node = root
        while node.is_fully_expanded() and node.terminal_state()==0:
            node = node.best_child()

        if not node.is_fully_expanded() and node.terminal_state()==0:
            node = node.expand()
        
        if node.terminal_state():
            winner = node.terminal_state()
        else:    
            winner = node.rollout()

        node.backpropagate(winner)
    best = max(root.children, key=lambda c: c.visits)
    return best.move
def ChooseRolloutMove(moves:list)->int:
    return random.choice(moves) 

def main():
    t1 = perf_counter()
    
    t2 = perf_counter()
    print(t2 - t1)
if __name__ == '__main__':
    main()