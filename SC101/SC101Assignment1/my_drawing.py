"""
File: my_drawing.py
Name: Nancy
----------------------
Draw a sleeping Snoopy!
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Sleeping Snoopy

    This is my best friend Snoopy!
    He is mischievous and always mess around but he has accompanied me through laughter and tears.
    This is a picture of him sleeping at his favorite spot.
    """
    window = GWindow(width=500, height=500, title='My Drawing')
    background_1 = GRect(500, 150, x=0, y=350)
    background_1.filled = True
    background_1.fill_color = 'sage'
    background_1.color = 'sage'
    window.add(background_1)

    background_2 = GRect(500, 350)
    background_2.filled = True
    background_2.fill_color = 'skyblue'
    background_2.color = 'skyblue'
    window.add(background_2)

    nose = GOval(9, 9, x=166, y=225)
    nose.filled = True
    window.add(nose)

    head_1 = GOval(60, 40, x=172, y=198)
    head_1.filled = True
    head_1.fill_color = 'white'
    head_1.color = 'white'
    window.add(head_1)

    head_2 = GOval(48, 48, x=203, y=190)
    head_2.filled = True
    head_2.fill_color = 'white'
    head_2.color = 'white'
    window.add(head_2)

    body_1 = GRect(40, 30, x=240, y=220)
    body_1.filled = True
    body_1.fill_color = 'white'
    body_1.color = 'white'
    window.add(body_1)

    body_2 = GOval(53, 45, x=260, y=200)
    body_2.filled = True
    body_2.fill_color = 'white'
    body_2.color = 'white'
    window.add(body_2)

    feet = GOval(20, 30, x=310, y=210)
    feet.filled = True
    feet.fill_color = 'white'
    feet.color = 'white'
    window.add(feet)

    toe_1 = GLine(318, 234, 318, 240)
    window.add(toe_1)
    toe_2 = GLine(323, 234, 323, 240)
    window.add(toe_2)

    tail = GOval(15, 5, x=300, y=198)
    tail.filled = True
    window.add(tail)

    ear = GOval(30, 48, x=218, y=196)
    ear.filled = True
    window.add(ear)

    eye = GOval(2, 10, x=200, y=200)
    eye.filled = True
    window.add(eye)

    hand = GOval(15, 15, x=275, y=225)
    hand.filled = True
    hand.fill_color = 'white'
    window.add(hand)

    arm_1 = GLine(265, 230, 275, 230)
    window.add(arm_1)
    arm_2 = GLine(265, 236, 275, 236)
    window.add(arm_2)

    roof_1 = GPolygon()
    roof_1.add_vertex((170, 240))
    roof_1.add_vertex((130, 330))
    roof_1.add_vertex((370, 330))
    roof_1.filled = True
    roof_1.fill_color = 'red'
    roof_1.color = 'red'
    window.add(roof_1)

    roof_2 = GPolygon()
    roof_2.add_vertex((170, 240))
    roof_2.add_vertex((330, 240))
    roof_2.add_vertex((370, 330))
    roof_2.filled = True
    roof_2.fill_color = 'red'
    roof_2.color = 'red'
    window.add(roof_2)

    n = 0
    for i in range(3):
        house = GRect(200, 30, x=150, y=330+n)
        house.filled = True
        house.fill_color = 'red'
        window.add(house)
        n += 30

    a = 0
    b = 0
    for i in range(3):
        z_sign = GLabel('z', x=245+a, y=185-b)
        z_sign.color = 'gray'
        z_sign.font = 'arial-15-italic'
        window.add(z_sign)
        a += 12
        b += 8


if __name__ == '__main__':
    main()
