import pygame

window_width = 1100
window_height = 550
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooting Game Piu Piu')

background = pygame.image.load('background.png').convert_alpha()

player = pygame.image.load('main_1.png')
BLACK = (0, 0, 0)

BULLET_VELOCITY = 15
MAX_BULLETS = 5  # number of bullet that a character can shoot at a time


class Character:
    def __init__(self, x, y, width, height, window_height):

        self.window_height = window_height
        self.player = pygame.transform.scale(player, (width, height))
        self.player_react = self.player.get_rect(topleft=(x, y))
        self.player_react_ref = self.player.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.speed = 5
        self.movement = 0
        self.BOTTOM = self.window_height
        self.flag_jump = False

    def draw(self, bg):
        screen.blit(self.player, (self.player_react.left + bg.x, self.player_react.top + bg.y))


    def move(self, left, right, character, bg):

        if character.player_react.right > window_width - self.x:  # kịch màn hình trái phải
            self.x -= character.speed
        if character.player_react.left < -self.x:
            self.x += character.speed

        if left:  # speed di chuyển tránh ra khỏi màn hình khi đi lùi
            self.player_react.centerx -= self.speed
        if right:
            self.player_react.centerx += self.speed

        if self.player_react.right > bg.background.get_width():  # kịch màn hình trái phải
            self.player_react.right = bg.background.get_width()

        if self.player_react.left < 0:
            self.player_react.left = 0

        self.player_react_ref.centerx = self.player_react.centerx + bg.x
        self.player_react_ref.centery = self.player_react.centerx + bg.y

        self.player_react.bottom += self.movement  # Jump
        if self.player_react.bottom >= self.BOTTOM:
            self.player_react.bottom = self.BOTTOM
            self.flag_jump = True

    def update(self):
        pass
