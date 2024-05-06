import pygame

# Create window
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Variables 
TILE_SIZE = 40

class World():
    def __init__(self, data):
        self.tile_list = []

        #load image
        dirt_img = pygame.image.load('img/tilesheets/Mossy Tileset/tile1.png')
        wall_img = pygame.image.load('img/tilesheets/Mossy Tileset/tile_wall_grass.png')
        left_down_corner_img = pygame.image.load('img/tilesheets/Mossy Tileset/corner_tile_grass.png')
        left_top_corner_img = pygame.image.load('img/tilesheets/Mossy Tileset/corner_tile_grass2.png')
        right_down_corner_img = pygame.image.load('img/tilesheets/Mossy Tileset/corner_tile_grass4.png')
        right_top_corner_img = pygame.image.load('img/tilesheets/Mossy Tileset/corner_tile_grass3.png')
        dark_img = pygame.image.load('img/tilesheets/Mossy Tileset/dark_tile.png')
        small_corner_top_left = pygame.image.load('img/tilesheets/Mossy Tileset/small_green_corner_topL.png')
        small_corner_right_TnB_R = pygame.image.load('img/tilesheets/Mossy Tileset/small_green_grass_T&B-R.png')
        small_corner_bottom_left = pygame.image.load('img/tilesheets/Mossy Tileset/small_green_corner_downL.png')
        small_corner_top_right = pygame.image.load('img/tilesheets/Mossy Tileset/small_green_corner_topR.png')
        grass_top_img = pygame.image.load('img/tilesheets/Mossy Tileset/grass_top.png')
        grass_wall_L = pygame.image.load('img/tilesheets/Mossy Tileset/grass_wall_left.png')
        grass_wall_R = pygame.image.load('img/tilesheets/Mossy Tileset/grass_wall_right.png')
        grass_bottom = pygame.image.load('img/tilesheets/Mossy Tileset/grass_bottom.png')
        grass_end_R = pygame.image.load('img/tilesheets/Mossy Tileset/grass_end_Right.png')
        small_grass_Top_LR = pygame.image.load('img/tilesheets/Mossy Tileset/small_green_grass_TnB_top.png')
        grass_end_top = pygame.image.load('img/tilesheets/Mossy Tileset/grass_end_top.png')
        small_corner_bottom_right = pygame.image.load('img/tilesheets/Mossy Tileset/small_green_corner_downR.png')
        small_corner_LnR_bottom = pygame.image.load('img/tilesheets/Mossy Tileset/small_green_LR_Bottom.png')
        grass_end_bottom = pygame.image.load('img/tilesheets/Mossy Tileset/grass_end_bottom.png')
        grass_end_left = pygame.image.load('img/tilesheets/Mossy Tileset/grass_end_Left.png')
        thorns_top = pygame.image.load('img/tilesheets/Mossy Tileset/Thorns_grass_top.jpg')

        tile_images = [
            dirt_img, wall_img, left_down_corner_img, left_top_corner_img, 
            right_down_corner_img, right_top_corner_img, dark_img, small_corner_top_left,
            small_corner_right_TnB_R, small_corner_bottom_left, grass_top_img, small_corner_top_right, 
            grass_wall_L, grass_wall_R, grass_bottom, grass_end_R, 
            small_grass_Top_LR, grass_end_top, small_corner_bottom_right, 
            small_corner_LnR_bottom, grass_end_bottom, grass_end_left, thorns_top
            ]
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:    
                for i, n in enumerate(tile_images):
                    if tile == i + 1: 
                        img = pygame.transform.scale(n, (TILE_SIZE, TILE_SIZE))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * TILE_SIZE
                        img_rect.y = row_count * TILE_SIZE
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                col_count += 1 
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            WIN.blit(tile[0], tile[1])
            # pygame.draw.rect(WIN, (255, 255, 255), tile[1], 1)
    

world_data = [
[14, 0, 0, 0, 0, 0, 3, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10],
[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
[12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 6, 0, 0, 0, 0, 0, 0, 13],
[19, 15, 15, 15, 20, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 5, 0, 0, 0, 0, 0, 0, 13],
[14, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 11, 11, 11, 11, 8],
[14, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 7, 7, 7, 7, 7],
[14, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 7, 7, 7, 7, 7],
[14, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 7, 7, 7, 7, 7],
[12, 11, 11, 11, 17, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 8, 7, 7, 7, 7, 7],
]

world = World(world_data)