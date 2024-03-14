import cv2 as cv
"""
this script decrypts the the data from a .pmd file created with encrypt_image.py

author: Mees Winters
date: March 2024
"""
def get_bytes(image_path):
    """
    translates all pixels in the image back into bytes using opencv
    :param: image_path: path to the image with encrypted data
    :return: bytes
    """
    image = cv.cvtColor(cv.imread(image_path), cv.COLOR_BGRA2GRAY)

    bytesimage = []
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            bytesimage.append(image.data[y, x])

    return bytesimage


def write_bytes(bytesimage, file_path):
    """
    writes the bytes from get_bytes() to an empty file
    :param: bytesimage: byte list from get_bytes()
    :param: file_path: path of the file containing the encrypted data
    :return: decrypted file

    """
    file = open(file_path, "wb").write(bytes(bytesimage))

    return file
def main():
    image_path = "encrypted.bmp"
    file_path = "decrypted"
    bytes_from_image = get_bytes(image_path)
    write_bytes(bytes_from_image, file_path)

if __name__ == "__main__":
    main()