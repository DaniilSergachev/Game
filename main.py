import pygame
import sys
from settings import *
from level import Level
from button import Button
from level import LEVEL_MAP

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
BG_IMG = pygame.image.load("background.png")  
BG_IMG = pygame.transform.scale(BG_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))
BG_buttons = pygame.image.load("fossil_cave.jpg")
BG_buttons = pygame.transform.scale(BG_buttons, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Пещерный спелеолог')
clock = pygame.time.Clock()

def main_menu():
    start_button = Button(SCREEN_WIDTH/2-(252/2),150,252,74,"Новая игра","start_game.jpg","start_game_hover.jpg")
    exit_button = Button(SCREEN_WIDTH/2-(252/2),250,252,74,"Выйти","start_game.jpg","start_game_hover.jpg")
    running = True
    while running:
        screen.fill((0,0,0))
        global level
        level =  None
        font =pygame.font.Font(None,72)
        text_surface = font.render("Menu", True,(255,255,255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2,100))
        screen.blit(text_surface,text_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit

            if event.type == pygame.USEREVENT and event.Button == start_button:
                new_game()
            if event.type == pygame.USEREVENT and event.Button == exit_button: 
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button,exit_button]:
                btn.handle_event(event)
        screen.blit(BG_buttons,(0,0))
        for btn in [start_button,exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

       

        pygame.display.flip()

def new_game():
    global level
    level = Level()
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.blit(BG_IMG, (0, 0))

        level.run()
        pygame.display.update()
        clock.tick(60)            
        


if __name__ == "__main__":
    main_menu()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT :
#             pygame.quit()
#             sys.exit()

#     screen.blit(BG_IMG, (0, 0))
    
    
#     level.run()

#     pygame.display.update()
#     clock.tick(60)
