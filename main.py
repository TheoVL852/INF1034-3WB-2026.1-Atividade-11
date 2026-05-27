import pygame, sys
from pygame.locals import QUIT,KEYDOWN

clock = pygame.time.Clock()

parado = True
run_animation= False
pulando = False

altura = -5
posicaoSheet = 48
pos_x = 0
pos_y = 0
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
            if event.key == pygame.K_a: #Mudar a direção do boneco se for para a esquerda ( ele olha pra esquerda )
                hero = mm_flip
            if event.key == pygame.K_d: #Muda a direção de volta dse ele tiver olhando pro outro lado
                hero = mm_spritesheet
            if event.key == pygame.K_SPACE and pulando == False: #Espaço pra pular / nao pode fazer double jump
                pulando = True
                altura = -5 #altura do pulo


                
        
            
    clock.tick(60)
    dt = clock.get_time()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]: #D para ir pra direita
        pos_x+=2
        run_animation = True
    
    if keys[pygame.K_a]: #A para ir pra esquerda
        pos_x-=2
        run_animation = True
    
    else: # Se não tá indo pra direita ou esquerda, ele ta parado
        parado = True
    

    if run_animation: #animação pra correr
        parado = False
        posicaoSheet = 192
        
        anim_time_mm+=dt
        anim_time_sec_mm = anim_time_mm/500
        if anim_time_sec_mm > 0.3:
            curr_frame_mm+=1
            if curr_frame_mm > 10:
                curr_frame_mm = 0
                run_animation = False
            anim_time_mm = 0  
    
    if pulando: # animação do pulo
        pos_y += altura #posição recebe a "altura"/velocidade que no inicio é negativa, então ela vai diminuindo cada vez mais
        altura += 0.5 #enquanto os frames passam, a altura vai aumentando de valor, uma hora ela vira positiva
                    # de 0.5 em 0.5, a altura aumenta e se adiciona a pos_y, o que faz com q ela aumente tbm chegando até 0
    if pos_y >= 0: # quando pos_y = 0 = chao, o pulo acaba
        pos_y = 0
        pulando = False
    
    if parado: #parado, animação parada
        posicaoSheet=48 
        #mudar a posição na sheet pra onde ele tem a animacao dele parado
        anim_time_mm+=dt
        anim_time_sec_mm = anim_time_mm/500
        if anim_time_sec_mm > 0.3:
            curr_frame_mm+=1
            if curr_frame_mm > 10:
                curr_frame_mm = 0
                run_animation = False
            anim_time_mm = 0    
            
    #Desenho dos elementos 
    screen.fill((255,255,255))

    screen.blit(hero,(200+pos_x,200+pos_y),(48*(curr_frame_mm%6),posicaoSheet,60,60))
    
    pygame.display.update()