#the more wins that the root mcts node has, the better the position is for X aka False
import math
import random
import lib
from time import perf_counter


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
        self.terminal = (GetMoves(board)==[])
    def data(self):
        return self.move, self.player, self.visits, self.wins, self.untried_moves
    def is_fully_expanded(self):
        return len(self.untried_moves) == 0
    
    def expand(self):
        move = self.untried_moves.pop()
        new_board = self.board.copy()
        new_board.MakeMove(new_board.o,move[0],move[1])
        new_board.BoardFinished(move[0],new_board.o)
        new_board.o = not new_board.o

        child = MCTSNode(new_board, parent=self, move=move, player=self.board.o)
        self.children.append(child)
        return child
    
    def best_child(self, c=1.4):
        #print(self.children)
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
            moves = GetMoves(board)
            if not moves:
                return None
            move = random.choice(moves)
            board.MakeMove(o,move[0],move[1])
            board.BoardFinished(move[0],o)
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
        
    eval = root.wins/root.visits*100-50
    print(eval)
    best = max(root.children, key=lambda c: c.visits)
    return best.move
    
def RandomEval(board:lib.Board) ->list:
    return random.choice(GetMoves(board))
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
def Compare(func1:callable,func2:callable,games:int)->list:
    a = True
    result = [0,0,0]#func1 win, func2 win, draw
    for _ in range(games):
        board = lib.BoardInit()
        while True:
            o = board.o
            if not GetMoves(board):
                result[2]+=1
                break
            if o:
                move = func1(board)
            if not o:
                move = func2(board)
            board.MakeMove(o,move[0],move[1])
            board.BoardFinished(move[0],o)
            if o and board.GameFinished(o):
                result[0]+=1
                break
            elif board.GameFinished(o):
                result[1]+=1
                break
            board.o = not board.o
    for _ in range(games):
        board = lib.BoardInit()
        while True:
            o = board.o
            if not GetMoves(board):
                result[2]+=1
                break
            if not o:
                move = func1(board)
            if o:
                move = func2(board)
            board.MakeMove(o,move[0],move[1])
            board.BoardFinished(move[0],o)
            if o and board.GameFinished(o):
                result[1]+=1
                break
            elif board.GameFinished(o):
                result[0]+=1
                break
            board.o = not board.o
    return result

""" 
9 if ( maximize ):
10 best_value = -99999
11 for move in board . legal_moves :
12 board . push ( move )
13 best_value = max ( best_value ,
14 minimax ( board , depth -1 , not maximize ))
15 board . pop ()
16 return best_value
17 if ( minimize ):
18 best_value = 99999
19 for move in board . legal_moves :
20 board . push ( move )
21 best_value = min ( best_value ,
22 minimax ( board , depth -1 , not maximize ))
23 board . pop ()
24 return best_value"""
def minimax(board:lib.Board,depth:int,maximize:bool)->int:
    if board.GameFinished(True): return 10000
    elif board.GameFinished(False): return -10000
    elif GetMoves(board) == []: return 0
    if depth == 0:
        pass
def main():
    t1 = perf_counter()
    print(mcts_search(lib.BoardInit()))
    t2 = perf_counter()
    print(t2 - t1)
if __name__ == '__main__':
    main()