from Common import *

class BulletManager:
    def __init__(self):
        self.bullets = []

    def add(self, x, y, r, rad):
        self.bullets.append(Bullet(x, y, r, rad))

    def update(self, stage):
        # 弾が画面外に行った場合削除
        for bullet in self.bullets:
            bullet.update()
            if bullet.valid(stage) == False:
                self.bullets.remove(bullet)
        """
        #敵の打った弾が自機と衝突した場合削除
        for bullet in self.bullets:
            bullet.update(player)
            if enemy.valid(player) == False:
                self.enemys.remove(bullet)
        """

    def draw(self, screen, player, stage):
        for bullet in self.bullets:
            bullet.draw(screen, player, stage)
