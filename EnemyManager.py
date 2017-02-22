from Common import *

class EnemyManager:
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.enemys = []

    def update(self, player, enemy_bullet_manager):
        if pygame.time.get_ticks() - self.time > 3000:
            self.time = pygame.time.get_ticks()
            self.enemys.append(Enemy())
        # 自機との衝突時に消滅
        for enemy in self.enemys:
            enemy.update(player, enemy_bullet_manager)

    def draw(self, screen, player, stage):
        for enemy in self.enemys:
            enemy.draw(screen, player, stage)
