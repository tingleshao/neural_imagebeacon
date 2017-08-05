import sys
import cv2
import numpy as np

# merge foreground image and background image based on binary map.

def blend(bin_img, background_img, foreground_img):
    background_img = cv2.multiply(background_img, bin_img)
    foreground_img = cv2.multiply(cv2.subtract(np.ones(64,64), bin_img), foreground_img)
    result_img = cv2.add(background_img, foreground_img)
    return result_img


def main():
    foreground_img = cv2.imread(sys.argv[1])
    backgrund_img = cv2.imread(sys.argv[2])
    bin_img = cv2.imread(sys.argv[3])
    result_img = blend(bin_img, backgrund_img, foreground_img)
    cv2.imwrite("result.jpg", result_img)


if __name__ == "__main__":
    main()
