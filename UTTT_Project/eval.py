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
    wb = board.wonboards
    



def main():
    board = lib.BoardInit()
    lib.StartRound(board,True)
    print(GetMoves(board))
if __name__ == '__main__':
    main()