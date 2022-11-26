import random

import cv2
import numpy as np


IMAGE_SHAPE = [1080, 1080]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [100, 220, 100]
BLUE = [255, 0, 0]


def create_square():
    black_square = np.zeros((IMAGE_SHAPE[0], IMAGE_SHAPE[1], 3), np.uint8)
    for i in range(8):
        a = i * 135
        cv2.rectangle(black_square, (0 + a, 0 + a), (135 + a, 135 + a), WHITE, -1)
    cv2.circle(black_square, (650, 350), 75, GREEN, -1)
    black_square = change_colors(black_square)
    cv2.imshow("shaked", black_square)
    cv2.waitKey(0)


def change_colors(image):
    selected_background = np.all(image == BLACK, axis=-1)  # the selected area.
    selected_squares = np.all(image == WHITE, axis=-1)
    selected_circle = np.all(image == GREEN, axis=-1)
    image[selected_background] = BLUE
    image[selected_squares] = GREEN
    image[selected_circle] = BLACK
    return image


if __name__ == '__main__':
    # create_square()
    test = [0,1,2,3,4,5,6,7,8,9]
    print(test[:2])
