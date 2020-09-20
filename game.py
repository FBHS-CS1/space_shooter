import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Space Blaster"


class Enemy(arcade.Sprite):
    def __init__(self, x, y, num):
        super().__init__(f'images/enemy{num}.png')
        self.center_x = x
        self.center_y = y
        self.scale = 0.5
        self.lasers = []
        self.shot_speed = 10
        self.change_x = 5
        
    def update(self):
        super().update()
        if self.center_x > SCREEN_WIDTH or self.center_x < 0:
            self.center_y -= 5
            self.change_x *= -1
            
            
class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('images/playerShip1_red.png')
        self.center_x = x
        self.center_y = y
        self.scale = 0.5
        self.lasers = []
        self.shot_speed = 10
    
    def shoot(self):
        shot = arcade.Sprite('images/player_laser.png',
                             center_x = self.center_x,
                             center_y = self.center_y + 50)
        shot.change_y = self.shot_speed
        self.lasers.append(shot)
        
    def draw(self):
        super().draw()
        for shot in self.lasers:
            shot.draw()
        
    def update(self):
        super().update()
        to_remove = []
        for shot in self.lasers:
            shot.update()
            if shot.center_y > SCREEN_HEIGHT + 100:
                to_remove.append(shot)
                
        for shot in to_remove:
            self.lasers.remove(shot)
            
            

class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player = None
        self.enemies = None
        arcade.set_background_color(arcade.color.MAROON)

        

    def setup(self):
        self.background = arcade.load_texture('images/bg.jpg')
        self.player = Player(SCREEN_WIDTH//2, 50)
        self.enemies = arcade.SpriteList()
        self.enemies.append(Enemy(SCREEN_WIDTH, SCREEN_HEIGHT-50, 2))
        

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player.draw()
        self.enemies.draw()


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player.update()
        self.enemies.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if key == arcade.key.LEFT:
            self.player.change_x = -5
            
        if key == arcade.key.RIGHT:
            self.player.change_x = 5
            
        if key == arcade.key.SPACE:
            self.player.shoot()

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT:
            self.player.change_x = 0
            
        if key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()