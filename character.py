from logging.config import stopListening


class Character:
    def __init__(self,reaction, intelligence,dexterity,x,y,image,):
        self.reaction = reaction
        self.intelligence = intelligence
        self.dexrerity = dexterity
        self.x = x
        self.org_y = y
        self.y = y
        self.image = image
        self.on_ground = True
        self.velocity = 0
        self.g = 0.98
        self.max_jump_flag = False
        self.max_jump = self.y - 3
        self.flor = 600
        self.rect = self.image.get_rect(topleft=(x, y))










#Прыжок
    def jump(self):
        if self.on_ground == True:
            self.velocity = self.velocity + 1
            self.y = self.y - self.velocity
            if self.max_jump >= self.y:
                self.max_jump_flag = True
            self.on_ground = False

        if self.on_ground == False:
            if self.max_jump_flag == False:
                self.velocity = self.velocity + 1
                self.y = self.y - self.velocity
                if self.max_jump >= self.y:
                    self.max_jump_flag = True
                self.on_ground = False
            if self.max_jump_flag == True:
                self.y = self.y + self.velocity
                if self.org_y == self.y:
                    self.on_ground = True
                    if self.y >= self.flor:
                        self.on_ground = True
























class cup:
    def __init__(self,x,y,image,value):
        self.x = x
        self.y = y
        self.image = image
        self.value = value



