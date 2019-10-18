import pygame

#holds all colliders
rect_list = []
#holds position of all colliders
rect_pos_list = []

def add_collider(x, y):
    rect = pygame.Rect(x*32, y*32, 32, 32)
    rect_list.append(rect)
    rect_pos_list.append((x*32, y*32))

def get_colliders():
    return rect_list

def get_colliders_pos():
    return rect_pos_list

def draw_colliders(window):
    for c in rect_list:
        pygame.draw.rect(window, [255, 0, 0], c, 1)

def is_collide(id):
    if id == 36 or id == 34 or id == 258 or id == 257 or id == 33 or id == 66 or id == 35 or id == 323 or id == 98:
        return True
    else:
        return False
