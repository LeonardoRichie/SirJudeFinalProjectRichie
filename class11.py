import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()

jump_fx = pygame.mixer.Sound('img_jump.wav')
jump_fx.set_volume(0.5)
screen_width = 1000
screen_height = 1000
game_over_fx = pygame.mixer.Sound('img_game_over.wav')
game_over_fx.set_volume(0.5)
tile_size = 50


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


#WORLD1
slug_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
#decoration
arrow_group = pygame.sprite.Group()
trunk_group = pygame.sprite.Group()

#WORLD2
slug_group2 = pygame.sprite.Group()
water_group2 = pygame.sprite.Group()
door_group2 = pygame.sprite.Group()
#decoration
arrow_group2 = pygame.sprite.Group()
trunk_group2 = pygame.sprite.Group()

screen = pygame.display.set_mode((screen_width, screen_height))

#GAME WORLD DESIGN
world_data = [
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 2, 2, 2, 2, 1, 7, 7, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 1, 7, 7, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 9, 0, 0, 7, 7, 1, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 0, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 1, 3, 1, 3, 3, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 6, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 1],
[1, 3, 2, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1],
[1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
[1, 5, 0, 2, 1, 1, 3, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1],
[1, 2, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
,
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 5, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 7, 0, 0, 1],
[1, 0, 0, 2, 7, 2, 0, 0, 0, 0, 0, 1, 3, 3, 1, 0, 7, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 7, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 0, 1, 7, 1, 1, 1, 0, 1, 2, 0, 0, 0, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 3, 7, 3, 3, 1],
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 4, 0, 2, 2, 0, 4, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 2, 3, 3, 2, 2, 2, 7, 1, 2, 7, 2, 2, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 7, 7, 7, 0, 0, 1, 1, 2, 2, 0, 0, 1],
[1, 1, 1, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
[1, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 2, 1, 7, 0, 2, 0, 1],
[1, 5, 0, 2, 1, 1, 3, 3, 3, 3, 3, 3, 3, 1, 1, 7, 3, 3, 3, 1],
[1, 2, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
]
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        #mouseposition
        position = pygame.mouse.get_pos()
        #pressing mouse
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:#being clicked
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:#reset when not clicked
                self.clicked = False


        #add button
        screen.blit(self.image, self.rect)

        return action

class Player():
    def __init__(self, x, y):
        self.reset(x, y)
        
    
    def update(self, game_over,world_num):
        dx = 0
        dy = 0
        walk_cooldown = 10

        if game_over == 0:

        #getkeypresses
        
            key = pygame.key.get_pressed()

            if key[pygame.K_SPACE] and self.jumped == False and self.air == False:
                jump_fx.play()
                self.vel_y = -15#move 15 pixel to the top
                self.jumped = True

            if key[pygame.K_SPACE] == False:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 5#move 5 pixel to the left
                self.counter += 1
                self.direction = -1

            if key[pygame.K_RIGHT]:
                dx += 5#move 5 pixel to the right
                self.counter += 1
                self.direction = 1

            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT]== False:
                self.counter = 0
                self.index = 0
                #if player head left / right, change the image view
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            #animation
            if self.counter > walk_cooldown:#moves after 0 pixel
                self.counter = 0
                self.index += 1
                #moving animation
                if self.index >= len(self.images_right):
                    self.index = 0#loop the image
                    
                if self.direction == 1:
                    self.image = self.images_right[self.index]#going right
                if self.direction == -1:
                    self.image = self.images_left[self.index]#going left

            #add gravity
            self.vel_y += 1#go 1 pixel down everytime player jumps
            if self.vel_y > 10:
                self.vel_y = 10

            dy += self.vel_y

            #check for collision
            self.air = True
            if world_num == 1:
                for tile in world.tile_list1:
                    #collision x direction
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0
                    #collision y direction
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        #check if below the ground jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.air = False
            if world_num == 2:
                for tile in world2.tile_list:
                    #collision x direction
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):#coordinates,size of the image
                        dx = 0
                    #collision y direction
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        #check if below the ground jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                        #check above the ground
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.air = False
                        
            if world_num == 1:
            #check collision with enemies
                if pygame.sprite.spritecollide(self, slug_group, False):
                    game_over_fx.play()
                    game_over = -1

                #check collision with water
                if pygame.sprite.spritecollide(self, water_group, False):
                    game_over_fx.play()
                    game_over = -1
                    
                #check collision with door
                if pygame.sprite.spritecollide(self, door_group, False):
                    game_over = 1

            if world_num == 2:
            #check collision with enemies
                if pygame.sprite.spritecollide(self, slug_group2, False):
                    game_over_fx.play()
                    game_over = -1

                #check collision with water
                if pygame.sprite.spritecollide(self, water_group2, False):
                    game_over_fx.play()
                    game_over = -1
                    
                #check collision with door
                if pygame.sprite.spritecollide(self, door_group2, False):
                    game_over = 1

            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0

        elif game_over == -1:
            self.image = self.dead_image

        #draw player unto screen
        screen.blit(self.image, self.rect)

        return game_over

    def reset(self,x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(3,6):
            img_right = pygame.image.load(f'Woodcutters{num}.png')
            img_right = pygame.transform.scale(img_right, (50, 60))
            img_left = pygame.transform.flip(img_right, True, False )#flipimage
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        grave_image = pygame.image.load('Grave.png') #dead image
        self.dead_image = pygame.transform.scale(grave_image, (50, 60))# resizing to the game size
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0 #Gravity
        self.jumped = False #jump by pressing the space 1 time (no holding spaces)
        self.direction = 0
        self.air = True #jump once only (no double or more jumps)

class World():
    def __init__(self, data):
        self.tile_list1 = []

        #load image
        dirt_img = pygame.image.load('Tile_12.png')
        dirtgrass_img = pygame.image.load('Tile_02.png')
        water_img = pygame.image.load('Tile_10.png')

        row_count = 0
        for row in data:
            col_count = 0

            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img,(tile_size, tile_size))
                    img_rect = img.get_rect()#create image rectangle
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)#listing
                    self.tile_list1.append(tile)#put all tile in the list

                if tile == 2:
                    img = pygame.transform.scale(dirtgrass_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)
                    self.tile_list1.append(tile)

                if tile == 3:
                    water = Water(col_count * tile_size, row_count * tile_size)
                    water_group.add(water)

                if tile == 4:
                    slug = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    slug_group.add(slug)

                if tile == 5:
                    exit = Exit(col_count * tile_size, row_count * tile_size)
                    door_group.add(exit)
                
                if tile == 6:
                    img = pygame.transform.scale(trunk_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)
                    self.tile_list1.append(tile)

                if tile == 7:
                    img = pygame.transform.scale(hedge_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)
                    self.tile_list1.append(tile)

                if tile == 8:
                    arrow = Arrow(col_count * tile_size, row_count * tile_size + 15)
                    arrow_group.add(arrow)
                
                if tile == 9:
                    trunk = Trunk(col_count * tile_size, row_count * tile_size + 15)
                    trunk_group.add(trunk)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list1:
            screen.blit(tile[0], tile[1])#draw picture in the place of the rectangle
            #pygame.draw.rect(screen, (255, 255, 255), tile[1],2)

