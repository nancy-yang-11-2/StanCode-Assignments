"""
File: blur.py
Name: Nancy
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    Method to create a blurred image:
    Identify the R, G, B of the neighboring pixel and get an average R, G, B
    Replace the blank image's pixel with the average R, G, B
    """
    new_img = SimpleImage.blank(old_img.width, old_img.height)  # create a blank image
    for x in range(old_img.width):
        for y in range(old_img.height):
            total_r = 0
            total_g = 0
            total_b = 0
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # identify the neighboring pixel

                    new_x = x + i
                    new_y = y + j
                    if 0 <= new_x < old_img.width and 0 <= new_y < old_img.height:
                        # make sure all the pixel is within boundary

                        pixel = old_img.get_pixel(new_x, new_y)
                        total_r += pixel.red
                        total_g += pixel.green
                        total_b += pixel.blue
                        count += 1
            avg_red = total_r / count
            avg_green = total_g / count
            avg_blue = total_b / count
            pixel = new_img.get_pixel(x, y)
            pixel.red = avg_red
            pixel.green = avg_green
            pixel.blue = avg_blue
    return new_img


def main():
    """
    Open the image 'smiley-face', create a blurred version of this image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
