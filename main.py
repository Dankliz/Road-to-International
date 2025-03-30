import pygame
pygame.init()
display = pygame.display.set_mode((800,600))
display.fill("black")
pygame.image.load("assets/images/Miposhka.png")
image = pygame.image.load("assets/images/Miposhka.png")

from character import Character
Miposhka = Character(50,50,50,100,-60,image)

exit = False
while not exit:
    display.fill("black")
    Miposhka.x = Miposhka.x + 1
    display.blit(Miposhka.image, (Miposhka.x,Miposhka.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()

print(type(exit))
