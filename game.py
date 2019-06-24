
import pygame
from pygame.locals import *
import math
import random

class game:
    pygame.init()
    width, height = 640, 480
    screen=pygame.display.set_mode((width, height))
    keys = [False, False, False, False, False]
    playerpos=[100,100]
    acc=[0,0]
    walls = 5
    score = 0
    arrows=[]
    badtimer=400
    badtimer1=0
    badtime = 0
    badguys=[[640,100]]
    healthvalue=194
    pygame.mixer.init()
    arrayofwalls = []
    player = pygame.image.load("resources/images/dude.png")
    grass = pygame.image.load("resources/images/concre.jpg")
    castle = pygame.image.load("resources/images/castle.png")
    arrow = pygame.image.load("resources/images/bullet.png")
    badguyimg1 = pygame.image.load("resources/images/badguy.png")
    badguyimg=badguyimg1
    healthbar = pygame.image.load("resources/images/healthbar.png")
    health = pygame.image.load("resources/images/health.png")
    gameover = pygame.image.load("resources/images/gameover.png")
    youwin = pygame.image.load("resources/images/youwin.png")
    wall = pygame.image.load("resources/images/mine.png")
    hit = pygame.mixer.Sound("resources/audio/explode.wav")
    enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
    shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
    hit.set_volume(0.05)
    enemy.set_volume(0.05)
    shoot.set_volume(0.05)
    pygame.mixer.music.load('resources/audio/ag.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    running = 1
    exitcode = 0
    while running:
        badtimer-=1
        screen.fill(0)
        for x in range(int(width/grass.get_width()+1)):
            for y in range(int(height/grass.get_height()+1)):
                screen.blit(grass,(x*100,y*100))
        screen.blit(castle,(0,10))
        screen.blit(castle,(0,100))
        screen.blit(castle,(0,190))
        screen.blit(castle,(0,280))
        screen.blit(castle,(0,370 ))
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
        playerrot = pygame.transform.rotate(player, 360-angle*57.29)
        playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
        screen.blit(playerrot, playerpos1)
        
        for bullet in arrows:
            score = score - 1
            index=0
            velx=math.cos(bullet[0])*10
            vely=math.sin(bullet[0])*10
            bullet[1]+=velx
            bullet[2]+=vely
            if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                arrows.pop(index)
            index+=1
            for projectile in arrows:
                arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
                screen.blit(arrow1, (projectile[1], projectile[2]))
     
        if badtimer==0:
            badguys.append([640, random.randint(50,430)])
            badtimer=100-(badtimer1*2)
            if badtimer1>=35:
                badtimer1=35
            else:
                badtimer1+=5
        index=0
        for badguy in badguys:
            if badguy[0]<-64:
                badguys.pop(index)
            badguy[0]-=7
            badrect=pygame.Rect(badguyimg.get_rect())
            badrect.top=badguy[1]
            badrect.left=badguy[0]
            if badrect.left<64:
                hit.play()
                healthvalue -= random.randint(5,20)
                badguys.pop(index)
            index1=0
            for bullet in arrows:
                bullrect=pygame.Rect(arrow.get_rect())
                bullrect.left=bullet[1]
                bullrect.top=bullet[2]
                if badrect.colliderect(bullrect):
                    enemy.play()
                    acc[0]+=1
                    badguys.pop(index)
                    arrows.pop(index1)
                    score = score + 100
            for mine in arrayofwalls:
                minerect=pygame.Rect(wall.get_rect())
                minerect.left=mine[0]
                minerect.top=mine[1]
                if badrect.colliderect(minerect):
                    enemy.play()
                    badguys.pop(index)
                    arrayofwalls.pop(index1)
                    score = score + 20
                index1+=1
            index+=1
        for badguy in badguys:
            screen.blit(badguyimg, badguy)
        font = pygame.font.Font(None, 24)
      
        survivedtext = font.render(str(int((90000-pygame.time.get_ticks())/60000))+":"+str(int((90000-pygame.time.get_ticks())/1000%60)).zfill(2), True, (0,0,0))
        textRect = survivedtext.get_rect()
        textRect.topright=[635,5]
        screen.blit(survivedtext, textRect)
        survivedtext1 = font.render(' Mines:' + str(walls), True, (0,0,0))
        textRect1 = survivedtext1.get_rect()
        textRect1.topright=[635,20]
        screen.blit(survivedtext1, textRect1)
        survivedtext2 = font.render(' Score:' + str(score), True, (0,0,0))
        textRect2 = survivedtext1.get_rect()
        textRect2.topright=[600,45]
        screen.blit(survivedtext2, textRect2)
        
        screen.blit(healthbar, (5,5))
        for health1 in range(healthvalue):
            screen.blit(health, (health1+8,8))
            
        if arrayofwalls :
            for wallo in arrayofwalls:
                 screen.blit(wall, wallo)
        

        pygame.display.flip()
        # pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)

               
                
            if event.type == pygame.KEYDOWN:
                
                if event.key==K_w:
                    keys[0]=True
                elif event.key==K_a:
                    keys[1]=True
                elif event.key==K_s:
                    keys[2]=True
                elif event.key==K_d:
                    keys[3]=True
                elif event.key==K_p:
                    keys[4]=True
                    
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    keys[0]=False
                elif event.key==pygame.K_a:
                    keys[1]=False
                elif event.key==pygame.K_s:
                    keys[2]=False
                elif event.key==pygame.K_d:
                    keys[3]=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                shoot.play()
                position=pygame.mouse.get_pos()
                acc[1]+=1
                arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])


##
        class Bullet:
            def __init__(self, position, speed):
                self.position = position
                self.speed = speed
                
            def move(self):
                self.position[1] += self.speed

##
                    
        if keys[0]:
            playerpos[1]-=3
        elif keys[2]:
            playerpos[1]+=3
        if keys[1]:
            playerpos[0]-=3
        elif keys[3]:
            playerpos[0]+=3
        elif keys[4] and walls > 0:
            arrayofwalls.append((playerpos[0],playerpos[1]))
            walls = walls-1
            keys[4]=False
        
        if pygame.time.get_ticks()>=90000:
            running=0
            exitcode=1
        if healthvalue<=0:
            running=0
            exitcode=0
        if acc[1]!=0:
            accuracy=acc[0]*1.0/acc[1]*100
        else:
            accuracy=0

    def file():
        try:
            with open('best.txt', 'r') as f:
                a = f.readline().strip()
                if a == '':
                    return 0
                else:
                    return  int(a)
        except FileNotFoundError:
            return 0

    a = file()        
    if exitcode==0:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        if a < score:
            text = font.render("Accuracy  : "+str(int(accuracy))+"%"  + "    New best Score:" + str(score), True, (255,0,0))
            with open('best.txt', 'w') as filehandle:  
                filehandle.write(str(score))    
        else:
            text = font.render("Accuracy  : "+str(int(accuracy))+"%"  + "    Best Score:" + str(a), True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(gameover, (0,0))
        screen.blit(text, textRect)
    else:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        if a < score:
            text = font.render("Accuracy  : "+str(int(accuracy))+"%"  + "    New best Score:" + str(score), True, (255,0,0))
            with open('best.txt', 'w') as filehandle:  
                filehandle.write(str(score))          
        else:
            text = font.render("Accuracy  : "+str(int(accuracy))+"%"  + "    Best Score:" + str(a), True, (255,0,0))
        textRect = text.get_rect()
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(youwin, (0,0))
        screen.blit(text, textRect)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.flip()


g = game
