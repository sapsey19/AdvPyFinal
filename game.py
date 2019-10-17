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
tileset.draw_map(window, table)

#(xpos, ypos, width, height)
player = player(200, 300, 32, 48)

def redrawGameWindow():
    tileset.draw_map(window, table)
    player.draw(window)
    pygame.display.update()

run = True
player_rect = player.get_collider()
#main game loop
while run:
    clock.tick(30)
    #list of events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    #handles keyboard input
    keyboard.events(player)

    #this slows down the game a LOT, needs to be fixed
    for c in collider.get_collider():
        if player.get_collider().colliderect(c):
            print('Collide')
            player.x = 400
            player.y = 400

    redrawGameWindow()
    fps = clock.get_fps()
    print(fps)
pygame.quit()
