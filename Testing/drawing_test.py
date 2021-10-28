""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Boat:
    def __init__(self, position_x, position_y, change_x, change_y, color):
        self.position_x = x
        self.position_y = y
        self.change_x = self.change_x
        self.change_y = self.change_y
        self.color = color

    def draw(self):
        arcade.draw.arc(self.position_x,


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, 800, 600, 500, arcade.color.YELLOW)
        arcade.draw_lrtb_rectangle_filled(0, 800, 500, 300, (255, 216, 23))
        arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.SAND)

        arcade.draw_arc_filled(x, y, 200, 100, arcade.color.DARK_BROWN, 180, 360)
        arcade.draw_rectangle_filled(x - 30, y + 50, 10, 100, arcade.color.BROWN)
        arcade.draw_rectangle_filled(x - 10, y + 90, 50, 30, arcade.color.RED)


def main():
    window = MyGame()
    arcade.run()


main()
