function [img_output] = resample_bin_image(file_name, w, h)

    img = imread(['neural_imagebeacon_data/', file_name, '.png']);
    img = rgb2gray(img);
    img = imresize(img, [w, h], 'nearest');
    img(img > 100) = 255;
    img(img <= 100) = 0;
    
    img_output(:,:,1) = img;
    img_output(:,:,2) = img;
    img_output(:,:,3) = img;
    imwrite(img_output, [file_name, num2str(w), 'x', num2str(h), '.png']);
end