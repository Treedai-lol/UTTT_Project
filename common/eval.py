from lib import Board
from lib import BoardInit
#Eval functions return a value from -1 to 1, with -100 and 100 meaning game over. positive is good for O
rtlc = [[0,1],[0,3],[0,4],[1,2],[1,4],[2,4],[2,5],[3,4],[3,6],[4,5],[4,6],[4,7],[4,8],[5,8],[6,7],[7,8]]
rblc = [2,6,8,0,7,6,8,5,0,3,2,1,0,2,8,6]
rtls = [[0,2],[0,6],[0,8],[1,7],[2,6],[2,8],[3,5],[6,8]]
rbls = [1,3,4,4,4,5,4,7]
rwin = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
win = [7,56,448,73,146,292,273,168]
tlc=[3,9,17,6,18,20,36,24,72,48,80,144,272,288,192,384]
blc=[4,64,256,1,128,64,256,32,1,8,4,2,1,4,256,64]
tls=[5,65,257,130,68,260,40,320]
bls=[2,8,16,16,16,32,16,128]
val1 = 100
val2 = -100
val3 = 100
val4 = -100
#the smoother should take in values from 0 to 2240
#any value above 280 is worth little
#TODO:MAKE SMOOTHER NOT HAVE MAGIC NUMBERS!!!
def MagicalFlatten(r:int)->float:
    if r<=0:
        return 0
    if r==100:
        return 0.5
    if r==200:
        return 0.8
    if r==300:
        return 0.85
    if r==400:
        return 0.88
    if r>=500:
        return 0.9
def ModSig(r:int)->float: #accepts non-negative integers and compresses them into 0 to 1 range
    if r<280:
        return 0.9*r/280
    return (r+17360)/2240
def Eval(board:Board) ->int:
    r = board.GameFinished()
    if r==1:
        return 100
    if r==2:
        return -100
    if r==3:
        return 0
    o_score = [0,0,0,0,0,0,0,0,0]
    x_score = [0,0,0,0,0,0,0,0,0]
    o_eval = 0
    x_eval = 0
    boards_to_eval = [0,1,2,3,4,5,6,7,8]
    for i in range(9):
        if (board.wonboards.o)&(1<<i)==(1<<i):
            boards_to_eval.remove(i)
            o_score[i] = 1
        if (board.wonboards.x)&(1<<i)==(1<<i):
            boards_to_eval.remove(i)
            x_score[i] = 1
        if (board.wonboards.d)&(1<<i)==(1<<i):
            boards_to_eval.remove(i)

    for sb in boards_to_eval:
        for i in range(len(tlc)):
            if (board.bs.o&(tlc[i]<<(sb*9)))==(tlc[i]<<(sb*9)):
                o_score[sb]+=val1
                if (board.bs.x&(blc[i]<<(sb*9)))==(blc[i]<<(sb*9)):
                    o_score[sb]+=val2
        for i in range(len(tls)):
            if (board.bs.o&(tls[i]<<(sb*9)))==(tls[i]<<(sb*9)):
                o_score[sb]+=val3
                if (board.bs.x&(bls[i]<<(sb*9)))==(bls[i]<<(sb*9)):
                    o_score[sb]+=val4
    for sb in boards_to_eval:
        for i in range(len(tlc)):
            if (board.bs.x&(tlc[i]<<(sb*9)))==(tlc[i]<<(sb*9)):
                x_score[sb]+=val1
                if (board.bs.o&(blc[i]<<(sb*9)))==(blc[i]<<(sb*9)):
                    x_score[sb]+=val2
        for i in range(len(tls)):
            if (board.bs.x&(tls[i]<<(sb*9)))==(tls[i]<<(sb*9)):
                x_score[sb]+=val3
                if (board.bs.o&(bls[i]<<(sb*9)))==(bls[i]<<(sb*9)):
                    x_score[sb]+=val4
    for i in boards_to_eval:
        o_score[i] = MagicalFlatten(o_score[i])
        x_score[i] = MagicalFlatten(x_score[i])
    for i in rwin:
        o_eval+=(o_score[i[0]]*o_score[i[1]]*o_score[i[2]])
        x_eval+=(x_score[i[0]]*x_score[i[1]]*x_score[i[2]])
    #print(o_score)
    #print(x_score)
    #print(o_eval)
    #print(x_eval)
    #print(o_eval-x_eval)
    return (o_eval-x_eval)

def main():
    b = BoardInit(3)
    Eval(b)
    
if __name__== '__main__':
    main()

"""
two in a line(continuous, no potential)
13/15/37/57
two in a line continuous,blocked
01/03/04/12/14/24/25/34/36/45/46/47/48/58/67/78
2/6/8/0/7/6/8/5/0/3/2/1/0/2/8/6
two in a line seperated,blocked
02/06/08/17/26/28/35/68
1/3/4/4/4/5/4/7
three in a line (win)
012/345/678/036/147/258/048/357
[7,56,448,73,146,292,273,168]
double two in a line(straight and diagonal)(3 potential)
014/034/245/214/854/874/674/634
double two in a line(both straight,through mid)
134/145/457/347
double two in a line(both straight, corner)
013/125/578/367
double two in a line(both diagonal)
024/248/468/046
tln=[10,34,136,160]
tlc=[3,9,17,6,18,20,36,24,72,48,80,144,272,288,192,384]
blc=[4,64,256,1,128,64,256,32,1,8,4,2,1,4,256,64]
tls=[5,65,257,130,68,260,40,320]
bls=[2,8,16,16,16,32,16,128]
win=[7,56,448,73,146,292,273,168]
[19,25,52,22,304,400,208,88]
[26,50,176,152]
[11,38,416,200]
[21,276,336,81]
"""