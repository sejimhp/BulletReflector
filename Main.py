from Common import *

def main():

    # Pygameを初期化
    pygame.init()

    game = Game()

    # ゲームループ
    while True:
        # ゲームの実行
        game.update()
        # ゲームの描画
        game.draw()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

if __name__ == "__main__":
    main()
