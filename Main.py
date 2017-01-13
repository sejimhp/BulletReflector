#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import pygame.mixer
import random

# from Firework import *

def main():
    SCREEN_SIZE = (640, 480)  # 画面サイズ

    # Pygameを初期化
    pygame.init()
    # SCREEN_SIZEの画面を作成
    screen = pygame.display.set_mode(SCREEN_SIZE)

    #複数の花火を管理
    fireworks = []

    # ゲームループ
    while True:
        screen.fill((0,0,0))   # 画面を青色で塗りつぶす

        pygame.display.update()  # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

if __name__ == "__main__":
    main()
