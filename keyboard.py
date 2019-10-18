import pygame

def events(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.right = True
        player.left = False
    if keys[pygame.K_LEFT]:
        player.left = True
        player.right = False
    if keys[pygame.K_UP]:
        player.up = True
        player.down = False
    if keys[pygame.K_DOWN]:
        player.down = True
        player.up = False
    if keys[pygame.K_LSHIFT]:
        player.speed = 4.5
    if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
        player.left = False
        player.right = False
    if keys[pygame.K_UP] == False and keys[pygame.K_DOWN] == False:
        player.up = False
        player.down = False
    if keys[pygame.K_LSHIFT] == False:
        player.speed = 3

    player.update()
