import pygame

rect_list = []

def add_collider(window, x, y):
    rect = pygame.rect = (x*32, y*32, 32, 32)
    pygame.draw.rect(window, [255, 0, 0], rect, 1)
    rect_list.append(rect)

def get_collider():
    return rect_list

def is_collide(id):
    if id == 36 or id == 34 or id == 258 or id == 257 or id == 33 or id == 66 or id == 35 or id == 323:
        return True
    else:
        return False
