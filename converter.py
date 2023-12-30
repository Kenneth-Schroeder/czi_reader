from czifile import CziFile, imread
from PIL import Image
import glob
import re

paths = glob.glob('czi_input/*.czi')
for file_path in paths:
    try:
        img_arrs = imread(file_path)
    except ValueError as e:
        print(f"Error processing file {file_path} with {e}.")
        continue
    for img_arr in img_arrs:
        img = Image.fromarray(img_arr)
        file_name = re.split('/|\.', file_path)[-2]
        out_path = f"jpeg_output/{file_name}.jpeg"
        img.save(out_path)
        print(f"Saved file to {out_path}")
