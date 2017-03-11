from Common import *

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

class Damage(Effect):
    def __init__(self):
        Effect.__init__(self)
        self.image = pygame.image.load("image/damage_effect2.png.png")
        # 点滅回数
        self.val = 3
        self.time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.time > 10:
            self.time = pygame.time.get_ticks()
            self.val -= 1

    def draw(self, screen):
        if pygame.time.get_ticks() - self.time < 50:
            screen.blit(self.image, (0, 0))

    def valid(self):
        return self.val
