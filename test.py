import pygame
import button
import random

# Create window
BG = (32, 32, 36)
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Quest")

clock = pygame.time.Clock()
FPS = 60

# Load images
BG_IMAGE = pygame.image.load("img/room1.png") # ---------------------------------------------- Byt ut bakgrunds bilden så småning om
start_img = pygame.image.load("img/buttons/start_image.png").convert_alpha()
quit_img = pygame.image.load("img/buttons/quit_image.png").convert_alpha()
# Collectibles
coins_img = pygame.image.load("img/icons/coin.png").convert_alpha()
trophy_img = pygame.image.load("img/icons/trophy.png").convert_alpha()
collectibles = {
    "Coin"      : coins_img,
    "Trophy"    : trophy_img
}

# Variables
GRAVITY = 0.65  
TILE_SIZE = 40

start_game = False
# Player action variables
moving_left = False
moving_right = False
jump = False

def draw_bg():
    WIN.blit(BG_IMAGE, (0, 0))
    pygame.draw.line(WIN, "red", (0, 500), (WIDTH, 500))

start_button = button.Button((WIDTH / 2) - 100, 150, start_img, 2)
quit_button = button.Button((WIDTH / 2) - 100, 300, quit_img, 2)

# Character class
class Char(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, keys):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False
        self.keys = keys
        img = pygame.image.load(f"img/{self.char_type}/Idle/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        # self.char_mask = char_mask
        # self.char_mask = pygame.mask.from_surfce(self.image)
        self.rect.center = (x, y)
        # AI specific variavles
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 0

    def move(self, moving_left, moving_right):
        # Reset movement variables
        dx = 0
        dy = 0

        # Assing movement variables if moving left or right or jumping
        if self.char_type == "enemy":
            if moving_left:
                dx = -self.speed
                self.flip = True
                self.direction = -1
            if moving_right:
                dx = self.speed
                self.flip = False
                self.direction = 1
            if moving_left == False and moving_right == False:
                dx = 0
        else:
            keys = pygame.key.get_pressed()
            if keys[self.keys[0]]:
                dx = -self.speed
                self.flip = True
                self.direction = -1
            if keys[self.keys[1]]:
                dx = self.speed
                self.flip = False
                self.direction = 1
            if keys[self.keys[2]] and self.rect.bottom == 500:
                self.vel_y = -13.5
                self.jump = False

        # Apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # Check for colision
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy
 
    def ai(self):
        # Add "alive" check
        if self.idling == False and random.randint(1, 200) == 1:
            self.idling = True
            self.idling_counter = 50
        
        if self.idling == False:
            if self.direction == 1:
                ai_moving_right = True
            else:
                ai_moving_right = False

            ai_moving_left = not ai_moving_right 
            self.move(ai_moving_left, ai_moving_right) # ------------------------------- sätt på när AI ska röra sig!!!
            self.move_counter += 0.5

            if self.move_counter > TILE_SIZE * 3:
                self.direction *= -1
                self.move_counter *= -1
        else:
            self.idling_counter -= 1
            if self.idling_counter <= 0:
                self.idling = False

    def draw(self):
        WIN.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


# Collision code testing


# collectibles 
class Collectible(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = collectibles[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

# Create sprite groups
enemy_group = pygame.sprite.Group()
collectible_group = pygame.sprite.Group()

player1 = Char("player1", 200, 200, 0.15, 5, [pygame.K_a, pygame.K_d, pygame.K_w])
player2 = Char("player2", 300, 200, 0.15, 5, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP])
enemy = Char("enemy", 400, 300, 0.2, 0.8, [moving_left, moving_right, jump])
enemy2 = Char("enemy", 500, 300, 0.2, 0.8, [moving_left, moving_right, jump])
enemy_group.add(enemy)
enemy_group.add(enemy2)

collectible = Collectible("Coin", 200, 200)
collectible_group.add(collectible)
collectible = Collectible("Trophy", 400, 200)
collectible_group.add(collectible)

# Grid layout
def draw_grid():
    for line in range(0,5):
        pygame.draw.line(WIN, (255, 255, 255), (0, line * TILE_SIZE), (WIDTH, line * TILE_SIZE))
        pygame.draw.line(WIN, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))

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
        grass_top_img = pygame.image.load('img/tilesheets/Mossy Tileset/grass_top.png')

        
        # Create image array for tiles
        tile_images = ['dirt_img', 'wall_img', 'left_down_corner_img', 'left_top_corner_img', 'right_down_corner_img']

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
                col_count += 1 
            row_count += 1

    
    def draw(self):
        for tile in self.tile_list:
            WIN.blit(tile[0], tile[1])
    

world_data = [
[2, 0, 0, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 8],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 7, 7, 7, 7],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 7, 7, 7, 7],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 7, 7, 7, 7],
[3, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 8, 7, 7, 7, 7, 7],
]

world = World(world_data)

run = True
while run:
    clock.tick(FPS)

    if start_game == False:
        WIN.fill(BG)

        if start_button.draw(WIN):
            start_game = True          
        if quit_button.draw(WIN):
            run = False
    else:        
        WIN.fill(BG)
        draw_bg()

        collectible_group.draw(WIN)

        # Player 1
        player1.draw()
        player1.move(False, False)
        # Player 2
        player2.draw()
        player2.move(False, False)
        # Enemy
        for enemy in enemy_group:
            enemy.ai()
            enemy.draw()
            enemy.move(False, False)

        world.draw()
        # Grid
        # draw_grid()


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                start_game = False
    
    pygame.display.flip()

pygame.quit()