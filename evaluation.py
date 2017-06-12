# transfer color of style image
# so the result style transfer image preserves color

import os
from scipy.misc import imread, imsave

from skimage import data, img_as_float
from skimage.measure import compare_ssim as ssim


def process_image(input_style_image_name, input_content_image_name):
    return None


def main():
    # list all image dirs
    img_dir = '/home/tinnitant/Downloads/test_image/'
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
    run_building_test = True
    if run_building_test:
       for i in range(building_set_num):
           if i > 2:
              curr_dir = building_dir + "set{}/".format(i)
              image_names = os.listdir(curr_dir + "/jpeg_res/")
              image_names.sort()
              image_name = image_names[-1]
        # retrieve the largest threshold image
              curr_img = imread(curr_dir + "/jpeg_res/" + image_name)
        # process this image
              processed_curr_img = process_image(curr_img)
              quality = evaluate_quality(processed_curr_img, original_img)
              building_quality.append(quality)
#    for i in range(near_indoor_set_num):
#        curr_dir = near_indoor_objs_dir + "set{}/".format(i)
#        image_names = os.listdir(curr_dir)
#        image_names.sort()
#        image_name = image_names[-1]
        # retrieve the largest threshold image
#        curr_img = imread(image_name)
        # process this image
#        processed_curr_img = process_image(curr_img)
#        quality = evaluate_quality(processed_curr_img, original_img)
#        near_indoor_quality.append(quality)
#    for i in range(near_outdoor_set_num):
#        curr_dir = near_outdoor_objs_dir + "set{}/".format(i)
#        image_names = os.listdir(curr_dir)
#        image_names.sort()
#        image_name = image_names[-1]
        # retrieve the largest threshold image
#        curr_img = imread(image_name)
        # process this image
#        processed_curr_img = process_image(curr_img)
#        quality = evaluate_quality(processed_curr_img, original_img)
#        near_outdoor_quality.append(quality)
#    for i in range(signs_set_num):
#        curr_dir = signs_dir + "set{}/".format(i)
#        image_names = os.listdir(curr_dir)
#        image_names.sort()
#        image_name = image_names[-1]
#        # retrieve the largest threshold image
#        curr_img = imread(image_name)
        # process this image
#        processed_curr_img = process_image(curr_img)
#        quality = evaluate_quality(processed_curr_img, original_img)
#        signs_quality.append(quality)
    print("building_quality" + str(building_quality))
    print("near_indoor_quality" + str(near_indoor_quality))
    print("near_outdoor_quality" + str(near_outdoor_quality))
    print("signs_quality" + str(signs_quality))

def evaluate_quality(image_a, ref_iamge):
    ssim_value = ssim(img_a, ref_image, data_range=img_a.max() - img_a.min())
    return ssim_value


def process_image(image):
    neural_doodle_dir = '/home/tinnitant/dev/neural-doodle_chong'
    content_img_dir = '' # TODO: fix here
    style_img_dir = ''
    output_name = ''
    # style transfer
    # change dir
    smoothness = 0.4
    content_weight = 0.4
    style_weight = 0.4
    semantic_weight = 0.4
    cwd = os.getcwd()
    os.chdir(neural_doodle_dir)
    os.system("python3 doodle.py --content {0} --style {1} --output {2} --phases=1 \
    --smoothness={3} --seed=\"content\" --iterations=500 --content-weight={4} \
    --style-weight={5} --semantic-weight={6}".format(content_img_dir, style_img_dir, \
    output_name, smoothness, content_weight, style_weight, semantic_weight))

    os.chdir(cwd)
    # blending

    os.system("python3 overlap.py {0} {1}".format(content_img_dir, output_name))


if __name__ == '__main__':
    main()
