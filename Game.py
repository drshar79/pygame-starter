import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/hero/sliced/idle-1.png').convert_alpha()
img=pygame.transform.scale(img,(50,50))
img2=pygame.image.load("assets/Zelda map.png").convert()
img2=pygame.transform.scale(img2,(800,500))

x=400
y=300

# Load the spritesheet
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            

    win.fill((0, 0, 0))
    win.blit(img2,(0,60))
    win.blit(img, (x, y))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x-=.3
    if keys[pygame.K_d]:
        x+=.3
    if keys[pygame.K_w]:
        y-=.3
    if keys[pygame.K_s]:
        y+=.3


    pygame.display.update()

pygame.quit()