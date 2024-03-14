import math
import numpy as np
import cv2 as cv
"""
this scripts will encrypt an image by translating the bytes into greyscale pixel and putting these pixels into an .bmp image

author: Mees Winters
date: March 2024
"""
def get_bytes(path):
    """
    reads the image and returns bytes
    :param path: path to file that gets encrypted
    :return: bytes object
    """
    return open(path, mode="rb").read() #reads the bytes

def get_resolution(data):
    """
    determines factor closest to square
    :param data: bytes from to be encrypted file; result of get_bytes()
    :return: factor closest to square
    """
    sqrt = math.floor(math.sqrt(len(data)))

    for i in range(sqrt): #takes sqaure root of total amount of bytes
        if len(data) % (sqrt-i) == 0:
            return [sqrt-i, len(data) // (sqrt-i)] #subtracts 1 from sqrt until a factor is found


def make_img(resolution, data):
    """
    takes the bytes and puts the corresponding value in an image as a pixel
    :param resolution: resolution of the image that is created; result of get_resolution()
    :param data: bytes list
    :return: opencv greyscale image
    """
    image = np.zeros((resolution[0], resolution[1], 1), dtype=np.uint8) #[y, x]

    index = 0
    for y in range(resolution[0]):
        for x in range(resolution[1]):
            image[y, x] = data[index]
            index += 1

    cv.imwrite("encrypted.bmp", image)

    return image
def main():
    path = ("Cube.jpg")

    data_original = get_bytes(path)
    resolution = get_resolution(data_original)
    make_img(resolution, data_original)

if __name__ == "__main__":
    main()