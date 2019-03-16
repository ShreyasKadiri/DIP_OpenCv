import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
    windowName="Live Video Feed"
    cv2.namedWindow(windowName)
    
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret=False;
        
    
    
#TO capture Video Recordings
    while ret:
        ret,frame=cap.read()
        output= cv2.imshow(windowName,frame)
        cv2.imshow("Gray",output)

        if cv2.waitKey(1)==27:
            break
        
    cv2.destroyWindows()
        
    
    
    cap.isrelease()
    
    
    
    
    
if __name__ == "__main__":
    main()