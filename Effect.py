from Common import *

damage_effect = pygame.image.load("image/damage_effect2.png.png")

class Effect:
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.image = 0

    def update(self):
        return

    def draw(self, screen):
        return

    def valid(self):
        return

# ダメージを受けた時のエフェクト
class Damage(Effect):
    def __init__(self):
        Effect.__init__(self)
        self.image = damage_effect
        # 点滅回数
        self.val = 3
        self.time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.time > 10:
            self.time = pygame.time.get_ticks()
            self.val -= 1

    def draw(self, screen, stage, player):
        if pygame.time.get_ticks() - self.time < 50:
            screen.blit(self.image, (0, 0))

    def valid(self):
        return self.val <= 0

# 敵を倒した時のエフェクト
class Bom(Effect):
    def __init__(self, x, y):
        Effect.__init__(self)
        self.x = x
        self.y = y
        self.images = []
        self.images.append(pygame.image.load("image/effect/effect0.png"))
        self.images.append(pygame.image.load("image/effect/effect1.png"))
        self.images.append(pygame.image.load("image/effect/effect2.png"))
        self.images.append(pygame.image.load("image/effect/effect3.png"))
        self.images.append(pygame.image.load("image/effect/effect4.png"))
        self.images.append(pygame.image.load("image/effect/effect5.png"))
        # エフェクトの数
        self.val = 0
        self.time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.time > 100:
            self.time = pygame.time.get_ticks()
            self.val += 1

    def draw(self, screen, stage, player):
        x = self.x
        y = self.y
        if player.x > SCREEN_SIZE[0]/2:
            x -= (player.x - SCREEN_SIZE[0]/2)
        if player.y > SCREEN_SIZE[1]/2:
            y -= (player.y - SCREEN_SIZE[1]/2)
        if player.x + SCREEN_SIZE[0]/2 > stage.img_rect[2]:
            x = self.x - (stage.img_rect[2] - SCREEN_SIZE[0])
        if player.y + SCREEN_SIZE[1]/2 > stage.img_rect[3]:
            y = self.y - (stage.img_rect[3] - SCREEN_SIZE[1])

        screen.blit(self.images[self.val], (x-30, y-30))

    def valid(self):
        return self.val > 5
