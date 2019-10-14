import pygame
import pygame.locals
import tileset
import keyboard
from player import player
pygame.init()

screenWidth = tileset.tile_size * tileset.map_width
screenHeight = tileset.tile_size * tileset.map_height


window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Dude.Game')

clock = pygame.time.Clock()

table = tileset.load_tile_table("res/bettertileset.png",tileset.tile_size, tileset.tile_size)
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    keyboard.events(player)
    #player.update(keys)

    redrawGameWindow()
pygame.quit()
