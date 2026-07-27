import cProfile
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
        self.visits = 0.0
        self.wins = 0.0
        self.untried_moves = board.GetMoves()
    
    def getinfo(self):
        for i in self.children:
            print(i.move.bit_length()-1,end=" ")
            print(i.visits,end=" ")
            print(i.wins)
        print(self.visits)
        print(self.wins)
    def is_fully_expanded(self):
        return self.untried_moves == 0
    
    def expand(self):
        move = self.untried_moves&-self.untried_moves
        self.untried_moves&=self.untried_moves-1
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
            if self.player==2:
                winlocal = child.wins
            elif self.player==1:
                winlocal = child.visits-child.wins
            exploit = winlocal / child.visits
            explore = c * math.sqrt(math.log(self.visits) / child.visits)
            return exploit + explore

        return max(self.children, key=ucb)
    
    def rollout(self)->int: #uses random moves to finish the game, 1,2,3
        board = self.board.copy()
        while True:
            moves = board.GetMoves()
            if moves==0:
                return 0.5
            move = ChooseRolloutMove(moves,0)
            board.MakeMove(move)
            g = board.GameFinished()
            if g==1:
                return 1.0
            if g==2:
                return 0.0
            
    def backpropagate(self, winner):
        self.visits += 1
        self.wins+=winner
        if self.parent:
            self.parent.backpropagate(winner)
def mcts_search(root_board = BoardInit(), time=1):
    t1 = perf_counter()
    t2 = perf_counter()
    if(root_board.player==1):
        p = 2
    if(root_board.player==2):
        p = 1
    root = MCTSNode(root_board,player=p)
    while (t2-t1)<time:
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
        t2 = perf_counter()
    best = max(root.children, key=lambda c: c.visits)
    #root.getinfo()
    return best.move
def ChooseRolloutMove(moves:int,type=0)->int:
    if type==0:
        total = moves.bit_count()
        target = random.randint(1,total)
        for i in range(target-1):
            moves&=moves-1
        return moves&-moves
    weight = []
    for i in moves:
        if i%9==4: #center
            weight.append(5)
        elif i%9==0 or i%9==2 or i%9==6 or i%9==8: #corner
            weight.append(3)
        else: #edge
            weight.append(2)
    return random.choices(moves,weights=weight)[0]

def main():
    board = BoardInit()
    #print(mcts_search(board,1).bit_length()-1)
    cProfile.run('mcts_search()',None,'tottime')
if __name__ == '__main__':
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(t2 - t1)