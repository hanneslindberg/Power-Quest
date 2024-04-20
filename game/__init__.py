import pygame
import sys
from tilesheet import Tilesheet


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 640))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color('black')

        self.tiles = Tilesheet('img/tilesheets/Mossy Tileset/main_tilesheet.png', 300, 300, 7, 8)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)
        self.tiles.draw(self.screen)
        pygame.display.flip()