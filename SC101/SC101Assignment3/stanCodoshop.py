"""
File: stanCodoshop.py
Name: Nancy
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""
import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # dist = math.sqrt((red-pixel.red**2)**2 + (green-pixel.green**2)**2 + (blue-pixel.blue**2)**2)
    pixel_red = (red - pixel.red) ** 2
    pixel_green = (green - pixel.green) ** 2
    pixel_blue = (blue - pixel.blue) ** 2
    dist = math.sqrt((pixel_red + pixel_green + pixel_blue))
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_red = 0
    total_green = 0
    total_blue = 0
    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue
    red = total_red // len(pixels)
    green = total_green // len(pixels)
    blue = total_blue // len(pixels)
    rgb = [red, green, blue]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg = get_average(pixels)
    avg_red = avg[0]
    avg_green = avg[1]
    avg_blue = avg[2]
    best = pixels[0]
    max_dist = math.sqrt((255**2)*3)  # if pixel is 0 and average pixel is 255
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_red, avg_green, avg_blue)
        if dist < max_dist:
            max_dist = dist
            best.red = pixel.red
            best.green = pixel.green
            best.blue = pixel.blue
        else:
            break
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(result.width):
        for y in range(result.height):
            pixel_lst = []                         # make a list of pixel of the blank image
            for image in images:
                pixel = image.get_pixel(x, y)      # get the pixel on the same location in every images being processed
                pixel_lst.append(pixel)            # make it into a list
            best = get_best_pixel(pixel_lst)       # identify the best pixel
            result_pixel = result.get_pixel(x, y)  # put the best pixel into the blank image
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
