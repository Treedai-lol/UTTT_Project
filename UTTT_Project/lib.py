class Board():
    def __init__(self, bs:list, wonboards:list, o:bool,gg:bool) -> None:
        self.bs = bs
        self.o = o
        self.wonboards = wonboards
        self.gg = gg
def PrintBoard(board:Board) ->None: #print board function
    for i in range(0,3):
        for j in range(0,3):
            for k in range(3*i,3*i+3):
                for l in range(3*j,3*j+3):
                    print(board.bs[k][l],end=" ")
            print("\n",end="")
        pass
    pass
def GetOwnerShip(board:Board,index:int,o:bool) ->list: #returns the indices of pieces owned
    output = []
    if o:
        for i in range(0,9):
            if  board.bs[index][i] == 1:
                output.append(i)
    else:
        for i in range(0,9):
            if  board.bs[index][i] == 2:
                output.append(i)
    return output
def BoardFinished(board:Board,index:int,o:bool) ->bool: #returns whether the board has been finished
    output = False
    piecelist = GetOwnerShip(board,index,o)
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
    if output & o == True:
        board.wonboards[index] = 1
    elif output:
        board.wonboards[index] = 2
    return output
def GameFinished(board:Board,o:bool) ->bool: #returns whether the game has been finished
    output = False
    tmp = board.wonboards
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
    board.gg = output
    return output

def GameStart(board:Board,o:bool):
    a = b = 99
    PrintBoard(board)
    if o:
        player = "O"
    else:
        player = "X"
    inpt = input(f"{player}'s turn, please make a move") #takes "ab" as input, puts piece on board a, position b
    a = int(inpt[0])
    b = int(inpt[1])
    if o:
        board.bs[a][b] = 1
    else:
        board.bs[a][b] = 2
    board.o = not o
    BoardFinished(board,a,o)
    GameFinished(board,o)
    PrintBoard(board)
    print(board.gg)
    if not board.gg:
        GameStart(board,not o)


def BoardInit() ->Board:
    list = []
    for i in range(0,9):
        list.append([])
        for j in range(0,9):
            list[i].append(0)
    """list[0][0] = 0
    list[0][1] = 0
    list[0][2] = 0
    list[0][3] = 0
    list[0][4] = 0
    list[0][5] = 0
    list[0][6] = 2
    list[0][7] = 2
    list[0][8] = 2"""
    wb = [1,1,1,0,0,0,0,0,0]
    """for i in range(0,9):
        wb.append(1)"""
    board = Board(list,wb,True,False)
    return board
def main():
    board = BoardInit()
    GameStart(board,True)
if __name__ == '__main__':
    main()