import pygame

pygame .init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("DinoGame")

color = (35, 95, 135)

GROUND_Y = 330
dino = pygame.Rect(80, GROUND_Y-50, 45, 50)
DINO_Speed = 10

clock = pygame.time.Clock()

running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        screen.fill(color)
        pygame.draw.rect(screen, (80, 180, 80), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
        pygame.draw.rect(screen, (40, 40, 40), dino)

        pygame.draw.circle(screen, (200, 190, 0), (WIDTH-100, 100), 30)
        
        pygame.display.flip()
        clock.tick(60) #60FPS
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                dino.x -= DINO_Speed
        if keys[pygame.K_RIGHT]:
                dino.x += DINO_Speed
        
        if dino.left < 0:
                dino.left = 0
        if dino.right > WIDTH:
                dino.right = WIDTH
pygame.quit()