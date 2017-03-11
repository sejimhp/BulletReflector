from Common import *

class EnemyManager:
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.enemys = []

    def update(self, player, enemy_bullet_manager, \
    player_bullet_manager):
        if pygame.time.get_ticks() - self.time > 3000:
            self.time = pygame.time.get_ticks()
            number = random.randint(4, 4)
            if number == 1:
                self.enemys.append(Enemy1())
            elif number == 2:
                self.enemys.append(Enemy2())
            elif number == 3:
                self.enemys.append(Enemy3())
            elif number == 4:
                self.enemys.append(Enemy4())
        # 自機との衝突時に消滅
        for enemy in self.enemys:
            enemy.update(player, enemy_bullet_manager)
            if enemy.valid(player_bullet_manager):
                self.enemys.remove(enemy)

    def draw(self, screen, player, stage):
        for enemy in self.enemys:
            enemy.draw(screen, player, stage)
