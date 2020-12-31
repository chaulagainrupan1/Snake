import pygame
import time
import random

pygame.init()

white = (255,255,255) #256*256*256 combination of RGB color
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

icon = pygame.image.load('snakehead1.png')
pygame.display.set_icon(icon)
block_size = 20
img = pygame.image.load('snakehead1.png')#to include the image in game
img1 = pygame.image.load('apple.png')
AppleThickness = 20
fps = 20
direction = "right"
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Paused",black,-100,size="large")
        message_to_screen("press C to continue or Q to quit.",black,25)
        pygame.display.update()
        clock.tick(5)
        
def score(score):
    text = smallfont.render("score:"+str(score),True,black)
    gameDisplay.blit(text,[0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0,display_width - AppleThickness))
    randAppleY = round(random.randrange(0, display_height - AppleThickness))
    return randAppleX,randAppleY



def game_intro():
    intro = True
        
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",green,-100,"large")
        message_to_screen("The objective of the game is to eat red apples",black,-30)
        message_to_screen("The more apples you eat,the longer you get",black,10)
        message_to_screen("Press C to play , P to pause or Q to quit",black,70)
        message_to_screen("created by: Rupan",black,180)
        pygame.display.update()
        clock.tick(15)
        
        

def Snake(block_size,snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)

    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    
    return textSurface, textSurface.get_rect()
    

def message_to_screen(msg,color,y_displace=0,size= "small" ):#passing the parameter for message and color
     textSurf, textRect = text_objects(msg,color, size)
     textRect.center = (display_width/2),(display_height / 2)+y_displace
     gameDisplay.blit(textSurf, textRect)


#pygame.display.flip()
#pygame.display.update()



clock = pygame.time.Clock()


def gameLoop():
    global direction
    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    
    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()
        

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",red,-50,size= "large")
            message_to_screen("Press C to play again and Q to quit",black,50,size= "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()
                        
                        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
             #makes the snake keep on going
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
             gameOver = True
       
        gameDisplay.fill(white)
       
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(img1,(randAppleX , randAppleY))

        #gameDisplay.fill(red, rect=[0,0,20,20])can also be used to draw and color objects
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for e in snakeList[:-1]:
            if e == snakeHead:
                gameOver = True

        Snake(block_size, snakeList)
        score(snakeLength-1)
        pygame.display.update() #you draw everything in background and then we render it so the update is required!!
        
        

##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##              if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                  randAppleX = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
##                  randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
##                  snakeLength += 1

        if (lead_x > randAppleX and lead_x < randAppleX + AppleThickness) or (lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness):
            
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
            
                randApplex,randAppleY = randAppleGen()
                snakeLength += 1
                
            if lead_y + block_size > randAppleY and lead_y + AppleThickness < randAppleY + AppleThickness:
                randApplex,randAppleY = randAppleGen()
                snakeLength += 1

        if randAppleY > lead_y:
            lead_x_change = 0
            lead_y_change = -(randAppleY - lead_y) 
##            elif event.key == pygame.K_RIGHT:
##                    direction = "right"
##                    lead_y_change = 0
##                    lead_x_change = block_size/2
##            elif event.key == pygame.K_UP:
##                    direction = "up"
##                    lead_x_change = 0
##                    lead_y_change = -block_size/2
##            elif event.key == pygame.K_DOWN:
##                    direction = "down"
##                    lead_x_change = 0
##                    lead_y_change = block_size/2
                
            lead_y += lead_y_change            
            lead_x += lead_x_change 
                
        clock.tick(fps) #changing speed of your game 24 here is fps        

    
    pygame.quit()
    quit()
game_intro()
gameLoop()



