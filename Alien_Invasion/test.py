import pygame
import sys
class Test:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)

if __name__ == '__main__':
    alien_invasion = Test()
    alien_invasion.run()

            

