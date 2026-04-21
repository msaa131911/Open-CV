import numpy as np
import cv2
video_path1=r"E:\\ALL_IN_ONE\\OPEN CV\\video\\WhatsApp Video 2026-03-20 at 2.42.32 PM.mp4"
video_path2=r"E:\\ALL_IN_ONE\\OPEN CV\\video\\WhatsApp Video 2026-03-20 at 2.40.10 PM.mp4"
cap1=cv2.VideoCapture(video_path1)
cap2=cv2.VideoCapture(video_path2)
cap3=cv2.VideoCapture(0)
#jodi 0 day tahola camera open hobe

while cap1.isOpened() and cap2.isOpened() and cap3.isOpened():#jodi video open hoy tahola loop cholbe
    ret,frame=cap1.read()#ret=video read
    ret,frame1=cap2.read()#ret=video read
    ret,frame2=cap3.read()#ret=video read

    if ret:
        frames=cv2.resize(frame,(400,400))#video ke 400,400 size e convert kore dibe
        frames1=cv2.resize(frame1,(400,400))#video ke 400,400 size e convert kore dibe
        camera=cv2.resize(frame2,(400,400))#video ke 400,400 size e convert kore dibe

        imges1=np.hstack((frames,frames1))#video ke horizontal vabe 2 bar show korbe
        imges2=np.hstack((imges1,camera))#video ke vertical v
        cv2.imshow("video",imges2)#video ke show korbe
        if cv2.waitKey(25) & 0xFF==ord("q"):#video ke 25ms por por update korbe, jodi user "q" key press kore tahola video stop hobe
            break
    else:
        break
cap1.release()
cv2.destroyAllWindows()