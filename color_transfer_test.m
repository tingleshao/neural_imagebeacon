style_img = imread('neural_imagebeacon_data/building_gc1.png');
content_img = imread('neural_imagebeacon_data/building_test4.png');
t = color_transfer(style_img, content_img)