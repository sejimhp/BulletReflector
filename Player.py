from Common import *

class Player:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.hp = 10
        self.time = pygame.time.get_ticks()
        self.x = 100
        self.y = 100

    def update(self, enemy_manager, player_bullet_manager, enemy_bullet_manager):
        # hpの判定
        if self.valid(enemy_manager):
            sys.exit()

        #弾と自機の当たり判定
        for bullet in enemy_bullet_manager.bullets:
            if bullet.x -19 <= self.x <= bullet.x +19 and \
               bullet.y -19 <= self.y <= bullet.y +19:
               player_bullet_manager.add(\
                bullet.x, bullet.y, bullet.r + 3, bullet.rad + math.pi)
               enemy_bullet_manager.bullets.remove(bullet)
        # 押されているキーをチェック
        self.pressed_keys = pygame.key.get_pressed()
        # 矢印キーでの移動と移動可能範囲の指定
        if self.x >= 25 and \
           self.pressed_keys[K_LEFT]:
            self.x -= 2
        if self.x <= 3786 and \
           self.pressed_keys[K_RIGHT]:
            self.x += 2
        if self.y <= 2346 and \
           self.pressed_keys[K_DOWN]:
            self.y += 2
        if self.y >= 25 and \
           self.pressed_keys[K_UP]:
            self.y -= 2

    def valid(self, enemy_manager, item_manager):
        #敵と自機の衝突判定
        for enemy in enemy_manager.enemys:
            if self.x -39 <= enemy.x <= self.x +39 and \
               self.y -39 <= enemy.y <= self.y +39:
               enemy_manager.enemys.remove(enemy)
               self.hp -= 1
        return self.hp <= 0

        for item in item_manager.items:
            if self.x == item.x and self.y == item.y:
                item_manager.items.remove(item)
                item_id = random.uniform(1,2)
                if item_id == 1:
                    self.hp += 1

    def draw(self, screen, stage):
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

        pygame.draw.circle(screen, (100,0,0),\
         (int(1100+self.x/15), int(50+self.y/15)), 3)
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 20)
        text = self.font.render(str(self.hp) , True, (0,0,0))
        screen.blit(text, (x, y))
