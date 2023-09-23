#   Racing Car Game
#       Luciana

#    Common Pygame Structure
import pygame
import time
import random

background_music = "172. DUET.mp3"
crasher = "bonk_BEtiM8g (1).mp3"


def button(msg, x, y, w, h, ic, ac):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        
        if click[0] == 1:
            if msg == "Go!":
                game_loop()
            
            
            elif msg == "Quit?":
                game_quit()

            
            else:
                print("Oops, something went wrong!!")
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    
    smallText = pygame.font.SysFont(None,40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( ( x+(w/2) , y+(h/2) )  )
    gameDisplay.blit(textSurf,textRect)

def game_intro():
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',105)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((displayWidth/2),(displayHeight/2))
        gameDisplay.blit(TextSurf, TextRect)


        button("Go!", 150, 450, 100, 50, green, darkgreen)
        
        button("Quit?", 550, 450, 100, 50, red, darkred)
        
        
        

        pygame.display.update()
        clock.tick(15)
        

def game_quit():
    pygame.quit()
    quit()


def enemy_dodged(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Dodged: "+str(count * 10), True, black)
    gameDisplay.blit(text,(0,0))

def game_loop():
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1)
    x = 283
    y = 430
    x_change = 0
    carWidth = 96
    gameExit = False
    dodged = 0
    
    enemy_startx1 = random.randrange(0, displayWidth)
    enemy_starty1 = -600
    
    enemy_startx2 = random.randrange(0, displayWidth)
    enemy_starty2 = -600
    
    while enemy_startx2 == enemy_startx1:
        enemy_startx2 = random.randrange(0, displayWidth)
    
    enemy_width1 = 72
    enemy_height1 = 155
    enemy_speed = 7
    
    enemy_width2 = 72
    enemy_height2 = 117

    
    #  Game loop
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -14
                
                elif event.key == pygame.K_RIGHT:
                    x_change = 14
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            print(event)
        
        gameDisplay.fill(white)
        x += x_change
        if x > displayWidth - carWidth:
            x = displayWidth - carWidth
        elif x < 0:
            x = 0
        
        enemy(enemy_startx1, enemy_starty1, enemyImg1)
        
        enemy(enemy_startx2, enemy_starty2, enemyImg2)

        enemy_starty1 += enemy_speed
        
        enemy_starty2 += enemy_speed
        
        car(x, y)
        
        enemy_dodged(dodged)
        
        if enemy_starty1 > displayHeight or enemy_starty2 > displayHeight:
            enemy_starty1 = enemy_starty2 = 0 - enemy_height1
            enemy_startx1 = random.randrange(0,displayWidth)
            enemy_startx2 = random.randrange(0, displayWidth)
            dodged += 1
            enemy_speed += 0.5



        
        if y < enemy_starty1+enemy_height1:
            print('y crossover')
            if (x > enemy_startx1 and x < enemy_startx1 + enemy_width1 or x+carWidth > enemy_startx1 and x + carWidth < enemy_startx1+enemy_width1):
                print('x crossover')
                crash()
        
        if y < enemy_starty2+enemy_height2:
            print('y crossover')
            if (x > enemy_startx2 and x < enemy_startx2 + enemy_width2 or x+carWidth > enemy_startx2 and x + carWidth < enemy_startx2+enemy_width2):
                print('x crossover')
                crash()
                    
        

        pygame.display.update()
        clock.tick(30)

pygame.init()

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Racing Car Game, Luciana")
clock = pygame.time.Clock()

blue = (173, 216, 230)
black = (0, 0, 0)
white = (255, 255, 255)
green = (193, 225, 193)
red = (255, 112, 102)
darkgreen = (86, 174, 87)
darkred = (170, 67, 68)

carImg = pygame.image.load("tank.png")

enemyImg1 = pygame.image.load("enemy.png")

enemyImg2 = pygame.image.load("enemy2.png")


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def enemy(ex, ey, enemyImg):
    gameDisplay.blit(enemyImg, (ex, ey))


def message(text):
    largeFont = pygame.font.Font("Cambria-Font-For-Windows.ttf", 70)
    TextSurf, TextRect = text_objects(text, largeFont)
    TextRect.center = ( (displayWidth/2, displayHeight/2) )
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    time.sleep(3)
    
    game_loop()




def crash():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(crasher)
    pygame.mixer.music.play(1)
    message("You Crashed!")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



game_intro()

game_loop()

game_quit()
