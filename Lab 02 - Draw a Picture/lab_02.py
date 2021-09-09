# Import Arcade
import arcade

# Open up a window
arcade.open_window(800, 600, "Lab 2")

# Background Color
arcade.set_background_color(arcade.color.BEIGE)

# Rendering
arcade.start_render()

# Entertainment Stand
arcade.draw_rectangle_filled(400, 300, 300, 60, arcade.color.DARK_BROWN)
arcade.draw_line(300, 270, 300, 330, arcade.color.BLACK, 2)
arcade.draw_line(500, 270, 500, 330, arcade.color.BLACK, 2)
arcade.draw_line(300, 300, 500, 300, arcade.color.BLACK, 2)

# Left Lamp
arcade.draw_rectangle_filled(750, 95, 10, 50, arcade.color.GRAY)
arcade.draw_arc_filled(750, 168, 50, 100, arcade.color.GRAY, 180, 360)


# Right Lamp
arcade.draw_rectangle_filled(600, 320, 10, 100, arcade.color.GRAY)
arcade.draw_arc_filled(600, 400, 50, 100, arcade.color.GRAY, 180, 360)

# TV
arcade.draw_rectangle_filled(400, 400, 200, 75, arcade.color.BLACK)
arcade.draw_rectangle_filled(400,400, 175, 60, arcade.color.SKY_BLUE)

# Couch/Bed
arcade.draw_rectangle_filled(400 , 0, 500, 60, arcade.color.LIGHT_BROWN)
arcade.draw_rectangle_filled(400, 0, 500, 40, arcade.color.WHITE)
arcade.draw_arc_filled(400, 20, 500, 270, arcade.color.LIGHT_BROWN, 0, 180)

# Walls
arcade.draw_line(0, 0, 253, 270, arcade.color.BLACK, 3)
arcade.draw_line(250, 325, 260, 800, arcade.color.BLACK, 3)

# TV Stuff
arcade.draw_circle_filled(400, 400, 10, arcade.color.YELLOW)
arcade.draw_circle_filled(380, 380, 10, arcade.color.PURPLE)
arcade.draw_circle_filled(350, 420, 10, arcade.color.ORANGE)

# Dresser
arcade.draw_rectangle_filled(750, 20, 100, 100, arcade.color.DARK_BROWN)




















# Finished Drawing
arcade.finish_render()

# Keeping window up
arcade.run()
