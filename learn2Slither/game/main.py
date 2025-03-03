import pygame
from snake import Snake

WIDTH, HEIGHT = 500,500
ARRAY_WIDTH = 10
SQUARE_WIDTH = WIDTH / ARRAY_WIDTH

WHITE = (220,220,220)
BLACK = (10,10,10)
BLUE = (0,0,230)

def init_game():
    pygame.display.set_caption("Learn2Slither")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    if screen and clock:
        running = True
    else:
        running = False
    return screen, running, clock


def draw_background(screen):
    for x in range(ARRAY_WIDTH):
            for y in range(ARRAY_WIDTH):
                if not (x + y) % 2: 
                    pygame.draw.rect(screen, BLACK, (x * SQUARE_WIDTH, y * SQUARE_WIDTH, 50, 50))


def main():
    screen, running, clock = init_game()
    #init()
    snake = Snake(screen, SQUARE_WIDTH, BLUE)

    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                snake.move(event.key)
                snake.print_grid(event.key)

        #update()

        #draw()
        screen.fill(WHITE)
        draw_background(screen)
        frame = snake.draw()

        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()