import pygame, sys
from pygame.locals import QUIT,KEYDOWN

clock = pygame.time.Clock()

hero_img = pygame.image.load('assets/Hero_walk_01.png')

run_animation = False
#tem que ter uma dessas 3 variaveis para cada animção
curr_frame = 0
anim_time = 0
hero_walk_list = []
for i in range(4):
    hero_walk_list.append(pygame.image.load(f'assets/Hero_walk_0{i+1}.png'))

curr_frame_mm = 0
anim_time_mm = 0
mm_spritesheet = pygame.image.load('megaman_spritesheet.png')





pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello world!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                run_animation = True
    clock.tick(60)
    dt = clock.get_time()
    anim_time+=dt
    anim_time_sec = anim_time/1000

    
    if anim_time_sec > 0.15:
        curr_frame+=1
        if curr_frame > len(hero_walk_list)-1:
            curr_frame = 0
        anim_time = 0
    
    if run_animation:
        anim_time_mm+=dt
        anim_time_sec_mm = anim_time_mm/1000
        if anim_time_sec_mm > 0.05:
            curr_frame_mm+=1
            if curr_frame_mm > 9:
                curr_frame_mm = 0
                run_animation = False
            anim_time_mm = 0    
    #Desenho dos elementos 
    screen.fill((255,255,255))

    screen.blit(hero_walk_list[curr_frame],(0,0))

    screen.blit(mm_spritesheet,(200,200),(60*(curr_frame_mm % 5),60*(curr_frame_mm // 5),60, 60))


    pygame.display.update()