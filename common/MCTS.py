import math
import random
from time import perf_counter
from lib import Board
from lib import BoardInit
# For MCTS: 0 stands for not yet determined, 1 is o win, 2 is x win, 3 is draw
# For the backpropogation, 0.5 is a draw and 1 is o win, 0 is x win

class MCTSNode():

    board: Board

    def __init__(self, board, parent=None, move=None, player=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.player = player
        self.children = []
        self.visits = 0
        self.wins = 0.0
        self.untried_moves = board.GetMoves()
    
    def getinfo(self):
        for i in self.children:
            print(i.move,end=" ")
            print(i.visits,end=" ")
            print(i.wins)
    def is_fully_expanded(self):
        return len(self.untried_moves) == 0
    
    def expand(self):
        move = self.untried_moves.pop()
        new_board = self.board.copy()
        new_board.MakeMove(move)

        child = MCTSNode(new_board, parent=self, move=move, player=self.board.player)
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
            moves = board.GetMoves()
            if moves==[]:
                return 0.5
            move = ChooseRolloutMove(moves)
            board.MakeMove(move)
            if board.GameFinished()==1:
                return 1.0
            if board.GameFinished()==2:
                return 0.0
            
    def backpropagate(self, winner):
        self.visits += 1
        self.wins+=winner
        if self.parent:
            self.parent.backpropagate(winner)
def mcts_search(root_board, iterations=500):
    root = MCTSNode(root_board, player=False)
    for i in range(iterations):
        node = root
        while node.is_fully_expanded() and node.board.GameFinished()==0:
            node = node.best_child()

        if not node.is_fully_expanded() and node.board.GameFinished()==0:
            node = node.expand()
        
        if node.board.GameFinished():
            if node.board.GameFinished()==1:
                winner = 1.0
            if node.board.GameFinished()==2:
                winner = 0.0
            if node.board.GameFinished()==3:
                winner = 0.5   
        else:    
            winner = node.rollout()

        node.backpropagate(winner)
    best = max(root.children, key=lambda c: c.visits)
    root.getinfo()
    return best.move
def ChooseRolloutMove(moves:list)->int:
    return random.choice(moves) 

def main():
    t1 = perf_counter()
    board = BoardInit()
    print(mcts_search(board,50000))
    t2 = perf_counter()
    print(t2 - t1)
if __name__ == '__main__':
    main()