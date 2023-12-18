import pygame
from Ayarlar import *
from carpisma import Carpisma


class Top:
    def __init__(self, oyun):
        self.oyun = oyun
        self.dx, self.dy = 1, -1

    def draw(self):
        pygame.draw.circle(self.oyun.screen, pygame.Color('red'), TOP.center, TOP_YARICAPI )

    def top_kontrolü(self): 
       
       TOP.x += TOP_HIZI * self.dx
       if TOP.centerx < TOP_YARICAPI or TOP.centerx > GENISLIK - TOP_YARICAPI:
            self.dx = -self.dx
       
       TOP.y += TOP_HIZI * self.dy 
       if TOP.centery < TOP_YARICAPI:
           self.dy = -self.dy
       self.carpisma_top_blok()
       self.carpisma_top_raket()

       if TOP.bottom > YUKSEKLIK:
           self.oyun.ses.top_cikis_ses.set_volume(0.3)
           self.oyun.ses.top_cikis_ses.play()
           pygame.time.wait(1000)
           print('OYUN BITTI!')
           exit()
           
       elif not len(BLOK_LISTESI):
           print('KAZANDINIZ!!!')
           

    def carpisma_top_raket(self):
        if TOP.colliderect(RAKET) and self.dy > 0:
             self.dx, self.dy = Carpisma.carpisma_kontrolü(self, TOP, RAKET)
             self.oyun.ses.top_blok_ses.set_volume(0.3)
             self.oyun.ses.top_blok_ses.play()

    def carpisma_top_blok(self):
        isabet_index = TOP.collidelist(BLOK_LISTESI) 
        if isabet_index != -1:
            isabet_rect = BLOK_LISTESI.pop(isabet_index) 
            isabet_renk = BLOK_RENKLERI.pop(isabet_index) 
            self.dx, self.dy = Carpisma.carpisma_kontrolü(self, TOP, isabet_rect)
            self.oyun.ses.top_blok_ses.set_volume(0.3)
            self.oyun.ses.top_blok_ses.play()

          

        