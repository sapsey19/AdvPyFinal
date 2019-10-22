import pygame

#holds all colliders
rect_list = []
#holds position of all colliders
rect_pos_list = []
#list of block ids that should have a collider
collider_ids = [36, 34, 258, 257, 33, 66, 35, 323, 256, 290, 260, 227, 67, 98, 97]

def add_collider(x, y):
    rect = pygame.Rect(x*32, y*32, 32, 32)
    rect_list.append(rect)
    rect_pos_list.append((x*32, y*32))

#returns list of colliders
def get_colliders():
    return rect_list

#returns list of positions of colliders
def get_colliders_pos():
    return rect_pos_list

#draws the colliders (for debugging/testing)
def draw_colliders(window):
    for c in rect_list:
        pygame.draw.rect(window, [255, 0, 0], c, 1)

#checks if block id should have a collider
def is_collide(id):
<<<<<<< HEAD
    if id == 36 or id == 34 or id == 258 or id == 257 or id == 33 or id == 66 or id == 35 or id == 323 or id == 98:
=======
    if id in collider_ids:
>>>>>>> WIP
        return True
    else:
        return False

#checks if player's hitbox intersects with any wall colliders
def check_collision(player, prev_x, prev_y):
    for c in range(0, len(get_colliders())):
        if player.get_top_collider().colliderect(get_colliders()[c]):
            player.set_y(prev_y)
        if player.get_left_collider().colliderect(get_colliders()[c]) or player.get_right_collider().colliderect(get_colliders()[c]):
            player.set_x(prev_x)
