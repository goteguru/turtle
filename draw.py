from shapes import Rectangle, Polygon
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
    x,y,height,width=0,0,20,30
    for i in range(5):
        rectangle=Rectangle(height,width,x,y)
        pygame.draw.lines(screen, BLACK, False, rectangle.path(), 5)
        height+=10
        width+=10
        x+=10
        y+=10
        
##    poly=Polygon(120,40,50,50)
##    pygame.draw.aaline(screen, BLACK, (40, 0), (90,230), 5)
##    pygame.draw.aalines(screen, BLACK, False, [(0, 80), (50, 90), (200, 80), (220, 30)], 5)
    
    pygame.display.flip()
 
pygame.quit()
