from Common import *

class Enemy:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        #HP
        self.hp = 3
        # 座標(double, double)
        self.x = random.uniform(1, 3811)
        self.y = random.uniform(1, 2371)
        # 移動速度
        self.r = random.uniform(0.1, 1)
        # 弾用のタイマー
        self.time = pygame.time.get_ticks()
        # 角度
        self.rad = 2
        self.image = pygame.image.load("image/enemy1.png")

    def update(self, player, enemy_bullet_manager):
        if player.x > self.x:
            self.x += self.r
        if player.y > self.y:
            self.y += self.r
        if player.x < self.x:
            self.x -= self.r
        if player.y < self.y:
            self.y -= self.r
        #弾発射
        if pygame.time.get_ticks() - self.time > 1000:
            self.time = pygame.time.get_ticks()
            x = 1.0
            y = 1.0
            r = 1.0
            rad = math.atan2((player.y-self.y),(player.x-self.x))
            enemy_bullet_manager.add(self.x, self.y, r, rad)

    def valid(self, player_bullet_manager):
        #敵の跳ね返した弾と自機の衝突判定
        for bullet in player_bullet_manager.bullets:
            if bullet.x -19 <= self.x <= bullet.x +19 and \
               bullet.y -19 <= self.y <= bullet.y +19:
                player_bullet_manager.bullets.remove(bullet)
                self.hp -= 1
        return self.hp < 1

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

    def draw(self, screen, player, stage):
        x = self.x
        y = self.y
        if player.x > SCREEN_SIZE[0]/2:
            x -= (player.x - SCREEN_SIZE[0]/2)
        if player.y > SCREEN_SIZE[1]/2:
            y -= (player.y - SCREEN_SIZE[1]/2)
        if player.x + SCREEN_SIZE[0]/2 > stage.img_rect[2]:
            x = self.x - (stage.img_rect[2] - SCREEN_SIZE[0])
        if player.y + SCREEN_SIZE[1]/2 > stage.img_rect[3]:
            y = self.y - (stage.img_rect[3] - SCREEN_SIZE[1])

        self.rad += 2
        image, (x, y) = rotate_blit(screen, self.image, (x, y), self.rad, True)

        pygame.draw.circle(screen, (0,100,0),\
         (int(1100+self.x/15), int(50+self.y/15)), 3)
        screen.blit(image, (int(x), int(y)))
