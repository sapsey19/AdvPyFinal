import pygame
import pygame.image as img

#list of animations
walkUp = [img.load('res/runu1.png'), img.load('res/runu2.png'), img.load('res/runu3.png'), img.load('res/runu1.png'), img.load('res/runu2.png'), img.load('res/runu3.png')]
walkDown = [img.load('res/rund1.png'), img.load('res/rund2.png'), img.load('res/rund3.png'), img.load('res/rund1.png'), img.load('res/rund2.png'), img.load('res/rund3.png')]
walkLeft = [img.load('res/runl1.png'), img.load('res/runl2.png'), img.load('res/runl3.png'), img.load('res/runl1.png'), img.load('res/runl2.png'), img.load('res/runl3.png')]
walkRight = [img.load('res/runr1.png'), img.load('res/runr2.png'), img.load('res/runr3.png'), img.load('res/runr1.png'), img.load('res/runr2.png'), img.load('res/runr3.png')]
#scales the player size
scaled_size = 1.25

player_width, player_height = walkUp[0].get_size()
#scales the player's size
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
        self.speed = 3
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.last_pressed = 3
        self.top_rect = pygame.Rect(x, y, 32, 48)
        #self.bottom_rect = pygame.Rect(x, y, 32, 48)
        self.left_rect = pygame.Rect(x, y, 32, 48)
        self.right_rect = pygame.Rect(x, y, 32, 48)

    def get_pos(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_top_collider(self):
        self.top_rect = pygame.Rect(self.x + 17, self.y + 20, 15, 30)
        return self.top_rect

    def get_left_collider(self):
        self.left_rect = pygame.Rect(self.x + 10, self.y + 25, 5, 25)
        return self.left_rect

    def get_right_collider(self):
        self.right_rect = pygame.Rect(self.x + 32, self.y + 25, 5, 25)
        return self.right_rect

    def draw(self, window):
        if self.walkCount >= 60:
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[self.walkCount//10], (self.x, self.y))
            self.walkCount += 1
            self.last_pressed = 0
        elif self.right:
            window.blit(walkRight[self.walkCount//10], (self.x, self.y))
            self.walkCount += 1
            self.last_pressed = 1
        elif self.up:
            window.blit(walkUp[self.walkCount//10], (self.x, self.y))
            self.walkCount += 1
            self.last_pressed = 2
        elif self.down:
            window.blit(walkDown[self.walkCount//10], (self.x, self.y))
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

        #pygame.draw.rect(window, [0, 255, 0], self.top_rect, 1)
        #pygame.draw.rect(window, [255, 0, 0], self.left_rect, 1)
        #pygame.draw.rect(window, [0, 255, 255], self.right_rect, 1)

    def update(self):
        if self.left:
            self.xvel = -1
        if self.right:
            self.xvel = 1
        if self.up:
            self.yvel = -1
        if self.down:
            self.yvel = 1

        #updates player's position
        self.x += self.xvel * self.speed
        self.y += self.yvel * self.speed
        self.xvel = 0
        self.yvel = 0
