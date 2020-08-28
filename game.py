import pygame
import random
import sys
import os

pygame.init()

width=800
height=600
surface=pygame.Surface((100,100))

red=(255,0,0)
blue=(0,0,255)
yellow=(255,255,0)
bullet_color=(250,141,139)
background_color=(255,255,255)

player_size=30
player_position=[width/2,height-2*player_size]

bullet_size=10
bullet_position=[1,1]

enemy_size=35
enemy_position=[random.randint(0,width-enemy_size),0]
enemy_list=[enemy_position]

speed = 10
screen = pygame.display.set_mode((width, height))

game_over=False

score=0
hight_score=0
clock=pygame.time.Clock()
myFont = pygame.font.SysFont("monspace", 35)

pImg = pygame.image.load('C:\\Users\\vinh\\Pictures\\Saved Pictures\\images.png')
eImg = pygame.image.load('C:\\Users\\vinh\\Pictures\\Saved Pictures\\stone_PNG13593.png')


font = pygame.font.Font('freesansbold.ttf', 32)


def img_plane(player_position):
        # surface = pygame.Surface((800, 600), pygame.SRCALPHA)
        screen.blit(pImg, (player_position[0]-20,player_position[1]-10))

def img_enemy(enemy_position):
        screen.blit(eImg, (enemy_position[0],enemy_position[1]))

def set_level(score, speed):
        speed = score/10 + 1
        return speed

def drop_enemies(enemy_list):
        delay = random.random()
        if len(enemy_list)< 5 and delay < 0.1:
                x_pos = random.randint(0, width-enemy_size)
                y_pos = 0
                enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
        for enemy_position in enemy_list:
                pygame.draw.rect(screen, blue, (enemy_position[0], enemy_position[1], enemy_size, enemy_size))
                img_enemy(enemy_position)

def update_enemy_pos(enemy_list, score):
        for idx, enemy_position in enumerate(enemy_list):
                if enemy_position[1] >= 0 and enemy_position[1] < height:
                        enemy_position[1]+=speed
                else:
                        enemy_list.pop(idx)
                        score +=2
        return score

def update_hight_score(hight_score):
        if update_enemy_pos(enemy_list, score)>hight_score:
                hight_score=update_enemy_pos(enemy_list, score)
        return hight_score

def collision_check(enemy_list, player_position):
        for enemy_position in enemy_list:
                if detect_collision(enemy_position, player_position):
                        return True
        return False


def detect_collision(player_position, enemy_position):
        p_x = player_position[0]
        p_y = player_position[1]

        e_x = enemy_position[0]
        e_y = enemy_position[1]

        if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >=e_x and p_x < (e_x + enemy_size)):

                if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
                        return True
        return False

def del_enemy(enemy_list):
        b_y=bullet_position[1]

        e_y=enemy_position[1]
        if(e_y >= b_y and e_y < b_y + bullet_size) or (e_y <= b_y and b_y < e_y + bullet_size):
                value = enemy_list.pop(enemy_position)
                # enemy_list.pop(enemy_position[1])
                print(value)


def bullet_fire(bullet_position,player_position):
        
        if event.type == pygame.KEYDOWN:
                bullet_position[0]=int(player_position[0] + 15)
                bullet_position[1]=int(player_position[1] - 5)

                if event.key == pygame.K_SPACE:
                        for i in range(1,45):
                
                                bullet_position[1]-=bullet_size
                                print("n")
                                # bullet(bullet_size,player_position)
                                pygame.draw.circle(screen, bullet_color, (bullet_position[0],bullet_position[1]), bullet_size)     


def mes(collision_check):
        if collision_check(enemy_list,player_position)==True:
                text = font.render('Game Over', True, red, blue)
                textRect = text.get_rect()
                textRect.center = (width / 2, height / 2)
                screen.blit(text,textRect)

                time.sleep(2)

while not game_over:

        for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                        sys.exit()
        

                if event.type == pygame.KEYDOWN:
                        x=player_position[0]
                        y=player_position[1]

                        if event.key == pygame.K_a  and x>5:
                                x-=player_size
                        elif event.key == pygame.K_d and x<790:
                                x+=player_size
                        elif event.key == pygame.K_w and y>0:
                                y-=player_size
                        elif event.key == pygame.K_s and y<570:
                                y+=player_size
                        
                        player_position = [x,y]
                        print(x," ",y)
                


        screen.fill(background_color)
        
        img_plane(player_position)
        # img_enemy(enemy_position)

        
        drop_enemies(enemy_list)
        score = update_enemy_pos(enemy_list,score)
        speed = set_level(score, speed)
        hight_score = update_hight_score(hight_score)

        
        text = "Score:" + str(score)
        lable = myFont.render(text, 1, yellow)
        screen.blit(lable, (width-150, height-550))

        if collision_check(enemy_list, player_position):
                game_over=True
                break
        # del_enemy(enemy_list)
        # mes(collision_check)
        draw_enemies(enemy_list)
        bullet_fire(bullet_position,player_position)
        clock.tick(60)
        pygame.display.update()





