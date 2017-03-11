from Common import *

class BulletManager:
    def __init__(self):
        self.bullets = []

    def add(self, x, y, r, rad, bullet_type):
        if bullet_type == 1:
            self.bullets.append(MyBullet(x, y, r, rad))
        elif bullet_type == 2:
            self.bullets.append(EnemyBullet(x, y, r + random.randint(1, 3), rad))
        elif bullet_type == 3:
            self.bullets.append(Arrow(x, y, r, rad))
        elif bullet_type == 4:
            self.bullets.append(EnemyLaser(x, y, r, rad))
        elif bullet_type == 5:
            self.bullets.append(PlayerLaser(x, y, r, rad))

    def update(self, stage, player):
        # 弾が画面外に行った場合削除
        for bullet in self.bullets:
            bullet.update(player)
            if bullet.valid(stage) == False:
                self.bullets.remove(bullet)

    def draw(self, screen, player, stage):
        for bullet in self.bullets:
            bullet.draw(screen, player, stage)
