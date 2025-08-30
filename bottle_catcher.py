
import pgzrun
import random
from time import time  

WIDTH = 1214
HEIGHT = 800

diver = Actor("scuba diver 3")
diver.pos = (1000, 500)
fish = Actor("fish")
fish.pos = (600, 400)
cactus = Actor("cactus")
cactus.pos = random.randint(20, 1200), random.randint(20, 760)

bottles_collected = 0
seaweed_collected = 0
lives = 3
level = 1
bottles = []
seaweeds = []
fishes = []
game_over = False
won_game = False

fish_move_timer = time()
cactus_move_timer = time()  

def spawn_bottles(n):
    for i in range(n):
        bottle = Actor("bottle")
        bottle.pos = random.randint(20, 1200), random.randint(20, 760)
        bottles.append(bottle)

def spawn_seaweeds(n):
    for i in range(n):
        seaweed = Actor("seaweed")
        seaweed.pos = random.randint(20, 1200), random.randint(20, 760)
        seaweeds.append(seaweed)

def spawn_fishes(n):
    for i in range(n):
        fish = Actor("fish")
        fish.pos = random.randint(20, 1200), random.randint(20, 760)
        fishes.append(fish)

spawn_bottles(2)

def info(level,bottles,seaweed):
    screen.draw.text("In level " + str(level) + " you need to catch " + str(bottles) + " bottles and " + str(seaweed) + " seaweed !!!",(500,10), color = "white")

def draw():
    screen.blit("underwater backround", (0, 0))
    diver.draw()

    for bottle in bottles:
        bottle.draw()

    screen.draw.text("Bottles Collected: " + str(bottles_collected), (1000, 10), color="white")
    screen.draw.text("Level " + str(level), (1000, 50), color="white")

    if level == 1:
        info(1,5,0)

    if level == 2:
        info(2,15,5)

    if level == 3:
        info(3,15,10)

    if level == 4:
        info(4,15,15)

    if level == 5:
        info(5,20,15)

    if level == 6:
        info(6,25,20)

    if level >= 2:
        for seaweed in seaweeds:
            seaweed.draw()
        screen.draw.text("Seaweed Collected: " + str(seaweed_collected), (1000, 30), color="white")

    if level >= 3:
        fish.draw()
        screen.draw.text("Lives: " + str(lives), (1000, 70), color="white")

    if level >= 4:
        cactus.draw()

    if game_over == True:
        screen.fill("black")
        screen.draw.text("GAME OVER", center=(607, 400), color="white", fontsize=60)

    if won_game == True:
        screen.fill("PaleGreen")
        screen.draw.text("You won !!!", center = (607, 400), color = "black", fontsize = 60)

def update():
    global bottles_collected, seaweed_collected, level, lives, game_over, fish_move_timer , cactus_move_timer, won_game

    if game_over:
        return

    
    if level >= 3:
        if time() - fish_move_timer >= 3:  
            fish.pos = random.randint(50, 1200), random.randint(50, 750)  
            fish_move_timer = time()  

    if level >= 4:
        if time() - cactus_move_timer >=1.5:
            cactus.pos = random.randint(50, 1200), random.randint(50, 750)  
            cactus_move_timer = time()

    if keyboard.left and diver.x > 30:
        diver.x = diver.x - 2
    if keyboard.right and diver.x < 1200:
        diver.x = diver.x + 2
    if keyboard.up and diver.y > 30:
        diver.y = diver.y - 2
    if keyboard.down and diver.y < 770:
        diver.y = diver.y + 2

    for bottle in bottles:
        if diver.colliderect(bottle):
            bottles_collected = bottles_collected + 1
            bottle.pos = random.randint(50, 1200), random.randint(50, 750)

    for seaweed in seaweeds:
        if diver.colliderect(seaweed):
            seaweed_collected = seaweed_collected + 1
            seaweed.pos = random.randint(50, 1200), random.randint(50, 750)

    if diver.colliderect(cactus):
        bottles_collected = bottles_collected + 5
        cactus.pos = random.randint(20, 1200), random.randint(20, 760)

    if level >= 3 and diver.colliderect(fish):
        lives = lives - 1
        fish.pos = random.randint(50, 1200), random.randint(50, 750)
        if lives <= 0:
            game_over = True

    if level == 1 and bottles_collected >= 5:
        level = level + 1
        bottles_collected = 0
        spawn_seaweeds(2)

    if level == 2 and bottles_collected >= 15 and seaweed_collected >= 5:
        level = level + 1
        bottles_collected = 0
        seaweed_collected = 0
        spawn_bottles(4)
        spawn_seaweeds(3)

    if level == 3 and bottles_collected >= 15 and seaweed_collected >= 10:
        level = level + 1
        bottles_collected = 0
        seaweed_collected = 0
        spawn_bottles(1)
        spawn_fishes(1)

    if level == 4 and bottles_collected >= 15 and seaweed_collected >= 15 :
        level = level + 1
        bottles_collected = 0
        seaweed_collected = 0
        spawn_fishes(2)
        
    if level == 5 and bottles_collected >= 20 and seaweed_collected >= 15 :
        level = level + 1
        bottles_collected = 0
        seaweed_collected = 0

    if level == 6 and bottles_collected >=25 and seaweed_collected >= 20 :
        won_game = True


pgzrun.go()
