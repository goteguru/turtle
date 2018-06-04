import pygame
 
pygame.init()
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
screen_size = (400, 300)
screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("Turtle API Example")
 
quit = False
clock = pygame.time.Clock()
 
while not quit:
 
    # limit the while loop to a max of 10 times per second.
    clock.tick(20)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            quit = True 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit = True

 
    screen.fill(WHITE)
 
    pygame.draw.line(screen, BLACK, (0, 0), (50,230), 5)
    pygame.draw.aaline(screen, BLACK, (40, 0), (90,230), 5)
    pygame.draw.aalines(screen, BLACK, False, [(0, 80), (50, 90), (200, 80), (220, 30)], 5)
    
    pygame.display.flip()
 
pygame.quit()
