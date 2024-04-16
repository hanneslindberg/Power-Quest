import pygame

# Definiera några konstanter
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.5

# Definiera färger
WHITE = (255, 255, 255)

# Initialisera Pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Players Example")

# Klass för soldater
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, keys):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False
        self.keys = keys
        img = pygame.image.load(f"img/{self.char_type}/0.jpg")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self):
        # Reset movement variables
        dx = 0
        dy = 0
        
        # Assign movement variables based on key input
        keys = pygame.key.get_pressed()
        if keys[self.keys[0]]:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if keys[self.keys[1]]:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if keys[self.keys[2]] and self.rect.bottom == HEIGHT:
            self.vel_y = -11
            self.jump = True

        # Apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # Check collision with floor
        if self.rect.bottom + dy > HEIGHT:
            dy = HEIGHT - self.rect.bottom

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        WIN.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


def main():
    player1 = Soldier("soldier", 200, 300, 1, 5, [pygame.K_a, pygame.K_d, pygame.K_w])
    player2 = Soldier("soldier", 400, 300, 1, 5, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP])

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        player1.move()
        player1.draw()
        player2.move()
        player2.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
