import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Drawing Sand
def draw_sand():
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.SAND)


# Sunset
def draw_sunset():
    arcade.draw_lrtb_rectangle_filled(0, 800, 600, 500, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(0, 800, 500, 300, (255, 216, 23))


# Sun
def draw_sun():
    arcade.draw_arc_filled(400, 300, 200, 200, arcade.color.RED, 0, 180)


# Birds
def draw_birds(x, y):
    arcade.draw_arc_outline(x, y, 100, 100, arcade.color.BLACK, 10, 70, 5)
    arcade.draw_arc_outline(x, y, 100, 100, arcade.color.BLACK, 110, 170, 5)
    arcade.draw_circle_filled(x, y + 40, 20, arcade.color.BLACK)


# Boats
def draw_boat(x, y):
    arcade.draw_arc_filled(x, y, 200, 100, arcade.color.DARK_BROWN, 180, 360)
    arcade.draw_rectangle_filled(x - 30, y + 50, 10, 100, arcade.color.BROWN)
    arcade.draw_rectangle_filled(x - 10, y + 90, 50, 30, arcade.color.RED)


# Ball
def draw_basketball(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.ORANGE)
    arcade.draw_arc_outline(x, y, 75, 70, arcade.color.BLACK, 0, 120, 3, 90)
    arcade.draw_arc_outline(x + 20, y, 67, 70, arcade.color.BLACK, 0, 180, 3, 85)
    arcade.draw_arc_outline(x, y - 10, 75, 70, arcade.color.BLACK, 0, 180, 3)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_sand()
    draw_sunset()
    draw_sun()
    draw_birds(300, 400)
    draw_birds(500, 500)
    draw_birds(600, 400)
    draw_boat(200, 200)
    draw_boat(600, 250)
    draw_basketball(100, 100)
    draw_basketball(200, 210)

    # Finishing
    arcade.finish_render()
    arcade.run()


main()
