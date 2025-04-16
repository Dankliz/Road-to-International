import pygame
pygame.init()
display = pygame.display.set_mode((1800,1200))
display.fill("black")
pygame.image.load("assets/images/Miposhka.gif")
image = pygame.image.load("assets/images/Miposhka.gif")

transform = pygame.transform.scale(image,(450,500))

from character import Character
Miposhka = Character(50,50,50,0,-250,transform)
exit = False
while not exit:
    display.fill("gray")

    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(200, 200, 200, 200))

    display.blit(Miposhka.image, (Miposhka.x,Miposhka.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Miposhka.x = Miposhka.x - 1
    if keys[pygame.K_d]:
        Miposhka.x = Miposhka.x + 1
    if keys[pygame.K_s]:
        Miposhka.y = Miposhka.y + 1
    if keys[pygame.K_w]:
        Miposhka.y = Miposhka.y - 1

    if keys[pygame.K_SPACE] or Miposhka.on_ground == False:
        Miposhka.jump()

    pygame.display.update()
print(type(exit))


#
