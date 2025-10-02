from pygame import *
from random import randint
win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('ping-pong')
background = transform.scale(image.load('wood.jpg'),(700,500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))#распределяем,загружаем и задаём размеры спрайту
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 170:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 170:
            self.rect.y += self.speed
        
racket_1 = Player('platform racket.png', 30,200,100,167,15)
racket_2 = Player('platform racket.png', 550,200,100,167,15)
ball = GameSprite('ball.png', 200,200,30,35,15)
game = True
finish = False
speed_x = 5
speed_y = 5
font.init()#подключили все шрифты
font2 = font.SysFont('Arial',72)
lose_1 = font2.render('Player_1 lose!',True,(255,255,255))
lose_2 = font2.render('Player_2 lose!',True,(255,255,255))
while game:
    for e in event.get():#проходимся по получиным событиям
        if e.type == QUIT:#проверяем равно ли событие событию QUIT
            game = False
    if not finish:
        window.blit(background,(0,0))#отображаем фон 
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        racket_1.reset()
        racket_2.reset()
        racket_1.update_l()
        racket_2.update_r()
        if ball.rect.y <= 0 or ball.rect.y >= win_height -35:
            speed_y *= -1
        if sprite.collide_rect(ball,racket_1) or sprite.collide_rect(ball,racket_2):
            speed_x *= -1
        if ball.rect.x <= 0:
            finish = True
            window.blit(lose_1,(230,250))
        if ball.rect.x >= win_width:
            finish = True
            window.blit(lose_2,(230,250))
    display.update()#обновление кадров возникающих на экране
    time.delay(60)