class World2():
    def __init__(self, data):
        self.tile_list = []

        #load image
        dirt_img = pygame.image.load('Tile_12.png')
        dirtgrass_img = pygame.image.load('Tile_02.png')
        water_img = pygame.image.load('Tile_10.png') 
        

        row_count = 0
        for row in data:
            col_count = 0

            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(dirtgrass_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3:
                    water = Water2(col_count * tile_size, row_count * tile_size)
                    water_group2.add(water)

                if tile == 4:
                    slug = Enemy2(col_count * tile_size, row_count * tile_size + 15)
                    slug_group2.add(slug)

                if tile == 5:
                    exit = Exit(col_count * tile_size, row_count * tile_size)
                    door_group2.add(exit)

                if tile == 6:
                    img = pygame.transform.scale(trunk_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)
                    self.tile_list.append(tile)
                    
                if tile == 7:
                    img = pygame.transform.scale(hedge_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile  = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 8:
                    arrow = Arrow(col_count * tile_size, row_count * tile_size + 15)
                    arrow_group2.add(arrow)
                
                if tile == 9:
                    trunk = Trunk(col_count * tile_size, row_count * tile_size + 15)
                    trunk_group2.add(trunk)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen, (255, 255, 255), tile[1],2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Centipede.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        

    def update(self):
        self.image = pygame.image.load('Centipede.png')
        self.rect.x += self.move_direction
        self.move_counter += 1

        if self.move_counter > 50:
            self.move_direction *= -1
            self.move_counter *= -1

        if self.move_direction < 0:
            self.image = pygame.image.load('Centipede.png')

        if self.move_direction > 0:
            self.image = pygame.transform.flip(self.image, True, False)

class Water(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        water_img = pygame.image.load('Tile_10.png')
        self.image = pygame.transform.scale(water_img,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        Door_img = pygame.image.load('Door.png')
        self.image = pygame.transform.scale(Door_img,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Arrow1.png')
        self.image = pygame.transform.scale(self.image,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

class Trunk(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Trunk1.png')
        self.image = pygame.transform.scale(self.image,(tile_size + 200, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Centipede.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        

    def update(self):
        self.image = pygame.image.load('Centipede.png')
        self.rect.x += self.move_direction
        self.move_counter += 1

        if self.move_counter > 50:
            self.move_direction *= -1
            self.move_counter *= -1

        if self.move_direction < 0:
            self.image = pygame.image.load('Centipede.png')

        if self.move_direction > 0:
            self.image = pygame.transform.flip(self.image, True, False)

class Water2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        water_img = pygame.image.load('Tile_10.png')
        self.image = pygame.transform.scale(water_img,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

world = World(world_data[0])
world2 = World2(world_data[1])


