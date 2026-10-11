import random
import pygame

pygame .init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("DinoGame")
font = pygame.font.SysFont("Arial", 45)
big_font = pygame.font.SysFont("Arial", 80)
color = (135, 195, 235)

GROUND_Y = 330
dino = pygame.Rect(80, GROUND_Y-50, 60, 70)
dino_image = pygame.image.load("./assets/images/dino.png").convert_alpha()
dino_image = pygame.transform.scale(dino_image, (60, 70))
DINO_Speed = 10

dino_velocity_y= 0
GRAVITY = 1
JUMP_SPEED = -16
on_ground = True

cactus = pygame.Rect(850, GROUND_Y - 60, 30, 60)

game_over = False

score = 0.0

clock = pygame.time.Clock()

running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and on_ground and not game_over:
                                dino_velocity_y = JUMP_SPEED
                                on_ground = False
                        if event.key == pygame.K_r and game_over:
                                dino.topleft = (80, GROUND_Y-50)
                                cactus.topleft = (850, GROUND_Y - 60)
                                on_ground = True
                                game_over = False
                                score = 0.0
        if not game_over:   
                score += 0.1
                cactus_speed = 7 + int(score) // 100
                                     
                dino_velocity_y += GRAVITY
                dino.y += dino_velocity_y
                if dino.bottom >= GROUND_Y:
                        dino.bottom = GROUND_Y
                        dino_velocity_y = 0
                        on_ground = True
                
                cactus.x -= cactus_speed
                if cactus.right < 0:
                        cactus.x = WIDTH +  random.randint(150, 400)
                
                if dino.colliderect(cactus):
                        game_over = True              
        
        screen.fill(color)
        pygame.draw.rect(screen, (80, 180, 80), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
        screen.blit(dino_image, dino)
        pygame.draw.rect(screen, (20, 140, 40), cactus)
        pygame.draw.circle(screen, (200, 190, 0), (WIDTH-100, 100), 30)
        score_text = font.render(f"Score: {int(score)}", True, (30, 30, 30))
        screen.blit(score_text, (20, 20))
        
        if game_over:
                text = font.render("Game Over! Press R to Restart", True, (200, 0, 0))
                screen.blit(text, (200, 150))
        
        pygame.display.flip()
        clock.tick(60) #60FPS
        
        # #levo i desno kretanje
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #         dino.x -= DINO_Speed
        # if keys[pygame.K_a]:
        #         dino.x -= DINO_Speed
        # if keys[pygame.K_RIGHT]:
        #         dino.x += DINO_Speed
        # if keys[pygame.K_d]:
        #         dino.x += DINO_Speed   

        # if dino.left < 0:
        #         dino.left = 0
        # if dino.right > WIDTH:
        #         dino.right = WIDTH
pygame.quit()