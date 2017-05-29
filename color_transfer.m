function [] = color_transfer(content_img, style_img)
% pixel transform formula: 
%x_s' = Ax_s + b

% needs to find an and b
b = uc - Aus 
AsigmasAt = sigmac

% first compute mean pixel of all imagess
content_mean = mean(mean(content_img,2),1);
style_mean = mean(mean(style_img,2),1);

% find pixel covariance of all images 
% ? =\Sigmai(xi ? µ)(xi ? µ)T /N
height = size(content_img,1);
width = size(content_img,2);

matrix_vec = [];
for i = 1:height
    for j = 1:width 
        matrix_vec = [matrix_vec, content_img(i,j,:)];
    end
end
content_mean_vec = repmat(content_mean, (1, height * width));

n_matrix_vec = matrix_vec - content_mean_vec;

sum_for_cov = n_matrix_vec(:,1) * n_matrix_vec(:,1)';
for i = 1:height*width-1
    sum_for_cov = n_matrix_vec + n_matrix_vec(:,i) * n_matrix_vec(:,i)'; 
end 
content_cov = sum_for_cov / (height * width);



end