# runs the experiment:
# two stages:


neural_doodle_dir = '/Users/chongshao/dev/neural-doodle_chong'
content_img_dir = ''
style_img_dir = ''
output_name = ''
# style transfer
# change dir
os.chdir(neural_doodle_dir)
os.system("python3 doodle.py --content {0} --style {1} --output {2} --phases=1 \
--smoothness={3} --seed=\"content\" --iterations=500 --content-weight={} \
--style-weight={} --semantic-weight={}".format(content_img_dir, style_img_dir, \
output_name, smoothness, content_weight, style_weight, semantic_weight))

# blending


# future stages:
# foreground/background detection -> upscale -> style transfer (color preserving) -> blending
