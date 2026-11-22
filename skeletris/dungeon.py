import pygame
from settings import TILESIZE

WALL_COLOR = (65, 72, 90)
FLOOR_COLOR = (42, 46, 58)

MAP_DATA = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def is_walkable(col, row):
    if row < 0 or row >=len(MAP_DATA):
        return False
    if col < 0 or col >= len(MAP_DATA[row]):
        return False
    return MAP_DATA[row][col] == 0

def draw_map(screen):
    for row in range(len(MAP_DATA)):
        for col in range(len(MAP_DATA[row])):
            color = WALL_COLOR if MAP_DATA[row][col] == 1 else FLOOR_COLOR
            rect = pygame.Rect(col*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, color, rect)