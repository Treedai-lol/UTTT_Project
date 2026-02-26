class Board():
    def __init__(self, bs:list, wonboards:list, o:bool, gg:bool, sb:int) -> None:
        self.bs = bs
        self.o = o
        self.wonboards = wonboards
        self.gg = gg
        self.sb = sb
    def PrintBoard(self) ->None: #print board function
        for i in range(0,3):
            for j in range(0,3):
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        print(self.bs[k][l],end=" ")
                print("\n",end="")
            pass
        pass
    def GetOwnerShip(self,index:int,o:bool) ->list: #returns the indices of pieces owned
        output = []
        if o:
            for i in range(0,9):
                if  self.bs[index][i] == 1:
                    output.append(i)
        else:
            for i in range(0,9):
                if  self.bs[index][i] == 2:
                    output.append(i)
        return output
    def BoardFinished(self,index:int,o:bool) ->bool: #returns whether the board has been finished
        output = False
        piecelist = self.GetOwnerShip(index,o)
        winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in winning:
            a = b = c = False
            for j in piecelist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a & b & c:
                output = True
        if output & o == True:
            self.wonboards[index] = 1
        elif output:
            self.wonboards[index] = 2
        return output
    def GameFinished(self,o:bool) ->bool: #returns whether the game has been finished
        output = False
        tmp = self.wonboards
        piecelist = []
        if o:
            for i in range(0,9):
                if  tmp[i] == 1:
                    piecelist.append(i)
        else:
            for i in range(0,9):
                if  tmp[i] == 2:
                    piecelist.append(i)
        a = b = c = False
        winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in winning:
            for j in piecelist:
                if j == i[0]:
                    a = True
                if j == i[1]:
                    b = True
                if j == i[2]:
                    c = True
            if a & b & c:
                output = True
        self.gg = output
        return output
    def InputMove(self,player:str) ->list: #takes "ab" as input, puts piece on board a, position b
        ret = []
        temp =  input(player+"'s turn, please make a move")
        temp = int(temp)
        ret.append(int((temp-temp%10)/10))
        ret.append(temp%10)
        return ret
    def VerifyMove(self,a:int,b:int) ->int: #checks if the move is allowed
        if a>8 or b>8: #check if index is in range
            return 1 
        elif self.bs[a][b] != 0: #check if square is occupied
            return 2 
        elif a != self.sb and self.sb!=9: #check if the UTTT rule applies 
            return 3
        elif self.wonboards[a] != 0: #check if the board is won
            return 4
        else: #all good
            return 0
    def MakeMove(self,o:bool,a:int,b:int) ->None: #The target square MUST be empty
        self.sb = b
        if o:
            self.bs[a][b] = 1
        else:
            self.bs[a][b] = 2
    def StartRound(self,o:bool) ->None: #some jumbled up shit
        a = b = 99
        self.PrintBoard()
        if o:
            player = "O"
        else:
            player = "X"
        temp = self.InputMove(player)
        a = temp[0]
        b = temp[1]
        if self.VerifyMove(a,b) == 0:
            self.MakeMove(o,a,b)
        else:
            print("error "+str(self.VerifyMove(a,b)))
            return
        self.BoardFinished(a,o)
        if self.wonboards[b] != 0:
            self.sb = 9
        else:
           self.sb = b
        self.GameFinished(o)
        self.o = not o
def BoardInit() ->Board:
    list = []
    """for i in range(0,9):
        list.append([])
        for j in range(0,9):
            list[i].append(0)"""
    list = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    wb = [0,0,0,0,0,0,0,0,0]
    board = Board(list,wb,True,False,9)
    return board
def main():
    board = BoardInit()
    while not board.gg:
        board.StartRound(board.o)
        print(board.wonboards)
    print("GAME OVER")
if __name__ == '__main__':
    main()