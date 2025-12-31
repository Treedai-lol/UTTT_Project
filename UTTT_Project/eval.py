import lib

def GetMoves(board:lib.Board) ->list:
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
def Search(board:lib.Board,o:bool,depth:int):
    while depth>0:
        wl = GetMoves(board)
        for i in wl:
            print(i)
            #lib.MakeMove(board,o,i[0],i[1])

def main():
    board = lib.BoardInit()
    o = True
    Search(board,o,1)
if __name__ == '__main__':
    main()