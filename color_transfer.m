function [transfered_style_matrix_vec] = color_transfer(content_img, style_img)
% pixel transform formula: 
%x_s' = Ax_s + b

% needs to find an and b
%b = uc - Aus 
%AsigmasAt = sigmac

% first compute mean pixel of all imagess
content_mean = mean(mean(content_img,2),1);
style_mean = mean(mean(style_img,2),1);

% find pixel covariance of all images 
% ? =\Sigmai(xi ? µ)(xi ? µ)T /N
height = size(content_img,1);
width = size(content_img,2);

content_matrix_vec = [];
style_matrix_vec = [];
for i = 1:height
    for j = 1:width 
        content_matrix_vec = [content_matrix_vec, content_img(i,j,:)];
        style_matrix_vec = [style_matrix_vec, style_img(i,j,:)];
    end
end
content_mean_vec = repmat(content_mean, [1, height * width]);
style_mean_vec = repmat(style_mean, [1, height * width]);

con_n_matrix_vec = content_matrix_vec - content_mean_vec;
sty_n_matrix_vec = style_matrix_vec - content_mean_vec;


sum_for_content_cov = con_n_matrix_vec(:,1) * con_n_matrix_vec(:,1)';
sum_for_style_cov = sty_n_matrix_vec(:,1) * sty_n_matrix_vec(:,1)';

for i = 1:height*width-1
    sum_for_content_cov = sum_for_content_cov + con_n_matrix_vec(:,i) * con_n_matrix_vec(:,i)'; 
    sum_for_style_cov = sum_for_style_cov + sty_n_matrix_vec(:,i) * sty_n_matrix_vec(:,i)'; 
end 
content_cov = sum_for_content_cov / (height * width);
style_cov = sum_for_style_cov / (height * width);

% compute the 1/2 power of covariance using svd
[U,S,V] = svd(content_cov);
content_cov_sqrt = U * S.^(0.5) * V';
[U,S,V] = svd(style_cov);
style_cov_sqrt = U * S.^(0.5) * V';
A = content_cov_sqrt * style_cov_sqrt';
b = content_mean  - A * style_mean; 
for i = 1:height
    for j = 1:width 
        transfered_style_matrix_vec = A * style_img(j,i,:) + b;
    end
end
 
end