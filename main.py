import pygame # import library
pygame.init()

win = pygame.display.set_mode((800, 600))
img=pygame.image.load("assets/hero/Old hero.png").convert()
img2=pygame.image.load("assets/forest-assets/door.png")
img3=pygame.image.load("assets/forest-assets/cave.png")
img4=pygame.image.load("assets/hero/sliced/peace.png")
img5=pygame.image.load("assets/Zelda map.png")
# Create the font
font=pygame.font.SysFont("arial", 30)
font2=pygame.font.SysFont("arial",50)
font3=pygame.font.SysFont("arial",60)


# Create the text object
text = font.render("Hello, world", True, (255, 255, 255))
text2=font2.render("This is the", True, (255,255,255))
text3=font3.render("Best game you'll ever play!", True, (255,255,255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(img,(400,100))
    win.blit(img2,(400,200))
    win.blit(img3,(500,200))
    win.blit(img4,(300,300))
    win.blit(img5,(200,300))
    win.blit(text, (400, 300))
    win.blit(text2, (350, 350))
    win.blit(text3, (0, 450))

        
    pygame.display.update()

pygame.quit()

