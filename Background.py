import pygame

window_width = 1100
window_height = 550
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooting Game Piu Piu')

background = pygame.image.load('background.png').convert_alpha()
background_start = pygame.image.load('bg_start.png').convert_alpha()


class Background():  # background game
    def __init__(self, x, y, window_width, window_height):
        self.scroll_x = 0
        self.window_height = window_height
        self.window_width = window_width
        self.background = pygame.transform.scale(background, (window_width * 2, window_height))
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(self.background, (self.x, self.y))

    def move(self, character):  # di chuyển kéo background
        self.scroll_x = 0
        if character.player_react.right > self.window_height - self.x:
            self.scroll_x = -character.speed
            self.x += self.scroll_x

        if character.player_react.left < - self.x:
            self.scroll_x = character.speed
            self.x += self.scroll_x


class Background_start():  # background màn hình chính
    def __init__(self, x, y, window_width, window_height):
        self.window_height = window_height
        self.window_width = window_width

        self.background_start = pygame.image.load('bg_start.png')
        self.background_start = pygame.transform.scale(background_start, (window_width, window_height))

        self.x = x
        self.y = y

    def draw_bg_start(self):
        screen.blit(self.background_start, (self.x, self.y))
