#horizontal and vertical stacking of images
import cv2
import os
import numpy as np

path = r"E:\ALL_IN_ONE\OPEN CV\pic"

img_list = os.listdir(path)#list of all the images in the folder

for i in img_list:
    img_path_full = os.path.join(path, i)#

    img = cv2.imread(img_path_full)

    if img is None:
        print("Skip:", i)
        continue

  
    img_resized = cv2.resize(img, (300, 200))

    # horizontal (same height ✔)
    img_horizontal = np.hstack((img_resized, img_resized, img_resized))#horizontal 3 columns images

    # vertical (same width ✔)
    img_vertical = np.vstack((img_horizontal, img_horizontal, img_horizontal))#vertical 3 rows images

    cv2.imshow('image', img_vertical)
    cv2.waitKey(1000)

cv2.destroyAllWindows()