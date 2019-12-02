import pygame
import pygame.image as img
import math


fly = [img.load('res/bat1.png'), img.load('res/bat2.png'), img.load('res/bat3.png')]

scaled_size = 1.25

bat_width, bat_height = fly[0].get_size()

for i in range(0, len(fly)):
    temp = pygame.transform.scale(fly[i], (int(bat_width*scaled_size), int(bat_height*scaled_size)))
    fly[i] = temp

class bat(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.flapCount = 0
        self.rect = pygame.Rect(x, y, 32, 32)
        self.speed = 3

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
        if self.flapCount >= 30:
            self.flapCount = 0
        window.blit(fly[self.flapCount//10], (self.x, self.y))
        self.flapCount += 1

    def move_towards_player(self, player):
        dx, dy = player.get_pos()
        diff_x = dx - self.x
        diff_y = dy - self.y
        angle = math.degrees(math.atan2(diff_x, diff_y))
        self.x += self.speed * math.cos(angle)
        self.y -= self.speed * math.sin(angle)
