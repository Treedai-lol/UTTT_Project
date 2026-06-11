# Format of the raw input int list
# [0:81] board 0 empty 1 o 2 x
# [81:90] wonboards 0 not won 1 o 2 x
# [90:91] sb int 0-9
# [91:92] player 1 o 2 x
# for move representation: [67] is on floor(67/9)=6 and 67%9=4
from math import floor
from bitboard import BitBoard
WINNING = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
class Board():
    def __init__(self, raw: list) -> None:
        assert(len(raw)==92)
        self.bs = BitBoard(raw[0:81])
        self.wonboards = raw[81:90]
        self.sb = raw[90]
        self.player = raw[91]
    def OutputList(self) ->list:
        ret = []
        ret.extend(self.bs.outputlist())
        ret.extend(self.wonboards)
        ret.append(self.sb)
        ret.append(self.player)
        return ret
    def copy(self)->list:
        raw = self.OutputList()
        new = []
        for i in range(92):
            new.append(raw[i])
        return Board(new)
    def PrintBoard(self) ->None: #print board function
        self.bs.printbitboard()
    def Info(self) ->None:
        self.PrintBoard()
        print(self.wonboards)
        print("Board to play in: "+str(self.sb))
        print("Player: "+str(self.player))
    def MakeMove(self,move:int) ->None: #merged with BoardFinished
        o = self.player
        ind = move.bit_length()-1
        if o==1:
            self.bs.seto(move)
        else:
            self.bs.setx(move)
        if self.wonboards[ind%9] != 0:
            self.sb = 9
        else:
            self.sb = ind%9
        index = floor(ind/9)
        if self.wonboards[index]==0 and self.bs.iswon(index,self.player):
            self.wonboards[index] = o
        elif self.bs.isdraw(index):
            self.wonboards[index] = 3
        if o==1:
            self.player = 2
        else:
            self.player = 1
    def GameFinished(self) ->int: #returns 0,1,2,3
        output = 0
        for o in range(1,3):
            if self.wonboards[0]==o and self.wonboards[1]==o and self.wonboards[2]==o:
                output = o
                break
            elif self.wonboards[3]==o and self.wonboards[4]==o and self.wonboards[5]==o:
                output = o
                break
            elif self.wonboards[6]==o and self.wonboards[7]==o and self.wonboards[8]==o:
                output = o
                break
            elif self.wonboards[0]==o and self.wonboards[3]==o and self.wonboards[6]==o:
                output = o
                break
            elif self.wonboards[1]==o and self.wonboards[4]==o and self.wonboards[7]==o:
                output = o
                break
            elif self.wonboards[2]==o and self.wonboards[5]==o and self.wonboards[8]==o:
                output = o
                break
            elif self.wonboards[0]==o and self.wonboards[4]==o and self.wonboards[8]==o:
                output = o
                break
            elif self.wonboards[2]==o and self.wonboards[4]==o and self.wonboards[6]==o:
                output = o
                break
        if output==0 and self.GetMoves()==[]:
            output = 3
        return output
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
    board = BoardInit(2)
    print(board.GameFinished())
if __name__ == '__main__':
    main()