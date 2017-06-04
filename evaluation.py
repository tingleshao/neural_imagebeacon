# transfer color of style image
# so the result style transfer image preserves color

import os


def process_image(input_style_image_name, input_content_image_name):
    return None


def main():
    # TODO: evaluation based on SSIM
    # list all image dirs
    img_dir = '/Users/chongshao/Downloads/test_image/'
    building_dir = img_dir + "buildings/"
    near_indoor_objs_dir = img_dir + "near_indoor_objs/"
    near_outdoor_objs_dir = img_dir + "near_outdoor_objs/"
    signs_dir = img_dir + "signs/"
    # setnumber
    building_set_num = 9
    near_indoor_set_num = 21
    near_outdoor_set_num = 9
    signs_set_num = 20
    # TODO: read image


if __name__ == '__main__':
    main()
