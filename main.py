import pygame
import button

pygame.init()

# Create window
BG = (164, 244, 250)
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Quest")

# Load images
BG_IMAGE = pygame.image.load("img/bg.png")
start_image = pygame.image.load("img/start_image.png").convert_alpha()
quit_image = pygame.image.load("img/quit_image.png").convert_alpha()

clock = pygame.time.Clock()
FPS = 60

start_button = button.Button((WIDTH / 2) - 100, 150, start_image, 2)
quit_button = button.Button((WIDTH / 2) - 100, 300, quit_image, 2)

run = True
while run:
    clock.tick(FPS)

    WIN.fill(BG)
    #WIN.blit(BG, (0, 0)) --------------------------lägg när vi har bakgrundsbild

    if start_button.draw(WIN):
        print("START") #           -------------------------------------------------hät lägger man till vad man vill göra när man clickar start eller exit
    if quit_button.draw(WIN):
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()