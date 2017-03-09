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

from Stage import *
from Enemy import *
from Bullet import *
from BulletManager import *
from EnemyManager import *
from Player import *
from Item import *
from ItemManager import *
from Game import *
