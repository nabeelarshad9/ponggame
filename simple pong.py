import pygame 
import random

pygame.init()

# boolean game value 
gamerunning = True 

# variables
screenw = 800
screenh = 600
displacement = 5
clock = pygame.time.Clock() 
score = 0
gameovervar = "notouch" 
hitboost = 0

#fonts

scoreFont = pygame.font.Font('freesansbold.ttf', 30) 
gameOver = pygame.font.Font('freesansbold.ttf', 60) 
endFont = pygame.font.Font('freesansbold.ttf', 30) 
gameFont = pygame.font.Font('freesansbold.ttf', 40)

# PROCEDURE / procedure to draw sprites
def draw(color, sprite, Type):
    if Type == "Boost":
        for boost in sprite: 
            pygame.draw.ellipse(screen, color, boost)
    elif Type == "Paddle":
        pygame.draw.rect(screen, color, sprite) 
    elif Type == "Ball":
        pygame.draw.ellipse(screen, ballColor, ball)


# screen
screen = pygame.display.set_mode((screenw, screenh))

# paddle details
paddleW = 140
paddleH = 7
paddlex = screenw / 2 - (paddleW / 2) 
paddley = screenh - paddleH 
paddleColor = (231,60,69)


# ball details
ballR = 25
ballX = screenw / 2 - ballR / 2 
ballY = 0
 
ballColor = (252,128,21)
ballSpeed = 3 
ballSpeedX = ballSpeed 
ballSpeedY = ballSpeed


# boost details
boostR = 20
boostX = 400 - boostR / 2 
boostY = 0
boostColor = (255, 255, 255)


# assigning variables to make single sprite
paddle = pygame.Rect(paddlex, paddley, paddleW, paddleH)


ball = pygame.Rect(ballX, ballY, ballR, ballR)

# LIST / boost
boosts = []
numboost = random.randint(2,5) 
for i in range(numboost):
    boostX = random.randint(0,screenw-boostR)
    boostY = random.randint(0, (screenh-paddleH*3)) 
    boost = pygame.Rect(boostX, boostY, boostR, boostR) 
    boosts.append(boost)


# while loop
while gamerunning: 
    clock.tick(100)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            gamerunning = False 
    screen.fill((0, 0, 0))


# ball movement

    ball.x = ball.x + ballSpeedX 
    ball.y = ball.y + ballSpeedY 
    screen.fill((0, 0, 0))


# ball reflections
    if ball.left <= 0:
        ballSpeedX = ballSpeedX * -1
    if ball.right >= screenw: 
        ballSpeedX = ballSpeedX * -1
    if ball.top <= 0:
        ballSpeedY = ballSpeedY * -1


# keypress function	/	INPUT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0: 
        screen.fill((0, 0, 0))
        paddle.x = paddle.x - displacement
    if keys[pygame.K_RIGHT] and paddle.right < screenw: 
        screen.fill((0, 0, 0))
        paddle.x = paddle.x + displacement


# bottom screen collision/gameover indicator
    if ball.bottom >= screenh: 
        gameovervar = "touch" 
        ball.y = 0

# boosts
    for boost in boosts:
        if score >= 2 and ball.colliderect(boost):
            boost.y = random.randint(0, (screenh-paddleH*2)) 
            score = score + 2
            hitboost = hitboost + 1
            if ballSpeedX > 0 and ballSpeedY > 0: 
                ballSpeedX = ballSpeedX + 1 
                ballSpeedY = ballSpeedY + 1


            if ballSpeedX < 0 and ballSpeedY < 0: 
                ballSpeedX = ballSpeedX - 1 
                ballSpeedY = ballSpeedY - 1


            if ballSpeedX < 0 and ballSpeedY > 0: 
                ballSpeedX = ballSpeedX - 1 
                ballSpeedY = ballSpeedY + 1


            if ballSpeedX > 0 and ballSpeedY < 0: 
                ballSpeedX = ballSpeedX + 1 
                ballSpeedY = ballSpeedY - 1



# drawing sprites
 
    draw(paddleColor, paddle, "Paddle") 
    draw(ballColor, ball, "Ball")
    if score >= 2:
        draw(boostColor, boosts, "Boost")

# ball-paddle collision and scoring
    if ball.colliderect(paddle): 
        ballSpeedY = ballSpeedY * -1 
        score = score + 1

    if hitboost >= 4:
        for boost in boosts: 
            boost.y = -220








# score
    scoretext = scoreFont.render("Score: ", False, (255, 255, 255))
    spacescoretext = scoreFont.render(str(score), False, (255, 255, 255))
    screen.blit(scoretext, (30, 30))
    screen.blit(spacescoretext, (150, 30))
    gamenametext = gameFont.render("Pong Game", False, (43, 231, 252))
    screen.blit(gamenametext, (screenw / 1.45, 30))
#gameoverscreen


    if gameovervar == "touch":
        for boost in boosts: 
            boost.y = -20
        ball.y = -100
        paddle.y = -40
        screen.fill((0, 0, 0))
        gameovertext = gameOver.render("GAME OVER!!!", False, (255, 0, 0)) 
        screen.blit(gameovertext, (screenh / 3, screenw / 3)) 
        endgamescoretext = endFont.render("Final Score: ", False,(255, 255, 255))
        endscore = endFont.render(str(score), False, (255, 255, 255)) 
        screen.blit(endgamescoretext, (screenw / 2.75, screenh / 1.5)) 
        screen.blit(endscore, (screenw / 2.75 + 185, screenh / 1.5))

#display update 
    pygame.display.update() 

pygame.quit()
