import pygame
from snake import Snake

WIDTH, HEIGHT = 500,500
ARRAY_WIDTH = 10
SQUARE_WIDTH = WIDTH / ARRAY_WIDTH

WHITE = (200,200,200)
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
    frame = 0
    game_on = False

    #init()
    snake = Snake(screen, SQUARE_WIDTH, BLUE)
    screen.fill(WHITE)
    draw_background(screen)
    snake.draw()

    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    game_on = True
                snake.change_move(event.key)
                snake.print_grid(event.key)

        if game_on:
            #update()
            if frame > 20:
                snake.move()
                snake.print_grid(pygame.K_i)
                frame = 0

            if snake.is_dead():
                snake = Snake(screen, SQUARE_WIDTH, BLUE)
                game_on = False

            #draw()
            screen.fill(WHITE)
            draw_background(screen)
            snake.draw()
            frame += 1

        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()