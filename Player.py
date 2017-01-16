#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
STAGE_SIZE = (3000, 2000)
SCREEN_SIZE = (1366, 768)  # 本番環境画面サイズ

class Player:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        self.hp = 10
        self.x = 0
        self.y = 0

    def update(self):
        # 押されているキーをチェック
        self.pressed_keys = pygame.key.get_pressed()
        # 矢印キーなら画像を移動
        if self.pressed_keys[K_LEFT]:
            self.x -= 1
        if self.pressed_keys[K_RIGHT]:
            self.x += 1
        if self.pressed_keys[K_DOWN]:
            self.y += 1
        if self.pressed_keys[K_UP]:
            self.y -= 1

    def draw(self):
        pygame.draw.circle(self.screen, (255,0,0), (self.x, self.y), 20)
