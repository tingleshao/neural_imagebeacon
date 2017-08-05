# transfer color of style image, so the result style transfer image preserves color

import os


def transform(input_style_image_name, input_content_image_name):
    os.system("matlab -nodesktop -nosplash -r \"color_transfer('{0}', '{1}'); quit\"".format(input_content_image_name, input_style_image_name))
