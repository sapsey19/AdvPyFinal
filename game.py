import pygame
import pygame.locals
import tileset
import keyboard
from player import player
import collider
pygame.init()

screenWidth = tileset.tile_size * tileset.map_width
screenHeight = tileset.tile_size * tileset.map_height
WINDOW_SIZE = (screenWidth, screenHeight)
window = pygame.display.set_mode((screenWidth, screenHeight))
display = pygame.Surface((700, 700));
pygame.display.set_caption('Dude.Game')
clock = pygame.time.Clock()

table = tileset.load_tile_table("res/bettertileset.png", tileset.tile_size, tileset.tile_size)
tileset.load_map(table)
#(xpos, ypos, width, height)
player = player(200, 300, 32, 48)

def redrawGameWindow():
    #tileset.draw_map(window)
    tileset.test_draw(display, scroll)
    player.draw(display)
    collider.draw_colliders(display)
    window.blit(pygame.transform.scale(display, WINDOW_SIZE),(0,0))
    pygame.display.update()

run = True
#main game loop
avg_fps = 0
count = 0

true_scroll = [0,0]

while run:
    prev_x, prev_y = player.get_pos()
    clock.tick(60)
    display.fill((146, 244, 255))
    #list of events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    true_scroll[0] += (prev_x-true_scroll[0])
    true_scroll[1] += (prev_y-true_scroll[1])
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    #tileset.test_draw(display, scroll)
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
