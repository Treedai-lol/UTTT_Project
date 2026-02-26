import math
import random
import lib
from copy import deepcopy

class MCTSNode():
    def __init__(self, board:lib.Board, parent=None, move=None, player=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.player = player
        self.children = []
        self.visits = 0
        self.wins = 0.0
        self.untried_moves = GetMoves(board)

    def is_fully_expanded(self):
        return len(self.untried_moves) == 0
    
    def expand(self):
        move = self.untried_moves.pop()
        new_board = deepcopy(self.board)
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
        board = deepcopy(self.board)
        while True:
            o = board.o
            moves = GetMoves(board)
            if not moves:
                return None
            #print(moves)
            move = random.choice(moves)
            board.MakeMove(board.o,move[0],move[1])
            board.BoardFinished(move[0],o)
            winner = board.GameFinished(o)
            if winner is True:
                #print(o)
                return o
            #board.PrintBoard()
            #print(board.wonboards)
            #print("")
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
def mcts_search(root_state, iterations=5000):
    root = MCTSNode(root_state, player=None)
    for _ in range(iterations):
        node = root

        while not node.board.gg and node.is_fully_expanded():
            node = node.best_child()

        if not node.board.gg and not node.is_fully_expanded():
            node = node.expand()

        winner = node.rollout()
        node.backpropagate(winner)

    best = max(root.children, key=lambda c: c.visits)
    while root.children:
        print(root.children[-1].visits)
        root.children.pop()
    return best.move
def play_game():
    board = lib.BoardInit()
    move = mcts_search(board)
    print(move)
def DumbEval(board:lib.Board,o:bool) ->int:
    return 0
def NaiveEval(board:lib.Board,o:bool) ->int:
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
def GetMoves(board: lib.Board) ->list:
    movelist = []
    if board.sb != 9:
        for i in range(0,9):
            if board.bs[board.sb][i] == 0:
               movelist.append([board.sb,i])
    else:
        for i in range(0,9):
            for j in range(0,9):
               if board.bs[i][j] == 0:
                    movelist.append([i,j])
    return movelist
def Compare(func1,func2,games):
    for i in range(games):
        board = lib.BoardInit()
        if board.o:
            move = func1(board)
        if not board.o:
            move = func2(board)
        board.MakeMove(board.o,move[0],move[1])
        board.BoardFinished(move[0],o)
        board.o = not board.o

def main():
    play_game()
if __name__ == '__main__':
    main()