# Lägga till animationer för när man hoppar (PyGame Scrolling Shooter Game Beginner Tutorial in Python - PART 3 | Sprite Animation) 39:00

import pygame
import button
import random
import os
import worldmap
from worldmap import world_data
from worldmap import thorns_group

pygame.init()

# Create window
BG = (32, 32, 36)
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Quest")

clock = pygame.time.Clock()
FPS = 60
game_over = 0

# Load sound
bg_music = pygame.mixer.Sound("sound\Earth.mp3")
jump_sound = pygame.mixer.Sound("sound\jump_sound.mp3")
jump_sound.set_volume(0.1)

# Load images
BG_IMAGE = pygame.image.load("img/bg.jpg")
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
GRAVITY = 0.35  
TILE_SIZE = 16
start_game = False
bg_music_played = False

# Player action variables
moving_left = False
moving_right = False
jump = False

def draw_bg():
    WIN.blit(BG_IMAGE, (0, 0))
    
start_button = button.Button((WIDTH / 2) - 100, 150, start_img, 2)
quit_button = button.Button((WIDTH / 2) - 100, 300, quit_img, 2)

# Character class
class Char(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, keys, scalex, scaley):
        self.reset(char_type, x, y, scale, speed, keys, scalex, scaley)

    def move(self, moving_left, moving_right, game_over):
        # Reset movement variables
        dx = 0
        dy = 0
        on_ground = False
        
        if game_over == 0:
            # Assing movement variables if moving left or right or jumping
            if game_over == 0:
                keys = pygame.key.get_pressed()
                if keys[self.keys[0]]:
                    moving_left = True
                if keys[self.keys[1]]:
                    moving_right = True
                
            on_ground = self.rect.y >= HEIGHT - self.rect.height or any(tile[1].colliderect(self.rect.x, self.rect.y + 1, self.rect.width, self.rect.height) for tile in world.tile_list)

            # Assing movement variables if moving left or right or jumping
            if moving_left:
                dx = -self.speed
                self.flip = True
                self.direction = -1
            if moving_right:
                dx = self.speed
                self.flip = False
                self.direction = 1
            if not moving_left and not moving_right:
                dx = 0  
            if keys[self.keys[2]] and not self.jump and on_ground:
                jump_sound.play()

                self.vel_y = -10
                self.jump = True
            if not keys[self.keys[2]]:
                self.jump = False

            # Apply gravity
            self.vel_y += GRAVITY
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # Map collision -------------------------------------------------------------------------------
            for tile in world.tile_list:
                # Check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                    dx = 0

                # Check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height + 1):
                    # Check if below the ground i.e Jumping
                    if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                    # Check if above the ground i.e falling
                    elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0

            # Check for collision with thorns
            if pygame.sprite.spritecollide(self, thorns_group, False):
                game_over = -1

            # Update rectangle position
            self.rect.x += dx
            self.rect.y += dy

        return game_over

    def reset(self, char_type, x, y, scale, speed, keys, scalex, scaley):
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
        self.rect.scale_by_ip(scalex, scaley)
        self.rect.center = (x, y)

        # AI specific variables
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 0
        self.vision = pygame.Rect(0, 0, 300, self.rect.height)

    def ai(self):
        # Add "alive" check
        if self.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.idling = True
                self.idling_counter = 200
            
            if self.idling == False:
                if self.direction == 1:
                    ai_moving_right = True
                else:
                    ai_moving_right = False

                ai_moving_left = not ai_moving_right 
                self.move(ai_moving_left, ai_moving_right, game_over)
                self.update_action(1)# 1: run
                self.move_counter += 0.5
                # Update vision as it moves
                self.vision.center = (self.rect.centerx + 150 * self.direction, self.rect.centery)

                if self.move_counter > TILE_SIZE:
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
        if self.char_type == "enemy":
            WIN.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.center[0] - self.width / 2, self.rect.center[1] - self.height / 2 -8))
        else:
            WIN.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.center[0] - self.width / 2, self.rect.center[1] - self.height / 2))
        # pygame.draw.rect(WIN, "white", self.rect, 1)

class Collectible(pygame.sprite.Sprite):
    def __init__(self, item_type, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = pygame.transform.scale(collectibles[self.item_type], (int(collectibles[self.item_type].get_width() * scale), int(collectibles[self.item_type].get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

# Create sprite groups
enemy_group = pygame.sprite.Group()
collectible_group = pygame.sprite.Group()

player1 = Char("player1", 70, 500, 0.15, 5, [pygame.K_a, pygame.K_d, pygame.K_w], 1, 1 )
player2 = Char("player2", 130, 500, 0.15, 5, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP], 1, 1)
enemy = Char("enemy", 300, 300, 0.2, 0.6, [moving_left, moving_right, jump], 0.3, 0.6)
enemy_group.add(enemy)

trophy = Collectible("Trophy", 0.85, 165, 110)
collectible_group.add(trophy)

world = worldmap.World(world_data)

run = True
while run:
    clock.tick(FPS)

    if start_game == False:
        WIN.fill(BG)

        if not bg_music_played:
            bg_music.play(loops = -1)
            bg_music_played = True
        bg_music.set_volume(0.5)

        if start_button.draw(WIN):
            start_game = True          
        if quit_button.draw(WIN):
            run = False
    else:        
        WIN.fill(BG)
        draw_bg()

        bg_music.set_volume(3.0)

        collectible_group.draw(WIN)
        
        # Player 1
        if game_over == 0:
            player1.draw()
            if player1.rect.colliderect(enemy.rect):
                game_over = -1
            if player1.rect.colliderect(trophy.rect):
                game_over = -1
            if pygame.K_a or pygame.K_d:
                player1.update_action(1)# 1: run
            else:
                player1.update_action(2)# 2: idle
            game_over = player1.move(False, False, game_over)
        # Player 2

        if game_over == 0:
            player2.draw()
            if player2.rect.colliderect(enemy.rect):
                game_over = -1
            if player2.rect.colliderect(trophy.rect):
                game_over = -1
            if pygame.K_LEFT or pygame.K_RIGHT:
                player2.update_action(1)# 1: run
            else:
                player1.update_action(2)# 2: idle
            game_over = player2.move(False, False, game_over)
        # Enemy
        
        for enemy in enemy_group:
            enemy.update_animation()
            enemy.ai()
            enemy.draw()
                
            game_over = enemy.move(False, False, game_over)

        # Draw world
        world.draw()

        thorns_group.draw(WIN)

        # If player has died
        if game_over == -1:
            player1.reset("player1", 70, 500, 0.15, 5, [pygame.K_a, pygame.K_d, pygame.K_w], 1, 1)
            player2.reset("player2", 130, 500, 0.15, 5, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP], 1, 1)
            game_over = 0 

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