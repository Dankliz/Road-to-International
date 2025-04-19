import pygame
pygame.init()
display = pygame.display.set_mode((800,600))
display.fill("black")
pygame.image.load("assets/images/aegis.gif")
Cup_image = pygame.image.load("assets/images/aegis.gif")

from character import cup
Aegis = cup(0,-150,Cup_image,18000000)
exit = False
while not exit:
    display.fill("gray")

    display.blit(Aegis.image, (Aegis.x,Aegis.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()

print(type(exit))