#import modules, initialize screen, hide mouse and add background.
from livewires import games, color
import random
games.init(640, 480, 50)
games.mouse.is_visible = False
game_background = games.load_image("images/background.png")
games.screen.background = game_background
#create a sprite class for the ball, include initialization method,
#add score, update method with collision logic.
class Ball(games.Sprite):
    """a ball the player must keep from hitting the bottom"""
    ball = games.load_image("images/ball.png")
    def __init__(self):
        """load the ball and score into the game"""
        #use ball image, place in center of screen, give x and y velocity
        #and add a score.
        super(Ball, self).__init__(image = Ball.ball,
                                   x = games.screen.width/2,
                                   y = games.screen.height/2,
                                   dy = 2,
                                   dx = 2)
        self.score = games.Text(0,
                           size = 30, color = color.red,
                           x = games.screen.width-10,
                           y = 15,
                           is_collideable = False)
        games.screen.add(self.score)
    def update(self):
        #end game and display message if bottom of screen touched.
        if self.bottom > games.screen.height:
            self.destroy()
            end = games.Message("Game Over",
                                size = 100,
                                color = color.red,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                lifetime = 250,
                                after_death = games.screen.quit)
            games.screen.add(end)

        for Pannel in self.overlapping_sprites:
            self.score.value += 1
            self.score.right = games.screen.width-10
            #determines if the ball will move right or left and
            #applies a random number to the x and y velocity
            if games.keyboard.is_pressed(games.K_a):
                self.dx = random.randint(-4, -1)
            elif games.keyboard.is_pressed(games.K_d):
                self.dx = random.randint(1, 4)
            else:
                self.dx = self.dx
            self.dy = random.randint(-5, -1)
        #collision logic for sprite bouncing of walls and pannel.
        if self.top < 0:
            self.dy = -self.dy
        elif self.left < 0:
            self.dx = -self.dx
        elif self.right > games.screen.width:
            self.dx = -self.dx
#create a sprite class for the pannel, include initialization method,
#update method and collision logic.
class Pannel(games.Sprite):
    """a pannel to bounce the ball away"""
    pannel = games.load_image("images/pannel.png")
    def __init__(self):
        """set up the pannels attributes"""
        #set up pannel in centre of screen, just above the bottom of the screen.
        super(Pannel, self).__init__(image = Pannel.pannel,
                                     x = games.screen.width/2,
                                     y = games.screen.height -11)
    def update(self):
        #key movement and movement direction
        if games.keyboard.is_pressed(games.K_d):
            self.x += 5
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 5
        #collision logic to prevent pannel going out of screen.
        if self.right > games.screen.width:
            self.right = games.screen.width
        elif self.left < 0:
            self.left = 0
#events are detected, objects are loaded, the screen is kept open and esc quits.
games.screen.event_grab = True
the_ball = Ball()
games.screen.add(the_ball)
the_pannel = Pannel()
games.screen.add(the_pannel)
games.screen.mainloop()
if games.keyboard.is_pressed(games.K_ESCAPE):
    games.screen.quit()
