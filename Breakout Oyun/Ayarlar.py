import pygame
from random import randrange as rnd

RES = GENISLIK, YUKSEKLIK = 1600, 900
FPS = 60
KAYMA_HIZI = 6

RAKET_G = 330
RAKET_Y = 35
RAKET_HIZI = 15
RAKET = pygame.Rect(GENISLIK // 2 - RAKET_G // 2, YUKSEKLIK - RAKET_Y - 40, RAKET_G, RAKET_Y)

TOP_YARICAPI = 25
TOP_HIZI = 8
TOP_RECT = int(TOP_YARICAPI * 2 ** 0.5)
TOP = pygame.Rect(rnd(TOP_RECT, GENISLIK - TOP_RECT), YUKSEKLIK // 2, TOP_RECT, TOP_RECT)

BLOK_LISTESI = [pygame.Rect(30 + 130 *i, 30 + 80 * j, 100, 50) for i in range(12) for j in range(5)]
BLOK_RENKLERI = [(255, 127, 0) for i in range(12) for j in range(5)]