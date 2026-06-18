# Format of the raw input int list
# [0:81] board 0 empty 1 o 2 x
# [81:90] wonboards 0 not won 1 o 2 x
# [90:91] sb int 0-9
# [91:92] player 1 o 2 x
# for move representation: [67] is on floor(67/9)=6 and 67%9=4
from math import floor
from bitboard import BitBoard
from bitboard import SmallBoard
class Board():
    def __init__(self, raw: list)->None:
        assert(len(raw)==92)
        self.bs = BitBoard(raw[0:81])
        self.wonboards = SmallBoard(raw[81:90])
        self.sb = raw[90]
        self.player = raw[91]
    def OutputList(self)->list:
        ret = []
        ret.extend(self.bs.outputlist())
        ret.extend(self.wonboards.outputlist())
        ret.append(self.sb)
        ret.append(self.player)
        return ret
    def copy(self):
        new = object.__new__(Board)
        bb = object.__new__(BitBoard)
        bb.o = self.bs.o
        bb.x = self.bs.x
        new.bs = bb

        wb = object.__new__(SmallBoard)
        wb.o = self.wonboards.o
        wb.x = self.wonboards.x
        wb.d = self.wonboards.d
        new.wonboards = wb

        new.sb = self.sb
        new.player = self.player
        return new
    def PrintBoard(self)->None: #print board function
        self.bs.printbitboard()
        self.wonboards.printbitboard()
        print(self.sb,end=" ")
        print(self.player)
    def Info(self)->None:
        self.PrintBoard()
        print(self.wonboards)
        print("Board to play in: "+str(self.sb))
        print("Player: "+str(self.player))
    def MakeMove(self,move:int)->None: #Takes in a bitstring!!
        o = self.player
        ind = move.bit_length()-1
        if o==1:
            self.bs.seto(move)
        else:
            self.bs.setx(move)
        index = floor(ind/9)
        if self.wonboards.getpiece(index)==0 and self.bs.iswon(index,self.player):
            if o==1:
                self.wonboards.seto((1<<index))
            if o==2:
                self.wonboards.setx((1<<index))
        elif self.bs.isdraw(index):
            self.wonboards.setd((1<<index))
        if self.wonboards.getpiece(ind%9)!=0:
            self.sb = 9
        else:
            self.sb = ind%9

        if o==1:
            self.player = 2
        else:
            self.player = 1
    def GameFinished(self) ->int: #returns 0,1,2,3
        if self.wonboards.iswon(1):
            return 1
        if self.wonboards.iswon(2):
            return 2
        if self.wonboards.isdraw():
            return 3
        return 0
    def GetMoves(self) ->int:
        return self.bs.getmoves(self.sb)
def BoardInit(flavor=0) ->Board:
    if flavor==0:
        raw =  [0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0]
        extra = [0,0,0,0,0,0,0,0,0,9,1]
    if flavor==1:
        raw =  [1,1,1,1,1,1,1,1,1,
                2,2,2,2,2,2,2,2,2,
                1,1,1,1,1,1,1,1,1,
                2,2,2,2,2,2,2,2,2,
                0,0,0,0,0,0,0,0,0,
                2,2,2,2,2,2,2,2,2,
                1,1,1,1,1,1,1,1,1,
                2,2,2,2,2,2,2,2,2,
                1,1,1,1,1,1,1,1,1]
        extra = [1,2,1,2,0,2,1,2,1,4,1]
    if flavor==2:
        raw =  [0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0]
        extra = [1,1,0,1,0,1,2,2,2,9,1]
    if flavor==3:
        raw =  [0,1,2,1,2,1,1,2,1,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0]
        extra = [0,0,0,0,0,0,0,0,0,9,2]
    raw.extend(extra)
    board = Board(raw)
    return board
def main():
    board = BoardInit()
    nb = board.copy()
    nb.MakeMove(1)
    board.PrintBoard()
    nb.PrintBoard()
if __name__ == '__main__':
    main()