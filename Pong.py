from paddle import Paddle
import pygame
import sys
from paddle import Paddle
from ball import Ball
from random import randint


pygame.init()
black=(0,0,0)
white=(255,255,255)

size=(800,600)

game_display= pygame.display.set_mode(size)
pygame.display.set_caption('Pong')

paddle1=Paddle(white,10, 100)
paddle1.rect.x=25
paddle1.rect.y=250

paddle2=Paddle(white, 10, 100)
paddle2.rect.x=765
paddle2.rect.y=250

ball=Ball(white, 20, 20)
ball.rect.x=400
ball.rect.y=200

clock=pygame.time.Clock()

score1=0
score2=0

scoring_sound = pygame.mixer.Sound('scoring.wav')
poping_sound = pygame.mixer.Sound('poping.wav')

game_on=True

sprites_list=pygame.sprite.Group()

sprites_list.add(paddle1)
sprites_list.add(paddle2)
sprites_list.add(ball)

while game_on:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            game_on=False
        if event.type==pygame.KEYDOWN:
            if event.type==pygame.K_x:
                game_on=False
                
            
    keys=pygame.key.get_pressed()
        
    if keys[pygame.K_w]:
        paddle1.paddles_moving_up(7)
    if keys[pygame.K_s]:
        paddle1.paddles_moving_down(7)    
    if keys[pygame.K_UP]:
        paddle2.paddles_moving_up(7) 
    if keys[pygame.K_DOWN]:
        paddle2.paddles_moving_down(7) 
    
    sprites_list.update()    
    
    if ball.rect.x>= 780:
        score1+=1
        scoring_sound.play()
        ball.velocity[0]=ball.velocity[0]
        ball.rect.x=400
        ball.rect.y=200
    if ball.rect.x<= 2:
        score2+=1
        scoring_sound.play()
        ball.velocity[0]=ball.velocity[0]
        ball.rect.x=400
        ball.rect.y=200
    if ball.rect.y> 580:
        ball.velocity[1]=-ball.velocity[1]  
        
    if ball.rect.y<0:
        ball.velocity[1]=-ball.velocity[1]  
        
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        poping_sound.play()
        ball.bouncing()
    
    game_display.fill(black)
    
    pygame.draw.line(game_display, white, [400,0], [400, 600], 10)

    sprites_list.draw(game_display)
    
    font= pygame.font.Font(None, 100)
    
    text= font.render(str(score1), 1, white)
    game_display.blit(text, (350, 10))
    
    text= font.render(str(score2), 1, white)
    game_display.blit(text, (420, 10))
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()