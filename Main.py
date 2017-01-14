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
    SCREEN_SIZE = (1366, 768)  # 本番環境画面サイズ

    # Pygameを初期化
    pygame.init()
    # SCREEN_SIZEの画面を作成
    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)

    # ゲームループ
    while True:
        # 図形を描画
        screen.fill((0,0,0))   # 画面を青色で塗りつぶす

        pygame.draw.rect(screen, (255,255,0), Rect(10,10,300,200))
        pygame.display.update()  # 画面

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

if __name__ == "__main__":
    main()
