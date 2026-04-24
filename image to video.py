import cv2
import numpy as np
import os

heieght=720
width=1280
channel=3
fps=10
sec=5
fourcc=cv2.VideoWriter_fourcc(*'MP42')

video=cv2.VideoWriter('img_video.avi',fourcc,float(fps),(width,heieght))
dicrectory=r'E:\ALL_IN_ONE\OPEN CV\pic'
img_list=os.listdir(dicrectory)

for frame_count in range(fps*sec):
    img_name=np.random.choice(img_list)
    img_path=os.path.join(dicrectory,img_name)
    img=cv2.imread(img_path)
    img_resize=cv2.resize(img,(width,heieght))
    video.write(img_resize)

video.release()