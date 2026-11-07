import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Icy Jump")


iceman = pygame.Rect(380, 450, 40, 50)
iceman_speed = 5

platform = pygame.Rect(250, 520, 300, 30)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                iceman.y -= 150
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        iceman.x -= iceman_speed
    if keys[pygame.K_RIGHT]:
        iceman.x += iceman_speed
    
    if iceman.right > WIDTH:
        iceman.right = WIDTH
    if iceman.left < 0:
        iceman.left = 0

    screen.fill((80, 120, 155))

    pygame.draw.rect(screen, (255, 255, 255), platform)
    pygame.draw.rect(screen, (0, 0, 255), iceman)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()