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
start_img = pygame.image.load("img/start_image.png").convert_alpha()
quit_img = pygame.image.load("img/quit_image.png").convert_alpha()

start_button = button.Button((WIDTH / 2) - 100, 150, start_img, 2)
quit_button = button.Button((WIDTH / 2) - 100, 300, quit_img, 2)

# Variables
start_game = False
# Player action variables
moving_left = False
moving_right = False

def draw_bg():
    WIN.blit(BG_IMAGE, (0, 0))


# Character class
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f"img/{self.char_type}/0.jpg")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        #reset movment variables
        dx = 0
        dy = 0

        #assing moovement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        WIN.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

player = Soldier("player", 200, 200, 0.3, 5)
enemy = Soldier("enemy", 500, 200, 0.3, 5)

clock = pygame.time.Clock()
FPS = 60

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

        enemy.draw()
        player.draw()

        player.move(moving_left, moving_right)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                start_game = False

        # Keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    
    pygame.display.flip()

pygame.quit()