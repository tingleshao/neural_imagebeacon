function [img] = resample_bin_image(file_name, w, h)

    img = imread(['neural_imagebeacon_data/', file_name, '.png']);
    img = rgb2gray(img);
    img = imresize(img, [w, h], 'nearest');
    img(img > 100) = 255;
    img(img <= 100) = 0;
    imwrite(img, [file_name, num2str(w), 'x', num2str(h), '.png']);
end