import random
import pygame

pygame .init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DinoGame")
font = pygame.font.SysFont("Arial", 45)
big_font = pygame.font.SysFont("Arial", 80)
color = (135, 195, 235)
GROUND_Y = 330

dino = pygame.Rect(80, GROUND_Y-50, 60, 70)
cactus = pygame.Rect(850, GROUND_Y - 60, 40, 60)
bird = pygame.Rect(850, GROUND_Y - 120, 50, 30)
play_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 35, 200, 70)

active_obsticle = cactus

run_images = [
        pygame.transform.scale(pygame.image.load("./assets/images/dino_left.png").convert_alpha(), dino.size),
        pygame.transform.scale(pygame.image.load("./assets/images/dino_right.png").convert_alpha(), dino.size)
]
cactus_image = pygame.image.load("./assets/images/cactus.png").convert_alpha()
cactus_image = pygame.transform.scale(cactus_image, (40, 60))

jump_sound = pygame.mixer.Sound("./assets/sounds/dragon-studio-cartoon-jump-463196.wav")
hit_sound = pygame.mixer.Sound("./assets/sounds/universfield-powerful-impact-hit-567212.wav")

DINO_Speed = 10
dino_velocity_y= 0
GRAVITY = 1
JUMP_SPEED = -16
BIRD_HEIGHTS = [
        GROUND_Y - 150,
        GROUND_Y - 110,
        GROUND_Y - 70
]
MIN_GAP= 50
MAX_GAP= 200

on_ground = True
score = 0.0
high_score = 0.0
game_over = False
game_started = False

animation_timer = 0
animation_index = 0

clock = pygame.time.Clock()

def reset_game():
        global dino_velocity_y, on_ground, game_over, score, active_obsticle, cactus, bird
        dino.topleft = (80, GROUND_Y-50)
        cactus.topleft = (850, GROUND_Y - 60)
        bird.topleft = (WIDTH + random.randint(MIN_GAP, MAX_GAP), random.choice(BIRD_HEIGHTS))
        active_obsticle = random.choice([cactus, bird])
        dino_velocity_y = 0
        on_ground = True
        game_over = False
        score = 0.0

running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if not game_started:
                                if play_button.collidepoint(event.pos):
                                        game_started = True
        
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and on_ground and not game_over:
                                dino_velocity_y = JUMP_SPEED
                                on_ground = False
                                jump_sound.play()
                        if event.key == pygame.K_r and game_over:
                                reset_game()
                                
        if not game_over and game_started:
                score += 0.1
                cactus_speed = 10 + int(score) // 100
                                     
                dino_velocity_y += GRAVITY
                dino.y += dino_velocity_y
                if dino.bottom >= GROUND_Y:
                        dino.bottom = GROUND_Y
                        dino_velocity_y = 0
                        on_ground = True
                
                active_obsticle.x -= cactus_speed
                if active_obsticle.right < 0:
                        active_obsticle = random.choice([cactus, bird])
                        obstacle_x = WIDTH + random.randint(MIN_GAP, MAX_GAP)
                        
                        if active_obsticle is cactus:
                                cactus.topleft = (obstacle_x, GROUND_Y - 60)
                        else:
                                bird.y = random.choice(BIRD_HEIGHTS)
                                bird.topleft = (obstacle_x, bird.y)
                
                if dino.colliderect(active_obsticle):
                        game_over = True
                        hit_sound.play() 
                              
                animation_timer += 1
                if animation_timer >= 8:
                        animation_timer = 0
                        animation_index = (animation_index + 1) % len(run_images)
                
                                   
        if not game_started:
                screen.fill(color)
                pygame.draw.rect(screen, (80, 180, 80), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
                text = big_font.render("Dino Game", True, (30, 30, 30))
                screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 150))
                pygame.draw.rect(screen, (0, 200, 0), play_button)
                play_text = font.render("Play", True, (255, 255, 255))
                screen.blit(play_text, (play_button.x + play_button.width//2 - play_text.get_width()//2,
                                        play_button.y + play_button.height//2 - play_text.get_height()//2))
                pygame.display.flip()
                clock.tick(60)
                continue
        
        screen.fill(color)
        pygame.draw.rect(screen, (80, 180, 80), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
        screen.blit(run_images[animation_index], dino)
        if active_obsticle is cactus:
                pygame.draw.rect(screen, (20,140,40), cactus)
        else:
                pygame.draw.rect(screen, (120, 70, 30), bird)
                
        pygame.draw.circle(screen, (200, 190, 0), (WIDTH-100, 120), 30)
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