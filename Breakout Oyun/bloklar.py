import pygame
from Ayarlar import *

class Bloklar:
    def __init__(self, oyun):
        self.oyun = oyun


    def draw(self):
        [pygame.draw.rect(self.oyun.screen, BLOK_RENKLERI[color], block) for color, block in enumerate(BLOK_LISTESI)]

