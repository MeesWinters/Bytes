import cv2 as cv

def get_bytes(image_path):
    image = cv.cvtColor(cv.imread(image_path), cv.COLOR_BGRA2GRAY)

    bytesimage = []
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            bytesimage.append(image.data[y,x])

    return bytesimage


def write_bytes(bytesimage, file_path):
    file = open(file_path, "wb").write(bytes(bytesimage))

def main():
    image_path = "encrypted.bmp"
    file_path = "decrypted"
    bytes_from_image = get_bytes(image_path)
    write_bytes(bytes_from_image, file_path)

if __name__ == "__main__":
    main()