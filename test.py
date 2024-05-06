import pygame

pygame.init()

# Load image
image = pygame.image.load("img/player1/idle/0.png")
image_rect = image.get_rect()

# Desired dimensions for the smaller rectangle
small_rect_width = 50
small_rect_height = 50

# Position of the smaller rectangle relative to the image
small_rect_x = 100
small_rect_y = 100

# Create a rectangle smaller than the image
small_rect = pygame.Rect(small_rect_x, small_rect_y, small_rect_width, small_rect_height)

# Display setup
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the image
    screen.blit(image, image_rect)

    # Draw the smaller rectangle
    pygame.draw.rect(screen, (255, 0, 0), small_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
