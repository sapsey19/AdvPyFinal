import pygame
import pygame.locals
from player import player
import tileset

pygame.init()

screenWidth = 32*16
screenHeight = 32*16
tile_width = 16
tile_height = 16

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Dude.Game')

clock = pygame.time.Clock()

table = tileset.load_tile_table("res/bettertileset.png", tile_width, tile_height)
tileset.draw_map(window, table)
player = player(200, 300, 32, 32)

def redrawGameWindow():
    tileset.draw_map(window, table)
    player.draw(window)
    pygame.display.update()

run = True
#main game loop
while run:
    clock.tick(60)
    #list of events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #list of keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    #checks what key is pressed, and checkes for out of bounds

    if keys[pygame.K_LEFT] and player.x > player.xvel:
        player.xvel = -1
        player.left = True
        player.right = False
    elif keys[pygame.K_RIGHT] and player.x < screenWidth - player.width - player.xvel:
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
    elif keys[pygame.K_DOWN] and player.y < screenHeight - player.height - player.yvel:
        player.yvel = 1
        player.down = True
        player.up = False
    elif keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
        player.down = False
        player.up = False
        player.walkCount = 0
    #updates player x and y positions
    player.x += player.xvel * player.speed
    player.y += player.yvel * player.speed
    player.xvel = 0
    player.yvel = 0

    redrawGameWindow()
pygame.quit()
