import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_MINE = 0.5
COIN_COUNT = 50
MINE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= 1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        # Variables that will hold sprite lists.

        self.player_list = None

        self.coin_list = None

        self.mine_list = None

        # Set up the player info

        self.player_sprite = None

        self.score = 0

        # Don't show the mouse cursor

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.mine_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Player
        # Clip art from CityPNG.com
        self.player_sprite = arcade.Sprite("Mr.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            self.coin_list.append(coin)


        for i in range(MINE_COUNT):
            mine = arcade.Sprite("Mrs.png", SPRITE_SCALING_MINE)
            mine.center_x = random.randrange(SCREEN_WIDTH)
            mine.center_y = random.randrange(SCREEN_HEIGHT)
            self.mine_list.append(mine)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()
        self.mine_list.draw

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time: float):
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.mine_list)
        for mine in hit_list:
            mine.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
