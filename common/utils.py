import math
def bitmask_to_index(bitmask): #converts (1<<5) into 5
    return int(math.log2(bitmask))
def popmove(bb): #takes in a bitmask and removes the least significant bit and returns the rest
    ret = bb&-bb
    bb&=bb-1
    return ret
def getindex(bb)->list: #turns 7 into [0,1,2]
    indexes = []
    while bb:
        lsb = bb&-bb
        indexes.append(lsb)
        bb &= bb-1
    return indexes