from Common import *

class EnemyManager:
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.enemys = []

    def update(self, player):
        if pygame.time.get_ticks() - self.time > 3000:
            self.time = pygame.time.get_ticks()
            self.enemys.append(Enemy())
        for enemy in self.enemys:
            enemy.update(player)

    def draw(self, screen, player, stage):
        for enemy in self.enemys:
            enemy.draw(screen, player, stage)
