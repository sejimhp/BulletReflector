from Common import *

class BulletManager:
    def __init__(self):
        self.bullets = []

    def add(self, x, y, r, rad):
        self.bullets.append(Bullet(x, y, r, rad))

    def update(self, stage):
        for bullet in self.bullets:
            bullet.update()
            if bullet.valid(stage) == False:
                self.bullets.remove(bullet)

    def draw(self, screen, player, stage):
        for bullet in self.bullets:
            bullet.draw(screen, player, stage)
