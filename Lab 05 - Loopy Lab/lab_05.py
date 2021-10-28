import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
<<<<<<< HEAD
            x = 300  # Instead of zero, calculate the proper x location using 'column'
            y = 300  # Instead of zero, calculate the proper y location using 'row'
=======
            x = column * 10 + 5
            y = row * 10 + 5
>>>>>>> 788e083e2b941b607edd7816ebd154ce13fabb39
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
<<<<<<< HEAD
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    pass


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    pass
=======
    for row in range(30):
        for column in range(30):
            x = column * 10 + 305
            y = row * 10 + 5
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 605
            y = row * 10 + 5
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
>>>>>>> 788e083e2b941b607edd7816ebd154ce13fabb39


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
<<<<<<< HEAD
    pass
=======
    for row in range(30):
        for column in range(30):
            x = column * 10 + 905
            y = row * 10 + 5
            if row % 2 == 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
>>>>>>> 788e083e2b941b607edd7816ebd154ce13fabb39


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
<<<<<<< HEAD
    pass


def draw_section_6():
    pass


def draw_section_7():
    pass


def draw_section_8():
    pass


=======
    for row in range(30):
        for column in range(row):
            x = row * 10 + 5
            y = column * 10 + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(30):
        for column in range(30 - row):
            x = row * 10 + 305
            y = column * 10 + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for column in range(30):
        for row in range(column + 1):
            x = row * 10 + 605
            y = column * 10 + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
<<<<<<< HEAD
    for row in range(30):
        for column in range(30 - row):
            x = row * 10 + 905
            y = column * 10 + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

=======
    for row in range(35):
        for column in range(row + 6):
            x = (34 - column) * 10 + 905
            y = row * 10 + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


>>>>>>> 4e43884c33a7590216ae5b18f8840e569671fa27
>>>>>>> 788e083e2b941b607edd7816ebd154ce13fabb39
def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


<<<<<<< HEAD
main()
=======
main()
>>>>>>> 788e083e2b941b607edd7816ebd154ce13fabb39
