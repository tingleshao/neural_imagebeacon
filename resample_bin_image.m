function [] = resample_bin_image(file_name, w, h)

    img = imread([file_name, '.png'])
    img = rgb2gray(img)
    img = imresize(img, [w, h], 'nearest')
    
    imwrite(img, [file_name, num2str(w), 'x', num2str(h), '.png']);
   
end