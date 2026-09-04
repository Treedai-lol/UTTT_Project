from lib import Board
from lib import BoardInit
#Eval functions return a value from -1 to 1, with -100 and 100 meaning game over. positive is good for O
def Eval(board:Board,o:bool) ->int:
    r = board.GameFinished()
    if r==1:
        return 100
    if r==2:
        return -100
    if r==3:
        return 0
    

def main():
    b = BoardInit()
    
if __name__== '__main__':
    main()

"""
two in a line
gimme01/03/04/12/13/14/15/24/25/34/36/37/45/46/47/48/57/58/67/78
3
9
17
6
10
18
34
20
36
24
72
136
48
80
144
272
160
288
192
three in a line
gimme012/345/678/036/147/258/048/357
7
56
448
73
146
292
273
"""