import pygame
from settings import PLAYER_COLOR, TILESIZE

class Player:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.health = 100
        
    def move(self, dx, dy):
        self.col += dx
        self.row += dy
        
    def draw(self, screen):
        x = self.col * TILESIZE
        y = self.row * TILESIZE

        rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
        pygame.draw.rect(screen, PLAYER_COLOR, rect)