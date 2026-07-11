import pygame, sys, random
pygame.init()

W, H = 800, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()

player_y = 300
vel = 0
jumping = False
obstacle_x = 800
score = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if not jumping:
                jumping = True
                vel = -15
    
    screen.fill((135, 206, 235)) # sky
    pygame.draw.rect(screen, (34,139,34), (0, 350, W, 50)) # ground
    
    # jump
    if jumping:
        player_y += vel
        vel += 1
        if player_y >= 300:
            player_y = 300
            jumping = False
    
    # obstacle
    obstacle_x -= 6
    if obstacle_x < -50:
        obstacle_x = 800
        score += 1
    
    # draw
    pygame.draw.rect(screen, (255,0,0), (100, player_y, 50, 50)) # player
    pygame.draw.rect(screen, (139,69,19), (obstacle_x, 300, 50, 50)) # obstacle
    
    # score
    font = pygame.font.SysFont(None, 36)
    screen.blit(font.render(f'Score: {score}', True, (0,0,0)), (10,10))
    
    pygame.display.update()
    clock.tick(60)
