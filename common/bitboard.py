foo = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
WINNING = [7, 56, 448, 73, 146, 292, 273, 84]
class BitBoard:
    def __init__(self,raw:list)->None: #takes in a standard 9x9 board and converts it so a bitboard
        self.o = 0
        self.x = 0
        for i in range(81):
            if raw[i]==1:
                self.o|=(1<<i)
            elif raw[i]==2:
                self.x|=(1<<i)
    def seto(self,move)->None: #move is of bit string format
        self.o|=move
    def setx(self,move)->None: #move is of bit string format
        self.x|=move
    def clear(self,ind)->None: #clears the bitboard on index ind
        self.o&= ~(1<<ind)
        self.x&= ~(1<<ind)
    def getpiece(self,ind)->int: #returns piece on index ind
        if self.o&(1<<ind):
            return 1
        if self.x&(1<<ind):
            return 2
        return 0
    def outputlist(self)->list:
        ret = []
        for i in range(81):
            if self.o&(1<<i):
                ret.append(1)
                continue
            if self.x&(1<<i):
                ret.append(2)
                continue
            ret.append(0)
        return ret
    def printbitboard(self)->None:
        for i in range(0,3):
            for j in range(0,3):
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        print(self.getpiece(9*k+l),end=" ")
                    print(" ",end="")
                print("\n",end="")
            print("\n",end="")
    def isdraw(self,sb)->bool: #returns if board sb is a draw(filled)
        mask = ((1<<(sb+1)*9)-1)^((1<<sb*9)-1)
        haspiece = self.o|self.x
        if(mask&haspiece==mask):
            return 1
        return 0
    def iswon(self,sb,player)->bool: #returns if board sb is won by player
        mask = ((1<<(sb+1)*9)-1)^((1<<sb*9)-1)
        if player==1:
            tmp = mask&self.o
        elif player==2:
            tmp = mask&self.x
        for pat in WINNING:
            if(tmp&(pat<<sb*9)==(pat<<sb*9)):
                return 1
        return 0
    def getmoves(self,sb)->int:
        if sb==9:   
            mask = (1<<81)-1
        else:
            mask = ((1<<(sb+1)*9)-1)^((1<<sb*9)-1)
        haspiece = self.o|self.x
        return mask&~haspiece
    def getsb(self,sb,player)->int:
        mask = ((1<<(sb+1)*9)-1)^((1<<sb*9)-1)
        if player==1:
            tmp = mask&self.o
        elif player==2:
            tmp = mask&self.x
        return tmp>>(sb*9)
class SmallBoard:
    def __init__(self,raw:list)->None: #takes in a 3x3 board and converts it to a bitboard
        self.o = 0
        self.x = 0
        self.d = 0
        for i in range(9):
            if raw[i]==1:
                self.o|=(1<<i)
            elif raw[i]==2:
                self.x|=(1<<i)
            elif raw[i]==3:
                self.d|=(1<<i)
    def seto(self,move)->None: #move is of bit string format
        self.o|=move
    def setx(self,move)->None: #move is of bit string format
        self.x|=move
    def setd(self,move)->None: #move is of bit string format
        self.d|=move
    def getpiece(self,ind)->int: #returns piece on index ind
        if self.o&(1<<ind):
            return 1
        if self.x&(1<<ind):
            return 2
        if self.d&(1<<ind):
            return 3
        return 0
    def outputlist(self)->list:
        ret = []
        for i in range(9):
            if self.o&(1<<i):
                ret.append(1)
                continue
            if self.x&(1<<i):
                ret.append(2)
                continue
            if self.d&(1<<i):
                ret.append(3)
                continue
            ret.append(0)
        return ret
    def printbitboard(self)->None:
        for i in range(0,3):
            for j in range(0,3):
                print(self.getpiece(3*i+j),end=" ")
            print("\n",end="")
    def isdraw(self)->bool: #returns if game is a draw
        haspiece = self.o|self.x|self.d
        if(haspiece==(1<<9)-1):
            return 1
        return 0
    def iswon(self,player)->bool: #returns if game is won by player
        if player==1:
            tmp = self.o
        elif player==2:
            tmp = self.x
        for pat in WINNING:
            if(tmp&pat==pat):
                return 1
        return 0

def GetIndex(bb)->list:
    indexes = []
    while bb:
        lsb = bb&-bb
        indexes.append(lsb)
        bb &= bb-1
    return indexes
def Popmove(bb):
    ret = bb&-bb
    bb&=bb-1
    return ret
def main():
    raw = [1,1,1,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            1,1,1,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0]
    sb = SmallBoard([0,0,0,0,0,0,0,0,0])
    bb = BitBoard(raw)
    print(bb.getsb(2,1))
if __name__ == '__main__':
    main()