#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from Stage import *
from Player import *

STAGE_SIZE = (3000, 2000)
SCREEN_SIZE = (1366, 768)  # 本番環境画面サイズ

class Game:
    def __init__(self):
        # SCREEN_SIZEの画面を作成
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        self.stage = Stage()
        self.player = Player()

    def update(self):
        self.stage.update()
        self.player.update()

    def draw(self):
        self.screen.fill((0,0,0))   # 画面を青色で塗りつぶす
        self.stage.draw(self.player)
        self.player.draw(self.stage)
        pygame.display.update()  # 画面
