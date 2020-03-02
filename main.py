import pygame # import library
pygame.init()

win = pygame.display.set_mode((800, 600))
img=pygame.image.load("assets/forest-assets/wall-e-1.png").convert()

img5=pygame.transform.scale(img,(800,500))
# Create the font



# Create the text object

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(img,(0,0))
    for y in range(38):
        for x in range(19):
                win.blit(img,(x * 48,y*16))




    

        
    pygame.display.update()

pygame.quit()

