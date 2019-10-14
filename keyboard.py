import pygame

def events(player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.xvel:
        player.xvel = -1
        player.left = True
        player.right = False
    elif keys[pygame.K_RIGHT] and player.x < 1024 - player.width - player.xvel:
        player.xvel = 1
        player.right = True
        player.left = False
    elif keys[pygame.K_UP] == False and keys[pygame.K_DOWN] == False:
        player.right = False
        player.left = False
        player.walkCount = 0
    if keys[pygame.K_UP] and player.y > player.yvel:
        player.yvel = -1
        player.up = True
        player.down = False
    elif keys[pygame.K_DOWN] and player.y < 1024 - player.height - player.yvel:
        player.yvel = 1
        player.down = True
        player.up = False
    elif keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
        player.down = False
        player.up = False
        player.walkCount = 0

    player.x += player.xvel * player.speed
    player.y += player.yvel * player.speed
    player.xvel = 0
    player.yvel = 0
