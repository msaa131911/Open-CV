import cv2
import numpy as np
import os

heieght=720
width=1280
channel=3
fps=30
sec=5

fourcc=cv2.VideoWriter_fourcc(*'MP42')
video=cv2.VideoWriter('video.mp4',fourcc,float(fps),(width,heieght))
for frame_count in range(fps*sec):
    rand_arr=np.random.randint(0,255,size=(heieght,width,channel),dtype=np.uint8)
    video.write(rand_arr)

video.release()