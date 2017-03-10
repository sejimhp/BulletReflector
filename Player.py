from Common import *

class Player:
    def __init__(self):
        self.hp = 10
        self.mp = 10
        self.time = pygame.time.get_ticks()
        self.x = 100
        self.y = 100
        self.image = pygame.image.load("image/player.png")
        self.rad=0

    def update(self, enemy_manager, player_bullet_manager, enemy_bullet_manager, item_manager):
        # hpの判定
        if self.valid(enemy_manager, item_manager):
            sys.exit()

        #弾と自機の当たり判定
        for bullet in enemy_bullet_manager.bullets:
            if bullet.x -19 <= self.x <= bullet.x +19 and \
               bullet.y -19 <= self.y <= bullet.y +19:
               if bullet.id == 2:
                   player_bullet_manager.add(bullet.x, bullet.y, bullet.r + 3, bullet.rad + math.pi, 1)
                   enemy_bullet_manager.bullets.remove(bullet)
               elif bullet.id == 3:
                   player_bullet_manager.add(bullet.x, bullet.y, 0, bullet.rad + math.pi, 3)
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
		#自機とアイテムの衝突判定
        for item in item_manager.items:
            if self.x -39 <= item.x <= self.x +39 and \
               self.y -39 <= item.y <= self.y +39:
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

        self.rad += 2
        image, (x, y) = rotate_blit(screen, self.image, (x, y), self.rad, True)

        pygame.draw.circle(screen, (100,0,0),\
         (int(1100+self.x/15), int(50+self.y/15)), 3)
        screen.blit(image, (int(x), int(y)))

        # ゲージの表示
        pygame.draw.rect(screen, (255,255,0), Rect(10,10,30*self.hp,30))
        pygame.draw.rect(screen, (255,255,0), Rect(10,50,30*self.mp,30))

    def rotate_blit(dst_surf, src_surf, pos, angle, center=True):
        #回転させたイメージの作成
        rotateimg = pygame.transform.rotate(src_surf,angle)

        w1, h1 = src_surf.get_size()  #回転前のサイズ
        w2, h2 = rotateimg.get_size() #回転後のサイズ

        if center:
            topleft = (pos[0] - w2 / 2, pos[1] - h2 / 2)
        else:
            dx, dy = (w2 - w1) / 2, (h2 - h1) / 2
            topleft = (pos[0] - dx, pos[1] - dy)
        dst_surf.blit(rotateimg, topleft)
        return rotateimg, topleft
