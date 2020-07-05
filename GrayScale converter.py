from PIL import Image, ImageFilter
import os
import sys

# grab the first and the second argument
image_folder = sys.argv[1]
image_output = sys.argv[2]

# check if the output folder is exists or not if not create it
if(not os.path.exists(image_output)):
    os.makedirs(image_output)

# loop through all images in image_folder
for filename in os.listdir(image_folder):
    if(filename.endswith("jpg") or filename.endswith("png")):
        img = Image.open(f"{image_folder}{filename}")
        name = os.path.splitext(filename)[0]
        # convert image to greyscale and save it
        img = img.convert("L")
        img.save(f"{image_output}{name}.png", 'png')
        print("done")
