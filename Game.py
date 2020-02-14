import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
player = pygame.image.load('assets/hero/sliced/idle-1.png').convert_alpha()
player=pygame.transform.scale(player,(50,50))
BG=pygame.image.load("assets/BGimg.jpg").convert()
BG=pygame.transform.scale(BG,(800,600))
font=pygame.font.SysFont("arial", 30)

hp=200
text = font.render("HP going down", True, (255, 255, 255))

x=400
y=300

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    win.fill((0, 0, 0))
    win.blit(BG,(0,60))
    win.blit(player, (x, y))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x-=.4
    if keys[pygame.K_d]:
        x+=.4
    if keys[pygame.K_w]:
        y-=.4
    if keys[pygame.K_s]:
        y+=.4
    if x >= 800 or x<=0:
        hp -= 1
        print(hp)
    elif hp<=199:
        win.blit(text, (400, 300))


    pygame.display.update()

pygame.quit()