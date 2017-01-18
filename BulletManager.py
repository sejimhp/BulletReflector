from Common import *

class BulletManager:
    def __int__(self):
        self.bullets = []

    def add(self, x, y, r, rad):
        self.bullets.append(Bullet(x, y, r, rad))

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
