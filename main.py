from cards import *
from hand import *
from settings import *
import ctypes, platform, pygame, sys

if platform.system() == 'Window':
    ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.hand = Hand()


    def run(self):

        self.start_time = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get()
            

