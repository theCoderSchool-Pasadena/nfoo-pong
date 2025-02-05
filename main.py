from typing import Text
import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Pong!')
clock = pygame.time.Clock()
Paddle = pygame.Rect(30, 120, 8, 70)
Paddle2 = pygame.Rect(360, 120, 8, 70)
Ball = pygame.Rect(50, 150, 7, 7)
Ball.center=(200, 150)
PadTopBound = (0)
PadBotBound = (230)
BallTopBound = (0)
BallBotBound = (293)
BallRightBound = (390)
Ballup=True
BallX=True
Run=True
Font = pygame.font.SysFont("arial", 30)
Scoretext = Font.render("0 | 0", False, (0,0,0))
Score1, Score2 = 0, 0 
Winner = ""
WinnerText = Font.render("", False, (0,0,0))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed() 
    if Run:
        if keys[pygame.K_w]:
            Paddle.y-=1
            if Paddle.y < PadTopBound:
                Paddle.y = PadTopBound        
        if keys[pygame.K_s]:
            Paddle.y+=1
            if Paddle.y > PadBotBound:
                Paddle.y = PadBotBound
        if keys[pygame.K_UP]:
            Paddle2.y-=1
            if Paddle2.y < PadTopBound:
                Paddle2.y = PadTopBound
        if keys[pygame.K_DOWN]:
            Paddle2.y+=1
            if Paddle2.y > PadBotBound:
                Paddle2.y = PadBotBound        
    else:
        if keys[pygame.K_SPACE]:
            Paddle.y=120
            Paddle2.y=120
            Ball.x=200
            Ball.y=150
            Run=True
            if Winner != "":
                Score1, Score2 = 0, 0
                Winner = ""
                WinnerText = Font.render("", False, (0,0,0))
                DISPLAYSURF.blit(WinnerText, (160, 30))
                Scoretext = Font.render("0 | 0", False, (0,0,0))
                DISPLAYSURF.blit(Scoretext, (160, 0))
    DISPLAYSURF.fill("white")
    DISPLAYSURF.blit(Scoretext, (160,0))
    
    pygame.draw.rect(DISPLAYSURF, "black", Paddle)
    pygame.draw.rect(DISPLAYSURF, "black", Paddle2)
    pygame.draw.rect(DISPLAYSURF, "black", Ball)
    
    if Run:
        if Ball.colliderect(Paddle):
            BallX=False
    
        if Ball.colliderect(Paddle2):
            BallX=True
        # Moves y
        if Ballup:
            Ball.y-=1
        if Ballup==False:
            Ball.y+=1
        # Bounce edge
        if Ball.y < BallTopBound:
            Ball.y = BallTopBound
            Ballup=False
        if Ball.y > BallBotBound:
            Ball.y = BallBotBound
            Ballup=True
        # Moves x
        if BallX:
            Ball.x-=1
        if BallX==False:
            Ball.x+=1
        # Left edge
        if Ball.x < BallTopBound:
            Ball.x = BallTopBound
            BallLeft=False
            Run=False
            Score2+=1
            print(f"{Score1} | {Score2}")
            Scoretext = Font.render(f"{Score1} | {Score2}", False, (0,0,0))
        # Right edge
        if Ball.x > BallRightBound:
            Ball.x = BallRightBound
            BallX=True
            Run=False
            Score1+=1
            print(f"{Score1} | {Score2}")
            Scoretext = Font.render(f"{Score1} | {Score2}", False, (0,0,0))
    else:
        if Score1 == 2:
            Winner = "Player 1 won!"
            WinnerText = Font.render(Winner, False, (0,0,0))
        if Score2 == 2:
            Winner = "Player 2 won!"
            WinnerText = Font.render(Winner, False, (0,0,0))
        DISPLAYSURF.blit(WinnerText, (160, 30))
    pygame.display.update()
    clock.tick(160)