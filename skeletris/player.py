import pygame
from settings import PLAYER_COLOR, TILESIZE
from dungeon import is_walkable

class Player:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.health = 100
        
    def move(self, dx, dy):
        new_col = self.col + dx
        new_row = self.row + dy
        if is_walkable(new_col, new_row):
            self.col = new_col
            self.row = new_row
        
    def draw(self, screen):
        x = self.col * TILESIZE
        y = self.row * TILESIZE

        rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
        pygame.draw.rect(screen, PLAYER_COLOR, rect)