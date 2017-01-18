from Common import *

class Game:
    def __init__(self):
        # SCREEN_SIZEの画面を作成
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        self.stage = Stage()
        self.player = Player()
        self.enemy_manager = EnemyManager()
        self.player_bullet_manager = BulletManager()
        self.enemy_bullet_manager = BulletManager()

    def update(self):
        self.stage.update()
        self.player.update()
        self.enemy_manager.update(self.player)
        self.player_bullet_manager.update()
        self.enemy_bullet_manager.update()

    def draw(self):
        self.screen.fill((0,0,0))   # 画面を青色で塗りつぶす
        self.stage.draw(self.screen, self.player)
        self.player.draw(self.screen, self.stage)
        self.enemy_manager.draw(self.screen, self.player, self.stage)
        self.player_bullet_manager.draw(self.screen)
        self.enemy_bullet_manager.draw(self.screen)
        pygame.display.update()  # 画面
