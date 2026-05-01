#snake
import pygame

from snake import Snake
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.K_s:
            Snake.change_direction([0,-1])

        if e.type == pygame.K_w:
            Snake.change_direction([0,1])

        if e.type == pygame.K_a:
            Snake.change_direction([-1,0])

        if e.type == pygame.K_d:
            Snake.change_direction([1,0])