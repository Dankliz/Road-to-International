import pygame
pygame.init()
display = pygame.display.set_mode((800,600))
display.fill("black")
pygame.image.load("assets/images/Yatorogod.gif")
image = pygame.image.load("assets/images/Yatorogod.gif")

from character import Character
Yatoro = Character(50,50,50,0,-230,image)
exit = False
while not exit:
    display.fill("grey")
    display.blit(Yatoro.image, (Yatoro.x,Yatoro.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()

print(type(exit))
