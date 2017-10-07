import math

def hanoi_moves(n):
    if n == 0: return 0
    return 2 * hanoi_moves(n-1) + 1

