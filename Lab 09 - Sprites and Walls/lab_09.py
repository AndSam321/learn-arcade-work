import arcade

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.score = 0
        self.player_list = None
        self.coin_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.coin_sound = arcade.load_sound("arcade_resources_sounds_coin4.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # Coin Placement
        coordinate_list = [[200, 400],
                           [250, 400],
                           [300, 400],
                           [350, 400],
                           [400, 400],
                           [450, 400],
                           [-50, 400],
                           [0, 400],
                           [-189, 550],
                           [-150, 550],
                           [-50, 700],
                           [0, 700],
                           [-189, 850],
                           [-150, 850],
                           [200, 650],
                           [250, 650],
                           [300, 650],
                           [200, 850],
                           [250, 850],
                           [300, 850],
                           [800, 550],
                           [750, 550],
                           [700, 550],
                           [950, 250]]

        for coordinate in coordinate_list:
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
            coin.center_x = coordinate[0]
            coin.center_y = coordinate[1]
            self.coin_list.append(coin)

        # Starting Point Image taken from Novaskin.com
        for x in range(200, 1000, 64):
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        coordinate_list = [[190, 500],
                           [200, 600],
                           [250, 600],
                           [300, 600],
                           [310, 500]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Left Side of Map
        for y in range(350, 800, 64):
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = 50
            wall.center_y = y
            self.wall_list.append(wall)
        coordinate_list = [[-10, 350],
                           [-50, 350],
                           [-189, 500],
                           [-145, 500],
                           [-10, 650],
                           [-50, 650],
                           [-189, 800],
                           [-145, 800],
                           [200, 800],
                           [250, 800],
                           [300, 800]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Right Side of Map
        for y in range(350, 800, 64):
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = 500
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(500, 890, 64):
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        for y in range(500, 800, 64):
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = 880
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(650, 890, 64):
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        for y in range(500, 680, 64):
            wall = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)
            wall.center_x = 650
            wall.center_y = y
            self.wall_list.append(wall)

        # Border. Image taken from Novaskin.com
        # Left Wall
        for y in range(200, 1000, 64):
            wall = arcade.Sprite("minecraft-tnt-block-png-transparent.png", SPRITE_SCALING / 4)
            wall.center_x = -250
            wall.center_y = y
            self.wall_list.append(wall)
            # Bottom Wall
        for x in range(-200, 1000, 64):
            wall = arcade.Sprite("minecraft-tnt-block-png-transparent.png", SPRITE_SCALING / 4)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
            # Top Wall
        for x in range(-250, 980, 64):
            wall = arcade.Sprite("minecraft-tnt-block-png-transparent.png", SPRITE_SCALING / 4)
            wall.center_x = x
            wall.center_y = 1000
            self.wall_list.append(wall)
            # Right Wall
        for y in range(200, 1000, 64):
            wall = arcade.Sprite("minecraft-tnt-block-png-transparent.png", SPRITE_SCALING / 4)
            wall.center_x = 1000
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 400, 10, arcade.color.BLACK_BEAN, 30)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_sprite.update()
        self.coin_list.update()
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
