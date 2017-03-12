from Common import *

class Game:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 100)
        self.font_score = pygame.font.Font(None, 50)
        # ゲームの状態
        self.state = "MAIN"
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
        # アイテム管理
        self.item_manager = ItemManager()
        # エフェクト管理
        self.effect_manager = EffectManager()

    def update(self):
        if self.state == "MAIN":
            self.pressed_keys = pygame.key.get_pressed()
            if self.pressed_keys[K_RIGHT]:
                self.state = "GAME"
                self.player.hp = 10
                self.player.mp = 120
                self.score = 0
                self.enemy_bullet_manager.bullets.clear()
                self.player_bullet_manager.bullets.clear()
                self.item_manager.items.clear()
                self.enemy_manager.enemys.clear()
        elif self.state == "GAME":
            self.stage.update()
            self.item_manager.update(self.player)
            if self.enemy_manager.update(self.player, self.enemy_bullet_manager ,self.player_bullet_manager):
                self.score += 100
            if self.player.update(self.enemy_manager, self.player_bullet_manager, self.enemy_bullet_manager, self.item_manager, self.effect_manager):
                self.state = "SCORE"
            self.player_bullet_manager.update(self.stage, self.player)
            self.enemy_bullet_manager.update(self.stage, self.player)
            self.effect_manager.update()
        elif self.state == "SCORE":
            self.pressed_keys = pygame.key.get_pressed()
            if self.pressed_keys[K_SPACE]:
                self.state = "MAIN"



    def draw(self):
        self.screen.fill((0,0,0))   # 画面を青色で塗りつぶす
        if self.state == "MAIN":
            self.stage.draw(self.screen, self.player)
            self.player.draw(self.screen, self.stage)
            text = self.font.render("Right GameStart" , True, (255,255,255))
            self.screen.blit(text, (400, 400))
        elif self.state == "GAME":
            self.stage.draw(self.screen, self.player)
            self.enemy_manager.draw(self.screen, self.player, self.stage)
            self.player_bullet_manager.draw(self.screen, self.player, self.stage)
            self.enemy_bullet_manager.draw(self.screen, self.player, self.stage)
            self.item_manager.draw(self.screen, self.player, self.stage)
            self.player.draw(self.screen, self.stage)            self.effect_manager.draw(self.screen)            text = self.font_score.render(str(self.score) , True, (255,255,255))            self.screen.blit(text, (50, 700))        elif self.state == "SCORE":            self.stage.draw(self.screen, self.player)            text = self.font.render("GameOver" , True, (255,255,255))            self.screen.blit(text, (400, 400))        pygame.display.update()  # 画面