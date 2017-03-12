from Common import *

class Player:
    def __init__(self):
        self.hp = 10
        self.mp = 120
        self.time = pygame.time.get_ticks()
        self.x = 100
        self.y = 200
        self.image = pygame.image.load("image/player.png")
        self.image_item = pygame.image.load("image/item_bullet.png")
        self.image_item = pygame.transform.scale(self.image_item, (30, 30))
        self.image_title = pygame.image.load("image/frame.png")
        self.rad=0
        # 弾増やすよう
        self.flag_increase_bullet = False
        # レーザーの連射防止よう
        self.time_rapid_laser = 0

    def update(self, enemy_manager, player_bullet_manager, enemy_bullet_manager, item_manager, effect_manager):
        # あたり判定
        self.collision(enemy_manager, item_manager, effect_manager, enemy_bullet_manager, player_bullet_manager)

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
        if pygame.time.get_ticks() - self.time_rapid_laser > 1000 and \
         self.pressed_keys[K_z] and self.mp >= 30:
            self.time_rapid_laser = pygame.time.get_ticks()
            self.mp -= 60
            min_x = 10000
            min_y = 10000
            for enemy in enemy_manager.enemys:
                if (min_x**2 + min_y**2) > (enemy.x**2 + enemy.y**2):
                    min_x = enemy.x
                    min_y = enemy.y
            rad = math.atan2((self.y-min_y),(self.x-min_x))
            player_bullet_manager.add(self.x, self.y, 10,  rad+math.pi, 5)

        return self.hp <= 0

    def collision(self, enemy_manager, item_manager, effect_manager, enemy_bullet_manager, player_bullet_manager):
        #敵と自機の衝突判定
        for enemy in enemy_manager.enemys:
            if self.x -39 <= enemy.x <= self.x +39 and \
               self.y -39 <= enemy.y <= self.y +39:
               enemy_manager.enemys.remove(enemy)
               self.hp -= 1
               effect_manager.effects.append(Damage())

		#自機とアイテムの衝突判定
        for item in item_manager.items:
            if self.x -80 <= item.x <= self.x +30 and \
               self.y -80 <= item.y <= self.y +20:
               item_manager.items.remove(item)
               if item.id == 1:
                   self.hp += 1
               elif item.id == 2:
                   self.mp += 60
               elif item.id == 3:
                   self.flag_increase_bullet = True
                   self.time = pygame.time.get_ticks()

        #弾と自機の当たり判定
        for bullet in enemy_bullet_manager.bullets:
           if bullet.id == 2:#普通の弾
               if bullet.x -20 <= self.x <= bullet.x +30 and \
                bullet.y -25 <= self.y <= bullet.y +25:
                   player_bullet_manager.add(bullet.x, bullet.y, bullet.r + 3, bullet.rad + math.pi, 1)
                   enemy_bullet_manager.bullets.remove(bullet)
                   if self.flag_increase_bullet:
                       player_bullet_manager.add(bullet.x, bullet.y, bullet.r + 3, bullet.rad + math.pi - 0.1, 1)
                       player_bullet_manager.add(bullet.x, bullet.y, bullet.r + 3, bullet.rad + math.pi + 0.1, 1)
                       if pygame.time.get_ticks() - self.time > 10000:
                           self.time = pygame.time.get_ticks()
                           self.flag_increase_bullet = False
           elif bullet.id == 3: # 矢
               if bullet.x -10 <= self.x <= bullet.x + 40 and \
                bullet.y -10 <= self.y <= bullet.y + 40:
                   player_bullet_manager.add(bullet.x, bullet.y, 0, bullet.rad + math.pi, 3)
                   enemy_bullet_manager.bullets.remove(bullet)
           elif bullet.id == 4:
               if bullet.x -10 <= self.x <= bullet.x + 40 and \
                bullet.y -10 <= self.y <= bullet.y + 40:
                   self.mp += 1
                   enemy_bullet_manager.bullets.remove(bullet)

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

        # 左上のゲージの表示
        pygame.draw.rect(screen, (81,168,255), Rect(70,35,27*self.hp,15))
        pygame.draw.rect(screen, (62,255,158), Rect(70,65,1.5*self.mp,15))
        pygame.draw.rect(screen, (255,255,255), Rect(70+3*30,65,1,15))
        pygame.draw.rect(screen, (255,255,255), Rect(70+3*60,65,1,15))
        screen.blit(self.image_title, (20, 20))
        if self.flag_increase_bullet:
            screen.blit(self.image_item, (25, 90))

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
