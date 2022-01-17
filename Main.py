import pygame
from pygame.locals import *
from pygame import mixer
from class11 import *

pygame.init()#use the pygames module

#setting the game

clock = pygame.time.Clock()
fps = 60

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)#apply background sound
jump_fx = pygame.mixer.Sound('img_jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('img_game_over.wav')#dead sound
game_over_fx.set_volume(0.5)

#screen size
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jungle Run') #title of the run application

#define game variables
tile_size = 50
game_over = 0
main_menu = 0

#upload image
bg_img = pygame.image.load('Background.png')
bg_img = pygame.transform.scale(bg_img,(2016,1134))
restart_img = pygame.image.load('Restart.png')
start_img = pygame.image.load('Start.png')
exit_img = pygame.image.load('Exit.png')
button1_img = pygame.image.load('Button1.png')
button1_img = pygame.transform.scale(button1_img,(160,114))
button2_img = pygame.image.load('Button2.png')
button2_img = pygame.transform.scale(button2_img,(160,114))
trunk_img = pygame.image.load('Trunk1.png')
hedge_img = pygame.image.load('Tile_15.png')
Rules_img = pygame.image.load('Title.png')

player = Player(100, screen_height - 110)

#create buttons
restart_button = Button(screen_width // 2 - 400, screen_height // 2 + 150, restart_img,)
start_button = Button(screen_width // 2 - 400, screen_height // 2 - 200, start_img)
exit_button = Button(screen_width // 2 + 50, screen_height // 2 - 200, exit_img)
button1_button = Button(screen_width // 2 - 300, screen_height // 2, button1_img)
button2_button = Button(screen_width // 2 + 150, screen_height // 2, button2_img)

#GAME RUNNING
run = True
while run:

    clock.tick(fps)#set fps
    screen.blit(bg_img,(0,0))#set background

    if main_menu == 0:#FIRST SCREEN
        screen.blit(Rules_img,(200, 500))

        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = 1      
            game_over = 0
           
    if main_menu == 1:#LEVEL SCREEN
        if button1_button.draw():
            main_menu = 2   
            world_num = 1     
            
        if button2_button.draw():
            main_menu = 2
            world_num = 2   
            
    if main_menu == 2:#WORLD LEVEL
        #world pick
        if world_num == 1:
            #decoration load
            arrow_group.draw(screen)
            trunk_group.draw(screen)
            #world object load (important)
            water_group.draw(screen)
            door_group.draw(screen)
            game_over = player.update(game_over,world_num)#load player
            slug_group.update()
            slug_group.draw(screen)
            world.draw()

        if world_num == 2:
            #decoration - DRAW TO SCREEN
            arrow_group2.draw(screen)
            trunk_group2.draw(screen)
            #world object (important) - DRAW TO SCREEN
            water_group2.draw(screen)
            door_group.draw(screen)
            game_over = player.update(game_over,world_num)
            slug_group2.update()
            slug_group2.draw(screen)
            world2.draw()
        
        if game_over == 1: #entering door
            main_menu = 0
            player.reset(100, screen_height - 110)#RESET PLAYER POSITION

        if game_over == -1: #when player died
            if restart_button.draw():
                player.reset(100, screen_height - 110)#RESET PLAYER POSITION
                game_over = 0

    for event in pygame.event.get():#QUIT THE GAME
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()#Updates the game

pygame.quit()