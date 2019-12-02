import pygame
import pygame.locals
import tileset
import keyboard
from player import player
import collider
from enemy import bat

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
bat = bat(300, 300, 32, 32)

def redrawGameWindow():
    tileset.draw_map(window)
    player.draw(window)
    bat.draw(window)
    #collider.draw_colliders(window)
    pygame.display.update()

def howtoscreen():
    howto = pygame.image.load('res/howtoimg.png')
    close = pygame.image.load('res/close.png')
    msg = True
    window.blit(howto, (234, 234))
    window.blit(close, (324, 454))
    while msg == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)
        print(click)
        if  444 > mouse[0] > 324 and 514 > mouse[1] > 454:
            window.blit(howto, (234, 234))
            window.blit(close, (324, 454))
            
            if click[0] == 1:
                msg = False
                print(msg)        
        else:
            window.blit(howto, (234, 234))
            window.blit(close, (324, 454))
        pygame.display.update()


def button1(x, y, w, h, img):
    intro = True
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        window.blit(img, (x, y))
        
        if click[0] == 1:
            intro = False        
    else:
        window.blit(img, (x, y))
    return intro


def button2(x, y, w, h, img):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        window.blit(img, (x, y))
        
        if click[0] == 1:
            howtoscreen()        
    else:
        window.blit(img, (x, y))

def button3(x, y, w, h, img):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        window.blit(img, (x, y))
        
        if click[0] == 1:
            pygame.quit()
            quit()      
    else:
        window.blit(img, (x, y))


#main game loop
avg_fps = 0
count = 0

def game_title():
    intro = True
    title = pygame.image.load('res/Title.png')
    btn1 = pygame.image.load('res/newgame.png')
    btn2 = pygame.image.load('res/howto.png')
    btn3 = pygame.image.load('res/quit.png')

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        window.blit(title, (0, 0))
        intro = button1(244, 309, 280, 70, btn1)
        button2(244, 429, 280, 70, btn2)
        button3(244, 549, 280, 70, btn3)
        pygame.display.update()
        clock.tick(15)

def game_loop():
    run = True
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
        bat.move_towards_player(player)
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

game_title()
game_loop()

pygame.quit()
