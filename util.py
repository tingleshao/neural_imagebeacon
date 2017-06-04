from scipy.misc import imread, imsave



def print_image(input_img):
    width, height, channels = input_img.shape
    for i in range(width):
        for j in range(height):
            print(input_img[i,j])


def change_map_color(input_img):
    # the map color is b and w, we want to change it to b and red
    # w: 255, 255 ,255
    # b: 0.0.0
    # red: 241, 38 38
    width, height, channels = input_img.shape
    for i in range(width):
        for j in range(height):
            if input_img[i,j,0] < 200:# background
                input_img[i,j] = [0,0,0]
            else:
                input_img[i,j] = [255,0,0]
    return input_img


def original_color_transform(content, generated, mask=None):
    generated = fromimage(toimage(generated, mode='RGB'), mode='YCbCr')  # Convert to YCbCr color space

    if mask is None:
        generated[:, :, 1:] = content[:, :, 1:]  # Generated CbCr = Content CbCr
    else:
        width, height, channels = generated.shape

        for i in range(width):
            for j in range(height):
                if mask[i, j] == 1:
                    generated[i, j, 1:] = content[i, j, 1:]

    generated = fromimage(toimage(generated, mode='YCbCr'), mode='RGB')  # Convert to RGB color space
    return generated


def main():
#    img = imread("images/test_sem.png")
#    print_image(img)
    img = imread("images/building_test1_sem.png")
    img2 = change_map_color(img)
    imsave('test.png', img2)


if __name__ == "__main__":
    main()
