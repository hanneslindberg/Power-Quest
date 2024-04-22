# Fixa alla bilder: (Enemy bilderna är för stora), (Animationer för player: Så att de flyter i luften)
# Lägga till animationer för när man hoppar (PyGame Scrolling Shooter Game Beginner Tutorial in Python - PART 3 | Sprite Animation) 39:00

import pygame
import button
import random
import os
import test3

pygame.init()

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
TILE_SIZE = 16

start_game = False
# Player action variables
moving_left = False
moving_right = False
jump = False

def draw_bg():
    WIN.blit(BG_IMAGE, (0, 0))
    # pygame.draw.line(WIN, "red", (0, 500), (WIDTH, 500))

start_button = button.Button((WIDTH / 2) - 100, 150, start_img, 2)
quit_button = button.Button((WIDTH / 2) - 100, 300, quit_img, 2)

# Character class
class Char(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, keys):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.alive = True
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False
        self.keys = keys
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Load all images for the characters
        animation_types = ["Idle", "Run", "Attack"]
        for animation in animation_types:
            # Reset temporary images
            temp_list = []
            # Count number of files in folder
            num_of_animations = len(os.listdir(f"img/{self.char_type}/{animation}"))
            for i in range(num_of_animations):
                img = pygame.image.load(f"img/{self.char_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # AI specific variavles
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 0

    def move(self, moving_left, moving_right):
        # Reset movement variables
        dx = 0
        dy = 0
        on_ground = False

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
            if keys[self.keys[2]] and self.jump == False:
                self.vel_y = -13.5
                self.jump = True
            if keys[self.keys[2]] == False:
                self.jump = False

        # Apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # Map collision -------------------------------------------------------------------------------
        for tile in world.tile_list:
            # Check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # Check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # Check if below the ground i.e Jumping
                if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                # Check if above the ground i.e falling
                elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0

                

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        # Draw player border onto screen
        pygame.draw.rect(WIN, (255, 255, 255), self.rect, 2)
 
    def ai(self):
        # Add "alive" check
        if self.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.idling = True
                self.idling_counter = 100
            
            if self.idling == False:
                if self.direction == 1:
                    ai_moving_right = True
                else:
                    ai_moving_right = False

                ai_moving_left = not ai_moving_right 
                self.move(ai_moving_left, ai_moving_right)
                self.update_action(1)# 1: run
                self.move_counter += 0.5

                if self.move_counter > TILE_SIZE * 3:
                    self.direction *= -1
                    self.move_counter *= -1
            else:
                self.idling_counter -= 1
                self.update_action(0)
            if self.idling_counter <= 0:
                self.idling = False

    def update_animation(self):
        # Update animation
        ANIMATION_COOLDOWN = 100
        # Update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # If the animation has run out, reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # Check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # Reset animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        WIN.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

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

world = test3.World(world_data)

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
        if player1.alive:
            player1.draw()
            if pygame.K_a or pygame.K_d:
                player1.update_action(1)# 1: run
            else:
                player1.update_action(2)# 2: idle
            player1.move(False, False)
        # Player 2
        if player1.alive:
            player2.draw()
            if pygame.K_LEFT or pygame.K_RIGHT:
                player2.update_action(1)# 1: run
            else:
                player1.update_action(2)# 2: idle
            player2.move(False, False)
        # Enemy
        if enemy.alive:
            for enemy in enemy_group:
                enemy.update_animation()
                enemy.ai()
                enemy.draw()
                enemy.move(False, False)

        # Draw world
        world.draw()

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