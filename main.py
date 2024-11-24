import pygame


pygame.init()


screen_width = 800
screen_height = 600


window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Screen with Rectangle and Text")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


font = pygame.font.SysFont("Arial", 36)


text = font.render("Welcome to the Game!", True, BLUE)


rect_width = 200
rect_height = 100
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    window.fill(WHITE)

    
    pygame.draw.rect(window, BLUE, rect)

    
    window.blit(text, ((screen_width - text.get_width()) // 2, 50))

    
    pygame.display.flip()


pygame.quit()

