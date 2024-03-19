import random
import pygame
from sys import exit

from pygame.sprite import Group

 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        player_walk1=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk2=pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk=[player_walk1, player_walk2]
        self.player_index=0
        self.player_jump=pygame.image.load('graphics/player/jump.png').convert_alpha()
        
        self.image=self.player_walk[self.player_index]
        self.rect=self.image.get_rect(midbottom=(90,300))
        self.gravity=0
        
        self.jump_sfx=pygame.mixer.Sound('bgm/wee.mp3')
        self.jump_sfx.set_volume(0.3)
        

    def player_input(self):
        keys =pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >=295:
            self.gravity=-18
            self.jump_sfx.play()
            
    def the_gravity(self):
        self.gravity+=1
        self.rect.y +=self.gravity
        if self.rect.bottom>=295:
            self.rect.bottom=295
            
    def animate_state(self):
        if self.rect.bottom<290:
            self.image=self.player_jump
        else:
            self.player_index+=0.1
            if self.player_index>=len(self.player_walk):self.player_index=0
            self.image=self.player_walk[int(self.player_index)]
    def update(self):
        self.player_input()
        self.the_gravity()
        self.animate_state()
 
 
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type=='fly':
            fly_1=pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2=pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames=[fly_1,fly_2]
            y_pos=190
        else:
            snail_1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames=[snail_1,snail_2]
            y_pos=295
        
        self.animation_index=0
        self.image=self.frames[self.animation_index]
        self.rect=self.image.get_rect(midbottom=(random.randint(900,1100),y_pos))
        
        
        
    def animation_state(self):
        self.animation_index+=0.1
        if self.animation_index>=len(self.frames): self.animation_index=0
        self.image=self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x-=6
        self.destroy()
    
    def destroy(self):
        if self.rect.x<=-100:
            self.kill()
            
     
 
def show_score():
    n_time=int(pygame.time.get_ticks() / 1000) - start_time
    score_surf=t_text.render(f'score: {n_time}', False, (64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return n_time
    
    
def obs_mov(obs_list):
    if obs_list:
        for obs_rect in obs_list:
            obs_rect.x-=5
            
            if obs_rect.bottom==295: screen.blit(snail_surface,obs_rect)
            else: screen.blit(fly_surf,obs_rect)
            
        obs_list=[obs for obs in obs_list if obs.x > -100]
        return obs_list
    
    else: return []

def collisions(player,obs):
    if obs:
        
        for obs_rect in obs:
            if player.colliderect(obs_rect): return False
            
    return True


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else: return True
                
def player_animate():
    global player_surface, player_index
    
    if player_rect.bottom < 290:
        player_surface=player_jump
    else:
        player_index+=0.1
        if player_index >=len(player_walk):player_index=0
        player_surface = player_walk[int(player_index)]

     
pygame.init()

screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('bruhN')
clock=pygame.time.Clock() 
t_text=pygame.font.Font('font/pixeltype.ttf',50)
game_active=False
start_time=0
score=0
BGM=pygame.mixer.Sound('bgm/bgm.mp3')
BGM.set_volume(0.1)
BGM.play(loops=-1)

#GROUPS
player=pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group=pygame.sprite.Group()


"""SURFACES"""
sky_surface=pygame.image.load('graphics/sky.png').convert()
ground_surface=pygame.image.load('graphics/ground.png').convert()

"""player"""
player_walk1=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk2=pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk=[player_walk1, player_walk2]
player_index=0
player_jump=pygame.image.load('graphics/player/jump.png').convert_alpha()
player_surface=player_walk[player_index]
player_rect=player_surface.get_rect(midbottom=(120,295))
player_gravity=0

"""loading screen"""
player_stand=pygame.image.load('graphics/player/player_stand.png').convert_alpha()
new_player_stand=pygame.transform.rotozoom(player_stand,180,2)
player_stand_rect=new_player_stand.get_rect(center=(400,200))

game_name=t_text.render('bruhN', False, '#234F1E')
game_name_rect=game_name.get_rect(center=(400,40))

start_text=t_text.render('Space to bruhN!', False, '#234F1E')  
start_text_rect=start_text.get_rect(center=(400, 340))


"""Obstacles"""
snail_1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames=[snail_1, snail_2]
snail_frame_index=0
snail_surface=snail_frames[snail_frame_index]

fly_1=pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_2=pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames=[fly_1, fly_2]
fly_frame_index=0
fly_surf=fly_frames[fly_frame_index]

obst_rect_list=[]

"""Timmer spawn"""
obs_timer=pygame.USEREVENT + 1
pygame.time.set_timer(obs_timer,1550)

snail_animation_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_animation_timer, 200)


while True:
    
    """input with event loop (#event for sake of pygame)"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #here the caps one shows the close button
            pygame.quit() #this lowercase one will close it.
            exit()
            
        if game_active:
                """mouse input"""
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos) and player_rect.bottom>=290:
                        player_gravity=-20
                        
                    """keybourd input"""
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE and player_rect.bottom>=290:
                        player_gravity=-20
        else:
              if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                  game_active=True
                #   snail_rect.left=790
                  start_time=int(pygame.time.get_ticks() / 1000)
                  #====================================================================================
        if game_active:          
            if event.type==obs_timer:
                obstacle_group.add(Obstacle(random.choice(['fly','snail','snail','snail'])))
                
                
                # if random.randint(0,2):
                #     obst_rect_list.append(snail_surface.get_rect(midbottom=(random.randint(900,1000),295)))
                # else:
                    
                #     obst_rect_list.append(fly_surf.get_rect(midbottom=(random.randint(900,1000),190)))
            
            if event.type == snail_animation_timer:
                if snail_frame_index==0: snail_frame_index=1
                else: snail_frame_index=0
                snail_surface=snail_frames[snail_frame_index]
                
            if event.type == fly_animation_timer:
                if fly_frame_index==0: fly_frame_index=1
                else: fly_frame_index=0
                fly_surf=fly_frames[fly_frame_index]
                
                      
            
        
    if game_active:
        """draw elements and update everything"""
        screen.blit(sky_surface,(0,0)) #blit stands for block img trnsfr
        screen.blit(ground_surface,(0,290))
        # pygame.draw.rect(screen,'#c0e8ec', score_rec)
        # pygame.draw.rect(screen,'#c0e8ec', score_rec,20)
        # screen.blit(score_surface,score_rec)
        score=show_score()
        
        # snail_rect.x-=4
        # if snail_rect.right <0: snail_rect.left=750
        
        # screen.blit(snail_surface,snail_rect)
        # player_rect.left+=1 #player speed
        
        """player"""
        # player_gravity+=0.5
        # player_rect.y+=player_gravity
        # if player_rect.bottom >=291: player_rect.bottom=291
        # player_animate()
        # screen.blit(player_surface,player_rect)
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        """obstacle movement"""
        # obs_rect_list=obs_mov(obst_rect_list)

        """collision"""
        game_active=collision_sprite()
        # game_active=collisions(player_rect,obs_rect_list)

            
    else:
    
        screen.fill('#1AA7EC')
        screen.blit(new_player_stand,player_stand_rect)
        obst_rect_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity=0
        
        
        
        score_txt=t_text.render(f'score:{score}',False, 'white')
        score_txt_rect=score_txt.get_rect(center=(400,330))
        screen.blit(game_name,game_name_rect)
        
        if score==0:
            screen.blit(start_text,start_text_rect)
        else:
            screen.blit(score_txt,score_txt_rect)
        
    
    pygame.display.update()
    clock.tick(60)
    