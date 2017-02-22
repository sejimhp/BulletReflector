from Common import *

class EnemyManager:
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.enemys = []

    def update(self, player):
        if pygame.time.get_ticks() - self.time > 3000:
            self.time = pygame.time.get_ticks()
            self.enemys.append(Enemy())
        # 自機との衝突時に消滅
        for enemy in self.enemys:
            enemy.update(player)
            if enemy.valid(player) == False:
                self.enemys.remove(enemy)

    def draw(self, screen, player, stage):
        for enemy in self.enemys:
            enemy.draw(screen, player, stage)
