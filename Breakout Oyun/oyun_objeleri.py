import pygame
from Ayarlar import *

class Ses:
    def __init__(self):
        self.top_cikis_ses = pygame.mixer.Sound('Breakout Oyun/Sesler/boom2.wav')
        self.top_blok_ses = pygame.mixer.Sound('Breakout Oyun/Sesler/laser5.wav')
        self.top_raket_ses = pygame.mixer.Sound('Breakout Oyun/Sesler/laser5.wav')
        self.oyun_müzik = pygame.mixer.Sound('Breakout Oyun/Sesler/through space.ogg')

class ArkaPlan:
    def __init__(self, oyun):
        self.oyun = oyun
        self.x = 0
        self.y = 0
        self.speed = KAYMA_HIZI - 2
        self.image = oyun.arkaplan_image

    def update(self):
        self.y = (self.y - self.speed) % -YUKSEKLIK

    def draw(self):
        self.oyun.screen.blit(self.image, (self.x, self.y))
        self.oyun.screen.blit(self.image, (self.x, YUKSEKLIK + self.y))