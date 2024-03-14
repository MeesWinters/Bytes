import math
import numpy as np
import cv2 as cv

def get_bytes(path):
    return open(path, mode="rb").read()

def get_resolution(data):
        sqrt = math.floor(math.sqrt(len(data)))

        for i in range(sqrt):
            if len(data) % (sqrt-i) == 0:
                return [sqrt-i, len(data) // (sqrt-i)]


def make_img(resolution, data):
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
nu

if __name__ == "__main__":
    main()