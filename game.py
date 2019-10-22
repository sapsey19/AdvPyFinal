import pygame
import pygame.locals
import tileset
import keyboard
from player import player
import collider
pygame.init()

screenWidth = tileset.tile_size * tileset.map_width
screenHeight = tileset.tile_size * tileset.map_height

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Dude.Game')
clock = pygame.time.Clock()

table = tileset.load_tile_table("res/bettertileset.png", tileset.tile_size, tileset.tile_size)
tileset.load_map(table)
#(xpos, ypos, width, height)
player = player(200, 300, 32, 48)

def redrawGameWindow():
    tileset.draw_map(window)
    player.draw(window)
    collider.draw_colliders(window)
    pygame.display.update()

run = True
#main game loop
avg_fps = 0
count = 0
while run:
    prev_x, prev_y = player.get_pos()
    clock.tick(60)
    #list of events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    #handles keyboard input
    keyboard.events(player)
    collider.check_collision(player, prev_x, prev_y)
    redrawGameWindow()

    #below prints the average fps every second, instead of 60 times per second
    '''
    avg_fps += clock.get_fps()
    count += 1
    if count == 60:
        print(avg_fps//60)
        count = 0
        avg_fps = 0
    '''
pygame.quit()
