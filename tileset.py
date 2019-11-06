import pygame
import pygame.locals
from functools import reduce
import collider

map_image_list = []

map_width = 32
map_height = 32
tile_size = 32

#takes tilesheet and chops in into a 2d list
def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    width = 16
    height = 16
    for tile_x in range(0, image_height//height):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_width//width):
            rect = (tile_y*width, tile_x*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

#loads the map, adds recangle colliders to walls
def load_map(table):
    f = open('res/map.txt')
    #flattens 2d array of images
    block_id_list = reduce(lambda z, y :z + y, table)
    #gets block ID's for map
    map_id = f.read().split(',')
    map_id = [x.split('\n') for x in map_id]
    map_id = reduce(lambda z, y :z + y, map_id)
    map_id.remove('')
    map_id = [int(i) for i in map_id]
    counter = 0
    for y in range(0, map_width):
        for x in range(0, map_height):
            #scaled image allows for increasing or decreasing of tilesheet blocks
            scaled_image = pygame.transform.scale(block_id_list[map_id[counter]], (tile_size, tile_size))
            map_image_list.append(scaled_image)
            if collider.is_collide(map_id[counter]):
                collider.add_collider(x, y)
            counter += 1
    return map_image_list

#draws the map to screen
def draw_map(window):
    counter = 0
    for y in range(0, map_width):
        for x in range(0, map_height):
            window.blit(map_image_list[counter], (x*tile_size, y*tile_size))
            counter += 1

def test_draw(window, scroll):
    counter = 0
    for y in range(0, map_width):
        for x in range(0, map_height):
            window.blit(map_image_list[counter], (x*tile_size-scroll[0], y*tile_size-scroll[1]))
            counter += 1
