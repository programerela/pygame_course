import pygame
from settings import WIDTH, HEIGHT, FPS, BACKGROUND_COLOR
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skeletris")
clock = pygame.time.Clock()

player = Player(3, 3)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)
            elif event.key == pygame.K_UP:
                player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
    
    screen.fill(BACKGROUND_COLOR)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()