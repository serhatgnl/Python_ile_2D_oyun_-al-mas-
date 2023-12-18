import pygame
from Ayarlar import *

class Carpisma:
    def __init__(self, oyun):
        self.oyun = oyun
        self.dx, self.dy = 1, -1
   
    def carpisma_kontrolü(self, top, rect):
        if self.dx > 0:
            delta_x = top.right - rect.left
        else:
            delta_x = rect.right - top.left

        if self.dy > 0:
            delta_y = top.bottom - rect.top
        else:
            delta_y = rect.bottom - top.top

        if abs(delta_x - delta_y) < 10:
            self.dx, self.dy = -self.dx, -self.dy
        elif delta_x > delta_y:
            self.dy = -self.dy
        elif delta_y > delta_x:
            self.dx = -self.dx
        return self.dx, self.dy

            


