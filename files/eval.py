#the more wins that the root mcts node has, the better the position is for X aka False
import math
import random
import lib
from time import perf_counter
from copy import deepcopy


class MCTSNode():
    def __init__(self, board:lib.Board, prob:float,parent=None, move=None, player=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.player = player
        self.children = []
        self.visits = 0
        self.wins = 0.0
        self.terminal = (GetMoves(board)==[])
        self.prob = prob
    def is_fully_expanded(self):
        return len(self.untried_moves) == 0
    
    def expand(self):
        temp = NaiveEval(self.board).pop(0)
        j = 0
        prevsb = deepcopy(self.board.sb)
        for i in GetMoves(self.board):
            self.board.MakeMove(i[0],i[1])
            self.children.append(MCTSNode(self.board,self,i,self.board.o,temp[j]))
            j+=1
            self.board.UnmakeMove(i[0],i[1],prevsb)
    def best_child(self, c=1.4):
        for child in self.children:
            if child.visits == 0:
                return child

        def ucb(child):
            exploit = child.wins / child.visits
            explore = c * math.sqrt(math.log(self.visits) / child.visits)
            return exploit + explore

        return max(self.children, key=ucb)
    
    def rollout(self)->list: #returns the average amount of wins for O(0 to 1)
        return NaiveEval(self.board)[0]
    def backpropagate(self, wins:float):
        self.visits += 1
        self.wins+=wins
        if self.parent:
            self.parent.backpropagate(wins)
def mcts_search(root_board, iterations=500):
    root = MCTSNode(root_board, player=False)
    for _ in range(iterations):
        node = root
        while not node.board.GameFinished(not node.board.o) and node.is_fully_expanded() and not node.terminal:
            node = node.best_child()

        if not node.board.GameFinished(not node.board.o) and not node.is_fully_expanded() and not node.terminal:
            node = node.expand()
        
        wins = node.rollout()

        node.backpropagate(wins)
    best = max(root.children, key=lambda c: c.visits)
    return best.move
    
def RandomEval(board:lib.Board) ->list:
    return random.choice(GetMoves(board))
def NaiveEval(board:lib.Board) ->list:
    output = []
    wb = board.wonboards
    for i in wb:
        if i == 1:
            temp+=1
        if i == 0:
            temp+=0.5
    temp/=9
    output.append(temp)
    for i in GetMoves(board):
        output.append(1/len(GetMoves))
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
        mcts_search(lib.BoardInit())
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