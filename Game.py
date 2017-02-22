from Common import *

class Game:
    def __init__(self):
        # SCREEN_SIZEの画面を作成
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        # 背景
        self.stage = Stage()
        # 自機
        self.player = Player()
        # 敵を管理
        self.enemy_manager = EnemyManager()
        # 自機の弾の管理
        self.player_bullet_manager = BulletManager()
        # 敵機の弾の管理
        self.enemy_bullet_manager = BulletManager()

    def update(self):
        self.stage.update()
        self.enemy_manager.update(self.player, self.enemy_bullet_manager)
        self.player.update(self.player_bullet_manager, self.enemy_manager)
        self.player_bullet_manager.update(self.stage)
        self.enemy_bullet_manager.update(self.stage)

    def draw(self):
        self.screen.fill((0,0,0))   # 画面を青色で塗りつぶす
        self.stage.draw(self.screen, self.player)
        self.player.draw(self.screen, self.stage)
        self.enemy_manager.draw(self.screen, self.player, self.stage)
        self.player_bullet_manager.draw(self.screen, self.player, self.stage, (0, 0, 255))
        self.enemy_bullet_manager.draw(self.screen, self.player, self.stage, (255, 0, 0))
        pygame.display.update()  # 画面
