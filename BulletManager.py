from Common import *

class BulletManager:
    def __init__(self):
        self.img_enemy1_bullet = pygame.image.load("image/enemy1_bullet.png").convert_alpha()
        self.img_player_bullet = pygame.image.load("image/player_bullet.png").convert_alpha()
        self.bullets = []

    def add(self, x, y, r, rad):
        self.bullets.append(Bullet(x, y, r, rad))

    def update(self, stage):
        # 弾が画面外に行った場合削除
        for bullet in self.bullets:
            bullet.update()
            if bullet.valid(stage) == False:
                self.bullets.remove(bullet)

    def draw(self, screen, player, stage, color):
        for bullet in self.bullets:
            if color == (0, 0, 255):
                bullet.draw(screen, player, stage, self.img_player_bullet)
            elif color == (255, 0, 0):
                bullet.draw(screen, player, stage, self.img_enemy1_bullet)
