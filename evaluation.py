# transfer color of style image
# so the result style transfer image preserves color

import os
from numpy.misc import imread, imsave


def process_image(input_style_image_name, input_content_image_name):
    return None


def main():
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
    building_quality = []
    near_indoor_quality = []
    near_outdoor_quality = []
    signs_quality = []
    for i in range(building_set_num):
        curr_dir = building_dir + "set{}/".format(i)
        image_names = os.listdir(curr_dir)
        image_names.sort()
        image_name = image_names[-1]
        # retrieve the largest threshold image
        curr_img = imread(image_name)
        # process this image
        processed_curr_img = process_image(curr_img)
        quality = evaluate_quality(processed_curr_img, original_img)
        building_quality.append(quality)
    for i in range(near_indoor_set_num):
        curr_dir = near_indoor_objs_dir + "set{}/".format(i)
        image_names = os.listdir(curr_dir)
        image_names.sort()
        image_name = image_names[-1]
        # retrieve the largest threshold image
        curr_img = imread(image_name)
        # process this image
        processed_curr_img = process_image(curr_img)
        quality = evaluate_quality(processed_curr_img, original_img)
        near_indoor_quality.append(quality)
    for i in range(near_outdoor_set_num):
        curr_dir = near_outdoor_objs_dir + "set{}/".format(i)
        image_names = os.listdir(curr_dir)
        image_names.sort()
        image_name = image_names[-1]
        # retrieve the largest threshold image
        curr_img = imread(image_name)
        # process this image
        processed_curr_img = process_image(curr_img)
        quality = evaluate_quality(processed_curr_img, original_img)
        near_outdoor_quality.append(quality)
    for i in range(signs_set_num):
        curr_dir = signs_dir + "set{}/".format(i)
        image_names = os.listdir(curr_dir)
        image_names.sort()
        image_name = image_names[-1]
        # retrieve the largest threshold image
        curr_img = imread(image_name)
        # process this image
        processed_curr_img = process_image(curr_img)
        quality = evaluate_quality(processed_curr_img, original_img)
        signs_quality.append(quality)
    print("building_quality" + str(building_quality))
    print("near_indoor_quality" + str(near_indoor_quality))
    print("near_outdoor_quality" + str(near_outdoor_quality))
    print("signs_quality" + str(signs_quality))


def evaluate_quality(image_a, ref_iamge):
    return None


def process_image(image):
    return None


if __name__ == '__main__':
    main()
