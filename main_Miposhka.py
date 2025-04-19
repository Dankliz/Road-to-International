from lib2to3.pytree import convert

import pygame
pygame.init()
display = pygame.display.set_mode((1800,1000))
display.fill("black")


#Изображения

pygame.image.load("assets/images/entrance.gif")
entrance_image = pygame.image.load("assets/images/entrance.gif")

pygame.image.load("assets/images/Miposhka.gif")
Miposhka_image = pygame.image.load("assets/images/Miposhka.gif")

pygame.image.load("assets/images/Yatorogod.gif")
Yatoro_image = pygame.image.load("assets/images/Yatorogod.gif")

pygame.image.load("assets/images/Game_Table.gif")
Game_Table_image = pygame.image.load("assets/images/Game_Table.gif")


pygame.image.load("assets/images/floor.jpg")
floor_image = pygame.image.load("assets/images/floor.jpg")

pygame.image.load("assets/images/banner.png")
banner_image = pygame.image.load("assets/images/banner.png")

pygame.image.load("assets/images/aegis.gif")
Cup_image = pygame.image.load("assets/images/aegis.gif")


#Изменение размера фото
entrance_image = pygame.transform.scale(entrance_image,(400,450))
Game_Table_image = pygame.transform.scale(Game_Table_image,(350,300))
banner_image = pygame.transform.scale(banner_image,(300,200))
Yatoro_image = pygame.transform.scale(Yatoro_image,(250,380))
Miposhka_image = pygame.transform.scale(Miposhka_image,(230,400))
floor_image = pygame.transform.scale(floor_image, (1800, 1800))
Cup_image = pygame.transform.scale(Cup_image , (150,150))


#Персонажи
from character import Character
Miposhka = Character(50,50,50,100,400,Miposhka_image)

#Выход
exit = False

#Обьекты
table = pygame.Surface((2000,2000),pygame.SRCALPHA, 32)
table = table.convert_alpha()

floor = pygame.Surface((2000, 1000))

banner = pygame.Surface((1200, 300),pygame.SRCALPHA, 32)
banner = banner.convert_alpha()

Game_Table = pygame.Surface((500,700),pygame.SRCALPHA, 32)
Game_Table = Game_Table.convert_alpha()

cup = pygame.Surface((1500,200),pygame.SRCALPHA, 32)
cup = cup.convert_alpha()

entrance = pygame.Surface((1500,200),pygame.SRCALPHA, 32)
cup = cup.convert_alpha()



#Текст
font = pygame.font.SysFont(None, 80)


while not exit:
#Дисплей и обьекты
    display.fill("gray")
    Miposhka.rect.topleft = (Miposhka.x, Miposhka.y)
    table.blit(Yatoro_image,(1450,300))
    floor.blit(floor_image, (0,0))
    banner.blit(banner_image, (450,50))
    Game_Table.blit(Game_Table_image,(50,50))
    cup.blit(Cup_image,(850, 50))
    entrance.blit(entrance_image,(1200, 50))


#Все обьекты писать ниже floor!!!
    display.blit(floor, (0, 0))
    display.blit(entrance_image, (1100, 0))
    display.blit(cup,(0, 0))
    display.blit(Game_Table, (0, 0))
    display.blit(banner, (0, 0))
    display.blit(table, (0, 0))
    display.blit(Miposhka.image, (Miposhka.x,Miposhka.y))

#Активные обьекты
    if Miposhka.rect.colliderect(table.get_rect(topleft=(1450, 300))):
        text_Surface = font.render("Yatoro", True, (0, 0, 0))
        display.blit(text_Surface, (1500, 200))
    if Miposhka.rect.colliderect(banner.get_rect(topleft=(450, 50))):
        text_Surface = font.render("Team Spirit", True, (0, 0, 0))
        display.blit(text_Surface, (465, 5))
    if Miposhka.rect.colliderect(banner.get_rect(topleft=(50, 50))):
        text_Surface = font.render("Тренировка", True, (0, 0, 0))
        display.blit(text_Surface, (70, 10))
    if Miposhka.rect.colliderect(banner.get_rect(topleft=(850, 50))):
        text_Surface = font.render("Кубки", True, (0, 0, 0))
        display.blit(text_Surface, (850, 0))








    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Miposhka.x = Miposhka.x - 3
    if keys[pygame.K_d]:
        Miposhka.x = Miposhka.x + 3
    if keys[pygame.K_s]:
        Miposhka.y = Miposhka.y + 3
    if keys[pygame.K_w]:
        Miposhka.y = Miposhka.y - 3

    if keys[pygame.K_SPACE] or Miposhka.on_ground == False:
        Miposhka.jump()

    pygame.display.update()
print(type(exit))


# python main_Miposhka.py

