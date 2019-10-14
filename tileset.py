import pygame
import pygame.locals
from functools import reduce


def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    '''
    for tile_x in range(0, image_width//width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height//height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    '''
    for tile_x in range(0, image_height//height):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_width//width):
            rect = (tile_y*height, tile_x*width, height, width)
            line.append(image.subsurface(rect))
    return tile_table

def draw_map(window, table):
    f = open('res/map3.txt')
    block_id_list = reduce(lambda z, y :z + y, table)
    map_id = f.read().split(',')
    map_id = [x.split('\n') for x in map_id]
    map_id = reduce(lambda z, y :z + y, map_id)
    map_id.remove('')
    map_id = [int(i) for i in map_id]
    counter = 0
    for y in range(0, 32):
        for x in range(0, 32):
            window.blit(block_id_list[map_id[counter]], (x*16, y*16))
            counter += 1

'''
def draw_map(window, table):
    f = open('res/map2.txt', 'r')
    coords = []
    for l in f:
        coords.append(l.split(' '))
    for y in range(0, len(coords)):
        for x in range(0, len(coords[0])):
            #some convoluted way of getting the coordinates for the spritesheet
            x_source = coords[y][x][0].split(',')
            y_source = coords[y][x][2].split(',')
            x_val = int(x_source[0])
            y_val = int(y_source[0])
            window.blit(table[x_val][y_val], (x*32, y*32))
'''
