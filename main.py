import pygame
import button

pygame.init()

# Create window
BG = (164, 244, 250)
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Quest")

# Load images
BG_IMAGE = pygame.image.load("img/bg.png") # ---------------------------------------------- Byt ut bakgrunds bilden så småning om
start_img = pygame.image.load("img/buttons/start_image.png").convert_alpha()
quit_img = pygame.image.load("img/buttons/quit_image.png").convert_alpha()

clock = pygame.time.Clock()
FPS = 60

# Variables
GRAVITY = 0.65

start_game = False
# Player action variables
moving_left = False
moving_right = False
moving_right2 = False
moving_left2 = False

def draw_bg():
    WIN.blit(BG_IMAGE, (0, 0))
    pygame.draw.line(WIN, "red", (0, 500), (WIDTH, 500))

start_button = button.Button((WIDTH / 2) - 100, 150, start_img, 2)
quit_button = button.Button((WIDTH / 2) - 100, 300, quit_img, 2)

# Character class
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False
        img = pygame.image.load(f"img/{self.char_type}/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        # Reset movement variables
        dx = 0
        dy = 0
        
        # Assing movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        
        # Jump
        if self.jump == True and self.rect.bottom == 500:
            self.vel_y = -11
            self.jump = False

        # Apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        
        dy += self.vel_y

        # Check collision with floor
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        WIN.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

player1 = Soldier("player1", 200, 200, 0.3, 5)
player2 = Soldier("player2", 500, 200, 0.3, 5)

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
        draw_bg()

        player2.draw()
        player1.draw()

        player1.move(moving_left, moving_right)
        player2.move(moving_left, moving_right)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_w: # Lägg till "and player1.alive" 23:00
                player1.jump = True
            if event.key == pygame.K_UP:
                player2.jump = True
            if event.key == pygame.K_ESCAPE:
                start_game = False

        # Keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                moving_right = False
    
    pygame.display.flip()

pygame.quit()