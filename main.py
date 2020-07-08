import pygame

pygame.init()

SCREEN_WIDTH = 255 * 2
SCREEN_HEIGHT = 500

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gradients All Around")

BLUE = [0, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

for i in range(255):
    pygame.draw.rect(window, tuple(BLUE), pygame.Rect(i, 0, 1, SCREEN_HEIGHT))
    BLUE[1] -= 1
    BLUE[2] -= 1

for i in range(SCREEN_WIDTH, 255, -1):
    print(tuple(RED))
    pygame.draw.rect(window, tuple(RED), pygame.Rect(i, 0, 1, SCREEN_HEIGHT))
    RED[0] -= 1


pygame.display.flip()
RED = [255, 0, 0]
BLUE = [0, 255, 0]
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
