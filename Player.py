from Common import *

class Player:
    def __init__(self):
        self.hp = 10
        self.time = pygame.time.get_ticks()
        self.x = 100
        self.y = 100

    def update(self, player_bullet_manager, enemy_manager):
        # 押されているキーをチェック
        self.pressed_keys = pygame.key.get_pressed()
        # 弾発射
        if pygame.time.get_ticks() - self.time > 100:
            self.time = pygame.time.get_ticks()
            x = 1.0
            y = 1.0
            r = 1.0
            rad = 1.0
            if len(enemy_manager.enemys) != 0:
                enemy = enemy_manager.enemys[0]
                rad = math.atan2((enemy.y-self.y),(enemy.x-self.x))
            player_bullet_manager.add(self.x, self.y, r, rad)
        # 矢印キーでの移動と移動可能範囲の指定
        if self.x >= 25 and \
           self.pressed_keys[K_LEFT]:
            self.x -= 2
        if self.x <= 1895 and \
           self.pressed_keys[K_RIGHT]:
            self.x += 2
        if self.y <= 1055 and \
           self.pressed_keys[K_DOWN]:
            self.y += 2
        if self.y >= 25 and \
           self.pressed_keys[K_UP]:
            self.y -= 2

    """
    def vaild(self, bullet, player):
        #弾と自機の当たり判定
        if bullet.x -39 <= self.x <= bullet.x +39 and \
           bullet.y -39 <= self.y <= bullet.y +39:
            if self.pressed_keys[M]:
                return False
            else :
                self.hp -= 1
    """
    
    def draw(self, screen, stage):
        #hp = self.hp
        x = self.x
        y = self.y
        if self.x > SCREEN_SIZE[0]/2:
            x = SCREEN_SIZE[0]/2
        if self.y > SCREEN_SIZE[1]/2:
            y = SCREEN_SIZE[1]/2
        if self.x + SCREEN_SIZE[0]/2 > stage.img_rect[2]:
            x = self.x - (stage.img_rect[2] - SCREEN_SIZE[0])
        if self.y + SCREEN_SIZE[1]/2 > stage.img_rect[3]:
            y = self.y - (stage.img_rect[3] - SCREEN_SIZE[1])

        pygame.draw.circle(screen, (100,0,0), (int(1100+self.x/10), int(50+self.y/10)), 3)
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 20)
