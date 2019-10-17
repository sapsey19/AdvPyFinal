import pygame
import pygame.image as img

#animations
walkUp = [img.load('res/runu1.png'), img.load('res/runu2.png'), img.load('res/runu3.png'), img.load('res/runu1.png'), img.load('res/runu2.png'), img.load('res/runu3.png')]
walkDown = [img.load('res/rund1.png'), img.load('res/rund2.png'), img.load('res/rund3.png'), img.load('res/rund1.png'), img.load('res/rund2.png'), img.load('res/rund3.png')]
walkLeft = [img.load('res/runl1.png'), img.load('res/runl2.png'), img.load('res/runl3.png'), img.load('res/runl1.png'), img.load('res/runl2.png'), img.load('res/runl3.png')]
walkRight = [img.load('res/runr1.png'), img.load('res/runr2.png'), img.load('res/runr3.png'), img.load('res/runr1.png'), img.load('res/runr2.png'), img.load('res/runr3.png')]
scaled_size = 1.5
player_width, player_height = walkUp[0].get_size()
for i in range(0, len(walkUp)):
    temp = pygame.transform.scale(walkUp[i], (int(player_width*scaled_size), int(player_height*scaled_size)))
    walkUp[i] = temp
    temp = pygame.transform.scale(walkDown[i], (int(player_width*scaled_size), int(player_width*scaled_size)))
    walkDown[i] = temp
    temp = pygame.transform.scale(walkRight[i], (int(player_width*scaled_size), int(player_width*scaled_size)))
    walkRight[i] = temp
    temp = pygame.transform.scale(walkLeft[i], (int(player_width*scaled_size), int(player_width*scaled_size)))
    walkLeft[i] = temp
idle = walkDown[1]

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xvel = 0
        self.yvel = 0
        self.speed = 6
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.last_pressed = 3

    def get_pos(self):
        player_pos = (self.x, self.y)
        return (self.x, self.y)

    def get_collider(self):
        rect = pygame.Rect(self.x + 8, self.y, 30, 44)
        #pygame.draw.rect(window, [0, 255, 0], rect, 1)
        return rect

    def draw(self, window):
        rect = (self.x + 8, self.y + 4, 32, 48)
        pygame.draw.rect(window, [0, 255, 0], rect, 1)
        if self.walkCount >= 30:
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[self.walkCount//5], (self.x, self.y))
            self.walkCount += 1
            self.last_pressed = 0
        elif self.right:
            window.blit(walkRight[self.walkCount//5], (self.x, self.y))
            self.walkCount += 1
            self.last_pressed = 1
        elif self.up:
            window.blit(walkUp[self.walkCount//5], (self.x, self.y))
            self.walkCount += 1
            self.last_pressed = 2
        elif self.down:
            window.blit(walkDown[self.walkCount//5], (self.x, self.y))
            self.walkCount += 1
            self.last_pressed = 3
        else:
            if self.last_pressed == 0:
                window.blit(walkLeft[1], (self.x, self.y))
            if self.last_pressed == 1:
                window.blit(walkRight[1], (self.x, self.y))
            if self.last_pressed == 2:
                window.blit(walkUp[1], (self.x, self.y))
            if self.last_pressed == 3:
                window.blit(walkDown[1], (self.x, self.y))
    def update(self):
        if self.left:
            self.xvel = -1
        if self.right:
            self.xvel = 1
        if self.up:
            self.yvel = -1
        if self.down:
            self.yvel = 1

        self.x += self.xvel * self.speed
        self.y += self.yvel * self.speed
        self.xvel = 0
        self.yvel = 0
