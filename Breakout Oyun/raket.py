import pygame
from Ayarlar import *

class Raket:
    def __init__(self, oyun):
        self.oyun = oyun

    
    def draw(self):
        pygame.draw.rect(self.oyun.screen, pygame.Color('grey'), RAKET)
        
    def raket_kontrolü(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and RAKET.left > 0:
            RAKET.left -= RAKET_HIZI
        if key[pygame.K_RIGHT] and RAKET.right < GENISLIK:
            RAKET.right += RAKET_HIZI
