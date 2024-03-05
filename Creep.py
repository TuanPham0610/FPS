import pygame
import time
import random

creep_time = random.randint(0, 5)
if creep_time == 0:
    creep_time += 1000
if creep_time == 1:
    creep_time += 1200
if creep_time == 2:
    creep_time += 1400
if creep_time == 3:
    creep_time += 1600
if creep_time == 4:
    creep_time += 1800
if creep_time == 5:
    creep_time += 2200

window_width = 1100
window_height = 550
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooting Game Piu Piu')

background = pygame.image.load('background.png').convert_alpha()

creep = pygame.image.load('creep_1.png')


# Class Creep

class Creep():

    def __init__(self, x, y, width, height):

        self.creep = pygame.transform.scale(creep, (width, height))
        self.x = x
        self.y = y
        self.speed = 3
        self.creep_react = self.creep.get_rect(topleft=(x + creep_time, y))

    def draw(self, x):
        self.x = x
        if self.creep_react.left <= -50: #Cho bot xuất hiện liên tục
            self.creep_react = self.creep.get_rect(topleft=(x + creep_time, 450))
        screen.blit(self.creep, self.creep_react)

    def move(self, left, right, bg):

        if left:
            self.creep_react.centerx -= self.speed

        if right:
            self.creep_react.centerx += self.speed

        if self.creep_react.right > bg.background.get_width():
            self.creep_react.right = bg.background.get_width()
