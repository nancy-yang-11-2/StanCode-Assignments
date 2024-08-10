"""
File: draw_line.py
Name: Nancy
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events import mouse
from campy.gui.events.mouse import onmouseclicked


window = GWindow(width=500, height=500, title='Draw a Line')
SIZE = 10
count = 1
x = 0
y = 0


def main():
    """
    Click on the window to get a circle as the starting point.
    Click on the window again to get an ending point.
    The starting point will disappear when the ending point is chosen.
    A line will be drew from the starting point to the ending point.
    """
    onmouseclicked(start_point)


def start_point(event):
    global count, x, y

    if count == 1:
        point_1 = GOval(10, 10, x=event.x-SIZE/2, y=event.y-SIZE/2)
        point_1.color = 'black'
        window.add(point_1)
        x = event.x
        y = event.y
        count = 0
    else:
        point_1 = window.get_object_at(x, y)
        window.remove(point_1)
        line = GLine(x, y, event.x, event.y)
        window.add(line)
        x = 0
        y = 0
        count = 1


if __name__ == "__main__":
    main()
