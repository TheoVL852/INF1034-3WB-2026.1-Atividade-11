import pygame, sys
from pygame.locals import QUIT,KEYDOWN

clock = pygame.time.Clock()

Flip = False
run_animation= False

pos_x = 0
curr_frame_mm = 0
anim_time_mm = 0
mm_spritesheet = pygame.image.load('player.png')
mm_flip = pygame.transform.flip(mm_spritesheet,True,False)
hero = mm_spritesheet


pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('Hello world!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_a:
                hero = mm_flip
            if event.key == pygame.K_d:
                hero = mm_spritesheet
        
            
    clock.tick(60)
    dt = clock.get_time()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        pos_x+=2
        run_animation = True
        

    if keys[pygame.K_a]:
        pos_x-=2
        run_animation = True


    if run_animation:
        anim_time_mm+=dt
        anim_time_sec_mm = anim_time_mm/500
        if anim_time_sec_mm > 0.1:
            curr_frame_mm+=1
            if curr_frame_mm > 10:
                curr_frame_mm = 0
                run_animation = False
            anim_time_mm = 0    
            
    #Desenho dos elementos 
    screen.fill((255,255,255))

    screen.blit(hero,(200+pos_x,200),(48*(curr_frame_mm%6),50,60,60))


    pygame.display.update()