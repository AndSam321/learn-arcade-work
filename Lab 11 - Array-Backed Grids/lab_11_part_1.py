import arcade
import random


WIDTH = 60
HEIGHT = 60
MARGIN = 10
ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # Create grid of numbers
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        print(self.grid)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT / 2
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE

                else:
                    color = arcade.color.BLACK

                arcade.draw_rectangle_filled(x, y,
                                             WIDTH, HEIGHT,
                                             color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)

        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        # Row
        if self.grid[row + 1][column] == 0:
            self.grid[row + 1][column] = 1
        else:
            self.grid[row][column] = 0

        if self.grid[row - 1][column] == 0:
            self.grid[row - 1][column] = 1
        else:
            self.grid[row][column] = 0

        # Column
        if self.grid[row][column + 1] == 0:
            self.grid[row][column + 1] = 1
        else:
            self.grid[row][column] = 0

        if self.grid[row][column - 1] == 0:
            self.grid[row][column - 1] = 1
        else:
            self.grid[row][column] = 0

        if self.








        print("click", row, column)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
