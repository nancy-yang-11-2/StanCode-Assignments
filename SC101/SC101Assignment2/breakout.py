"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from typing import Optional, Any

from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
graphics = BreakoutGraphics()


def main():
    onmouseclicked(move_ball)


def move_ball(mouse):
    graphics.moving = True

    while graphics.moving:
        graphics.ball.move(graphics.dx, graphics.dy)
        pause(FRAME_RATE)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.dx = -graphics.dx
        # if graphics.ball.y <= 0:
        #     graphics.dy = -graphics.dy
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.decrease_lives()
            graphics.reset_ball()
            graphics.moving = False

        obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        obj4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)

        if obj1 is not None:
            if obj1 is not graphics.paddle:
                graphics.remove_brick(obj1)
                graphics.dy = -graphics.dy
            else:
                if graphics.dy > 0:
                    graphics.bounce()
        elif obj2 is not None:
            if obj2 is not graphics.paddle:
                graphics.remove_brick(obj2)
                graphics.dy = -graphics.dy
            else:
                if graphics.dy > 0:
                    graphics.bounce()
        elif obj3 is not None:
            if obj3 is not graphics.paddle:
                graphics.remove_brick(obj3)
                graphics.dy = -graphics.dy
            else:
                if graphics.dy > 0:
                    graphics.bounce()
        elif obj4 is not None:
            if obj4 is not graphics.paddle:
                graphics.remove_brick(obj4)
                graphics.dy = -graphics.dy
            else:
                if graphics.dy > 0:
                    graphics.bounce()


if __name__ == '__main__':
    main()
