import lib
import numpy as np
import tensorflow as tf
def encode(board:lib.Board):
    obs = []
    xbs = []
    sbs = []
    bs = board.bs
    for i in range(9):
        for j in range(9):
            if bs[i][j] == 1:
                obs.append(1)
            elif bs[i][j] == 2:
                xbs.append(1)
            else:
                obs.append(0)
                xbs.append(0)
            if i == board.sb or board.sb == 9:
                sbs.append(1)
            else:
                sbs.append(0)
    