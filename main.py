import pygame
import random
import sys
import math
import time
pause=False

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

pygame.display.set_caption("Car Race Arcade")

'''
def show_score(car_passed, score):
    font = pygame.font.SysFont(None, 35)
    passed = font.render("Passed : " + str(car_passed), True, (1,1,1))
    score_ = font.render("Score :" + str(score), True, (1,1,1))
    screen.blit(passed, (0,50))
    screen.blit(score_,(0,100))
'''

entryimg = pygame.image.load('background.jpg')
instruction_part = pygame.image.load('background2.jpg')


def entrypage_loop():
    entry = True
    while entry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
        screen.blit(entryimg, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 70)
        show_font = font.render('Car Race Arcade', 2, (235, 52, 52))
        screen.blit(show_font, (120, 100))
        pygame.draw.rect(screen, (0, 200, 0), (320, 260, 150, 50))
        pygame.draw.rect(screen, (0, 0, 200), (300, 360, 190, 50))
        pygame.draw.rect(screen, (0, 120, 0), (320, 460, 150, 50))
        mouse = pygame.mouse.get_pos()
        if mouse[0] > 321 and mouse[0] < 470 and mouse[1] > 260 and mouse[1] < 310:
            pygame.draw.rect(screen, (0, 250, 0), (320, 260, 150, 50))
            if click == (True, 0, 0):
                countdown()

        if mouse[0] > 300 and mouse[0] < 490 and mouse[1] > 360 and mouse[1] < 410:
            pygame.draw.rect(screen, (0, 0, 255), (300, 360, 190, 50))
            if click == (True, 0, 0):
                instructions()

        if mouse[0] > 321 and mouse[0] < 470 and mouse[1] > 460 and mouse[1] < 510:
            pygame.draw.rect(screen, (0, 180, 0), (320, 460, 150, 50))
            if click == (True, 0, 0):
                pygame.quit()
                quit()

        smallText = pygame.font.Font('freesansbold.ttf', 25)
        textSurface, textRect = text_object("START", smallText)
        textRect.center = ((320 + 73)), (260 + 27)
        screen.blit(textSurface, textRect)

        textSurface, textRect = text_object("How to Play?", smallText)
        textRect.center = ((320 + 73)), (360 + 27)
        screen.blit(textSurface, textRect)

        textSurface, textRect = text_object("EXIT", smallText)
        textRect.center = ((320 + 73)), (460 + 27)
        screen.blit(textSurface, textRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.display.update()




def instructions():
    instruction = True
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruction_part, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = text_object("This is a car race game in which you need to dodge the incoming vehicle",
                                         smalltext)
        textRect.center = ((430), (230))

        TextSurf, TextRect = text_object("INSTRUCTIONS", largetext)
        TextRect.center = ((400), (100))
        screen.blit(TextSurf, TextRect)
        screen.blit(textSurf, textRect)
        stextSurf, stextRect = text_object("ARROW LEFT : MOVE LEFT ", smalltext)
        stextRect.center = ((150), (400))
        hTextSurf, hTextRect = text_object("ARROW RIGHT : MOVE  RIGHT ", smalltext)
        hTextRect.center = ((170), (450))
        atextSurf, atextRect = text_object("A : ACCELERATOR", smalltext)
        atextRect.center = ((150), (500))
        rtextSurf, rtextRect = text_object("B : BRAKE ", smalltext)
        rtextRect.center = ((150), (550))
        ptextSurf, ptextRect = text_object("P : PAUSE  ", smalltext)
        ptextRect.center = ((150), (350))
        sTextSurf, sTextRect = text_object("CONTROLS", mediumtext)
        sTextRect.center = ((350), (300))
        screen.blit(sTextSurf, sTextRect)
        screen.blit(stextSurf, stextRect)
        screen.blit(hTextSurf, hTextRect)
        screen.blit(atextSurf, atextRect)
        screen.blit(rtextSurf, rtextRect)
        screen.blit(ptextSurf, ptextRect)

        pygame.draw.rect(screen, (0, 200, 0), (550, 500, 150, 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 550 and mouse[0] < 700 and mouse[1] > 500 and mouse[1] < 550:
            pygame.draw.rect(screen, (0, 250, 0), (550, 500, 150, 50))
            if click == (True, 0, 0):
                entrypage_loop()

        smallText = pygame.font.Font('freesansbold.ttf', 25)
        textSurface, textRect = text_object("Back", smallText)
        textRect.center = ((550 + 73)), (500 + 27)
        screen.blit(textSurface, textRect)

        pygame.display.update()
        clock.tick(30)



def text_object(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


font = pygame.font.Font('freesansbold.ttf', 20)
global car_passed
global score
car_passed = 0
score = 0


def show_score(x, y):
    score1 = font.render("Score : " + str(score), True, (1, 1, 1))
    screen.blit(score1, (10, 10))
    passed = font.render("Car Passed : " + str(car_passed), True, (1, 1, 1))
    screen.blit(passed, (10, 40))


def enemycar(totalenemy_car_x, totalenemy_car_y, totalenemy_car):
    global enemycarimg
    if totalenemy_car == 0:
        enemycarimg = pygame.image.load("car2.jpg")
    elif totalenemy_car == 1:
        enemycarimg = pygame.image.load("car3.jpg")
    elif totalenemy_car == 2:
        enemycarimg = pygame.image.load("car4.jpg")
    elif totalenemy_car == 3:
        enemycarimg = pygame.image.load("car5.jpg")
    elif totalenemy_car == 4:
        enemycarimg = pygame.image.load("car6.jpg")
    elif totalenemy_car == 5:
        enemycarimg = pygame.image.load("car7.jpg")

    screen.blit(enemycarimg, (totalenemy_car_x, totalenemy_car_y))


grassimg = pygame.image.load('grass.jpg')
yellowstripe = pygame.image.load("yellow strip.jpg")
whitestripe = pygame.image.load("strip.jpg")
traffic_cone = pygame.image.load("cone.png")
backgroundimg = pygame.image.load('download12.jpg')

over_font = pygame.font.Font('freesansbold.ttf', 74)
over_text = over_font.render("Crashed! Game Over", 2, (245, 66, 66))

global playerX
global playerY

CarImg = pygame.image.load('car1.jpg')


def background():
    screen.blit(grassimg, (0, 0))
    screen.blit(grassimg, (700, 0))
    screen.blit(yellowstripe, (383, 0))
    screen.blit(yellowstripe, (383, 100))
    screen.blit(yellowstripe, (383, 200))
    screen.blit(yellowstripe, (383, 300))
    screen.blit(yellowstripe, (383, 400))
    screen.blit(yellowstripe, (383, 500))
    screen.blit(yellowstripe, (383, 600))
    screen.blit(whitestripe, (115, 0))
    screen.blit(whitestripe, (683, 0))
    screen.blit(traffic_cone, (90, 500))
    screen.blit(traffic_cone, (90, 400))
    screen.blit(traffic_cone, (90, 300))
    screen.blit(traffic_cone, (90, 200))
    screen.blit(traffic_cone, (90, 100))
    screen.blit(traffic_cone, (90, 20))
    screen.blit(traffic_cone, (90, 580))
    screen.blit(traffic_cone, (685, 500))
    screen.blit(traffic_cone, (685, 400))
    screen.blit(traffic_cone, (685, 300))
    screen.blit(traffic_cone, (685, 200))
    screen.blit(traffic_cone, (685, 100))
    screen.blit(traffic_cone, (685, 20))
    screen.blit(traffic_cone, (685, 580))


def playercar(x, y):
    screen.blit(CarImg, (x, y))


def isCollision(totalenemy_car_x, totalenemy_car_y, playerX, playerY):
    distance = math.sqrt(math.pow(totalenemy_car_x - playerX, 2) + (math.pow(totalenemy_car_y - playerY, 2)))
    if distance < 66:
        return True
    else:
        return False


def countdown_part():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()
    screen.blit(grassimg, (0, 0))
    screen.blit(grassimg, (700, 0))
    screen.blit(yellowstripe, (383, 0))
    screen.blit(yellowstripe, (383, 100))
    screen.blit(yellowstripe, (383, 200))
    screen.blit(yellowstripe, (383, 300))
    screen.blit(yellowstripe, (383, 400))
    screen.blit(yellowstripe, (383, 500))
    screen.blit(yellowstripe, (383, 600))
    screen.blit(whitestripe, (115, 0))
    screen.blit(whitestripe, (683, 0))
    screen.blit(traffic_cone, (90, 500))
    screen.blit(traffic_cone, (90, 400))
    screen.blit(traffic_cone, (90, 300))
    screen.blit(traffic_cone, (90, 200))
    screen.blit(traffic_cone, (90, 100))
    screen.blit(traffic_cone, (90, 20))
    screen.blit(traffic_cone, (90, 580))
    screen.blit(traffic_cone, (685, 500))
    screen.blit(traffic_cone, (685, 400))
    screen.blit(traffic_cone, (685, 300))
    screen.blit(traffic_cone, (685, 200))
    screen.blit(traffic_cone, (685, 100))
    screen.blit(traffic_cone, (685, 20))
    screen.blit(traffic_cone, (685, 580))
    screen.blit(CarImg, (365, 470))

def paused():
    pause=True

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            screen.blit(instruction_part,(0,0))
            largeText = pygame.font.Font('freesansbold.ttf', 100)
            textSurface, textRect = text_object("PAUSED", largeText)
            textRect.center = ((400), (300))
            screen.blit(textSurface, textRect)

            mouse = pygame.mouse.get_pos()
            '''click = pygame.mouse.get_pressed()
            
                pygame.draw.rect(screen, (0, 180, 0), (650, 0, 150, 50))
                if click == (True, 0, 0):
                    paused()'''

            #for continue


            if mouse[0] > 100 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500:
                pygame.draw.rect(screen, (0, 180, 0), (100, 450, 150, 50))

            else:
                pygame.draw.rect(screen, (0, 250, 0), (100, 450, 150, 50))
            smallText = pygame.font.Font('freesansbold.ttf', 25)
            textSurface, textRect = text_object("CONTINUE", smallText)
            textRect.center = ((100+(150/2)), (450+(50/2)))
            screen.blit(textSurface, textRect)
            #for restart
            pygame.draw.rect(screen, (0, 250, 0), (350, 450, 150, 50))
            smallText = pygame.font.Font('freesansbold.ttf', 25)
            textSurface, textRect = text_object("RESTART", smallText)
            textRect.center = ((350 + (150 / 2)), (450 + (50 / 2)))
            screen.blit(textSurface, textRect)
            #for main menu
            pygame.draw.rect(screen, (0, 250, 0), (600, 450, 150, 50))
            smallText = pygame.font.Font('freesansbold.ttf', 25)
            textSurface, textRect = text_object("MAIN MENU", smallText)
            textRect.center = ((600 + (150 / 2)), (450 + (50 / 2)))
            screen.blit(textSurface, textRect)

            pygame.display.update()
            clock.tick(30)


def countdown():
    countdown = True

    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.fill((119, 119, 119))

        countdown_part()

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        largetext_ = largetext.render("3", 2, (245, 66, 66))
        screen.blit(largetext_, (360, 250))
        pygame.display.update()
        clock.tick(1)
        screen.fill((119, 119, 119))

        countdown_part()

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        largetext_ = largetext.render("2", 2, (245, 66, 66))
        screen.blit(largetext_, (360, 250))
        pygame.display.update()
        clock.tick(1)
        screen.fill((119, 119, 119))
        countdown_part()

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        largetext_ = largetext.render("1", 2, (245, 66, 66))
        screen.blit(largetext_, (360, 250))
        pygame.display.update()
        clock.tick(1)
        screen.fill((119, 119, 119))
        countdown_part()

        largetext = pygame.font.Font('freesansbold.ttf', 125)
        largetext_ = largetext.render("START!", True, (1, 1, 1))
        screen.blit(largetext_, (180, 230))

        pygame.display.update()
        clock.tick(1)
        game_loop()
        quit()


def game_loop():
    running = True
    playerX_change = 0
    playerX = 365
    playerY = 470
    enemycar_speed = 10
    totalenemy_car = 0
    enemycar_speed_change = 0
    totalenemy_car_x = random.randrange(150, 640)
    totalenemy_car_y = -750
    global car_passed
    global score
    global crash
    crash = False

    y2 = True

    level = 1

    while running:
        screen.fill((119, 119, 119))
        background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_a:
                    enemycar_speed += 2
                if event.key == pygame.K_b:
                    enemycar_speed -= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change

        screen.fill((119, 119, 119))

        rel_y = y2 % backgroundimg.get_rect().width
        screen.blit(backgroundimg, (0, rel_y - backgroundimg.get_rect().width))
        screen.blit(backgroundimg, (700, rel_y - backgroundimg.get_rect().width))
        if rel_y < 800:
            screen.blit(backgroundimg, (0, rel_y))
            screen.blit(backgroundimg, (700, rel_y))
            screen.blit(yellowstripe, (383, rel_y))
            screen.blit(yellowstripe, (383, rel_y + 100))
            screen.blit(yellowstripe, (383, rel_y + 200))
            screen.blit(yellowstripe, (383, rel_y + 300))
            screen.blit(yellowstripe, (383, rel_y + 400))
            screen.blit(yellowstripe, (383, rel_y + 500))
            screen.blit(yellowstripe, (383, rel_y - 100))
            screen.blit(whitestripe, (115, rel_y - 200))
            screen.blit(whitestripe, (115, rel_y + 20))
            screen.blit(whitestripe, (115, rel_y + 30))
            screen.blit(whitestripe, (683, rel_y - 100))
            screen.blit(whitestripe, (683, rel_y + 20))
            screen.blit(whitestripe, (683, rel_y + 30))
            screen.blit(traffic_cone, (90, rel_y + 100))
            screen.blit(traffic_cone, (90, rel_y + 200))
            screen.blit(traffic_cone, (90, rel_y + 300))
            screen.blit(traffic_cone, (90, rel_y + 400))
            screen.blit(traffic_cone, (90, rel_y + 500))
            screen.blit(traffic_cone, (90, rel_y - 40))

            screen.blit(traffic_cone, (685, rel_y + 100))
            screen.blit(traffic_cone, (685, rel_y + 200))
            screen.blit(traffic_cone, (685, rel_y + 300))
            screen.blit(traffic_cone, (685, rel_y + 400))
            screen.blit(traffic_cone, (685, rel_y + 500))
            screen.blit(traffic_cone, (685, rel_y - 40))

        y2 += enemycar_speed

        totalenemy_car_y -= (enemycar_speed / 4)
        enemycar(totalenemy_car_x, totalenemy_car_y, totalenemy_car)
        totalenemy_car_y += enemycar_speed

        '''
        if playerX <= 90:
            playerX = 90

        elif playerX >= 650:
            playerX = 650
        '''

        playercar(playerX, playerY)

        collision = isCollision(totalenemy_car_x, totalenemy_car_y, playerX, playerY)
        if collision:
            screen.blit(over_text, (25, 250))
            score = score - score
            car_passed = car_passed - car_passed
            pygame.display.update()
            time.sleep(4)
            game_loop()
            break

        if playerX <= 95 or playerX >= 645:
            crash = True
            screen.blit(over_text, (25, 250))
            score = score - score
            car_passed = car_passed - car_passed
            pygame.display.update()
            time.sleep(4)
            game_loop()
            break

        if totalenemy_car_y >= 800:
            totalenemy_car_y = 0 - 56
            totalenemy_car_x = random.randint(150, 600)
            totalenemy_car = random.randint(0, 6)
            car_passed += 1
            score = car_passed * 10

            if int(car_passed) % 30 == 0:
                level += 1
                enemycar_speed += 2
                font1 = pygame.font.Font('freesansbold.ttf', 100)
                text = font1.render("Level" + ' ' + str(level), 2, (1, 1, 1))
                screen.blit(text, (230, 250))
                pygame.display.update()
                time.sleep(2)


        '''
        while crash is True:
            score.delete()
            pygame.display.update()
            game_loop()
        '''

        # screen.blit(over_text, (30, 250))
        # pygame.display.update()
        # time.sleep(2)

        clock.tick(80)
        show_score(score, car_passed)

        pygame.draw.rect(screen, (0, 250, 0), (650, 0, 150, 50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 650 and mouse[0] < 800 and mouse[1] > 0 and mouse[1] < 50:
            pygame.draw.rect(screen, (0, 180, 0), (650, 0, 150, 50))
            if click == (True, 0, 0):
                paused()
        else:
            pygame.draw.rect(screen, (0, 250, 0), (650, 0, 150, 50))
        smallText = pygame.font.Font('freesansbold.ttf', 25)
        textSurface, textRect = text_object("PAUSE", smallText)
        textRect.center = ((650 + 150 / 2)), (0 + 50 / 2)
        screen.blit(textSurface, textRect)






        pygame.display.update()


entrypage_loop()
game_loop()