"""
File: bouncing_ball.py
Name: Nancy
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)

VY = 0
count = 0


def main():
    onmouseclicked(bounce)


def bounce(mouse):
    global VX, VY, count
    count += 1
    if count > 3:
        reset_ball()
    else:
        while True:
            ball.move(VX, VY)
            VY += GRAVITY
            if ball.y + ball.height >= window.height:
                VY = VY * -1 * REDUCE
            if ball.x > window.width:
                reset_ball()
                break
            pause(DELAY)


def reset_ball():
    global VY
    ball.x = START_X
    ball.y = START_Y
    VY = 0


if __name__ == "__main__":
    main()
