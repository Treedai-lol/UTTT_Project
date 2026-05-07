# Format of the raw input int list
# [0:81] board 0 empty 1 o 2 x
# [81:90] wonboards 0 not won 1 o 2 x
# [90:91] sb int 0-9
# [91:92] player 1 o 2 x
# repeat
from copy import deepcopy
WINNING = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
class Board():
    def __init__(self, raw: list) -> None:
        assert(len(raw)==92)
        self.bs = raw[0:81]
        self.wonboards = raw[81:90]
        self.sb = raw[90]
        self.player = raw[91]
    def copy(self):
        return Board(deepcopy(self.bs),deepcopy(self.wonboards),deepcopy(self.o),deepcopy(self.sb))
    def PrintBoard(self) ->None: #print board function
        for i in range(0,3):
            for j in range(0,3):
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        print(self.bs[k*9+l],end=" ")
                    print(" ",end="")
                print("\n",end="")
            print("\n",end="")
        pass
    def GetOwnerShip(self,index:int,player:int) ->list: #returns the indices of pieces owned
        output = []
        if player==1:
            for i in range(0,9):
                if  self.bs[index*9+i] == 1:
                    output.append(i)
        else:
            for i in range(0,9):
                if  self.bs[index*9+i] == 2:
                    output.append(i)
        return output
    def MakeMove(self,a:int,b:int) ->None: #merged with BoardFinished
        o = self.player
        if o==1:
            self.bs[a][b] = 1
        else:
            self.bs[a][b] = 2
        if self.wonboards[b] != 0:
            self.sb = 9
        else:
            self.sb = b
        index = a
        wonsmallboard = False
        piecelist = self.GetOwnerShip(index,o)
        for i in WINNING:
            a = b = c = False
            for j in piecelist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a and b and c:
                wonsmallboard = True
        if wonsmallboard & (o==1):
            self.wonboards[index] = 1
        elif wonsmallboard:
            self.wonboards[index] = 2
        if o==1:
            self.player = 2
        else:
            self.player = 1
    def UnmakeMove(self,a:int,b:int,prevsb:int)->None:
        o = self.player
        self.bs[a][b] = 0
        self.sb = prevsb
        index = a
        output = False
        piecelist = self.GetOwnerShip(index,o)
        for i in WINNING:
            a = b = c = False
            for j in piecelist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a and b and c:
                output = True
        if not output:
            self.wonboards[index] = 0
        if o==1:
            self.player = 2
        else:
            self.player = 1
    def GameFinished(self) ->int: #returns whether the game has been finished
        output = 0
        tmp = self.wonboards
        olist = []
        xlist = []
        for i in range(0,9):
            if tmp[i] == 1:
                olist.append(i)
            if tmp[i] == 2:
                xlist.append(i)
        for i in WINNING:
            a = b = c = False
            for j in olist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a and b and c:
                output = 1
                break
            a = b = c = False
            for j in xlist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a and b and c:
                output = 2
        return output
    def GetMoves(self) ->list:
        movelist = []
        if self.sb != 9:
            for i in range(0,9):
                if self.bs[self.sb*9+i] == 0:
                    movelist.append([self.sb,i])
        else:
            for i in range(0,9):
                for j in range(0,9):
                    if self.bs[9*i+j] == 0:
                        movelist.append([i,j])
        return movelist
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
    raw.extend(extra)
    board = Board(raw)
    return board
def main():
    board = BoardInit()
    print(len(board.GetMoves()))
if __name__ == '__main__':
    main()