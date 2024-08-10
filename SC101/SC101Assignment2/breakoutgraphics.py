"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

import self as self
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
NUM_LIVES = 3  # Number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=self.window_width // 2 - paddle_width // 2, y=self.window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2, x=self.window_width // 2 - ball_radius,
                          y=self.window_height // 2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Create game over label
        self.game_over = GLabel('Game Over :(')
        self.game_over.color = 'Red'
        label_width = self.game_over.width
        label_height = self.game_over.height
        self.game_over.x = (self.window_width - label_width) // 2
        self.game_over.y = (self.window_height + label_height) // 2

        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        self.dx = self.__dx
        self.dy = self.__dy

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)

        # Draw bricks
        a = BRICK_OFFSET
        b = 0
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(BRICK_ROWS):
            a += BRICK_HEIGHT + BRICK_SPACING
            for j in range(BRICK_COLS):
                self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT)
                self.brick.filled = True
                self.brick.fill_color = color[i // 2]
                self.brick.color = color[i // 2]
                self.window.add(self.brick, b, a)
                b += BRICK_WIDTH + BRICK_SPACING
            b = 0

        # Set numbers of lives to play
        self.lives = NUM_LIVES

        # Put ball back to the starting position
        self.reset_ball()
        self.moving = False  # Check if the ball is moving

    def reset_ball(self):
        self.ball.x = (self.window_width - BALL_RADIUS * 2) // 2
        self.ball.y = (self.window_height - BALL_RADIUS * 2) // 2
        self.dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx
        self.dy = INITIAL_Y_SPEED

    def move_paddle(self, mouse):
        if mouse.x - self.paddle.width // 2 < 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width // 2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width // 2
            self.paddle.y = self.window.height - PADDLE_OFFSET - self.paddle.height

    def remove_brick(self, obj):
        self.window.remove(obj)
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = -self.__dy

    def bounce(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = -self.__dy
        self.dy = self.__dy

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            self.window.clear()
            self.window.add(self.game_over)
