from Common import *

class BulletManager:
    def __int__(self):
        self.bullets = []

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
