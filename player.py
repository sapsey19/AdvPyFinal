import pygame
import pygame.image as img

walkUp = [img.load('res/runu1.png'), img.load('res/runu2.png'), img.load('res/runu3.png'), img.load('res/runu1.png'), img.load('res/runu2.png'), img.load('res/runu3.png')]
walkDown = [img.load('res/rund1.png'), img.load('res/rund2.png'), img.load('res/rund3.png'), img.load('res/rund1.png'), img.load('res/rund2.png'), img.load('res/rund3.png')]
walkLeft = [img.load('res/runl1.png'), img.load('res/runl2.png'), img.load('res/runl3.png'), img.load('res/runl1.png'), img.load('res/runl2.png'), img.load('res/runl3.png')]
walkRight = [img.load('res/runr1.png'), img.load('res/runr2.png'), img.load('res/runr3.png'), img.load('res/runr1.png'), img.load('res/runr2.png'), img.load('res/runr3.png')]
#idle = img.load('res/rund1.png')
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
idle = walkDown[2]

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xvel = 0
        self.yvel = 0
        self.speed = 2.5
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, window):
        if self.walkCount >= 60:
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[self.walkCount//10], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount//10], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            window.blit(walkUp[self.walkCount//10], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            window.blit(walkDown[self.walkCount//10], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(idle, (self.x, self.y))