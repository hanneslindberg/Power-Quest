import pygame

pygame.init()
BG = pygame.image.load("img/bg.png")
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Quest")

clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    clock.tick(FPS)

    WIN.blit(BG, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()