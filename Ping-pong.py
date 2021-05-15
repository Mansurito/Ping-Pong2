import pygame as pg

class GameSprite(pg.sprite.Sprite):
    def __init__(self, color, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = pg.Surface((wight, height)) #вместе 55,55 - параметры
        self.image.fill(color=color)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
   def update(self):
       keys = pg.key.get_pressed()
       if keys[pg.K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pg.K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
class Player2(GameSprite):
   def update(self):
       keys = pg.key.get_pressed()
       if keys[pg.K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pg.K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

class Ball(pg.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #если мяч достигает границ экрана, меняем направление его движения
        if self.rect.y > win_height-50 or self.rect.y < 0:
           self.speed_y *= -1
    
    def collide_rocket(self, rocket):
        if pg.sprite.collide_rect(self, rocket):
           self.speed_x *= -1
           self.speed_y *= 1


#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
green = (50, 150, 50)
blue = (50, 50, 150)
win_width = 600
win_height = 500
window = pg.display.set_mode((win_width, win_height))

clock = pg.time.Clock()
FPS = 60
 
#создания мяча и ракетки   
racket2 = Player2(green, 15, 200, 4, 25, 150) 
racket1 = Player1(blue, win_width - 40, 200, 4, 25, 150)
ball = Ball('ball.png', 200, 200, 4, 40, 40)
 
pg.font.init()
font = pg.font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
 

#флаги, отвечающие за состояние игры
game = True
finish = False 
while game:
   for e in pg.event.get():
       if e.type == pg.QUIT:
           game = False
  
   if finish != True:
       window.fill(back)
       racket1.update()
       racket2.update()
       racket1.reset()
       racket2.reset()
       ball.update()
       ball.reset()
       ball.collide_rocket(racket1)
       ball.collide_rocket(racket2)

       #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
       if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
 
       #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
       if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
 
   pg.display.update()
   clock.tick(FPS)