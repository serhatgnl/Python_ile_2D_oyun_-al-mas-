import pygame
import sys
from Ayarlar import *
from oyun_objeleri import *
from raket import *
from top import *
from bloklar import *


class BreakoutOyun:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        
        self.asset_yükleme()
        self.ses = Ses()
        self.ses.oyun_müzik.set_volume(0.4)
        self.ses.oyun_müzik.play()
        self.yeni_oyun()

    def asset_yükleme(self):
        self.arkaplan_image = pygame.image.load('Breakout Oyun/images/BG_space.jpg').convert()
        self.arkaplan_image = pygame.transform.scale(self.arkaplan_image, RES)

    def yeni_oyun(self):
        self.arkaplan = ArkaPlan(self)
        self.raket = Raket(self)
        self.top = Top(self)
        self.bloklar = Bloklar(self)

    def draw(self):
        self.arkaplan.draw()
        self.raket.draw()
        self.top.draw()
        self.bloklar.draw()
        pygame.display.flip()

    def update(self):
        self.arkaplan.update()
        self.clock.tick(FPS)

    def olay_kontrolü(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.raket.raket_kontrolü()
        self.top.top_kontrolü()
        

    def run(self):
        while True:
            self.olay_kontrolü()
            self.update()
            self.draw()


if __name__ == '__main__':
    oyun = BreakoutOyun()
    oyun.run()