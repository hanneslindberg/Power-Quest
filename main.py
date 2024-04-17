import pygame
import button
import random

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
            #self.move(ai_moving_left, ai_moving_right) ------------------------------- sätt på när AI ska röra sig!!!
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