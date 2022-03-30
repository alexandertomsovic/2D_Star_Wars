# Star Wars 2D shooter
# Created by Alex Tomsovic
# This game is not associated with ⒸStar Wars, ⒸLucasfilm, or ⒸDisney in any form.

# Import list
import pygame
from colorama import Fore
import math
import sys
import time
import random

# Function for moving text


def typewrite(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

# Function for slower moving text


def slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.09)


# Title and credits start
typewrite("Welcome to " + Fore.YELLOW+"Star Wars" + Fore.WHITE +
          ". . . In " + Fore.RED+"2" + Fore.BLUE+"D")

typewrite("\nThis game was created by " +
          Fore.LIGHTGREEN_EX+"Alex Tomsovic.\n")

# Start game request
typewrite("\nPress 1 to play!\n")
start_game = int(input(">>: "))

# Softgate introduction to game
if start_game == 1:
    slow(Fore.YELLOW+"\nOnce upon a time in a galaxy far far away...")

# Initializes pygame window
pygame.init()

# Creates the screen
game_screen = pygame.display.set_mode((800, 590))

background = pygame.image.load('background.png')

# Window title
pygame.display.set_caption("Star Wars in 2D - Alex Tomsovic")

# Initializes the crosshair
cursurImg = pygame.image.load('crosshair.png')
cursurX = 0
cursurY = 0
pygame.mouse.set_visible(False)

# Initializes the players character
playerImg = pygame.image.load('character.png')
playerX = 400
playerY = 200
playerX_change = 0
playerY_change = 0
player_speed = 4

# Initializes the players blaster
gun1Img = pygame.image.load('blaster.png')
gun1X = playerX
gun1Y = playerY

# Initializes enemies and dictates actions
'''enemyImg = pygame.image.load('enemy.png')
enemyX = 400
enemyY = 10
enemyX_change = 1
enemyY_change = 1'''
enemy_speed = 1
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_image = ['droid1.png', 'droid2.png',
               'droid3.png', 'maul.png', 'grievous.png', ]
num_enemy = 5

for b in range(num_enemy):
    enemyImg.append(pygame.image.load(random.choice(enemy_image)))
    enemyX.append(random.randrange(100, 500))
    enemyY.append(10)
    enemyX_change.append(1)
    enemyY_change.append(1)

# Blaster bullet dictation
shoot_s = False
bullet_speed = 7
bulletImg = []
bulletX = []
bulletY = []
bulletX_change = []
bulletY_change = []
dx = []
dy = []


def player(x, y):
    game_screen.blit(playerImg, (x, y))


def cursur(x, y):
    game_screen.blit(cursurImg, (x, y))


def bullet(x, y):
    for i in range(len(bulletX)):
        game_screen.blit(bulletImg[i], (x, y))


'''def gun1(x, y):
    game_screen.blit(gun1Img, (x, y))'''


def enemy(x, y, i):
    game_screen.blit(enemyImg[b], (x, y))


def isCollision(enemyY, enemyX, bulletY, bulletX):
    global playerX
    global num_enemy

    # If statement to check for a bullet collision
    distance = math.sqrt(
        math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 32:
        return True
    else:
        return False


def Quit():
    globalrung
    run = False

# Tracks the enemies to the player


def tracker():
    global enemyX_change
    global enemyY_change
    for b in range(num_enemy):
        if playerX > enemyX[b]:
            enemyX_change[b] = enemy_speed
        if playerX < enemyX[b]:
            enemyX_change[b] = -enemy_speed
        if playerY > enemyY[b]:
            enemyY_change[b] = enemy_speed
        if playerY < enemyY[b]:
            enemyY_change[b] = -enemy_speed


def Bullet():
    global bulletX_change
    global bulletY_change
    global dx
    global dy
    bulletImg.append(pygame.image.load('bullet.png'))
    bulletX.append(playerX + 10)
    bulletY.append(playerY + 10)
    bulletX_change.append(0)
    bulletY_change.append(0)
    x, y = pygame.mouse.get_pos()
    angle = math.atan2(y - playerY, x - playerX)
    dx.append(math.cos(angle) * bullet_speed)
    dy.append(math.sin(angle) * bullet_speed)

    def move():
        global bulletX_change
        global bulletY_change
        global shoot_s
        for i in range(len(bulletX)):
            bulletX_change[i] = dx[i]
            bulletY_change[i] = dy[i]

    move()

# Removes bullet entity once it reaches the edge of the screen


def remove_bullet():
    bulletImg.pop(i - 1)
    bulletX.pop(i - 1)
    bulletY.pop(i - 1)
    bulletX_change.pop(i - 1)
    bulletY_change.pop(i - 1)
    dx.pop(i - 1)
    dy.pop(i - 1)

# Function for the blaster trigger following the crosshair


def blaster_rotate():
    global playerX
    global playerY
    pos = pygame.mouse.get_pos()
    # rise over run
    angle = 360 - math.atan2(pos[1] - playerY,
                             pos[0] - playerX) * 180 / math.pi
    rotimage = pygame.transform.rotate(gun1Img, angle)
    rect = rotimage.get_rect(center=(playerX + 15, playerY + 15))
    game_screen.blit(rotimage, rect)


# Updates game until a quit request is initiated
run = True
while run:

    time.sleep(0.01)

    # bg img
    game_screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # check weather keystroke is pressed

        if event.type == pygame.KEYDOWN:
            # check weather keystroke is right or left

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -player_speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = player_speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -player_speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = player_speed

            # checks if shooting
            if event.key == pygame.K_SPACE:
                pass

            # quits program
            if event.key == pygame.K_q:
                Quit()

            if event.key == pygame.K_SPACE:
                Bullet()

        # checks if key is realeased and stops player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                playerX_change = 0
                playerY_change = 0

        pressed = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:
            Bullet()

    for i in range(len(bulletX)):
        # bullet boundries
        if bulletY[i - 1] <= -50 or bulletY[i - 1] >= 710 or bulletX[
                i - 1] <= -50 or bulletX[i - 1] >= 830:
            remove_bullet()

    for i in range(len(bulletX)):
        bulletX[i] += bulletX_change[i]
        bulletY[i] += bulletY_change[i]
        bullet(bulletX[i], bulletY[i])
        # Collision
        for b in range(num_enemy):
            collision = isCollision(enemyX[b], enemyY[b], bulletX[i],
                                    bulletY[i])
            if collision:
                enemyX[b] = random.randint(100, 700)
                enemyY[b] = random.randint(10, 300)

    for b in range(num_enemy):
        enemyX[b] += enemyX_change[b]
        enemyY[b] += enemyY_change[b]
        enemy(enemyX[b], enemyY[b], b)
        tracker()

    # player boundries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 770:
        playerX = 770
    if playerY <= 0:
        playerY = 0
    elif playerY >= 560:
        playerY = 560

    # puts player
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)

    # places gun
    gun1X = playerX
    gun1Y = playerY + 5
    blaster_rotate()

    pos = pygame.mouse.get_pos()
    cursur(pos[0] - 0, pos[1] - 0)

    # update game_screen
    pygame.display.update()
