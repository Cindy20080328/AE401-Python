#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:15:31 2020

@author: zhuxinyan
"""

import pygame

white = (255,255,255)
black = (0,0,0)

pygame.init()
 
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cindy")

clock = pygame.time.Clock()

player_music = pygame.mixer.Sound("laser5.ogg")
player_image = pygame.image.load("playerShip1_orange.png")
player_backgrond = pygame.image.load("saturn_family1.jpg")

backgrond_postion = (0,0)
player_image.set_colorkey(black)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_music.play()

    screen.blit(player_backgrond,backgrond_postion)
    player_postion = pygame.mouse.get_pos()
    x = player_postion[0]
    y = player_postion[1]

    screen.blit(player_image,[x,y])
    pygame.display.flip()   
    clock.tick(60)
    
pygame.quit()