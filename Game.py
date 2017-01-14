#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

SCREEN_SIZE = (1366, 768)  # 本番環境画面サイズ

class Game:
    def __init__(self):
        # SCREEN_SIZEの画面を作成
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)

    def update(self):
        pygame.draw.rect(self.screen, (255,255,0), Rect(10,10,300,200))

    def draw(self):
        self.screen.fill((0,0,0))   # 画面を青色で塗りつぶす
        pygame.draw.rect(self.screen, (255,255,0), Rect(10,10,300,200))
        pygame.display.update()  # 画面
