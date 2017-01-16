#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

class Stage:
    def __init__(self):
        SCREEN_SIZE = (1366, 768)  # 本番環境画面サイズ
        self.img_bg = pygame.image.load("test.jpg").convert()
        self.img_rect = self.img_bg.get_rect()
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)

    def update(self):
        return

    def draw(self):
        self.screen.blit(self.img_bg, self.img_rect)
