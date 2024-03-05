import pygame,sys


window_width = 550
window_height = 550
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Test game')

 
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():  # các nút tương tác game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()
                