#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import pygame.mixer
# import pygame._view
import re
import random
STAGE_SIZE = (3811, 2371)
SCREEN_SIZE = (1366, 768)  # 本番環境画面サイズ

def rotate_blit(dst_surf, src_surf, pos, angle, center=True):
    """画像を回転させてblitする
    centerがTrueのとき，posはdst_surf上でsrc_surfの中心を差す
    centerがFalseのとき，posはdst_surf上でsrc_surfの左上を差す
    """
    #回転させたイメージの作成
    rotateimg = pygame.transform.rotate(src_surf,angle)

    w1, h1 = src_surf.get_size()  #回転前のサイズ
    w2, h2 = rotateimg.get_size() #回転後のサイズ

    if center:
        topleft = (pos[0] - w2 / 2, pos[1] - h2 / 2)
    else:
    # 回転したことによる中心位置の移動距離
        dx, dy = (w2 - w1) / 2, (h2 - h1) / 2
        topleft = (pos[0] - dx, pos[1] - dy)
    dst_surf.blit(rotateimg, topleft)
    return rotateimg, topleft

from Stage import *
from Enemy import *
from Bullet import *
from BulletManager import *
from Effect import *
from EffectManager import *
from EnemyManager import *
from Player import *
from Item import *
from ItemManager import *
from Game import *
