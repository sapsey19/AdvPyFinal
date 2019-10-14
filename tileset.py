import pygame
import pygame.locals
from functools import reduce

map_width = 32
map_height = 32
tile_size = 32

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    width = 16
    height = 16
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
            rect = (tile_y*width, tile_x*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

def draw_map(window, table):
    f = open('res/map3.txt')
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
            scaled_image = pygame.transform.scale(block_id_list[map_id[counter]], (tile_size, tile_size))
            #window.blit(block_id_list[map_id[counter]], (x*tile_size, y*tile_size))
            window.blit(scaled_image, (x*tile_size, y*tile_size))
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
