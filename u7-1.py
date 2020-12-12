# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:15:57 2020

@author: 88690
"""

import random,pygame

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

pygame.init()
size=(700,800)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Cindy")

class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        
block_list= pygame.sprite.Group()
all_sprites_list= pygame.sprite.Group()
         
for i in range(99):
    block=Block(red,15,15)
    block.rect.x=random.randrange(650)
    block.rect.y=random.randrange(650)
    block_list.add(block)

player = Block(black,20,15)
all_sprites_list.add(player)
done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    screen.fill(white)
    block_list.draw(screen)
    pygame.display.flip()

pygame.quit()









