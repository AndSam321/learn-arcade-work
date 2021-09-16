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
def draw_birds(x,y):
    arcade.draw_arc_outline(x, y, 100, 100, arcade.color.BLACK, 0 , 180, 3)





def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_sand()
    draw_sunset()
    draw_sun()
    draw_birds(50, 50)









# Finishing
    arcade.finish_render()
    arcade.run()

main()


































