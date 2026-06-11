foo = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
WINNING = [7, 56, 448, 73, 146, 292, 273, 84]
class BitBoard:
    def __init__(self,raw:list):
        self.o = 0
        self.x = 0
        for i in range(81):
            if raw[i]==1:
                self.o|=(1<<i)
            elif raw[i]==2:
                self.x|=(1<<i)
    def seto(self,move):
        self.o|=move
    def setx(self,move):
        self.x|=move
    def clear(self,ind):
        self.o&= ~(1<<ind)
        self.x&= ~(1<<ind)
    def getpiece(self,ind):
        if self.o&(1<<ind):
            return 1
        if self.x&(1<<ind):
            return 2
        return 0
    def isempty(self,ind):
        return bool(((self.x>>ind)&1)|((self.o>>ind)&1))
    def outputlist(self):
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
    def printbitboard(self):
        for i in range(0,3):
            for j in range(0,3):
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        print(self.getpiece(9*k+l),end=" ")
                    print(" ",end="")
                print("\n",end="")
            print("\n",end="")
    def isdraw(self,sb):
        mask = ((1<<(sb+1)*9)-1)^((1<<sb*9)-1)
        haspiece = self.o|self.x
        if(mask&haspiece==mask):
            return 1
        return 0
    def iswon(self,sb,player):
        mask = ((1<<(sb+1)*9)-1)^((1<<sb*9)-1)
        if player==1:
            tmp = mask&self.o
        elif player==2:
            tmp = mask&self.x
        for pat in WINNING:
            if(tmp==(pat<<sb*9)):
                return 1
        return 0
    def getmoves(self,sb):
        if sb==9:   
            mask = (1<<81)-1
        else:
            mask = ((1<<(sb+1)*9)-1)^((1<<sb*9)-1)
        haspiece = self.o|self.x
        return mask&~haspiece
def GetIndex(bb):
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
    raw =  [0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0]
    bb = BitBoard(raw)
    print(GetIndex(bb.getmoves(9)))
if __name__ == '__main__':
    main()