import pygame
from settings import TILESIZE

MAP_DATA = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def is_walkable(col, row):
    if row < 0 or row >=len(MAP_DATA):
        return False
    if col < 0 or col >= len(MAP_DATA[row]):
        return False
    return MAP_DATA[row][col] == 0

