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

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:    
                if tile == 1: 
                    img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2: 
                    img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3: 
                    img = pygame.transform.scale(left_down_corner_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4: 
                    img = pygame.transform.scale(left_top_corner_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5: 
                    img = pygame.transform.scale(right_down_corner_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6: 
                    img = pygame.transform.scale(right_top_corner_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7: 
                    img = pygame.transform.scale(dark_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8: 
                    img = pygame.transform.scale(small_corner_top_left, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 9: 
                    img = pygame.transform.scale(small_corner_right_TnB_R, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 10: 
                    img = pygame.transform.scale(small_corner_bottom_left, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 11: 
                    img = pygame.transform.scale(grass_top_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 12: 
                    img = pygame.transform.scale(small_corner_top_right, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 13: 
                    img = pygame.transform.scale(grass_wall_L, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 14: 
                    img = pygame.transform.scale(grass_wall_R, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 15: 
                    img = pygame.transform.scale(grass_bottom, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 16: 
                    img = pygame.transform.scale(grass_end_R, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 17: 
                    img = pygame.transform.scale(small_grass_Top_LR, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 18: 
                    img = pygame.transform.scale(grass_end_top, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 19: 
                    img = pygame.transform.scale(small_corner_bottom_right, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 20: 
                    img = pygame.transform.scale(small_corner_LnR_bottom, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 21: 
                    img = pygame.transform.scale(grass_end_bottom, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 22:
                    img = pygame.transform.scale(grass_end_left, (TILE_SIZE, TILE_SIZE))
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
            pygame.draw.rect(WIN, (255, 255, 255), tile[1], 1)
    

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

# run = True
# while run:
#     clock.tick(FPS)

#     if start_game == False:
#         WIN.fill(BG)

#         if start_button.draw(WIN):
#             start_game = True          
#         if quit_button.draw(WIN):
#             run = False
#     else:        
#         WIN.fill(BG)
#         draw_bg()

#         collectible_group.draw(WIN)

#         # Temp block
#         pygame.draw.rect(WIN, (255, 255, 255), player1, 2)
#         pygame.draw.rect(WIN, (255, 255, 255), player2, 2)

#         # Player 1
#         player1.draw()
#         player1.move(False, False)
#         # Player 2
#         player2.draw()
#         player2.move(False, False)
#         # Enemy
#         for enemy in enemy_group:
#             enemy.ai()
#             enemy.draw()
#             enemy.move(False, False)

#         world.draw()
#         # Grid
