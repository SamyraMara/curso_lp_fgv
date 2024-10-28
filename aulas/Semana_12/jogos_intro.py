import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)

rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
rect_color = (255, 0, 0)

is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print("Apertou o X!")
            is_running = False
    pygame.draw.rect(screen, rect_color, rect)
    pygame.display.flip()

pygame.quit()
